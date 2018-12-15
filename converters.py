try:
    import requests
except ModuleNotFoundError:
    pass
import math
"""
    input - из чего переводим
    output - во что переводим
    amount - количество переводимого
    
    Любая функция возвращает вещественное ЧИСЛО с 6 знаками после запятой - результат конвертирования

    Пример:
    currency("EUR', 'USD', 100) = 113.525032
    100 ЕВРО = 113.525032 БАЧЕЙ

    temperature("Шкала Фаренгейта", "Шкала Кельвина", 32) = 273.16
    32 по Фаренгейту = 273.16 по Кельвину (= Нулю по Цельсию соответственно)

    В других конвертерах принцип тот-же
"""

dict_currencies = {'Доллар США': 'USD', 'Австралийский доллар': 'AUD', 'Биткойн': 'BTC', 'Канадский доллар': 'CAD',
                   'Швейцарский франк': 'CHF', 'Японская йена': 'JPY', "Британский фунт": 'GBP', 'Рубль': 'RUB',
                   'Новозеландский доллар': 'NZD', 'Евро': 'EUR', 'Шведская крона': 'SEK', "Польский злотый": "PLN",
                   'Юань': 'CNH', "Мексиканский песо": 'MXN', "Турецкая крона": "TRY", "Украйнская гривна": "UAH"
                   }

list_temperatures = ['Шкала Цельсия', 'Шкала Кельвина', 'Шкала Фаренгейта']

dict_lengths = {'Нанометры': 1e-9, "Микроны": 1e-6, "Милиметры": 1e-3, "Сантиметры": 0.01, "Дециметры": 0.1,
                "Метры": 1, "Километры": 1000, "Дюймы": 0.0254, "Футы": 0.305, "Ярды": 0.91, 'Мили': 1609.34}

dict_squares = {"Квадратные миллиметры": 1e-6, "Квадратные сантиметры": 1e-3, "Квадратные метры": 1,
                "Квадратные километры": 1e6, "Гектары": 1e4,
                "Квадратные дюймы": 0.000645, "Квадратные футы": 0.0929, "Квадратные ярды": 0.836127, "Акры": 4046.86,
                "Квадратные мили": 2589988.11, "Сотки": 100}

dict_times = {"Микросекунды":1e-6, "Миллисекунды": 1e-3, "Секунды": 1, "Минуты": 60,
              "Часы": 3600, "Дни": 86400, "Недели": 604800, "Года": 31536000}

dict_masses = {"Карат": 1/5000, "Миллиграмм": 1e-6, "Сантиграмм": 1e-5, "Дециграмм": 1e-4,
               "Грамм": 1e-3, "Декаграмм": 1e-2, "Гектограмм": 0.1, "Килограмм": 1,
               "Метрическая тонна": 1e3, "Унция": 1/35.27396, "Фунт": 1/2.204623, "Стоун": 1/0.157473}


dict_speeds = {"Сантиметров в секунду": 0.01, "Метров в секунду": 1, "Километров в час": 1/3.6,
               "Футов в секунду": 1/3.28084, "Миль в час": 1/2.237136, "Узлов": 1/1.944012, "Число Маха": 1/0.002939}


dict_volumes = {"Миллилитров": 1e-9, "Кубических сантиметров": 1e-6, "Литров": 1e-3, "Кубических метров": 1,
                "Британских пинт": 1/1759.754, "Британских кварт": 1/879.877, "Британских галлонов": 1/219.9692,  "Баррели": 0.159}

import datetime

def currency(input, output, amount):
    try:
        link = "http://openexchangerates.org/api/latest.json?app_id=60da2bd9b3064714b2c5f2e8b00fbd40"
        data = requests.get(link)
        rates = data.json()["rates"]
        check_time = datetime.datetime.now().strftime("%Y.%m.%d. %H:%M")
        with open("current_currency.txt", "w") as save:
            save.write(str(rates) + "\n")
            save.write(str(check_time))


    except:
        with open("current_currency.txt", "r") as save:
            rates = dict(eval(str(save.readline())))
            check_time = str(save.readline())
    input_usd = rates[input]
    output_usd = rates[output]
    return ["%.6f" % (amount *   output_usd / input_usd), check_time]


def temperature(input, output, temp):
    if input == "Шкала Цельсия":
        if output == "Шкала Кельвина":
            return temp + 273.16
        else:
            return 9 / 5 * temp + 32

    elif input == "Шкала Кельвина":
        if output == "Шкала Цельсия":
            return temp - 273.16
        else:
            return 9 / 5 * (temp - 273.16) + 32

    elif input == "Шкала Фаренгейта":
        if output == "Шкала Цельсия":
            return 5 / 9 * (temp - 32)
        else:
            return 5 / 9 * (temp - 32) + 273.16


def lengths(input, output, amount):
    input_meters = amount * dict_lengths[input]
    return "%.6f" % (input_meters / dict_lengths[output])


def squares(input, output, amount):
    input_meters = amount * dict_squares[input]
    return "%.6f" % (input_meters / dict_squares[output])


def times(input, output, amount):
    input_secs = amount * dict_times[input]
    return "%.6f" % (input_secs / dict_times[output])


def masses(input, output, amount):
    input_kgs = amount * dict_masses[input]
    return "%.6f" % (input_kgs / dict_masses[output])


def volumes(input, output, amount):
    input_meter3 = amount * dict_volumes[input]
    return "%.6f" % (input_meter3 / dict_volumes[output])


def speeds(input, output, amount):
    input_mps = amount * dict_speeds[input]
    return "%.6f" % (input_mps / dict_speeds[output])




