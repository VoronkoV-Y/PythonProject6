from src.API_connect_class import APIConnectClass
from src.info_aeroplanes_class import InfoAeroplanesClass
from src.saver_class import JSONSaverClass
import pytest


@pytest.fixture
def API_connect_class_obj_1():
    return APIConnectClass("Malta")


@pytest.fixture
def info_aeroplanes_class_aeroplane_1():
    return InfoAeroplanesClass("callsign-test", "country_rgstr-test", 15000, 500)


@pytest.fixture
def info_aeroplanes_class_aeroplane_2():
    return InfoAeroplanesClass("callsign-test", "country_rgstr-test", 14000, 600)


@pytest.fixture
def my_data_list():
    return [
        ['46b8aa', 'AEE8GM  ', 'Greece', 1782766779, 1782766779, 14.6137, 36.152, 10965.18, False, 231.58, 268.47, 0, None, 11513.82, '7736', False, 0],
        ['4ca7b6', 'RYR822J ', 'Ireland', 1782766779, 1782766779, 14.5952, 36.0327, 3444.24, False, 137.56, 145.36, -5.2, None, 3695.7, '0234', False, 0]]


@pytest.fixture
def JSON_saver_test():
    return JSONSaverClass()


@pytest.fixture
def test_list_aeroplanes():
    return [InfoAeroplanesClass("callsign-test", "country_rgstr-test", 15000, 500), InfoAeroplanesClass("callsign-test2", "country_rgstr-test2", 15002, 502)]


@pytest.fixture
def test_list_aeroplanes_dict():
    return [
        {"callsign": "callsign-test", "country_rgstr": "country_rgstr-test", "baro_altitude": 15000, "velocity": 500},
        {"callsign": "callsign-test2", "country_rgstr": "country_rgstr-test2", "baro_altitude": 15002, "velocity": 502}
            ]


@pytest.fixture
def expected_data():
    return [{"callsign": "callsign-test", "country_rgstr": "country_rgstr-test", "baro_altitude": 15000, "velocity": 500}]


@pytest.fixture
def expected_data_2():
    return [
        {"callsign": "callsign-test", "country_rgstr": "country_rgstr-test", "baro_altitude": 15000, "velocity": 500},
        {"callsign": "callsign-test2", "country_rgstr": "country_rgstr-test2", "baro_altitude": 15002, "velocity": 502}
            ]
