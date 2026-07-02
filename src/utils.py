from src.info_aeroplanes_class import InfoAeroplanesClass



# Модуль для вспомогательных функций

def filter_aeroplanes(aeroplanes_data, filter_words):
    """Функция фильтрует данные о самолётах по странам регистрации"""

    data = []

    for word in filter_words:
        for item in aeroplanes_data:
            if item["country_rgstr"] == word:
                data.append(item)
    return data


def get_aeroplanes_by_altitude(aeroplanes_data, altitude_range):
    """Функция фильтрует данные о самолётах по диапозону высот"""

    data = []
    altitude_ranged_data = altitude_range.split()
    altitude_ranged_data = [int(altitude_ranged_data[0]), int(altitude_ranged_data[-1])]
    max_altitude = max(altitude_ranged_data)
    min_altitude = min(altitude_ranged_data)

    for item in aeroplanes_data:
        item["baro_altitude"] = 0 if item["baro_altitude"] is None else item["baro_altitude"]
        if min_altitude <= item["baro_altitude"] <= max_altitude:
            data.append(item)
    return data


def sort_aeroplanes(ranged_aeroplanes):
    """Функция сортирует самолеты по их высоте полета"""

    sorted_aeroplanes_data = sorted(ranged_aeroplanes, key=lambda x: x["baro_altitude"], reverse=True)
    return sorted_aeroplanes_data


def get_top_aeroplanes(sorted_aeroplanes, top_n):
    """Функция выводит топ-N самолетов по их высоте полета"""

    return sorted_aeroplanes[0:top_n]


