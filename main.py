from src.API_connect_class import APIConnectClass
from src.info_aeroplanes_class import InfoAeroplanesClass
from src.saver_class import JSONSaverClass

from src.utils import filter_aeroplanes, get_aeroplanes_by_altitude, get_top_aeroplanes, sort_aeroplanes


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    # Выбор пользователем источник информации
    data_flag = None
    while True:
        try:
            source_info = int(input("Выберите источник информации:\n 1. API \n 2. JSON - файл\n"))
            if source_info == 1:
                data_flag = 1
                break
            if source_info == 2:
                data_flag = 2
                break
            else:
                print("Неверно введены данные. \n")
                continue
        except ValueError:
            print("Неверно введены данные. \n")
            continue

    # Выбор пользователем набора данных для предоставления информации по самолетам
    country = input("Введите название страны: \n")
    top_n = int(input("Введите количество самолетов для вывода в топ N: \n"))
    filter_words = input("Введите названия стран для фильтрации по стране регистрации: \n").split()
    altitude_range = input("Введите диапазон высот полета: \n")  # Пример: 100000 - 150000

    # Использование выбранного ранее пользователем источника информации
    if data_flag == 1:
        user_api = APIConnectClass(country)
        user_data_list = user_api.get_aeroplanes()
        user_aeroplanes_data_object = InfoAeroplanesClass.cast_to_object_list(user_data_list)
        user_aeroplanes_data = []
        for item in user_aeroplanes_data_object:
            user_aeroplanes_data.append({"callsign": item.callsign, "country_rgstr": item.country_rgstr,
                                        "baro_altitude": item.baro_altitude, "velocity": item.velocity})

    if data_flag == 2:
        json_saver = JSONSaverClass()
        user_aeroplanes_data = json_saver.get_info()

    # Обработка полученных данных из источника
    filtered_aeroplanes = filter_aeroplanes(user_aeroplanes_data, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(user_aeroplanes_data, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)

    print("\nTоп N самолетов по высоте полета:")
    count = 1
    for aeroplane in top_aeroplanes:
        print(f"{count}. {aeroplane}")
        count += 1

    count = 1
    print("\nСписок самолетов по стране их регистрации:")
    for aeroplane in filtered_aeroplanes:
        print(f"{count}. {aeroplane}")
        count += 1


if __name__ == "__main__":
    user_interaction()
