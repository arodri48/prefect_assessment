from typing import Dict

import pytest


@pytest.fixture
def weather_data_input() -> Dict:
    return {"latitude": 30.303434, "longitude": -95.463776,
                                  "generationtime_ms": 0.13196468353271484, "utc_offset_seconds": 0, "timezone": "GMT",
                                  "timezone_abbreviation": "GMT", "elevation": 63.0,
                                  "current_weather": {"temperature": 31.2, "windspeed": 6.9, "winddirection": 118.0,
                                                      "weathercode": 0, "is_day": 1, "time": "2023-05-30T22:00"}}


@pytest.fixture
def expected_weather_json() -> Dict:
    return {"latitude": 30.303434, "longitude": -95.463776,
            "generationtime_ms": 0.13196468353271484, "utc_offset_seconds": 0, "timezone": "GMT",
            "timezone_abbreviation": "GMT", "elevation": 63.0,
            "current_weather": {"temperature": 31.2, "windspeed": 6.9, "winddirection": 118.0,
                                "weathercode": 0, "is_day": 1, "time": "2023-05-30T22:00"}}