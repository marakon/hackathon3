import requests
import json
import matplotlib.pyplot as plt

class Variables():
    API_KEY = "23a2a18e6e8932bc9e7746fec06a4881"
    BASE_URL = "http://api.openweathermap.org/data/2.5/group?"

def concatenate_list(lista):
    result= ''
    for element in lista:
        result += str(element['id'])
        if element == lista[-1]:
            break
        result += ','
    return result

def read_json():
    while True:
        file = input("Enter country code(UK/PL/DE): ").upper()
        try:
            with open(file + ".json") as raw_data:
                my_data = json.load(raw_data)
                break
        except FileNotFoundError:
            print('Country not available. Try other.')
    return my_data

def requester(id_list):
    while True:
        try:
            URL = Variables.BASE_URL + "appid=" + Variables.API_KEY + "&id=" + id_list
            data = requests.get(URL).json()
            count = data['cnt']
            print('Num of cities:', count)
            break
        except KeyError:
            print(data['message'])
            continue
    return data

def present_data():
    raw_data = read_json()
    raw_list = concatenate_list(raw_data)
    data = requester(raw_list)
    data_list = data['list']
    for element in data_list:
        name = element['name']
        print('\nCity:', name)
        temp = round(element['main']['temp'] - 273.15)
        print('Temp:', temp)
        both = name + ' ' + str(temp)
        print(both)
        plt.style.use('ggplot')
        plt.bar(both, temp)
        fig1 = plt.gcf()
        fig1.set_size_inches(15, 10)
    plt.show()

present_data()
