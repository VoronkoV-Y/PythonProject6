from src.API_connect_class import APIConnectClass


class InfoAeroplanesClass():
    """Класс для работы с информацией о самолетах"""

    # aeroplanes = []

    __slots__ = ("callsign", "country_rgstr", "baro_altitude", "velocity")

    callsign: str
    country_rgstr: str
    baro_altitude: float
    velocity: float

    def __init__(self, callsign, country_rgstr, baro_altitude, velocity):
        self.callsign = callsign
        self.country_rgstr = country_rgstr
        self.baro_altitude = baro_altitude
        self.velocity = velocity

    def __lt__(self, other):
        """Метод сравнения самолетов по их высоте полета"""

        if isinstance(other, InfoAeroplanesClass):
            return self.baro_altitude < other.baro_altitude
        else:
            print("Объект сравнения не принадлежит классу InfoAeroplanesClass")

    def velocity_compare(self, other):
        """Метод сравнения самолетов по их горизонтальной скорости полета"""

        if isinstance(other, InfoAeroplanesClass):
            return self.velocity < other.velocity
        else:
            print("Объект сравнения не принадлежит классу InfoAeroplanesClass")

    @classmethod
    def cast_to_object_list(cls, data_list: list):
        """Метод, который преобразует набор данных в список объектов"""

        aeroplanes = []
        for item in data_list:
            aeroplanes.append(InfoAeroplanesClass(item[1], item[2], item[7], item[9]))

        return aeroplanes


# my_cheking
if __name__ == "__main__":

    my_api = APIConnectClass("Malta")
    # print(my_api.get_coordinates())
    # print(my_api.get_aeroplanes())
    my_data_list = my_api.get_aeroplanes()

    print(InfoAeroplanesClass.cast_to_object_list(my_data_list))