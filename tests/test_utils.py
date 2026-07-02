from src.utils import filter_aeroplanes, get_aeroplanes_by_altitude, sort_aeroplanes, get_top_aeroplanes


def test_filter_aeroplanes(test_list_aeroplanes_dict, expected_data):
    assert filter_aeroplanes(test_list_aeroplanes_dict, ["country_rgstr-test"]) == expected_data


def test_get_aeroplanes_by_altitude(test_list_aeroplanes_dict, expected_data):
    assert get_aeroplanes_by_altitude(test_list_aeroplanes_dict, "1000 - 15001") == expected_data


def test_sort_aeroplanes(test_list_aeroplanes_dict):
    assert sort_aeroplanes(test_list_aeroplanes_dict) == [
        {"callsign": "callsign-test2", "country_rgstr": "country_rgstr-test2", "baro_altitude": 15002, "velocity": 502},
        {"callsign": "callsign-test", "country_rgstr": "country_rgstr-test", "baro_altitude": 15000, "velocity": 500}
            ]


def test_get_top_aeroplanes(test_list_aeroplanes_dict, expected_data):
    assert get_top_aeroplanes(test_list_aeroplanes_dict, 1) == expected_data
