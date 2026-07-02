from src.info_aeroplanes_class import InfoAeroplanesClass


def test_info_aeroplanes_class_init(info_aeroplanes_class_aeroplane_1):
    assert info_aeroplanes_class_aeroplane_1.callsign == "callsign-test"
    assert info_aeroplanes_class_aeroplane_1.country_rgstr == "country_rgstr-test"
    assert info_aeroplanes_class_aeroplane_1.baro_altitude == 15000
    assert info_aeroplanes_class_aeroplane_1.velocity == 500


def test_info_aeroplanes_class_lt(info_aeroplanes_class_aeroplane_1, info_aeroplanes_class_aeroplane_2):
    assert info_aeroplanes_class_aeroplane_1.__lt__(info_aeroplanes_class_aeroplane_2) == False


def test_info_aeroplanes_class_lt_error(capsys, info_aeroplanes_class_aeroplane_1):
    info_aeroplanes_class_aeroplane_1.__lt__("Test")
    screen_message = capsys.readouterr()
    assert (
            screen_message.out
            == "Объект сравнения не принадлежит классу InfoAeroplanesClass\n"
    )


def test_velocity_compare(info_aeroplanes_class_aeroplane_1, info_aeroplanes_class_aeroplane_2):
    assert info_aeroplanes_class_aeroplane_1.velocity_compare(info_aeroplanes_class_aeroplane_2) == True


def test_velocity_compare_error(capsys, info_aeroplanes_class_aeroplane_1):
    info_aeroplanes_class_aeroplane_1.velocity_compare("Test")
    screen_message = capsys.readouterr()
    assert (
            screen_message.out
            == "Объект сравнения не принадлежит классу InfoAeroplanesClass\n"
    )


def test_cast_to_object_list(my_data_list):
    assert len(InfoAeroplanesClass.cast_to_object_list(my_data_list)) == 2
    assert InfoAeroplanesClass.cast_to_object_list(my_data_list)[0].callsign == 'AEE8GM  '
