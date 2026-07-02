from src.API_connect_class import APIConnectClass
from unittest.mock import patch


def test_API_connect_class_init():
    assert APIConnectClass("Malta").country == "Malta"


def test_connect_to_API_200(API_connect_class_obj_1):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"test": "TEST"}
        assert API_connect_class_obj_1.connect_to_API("https://test_url.com", {}, {}) == {"test": "TEST"}
        mock_get.assert_called_once_with(url='https://test_url.com', params={}, headers={})


def test_connect_to_API_error(capsys, API_connect_class_obj_1):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 300
        API_connect_class_obj_1.connect_to_API("https://test_url.com", {}, {})
        screen_message = capsys.readouterr()
        assert (screen_message.out == "Ошибка соединения с API сервиса\n")
        mock_get.assert_called_once_with(url='https://test_url.com', params={}, headers={})


def test_get_coordinates(API_connect_class_obj_1):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
        {
        "boundingbox": [
            "50.1",
            "60.2",
            "-70.3",
            "-80.4"
        ]}]
        assert API_connect_class_obj_1.get_coordinates() == {
            'lamin': 50.1,
            'lamax': 60.2,
            'lomin': -70.3,
            'lomax': -80.4,
        }
        mock_get.assert_called_once_with(url="https://nominatim.openstreetmap.org/search", params={'country': "Malta",'format': 'json','limit': 1,}, headers={'User-Agent': 'test_my_app'})


def test_get_aeroplanes(API_connect_class_obj_1):
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"states": "test"}
        assert API_connect_class_obj_1.get_aeroplanes() == "test"
        mock_get.assert_called_once_with(url="https://opensky-network.org/api/states/all?", params=None, headers={})
