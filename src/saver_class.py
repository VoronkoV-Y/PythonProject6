from abc import ABC, abstractmethod
from idlelib.debugobj_r import remote_object_tree_item

from config import PATH_data
import json
from src.API_connect_class import APIConnectClass
from src.info_aeroplanes_class import InfoAeroplanesClass
from collections.abc import Iterable


class ABCSaverClass(ABC):
    """Абстрактный класс для создания классов сохранения информации о самолетах в разных форматах файлов"""

    @abstractmethod
    def add_info(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def delete_info(self):
        pass


class JSONSaverClass(ABC):
    """Класс для сохранения информации о самолетах в JSON-файл"""

    def __init__(self):
        self.path_to_file = str(PATH_data) + "\\" + "default_JSON_data.json"

    def add_info(self, new_data):
        try:
            with open(self.path_to_file, "r", encoding="UTF-8") as file:
                data = json.load(file)
                if isinstance(new_data, InfoAeroplanesClass):
                    data.append({"callsign": new_data.callsign, "country_rgstr": new_data.country_rgstr,
                                 "baro_altitude": new_data.baro_altitude, "velocity": new_data.velocity})
                elif isinstance(new_data, list):
                    for item in new_data:
                        data.append({"callsign": item.callsign, "country_rgstr": item.country_rgstr,
                                     "baro_altitude": item.baro_altitude, "velocity": item.velocity})
                else:
                    return "Неверный формат данных"
            with open(self.path_to_file, "w", encoding="UTF-8") as file:
                json.dump(data, file)
        except FileNotFoundError:
            if isinstance(new_data, InfoAeroplanesClass):
                data = []
                data.append({"callsign": new_data.callsign, "country_rgstr": new_data.country_rgstr,
                                 "baro_altitude": new_data.baro_altitude, "velocity": new_data.velocity})
            elif isinstance(new_data, Iterable):
                data = []
                for item in new_data:
                    data.append({"callsign": item.callsign, "country_rgstr": item.country_rgstr,
                                 "baro_altitude": item.baro_altitude, "velocity": item.velocity})
            else:
                return "Неверный формат данных"
            with open(self.path_to_file, "w", encoding="UTF-8") as file:
                json.dump(data, file)

    def get_info(self):
        try:
            with open(self.path_to_file, "r", encoding="UTF-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return "Файл с данными не найден."

    def delete_info(self, callsign):
        data = self.get_info()
        if data == "Файл с данными не найден.":
            print("Файл с данными не найден.")
            return None
        new_data = []
        for item in data:
            if item["callsign"] != callsign:
                new_data.append(item)
        with open(self.path_to_file, "w", encoding="UTF-8") as file:
            json.dump(new_data, file)
