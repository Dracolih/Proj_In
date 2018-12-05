from requests import get
from datetime import datetime, timedelta
from json import loads
from pprint import pprint
import io
import json


KEY = 'eaa0ff45bf8ccd0c7d976ca0619f48a7'

def get_city_id():
    with io.open('city.list.json',encoding='utf8') as f:
        data = loads(f.read())
        
    city = input("W jakim jestes miescie?\n" ) #wysw tekst, czekaj na stringa, zwroc stringa
    city_id = False
    
    for item in data: #petla for dla danych w data 
        if item['name'] == city: #
            
            if item['name'] == city:
                city_id = item['id']
                


            print('Czy to miasto ma dl i szer geo = ')
            print(item['coord'])
            answer = input('')
            if answer == 'y':
                city_id = item['id']
                break

    if not city_id:
        print('Nie mamy takiego miasta w bazie')
        exit()
#7530790
        
    return city_id

def get_weather_data(city_id):
#    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id=7530790&APPID=eaa0ff45bf8ccd0c7d976ca0619f48a7')
    weather_data = get('http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}'.format(city_id, KEY))

    return weather_data.json()

def get_arrival():
    today = datetime.now() #dostan obecna date
    max_day = today + timedelta(days = 4)
    
    print('Jakiego dnia miesiaca przyjedziesz?')
    print(today.strftime('%d'), '-', max_day.strftime('%d')) #wysw konkretne dni miesiaca
    day = input() #wczytaj odpowiedz
    print('O ktorej godzinie przyjedziesz?')
    print('0 - 24')
    hour = int(input()) #zrzutuj na inta wpisanego stringa z odpowiedzia
    hour = hour - hour % 3 #co 3 godziny nowa wartosc liczona od 0
    arrival = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + day + ' ' + str(hour) + ':00:00' #sformatuj dane tak jak wjsonie rok-miesiac-dzien-godzina
    return arrival #zwraca dane w stringu

def get_forecast(arrival, weather_data):
    for forecast in weather_data['list']: #iteracja po elementach listy weather_data
        if forecast['dt_txt'] = arrival:
            return forecast

        

