import json
import os
import pytest
from prefect.testing.utilities import prefect_test_harness
from src.workflow import lookup_weather, save_weather, parse_temp


@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    with prefect_test_harness():
        yield


def test_invalid_zip():
    with pytest.raises(ValueError):
        lookup_weather.fn(77301)


def test_save_weather(tmpdir, weather_data_input, expected_weather_json):
    os.chdir(tmpdir)
    save_weather.fn(weather_data_input, 'sample.json')
    with open('sample.json', 'r') as f:
        actual_json = json.load(f)
    assert actual_json == expected_weather_json


def test_parse_temp(weather_data_input):
    assert parse_temp.fn(weather_data_input) == 31.2
