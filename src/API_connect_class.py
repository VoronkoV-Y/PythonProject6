from abc import ABC, abstractmethod
import requests


class APIAbcClass(ABC):
    """Абстрактный класс для подключения к API сервисов и сбора информацци по координатом стран и самолётах"""

    @abstractmethod
    def connect_to_API(self, url):
        pass

    @abstractmethod
    def get_coordinates(self, country):
        pass

    @abstractmethod
    def get_aeroplanes(self):
        pass


class APIConnectClass(APIAbcClass):
    """Класс для подключения к API сервисов и сбора информацци по координатом стран и самолётах с сайтов nominatim.openstreetmap.org
    и opensky-network.org."""

    country: str

    __url_coordinates = "https://nominatim.openstreetmap.org/search"
    __url_aeroplanes = "https://opensky-network.org/api/states/all?"

    def __init__(self, country) -> None:
        self.country = country
        self.__geo_coordinates = None

    def connect_to_API(self, url, params, headers):
        response = requests.get(url=url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Ошибка соединения с API сервиса")


    def get_coordinates(self):
        url = APIConnectClass.__url_coordinates
        headers = {
            'User-Agent': 'test_my_app',
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params = {
            'country': self.country,
            'format': 'json',
            'limit': 1,
        }

        data = self.connect_to_API(url,params, headers)

        geo_coordinates = data[0].get('boundingbox')
        # Параметры для фильтрации самолетов по их географическим координатам.
        geo_params = {
            'lamin': float(geo_coordinates[0]),
            'lamax': float(geo_coordinates[1]),
            'lomin': float(geo_coordinates[2]),
            'lomax': float(geo_coordinates[3]),
        }

        self.__geo_coordinates = geo_params
        return geo_params

    def get_aeroplanes(self):
        url = APIConnectClass.__url_aeroplanes
        headers = {}

        # Указываем в параметрах координаты
        params = self.__geo_coordinates
        data = self.connect_to_API(url, params, headers)

        return data["states"]

if __name__ == "__main__":
    my_api = APIConnectClass("Malta")
    print(my_api.get_coordinates())
    print(my_api.get_aeroplanes())
