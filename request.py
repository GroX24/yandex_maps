#import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
import requests
from PIL import Image


def find_toponym(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass

    # Преобразуем ответ в json-объект
    json_response = response.json()
    # Получаем первый топоним из ответа геокодера.
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = list(map(float, toponym_coodrinates.split(" ")))
    return [toponym_longitude, toponym_lattitude]


def gib_me_da_pic(toponym_longitude, toponym_lattitude, delta):
    delta = str(delta)
    coords = ",".join([str(toponym_longitude), str(toponym_lattitude)])
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": coords,
        "spn": ",".join([delta, delta]),
        "l": "map",
        "size": ",".join(list(map(str, mapsize)))
    }
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    return Image.open(BytesIO(response.content))


maxdelta = 90.000
mindelta = 0.0001
defaultdelta = 0.005
mapsize = [600, 450]

#t = "Коптево"
#gib_me_da_pic(*find_toponym(t), defaultdelta).show()