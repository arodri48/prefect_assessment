import argparse
import json
from typing import Dict

import requests
from prefect import flow, task

JSON_FPATH = "weather_result.json"
ZIPCODE_COORDINATES = {77306: {"latitude": 30.31, "longitude": -95.46}}
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"


@task
def lookup_weather(zipcode: int) -> Dict:
    """
    Looks up the weather at a given zipcode using an API
    :param zipcode: int representing zipcode
    :return: json response from API call
    """
    if zipcode not in ZIPCODE_COORDINATES:
        raise ValueError("Zipcode is not supported")
    json_payload = {"current_weather": True, "temperature_unit": "fahrenheit"}
    json_payload.update(ZIPCODE_COORDINATES[zipcode])
    response = requests.get(WEATHER_API_URL, params=json_payload)
    return response.json()


@task
def save_weather(weather_data: Dict, json_fpath: str) -> None:
    """
    Saves the json response from weather API into a json file
    :param weather_data: dictionary containing weather information from API
    :param json_fpath: filepath for writing out json dictionary
    """
    with open(json_fpath, 'w') as f:
        json.dump(weather_data, f)


@task
def parse_temp(weather_data: Dict) -> float:
    """
    Simply returns the temperature from API response
    :param weather_data: dictionary containing weather information
    :return: temperature from json response
    """
    temperature = weather_data['current_weather']['temperature']
    return temperature


@flow
def temperature_workflow(zipcode: int) -> float:
    """
    Main workflow for executing tasks to obtain temperature for given zipcode
    :param zipcode:
    :return: temperature at zipcode
    """
    weather_dict = lookup_weather(zipcode)
    save_weather(weather_dict, JSON_FPATH)
    temperature = parse_temp(weather_dict)
    return temperature


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI for running Prefect workflow")
    parser.add_argument('-z', '--zipcode', required=True)
    args = parser.parse_args()
    temp = temperature_workflow(int(args.zipcode))
