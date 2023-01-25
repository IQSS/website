# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import copy
import json
import unittest
from unittest import mock

from main import app

TEST_PLACE_DCID = "Earth"
TEST_EVENT_TYPE = "EarthquakeEvent"
TEST_DATE = "2020-01"
TEST_DATE_2 = "2022-12"
TEST_FILTER_PROP = "filter_prop"
TEST_FILTER_UNIT = "filter_unit"
TEST_FILTER_UPPER_LIMIT = "8"
TEST_FILTER_LOWER_LIMIT = "1"
DATE_LIST = [
    "1990",
    "1991",
    "1992",
    "1993",
    "1994",
    "1995",
    "1996",
    "1997",
    "1998",
    "1999",
    "2000",
]
EVENT_1 = {
    "dcid": "event1",
    "dates": ["2020-01-01"],
    "places": [TEST_PLACE_DCID],
    "geoLocations": [{
        "point": {
            "longitude": 1,
            "latitude": 1
        }
    }],
    "provenanceId": "provId",
    "propVals": {
        "name": {
            "vals": ["event1Name"]
        },
        TEST_FILTER_PROP: {
            "vals": [f'{TEST_FILTER_UNIT} 5']
        }
    }
}
EVENT_2 = {
    "dcid": "event2",
    "dates": ["2020-01-01"],
    "places": [TEST_PLACE_DCID],
    "geoLocations": [{
        "point": {
            "longitude": 1,
            "latitude": 1
        }
    }],
    "provenanceId": "provId",
    "propVals": {
        "name": {
            "vals": ["event2Name"]
        },
        TEST_FILTER_PROP: {
            "vals": [f'{TEST_FILTER_UNIT}10']
        }
    }
}
JSON_RESP_EVENT_1 = copy.deepcopy(EVENT_1)
JSON_RESP_EVENT_1["provenanceId"] = ""
JSON_RESP_EVENT_2 = copy.deepcopy(EVENT_2)
JSON_RESP_EVENT_2["provenanceId"] = ""
EVENT_1_JSON = {
    "eventId": "event1",
    "name": "event1Name",
    "startDate": "2020-01-01",
    "affectedPlaces": [TEST_PLACE_DCID],
    "longitude": 1,
    "latitude": 1,
    TEST_FILTER_PROP: f'{TEST_FILTER_UNIT} 5'
}
EVENT_2_JSON = {
    "eventId": "event2",
    "name": "event2Name",
    "startDate": "2020-01-01",
    "affectedPlaces": [TEST_PLACE_DCID],
    "longitude": 1,
    "latitude": 1,
    TEST_FILTER_PROP: f'{TEST_FILTER_UNIT}10'
}
TEST_JSON_DATA = {
    TEST_EVENT_TYPE: {
        TEST_DATE: [EVENT_1_JSON, EVENT_2_JSON],
        TEST_DATE_2: [EVENT_1_JSON]
    }
}
EVENT_DATA = {
    "eventCollection": {
        "events": [EVENT_1, EVENT_2],
        "provenanceInfo": {
            "provId": {
                "domain": "provDomain",
                "importName": "provImportName",
                "provenanceUrl": "provUrl"
            }
        }
    }
}


class TestGetDateRange(unittest.TestCase):

  @mock.patch('routes.api.disaster_api.dc.get_event_collection_date')
  def test_has_dates(self, mock_event_collection_date):

    def date_side_effect(event_type, affected_place):
      if event_type == TEST_EVENT_TYPE and affected_place == TEST_PLACE_DCID:
        return {"eventCollectionDate": {"dates": DATE_LIST}}
      else:
        return None

    mock_event_collection_date.side_effect = date_side_effect

    response = app.test_client().get(
        f"/api/disaster-dashboard/event-date-range?eventType={TEST_EVENT_TYPE}&place={TEST_PLACE_DCID}&useCache=1"
    )
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert (response_data.get("maxDate") == DATE_LIST[-1])
    assert (response_data.get("minDate") == DATE_LIST[0])

  @mock.patch('routes.api.disaster_api.dc.get_event_collection_date')
  def test_no_dates(self, mock_event_collection_date):

    def date_side_effect(event_type, affected_place):
      if event_type == TEST_EVENT_TYPE and affected_place == TEST_PLACE_DCID:
        return {}
      else:
        return None

    mock_event_collection_date.side_effect = date_side_effect

    response = app.test_client().get(
        f"/api/disaster-dashboard/event-date-range?eventType={TEST_EVENT_TYPE}&place={TEST_PLACE_DCID}&useCache=1"
    )
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert (response_data.get("maxDate") == "")
    assert (response_data.get("minDate") == "")

  def test_has_dates_json(self):
    with app.app_context():
      app.config['DISASTER_DASHBOARD_DATA'] = TEST_JSON_DATA

      response = app.test_client().get(
          f"/api/disaster-dashboard/event-date-range?eventType={TEST_EVENT_TYPE}&place={TEST_PLACE_DCID}&useCache=0"
      )
      assert response.status_code == 200
      response_data = json.loads(response.data)
      assert (response_data.get("maxDate") == TEST_DATE_2)
      assert (response_data.get("minDate") == TEST_DATE)

  def test_no_dates_json(self):
    with app.app_context():
      app.config['DISASTER_DASHBOARD_DATA'] = TEST_JSON_DATA

      response = app.test_client().get(
          f"/api/disaster-dashboard/event-date-range?eventType=event&place={TEST_PLACE_DCID}&useCache=0"
      )
      assert response.status_code == 200
      response_data = json.loads(response.data)
      assert (response_data.get("maxDate") == "")
      assert (response_data.get("minDate") == "")


class TestGetData(unittest.TestCase):

  @mock.patch('routes.api.disaster_api.dc.get_event_collection')
  def test_has_data(self, mock_event_collection):

    def event_side_effect(event_type, affected_place, date, filter_prop,
                          filter_unit, filter_upper_limit, filter_lower_limit):
      if (event_type == TEST_EVENT_TYPE and
          affected_place == TEST_PLACE_DCID and date == TEST_DATE and
          filter_prop == "" and filter_unit == "" and
          filter_upper_limit == float("0") and
          filter_lower_limit == float("0")):
        return EVENT_DATA
      else:
        return None

    mock_event_collection.side_effect = event_side_effect

    response = app.test_client().get(
        '/api/disaster-dashboard/event-data?eventType={}&date={}&place={}'.
        format(TEST_EVENT_TYPE, TEST_DATE, TEST_PLACE_DCID))
    assert response.status_code == 200
    assert json.loads(response.data) == EVENT_DATA

  @mock.patch('routes.api.disaster_api.dc.get_event_collection')
  def test_no_data(self, mock_event_collection):

    def event_side_effect(event_type, affected_place, date, filter_prop,
                          filter_unit, filter_upper_limit, filter_lower_limit):
      if (event_type == TEST_EVENT_TYPE and
          affected_place == TEST_PLACE_DCID and date == TEST_DATE and
          filter_prop == "" and filter_unit == "" and
          filter_upper_limit == float("0") and
          filter_lower_limit == float("0")):
        return {}
      else:
        return None

    mock_event_collection.side_effect = event_side_effect

    response = app.test_client().get(
        '/api/disaster-dashboard/event-data?eventType={}&date={}&place={}'.
        format(TEST_EVENT_TYPE, TEST_DATE, TEST_PLACE_DCID))
    assert response.status_code == 200
    assert json.loads(response.data) == {}

  @mock.patch('routes.api.disaster_api.dc.get_event_collection')
  def test_with_filter(self, mock_event_collection):

    def event_side_effect(event_type, affected_place, date, filter_prop,
                          filter_unit, filter_upper_limit, filter_lower_limit):
      if (event_type == TEST_EVENT_TYPE and
          affected_place == TEST_PLACE_DCID and date == TEST_DATE and
          filter_prop == TEST_FILTER_PROP and
          filter_unit == TEST_FILTER_UNIT and
          filter_upper_limit == float(TEST_FILTER_UPPER_LIMIT) and
          filter_lower_limit == float(TEST_FILTER_LOWER_LIMIT)):
        return EVENT_DATA
      else:
        return None

    mock_event_collection.side_effect = event_side_effect

    response = app.test_client().get(
        '/api/disaster-dashboard/event-data?eventType={}&date={}&place={}&filterProp={}&filterUnit={}&filterUpperLimit={}&filterLowerLimit={}'
        .format(TEST_EVENT_TYPE, TEST_DATE, TEST_PLACE_DCID, TEST_FILTER_PROP,
                TEST_FILTER_UNIT, TEST_FILTER_UPPER_LIMIT,
                TEST_FILTER_LOWER_LIMIT))
    assert response.status_code == 200
    assert json.loads(response.data) == EVENT_DATA


class TestGetDataJson(unittest.TestCase):

  def test_has_data(self):
    with app.app_context():
      app.config['DISASTER_DASHBOARD_DATA'] = TEST_JSON_DATA
      response = app.test_client().get(
          '/api/disaster-dashboard/json-event-data?eventType={}&date={}&place={}'
          .format(TEST_EVENT_TYPE, TEST_DATE, TEST_PLACE_DCID))
      assert response.status_code == 200
      expected = {
          "eventCollection": {
              "events": [JSON_RESP_EVENT_1, JSON_RESP_EVENT_2],
              "provenanceInfo": {}
          }
      }
      assert json.loads(response.data) == expected

  def test_no_data(self):
    with app.app_context():
      app.config['DISASTER_DASHBOARD_DATA'] = TEST_JSON_DATA
      response = app.test_client().get(
          '/api/disaster-dashboard/json-event-data?eventType={}&date={}&place={}'
          .format(TEST_EVENT_TYPE, "2023-01", TEST_PLACE_DCID))
      assert response.status_code == 200
      assert json.loads(response.data) == {}

  def test_with_filter(self):
    with app.app_context():
      app.config['DISASTER_DASHBOARD_DATA'] = TEST_JSON_DATA
      response = app.test_client().get(
          '/api/disaster-dashboard/json-event-data?eventType={}&date={}&place={}&filterProp={}&filterUnit={}&filterUpperLimit={}&filterLowerLimit={}'
          .format(TEST_EVENT_TYPE, TEST_DATE, TEST_PLACE_DCID, TEST_FILTER_PROP,
                  TEST_FILTER_UNIT, TEST_FILTER_UPPER_LIMIT,
                  TEST_FILTER_LOWER_LIMIT))
      assert response.status_code == 200
      expected = {
          "eventCollection": {
              "events": [JSON_RESP_EVENT_1],
              "provenanceInfo": {}
          }
      }
      assert json.loads(response.data) == expected
