from unittest.mock import patch, mock_open, Mock
import json
from config import PATH_data
import os


def test_JSON_saver_class_init(JSON_saver_test):
    assert JSON_saver_test.path_to_file == f"{PATH_data}\\default_JSON_data.json"


def test_add_info_info_aeroplanes_class_one_object(JSON_saver_test, info_aeroplanes_class_aeroplane_1, expected_data):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"

    with open(JSON_saver_test.path_to_file, "w", encoding="UTF-8") as file:
        json.dump(([]), file)

    JSON_saver_test.add_info(info_aeroplanes_class_aeroplane_1)

    with open(JSON_saver_test.path_to_file, "r", encoding="UTF-8") as file:
        new_test_data = json.load(file)

    assert new_test_data == expected_data
    os.remove(JSON_saver_test.path_to_file)


def test_add_info_info_aeroplanes_class_list(JSON_saver_test, test_list_aeroplanes, expected_data_2):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"

    with open(JSON_saver_test.path_to_file, "w", encoding="UTF-8") as file:
        json.dump(([]), file)

    JSON_saver_test.add_info(test_list_aeroplanes)

    with open(JSON_saver_test.path_to_file, "r", encoding="UTF-8") as file:
        new_test_data = json.load(file)

    assert new_test_data == expected_data_2
    os.remove(JSON_saver_test.path_to_file)


def test_add_info_info_aeroplanes_class_type_error(JSON_saver_test):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    m = mock_open(read_data=json.dumps([]))
    with (patch("builtins.open", m)):
        assert JSON_saver_test.add_info("test") == "Неверный формат данных"


def test_add_info_info_aeroplanes_class_file_not_found(JSON_saver_test, info_aeroplanes_class_aeroplane_1, expected_data):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    JSON_saver_test.add_info(info_aeroplanes_class_aeroplane_1)

    with open(JSON_saver_test.path_to_file, "r", encoding="UTF-8") as file:
        new_test_data = json.load(file)

    assert new_test_data == expected_data
    os.remove(JSON_saver_test.path_to_file)


def test_add_info_info_aeroplanes_class_file_not_found_one_object(JSON_saver_test, info_aeroplanes_class_aeroplane_1, expected_data):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    JSON_saver_test.add_info(info_aeroplanes_class_aeroplane_1)

    with open(JSON_saver_test.path_to_file, "r", encoding="UTF-8") as file:
        new_test_data = json.load(file)

    assert new_test_data == expected_data
    os.remove(JSON_saver_test.path_to_file)


def test_add_info_info_aeroplanes_class_file_not_found_list(JSON_saver_test, test_list_aeroplanes, expected_data_2):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"

    JSON_saver_test.add_info(test_list_aeroplanes)

    with open(JSON_saver_test.path_to_file, "r", encoding="UTF-8") as file:
        new_test_data = json.load(file)

    assert new_test_data == expected_data_2
    os.remove(JSON_saver_test.path_to_file)


def test_add_info_info_aeroplanes_class_file_not_found_type_error(JSON_saver_test):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    m = mock_open(read_data=json.dumps([]))
    with (patch("builtins.open", m)):
        assert JSON_saver_test.add_info("test") == "Неверный формат данных"


def test_get_info(JSON_saver_test):
    m = mock_open(read_data=json.dumps(["TEST"]))
    with (patch("builtins.open", m)):
        assert JSON_saver_test.get_info() == ["TEST"]


def test_get_info_error(JSON_saver_test):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    assert JSON_saver_test.get_info() == "Файл с данными не найден."


def test_delete_info(JSON_saver_test):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    test_data = [
        {"callsign": "callsign-test", "country_rgstr": "country_rgstr-test", "baro_altitude": 15000, "velocity": 500},
        {"callsign": "callsign-test2", "country_rgstr": "country_rgstr-test2", "baro_altitude": 15002, "velocity": 502}
    ]

    expected_data = [{"callsign": "callsign-test2", "country_rgstr": "country_rgstr-test2", "baro_altitude": 15002, "velocity": 502}]

    with open(JSON_saver_test.path_to_file, "w", encoding="UTF-8") as file:
        json.dump(test_data, file)

    JSON_saver_test.delete_info("callsign-test")

    with open(JSON_saver_test.path_to_file, "r", encoding="UTF-8") as file:
        new_test_data = json.load(file)

    assert new_test_data == expected_data
    os.remove(JSON_saver_test.path_to_file)


def test_delete_info_error(capsys, JSON_saver_test):
    JSON_saver_test.path_to_file = str(PATH_data) + "\\" + "TEST_default_JSON_data.json"
    assert JSON_saver_test.delete_info("callsign-test") == None
    screen_message = capsys.readouterr()
    assert screen_message.out == "Файл с данными не найден.\n"
