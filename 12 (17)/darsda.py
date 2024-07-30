data = dict()

[
    {
        "title": "BAA dirhami",
        "code": "AED",
        "cb_price": "3435.74",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Avstraliya dollari",
        "code": "AUD",
        "cb_price": "8345.49",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Kanada dollari",
        "code": "CAD",
        "cb_price": "9197.46",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Shveytsariya franki",
        "code": "CHF",
        "cb_price": "13915.35",
        "nbu_buy_price": "13600.00",
        "nbu_cell_price": "14400.00",
        "date": "31.05.2024"
    },
    {
        "title": "Xitoy yuani",
        "code": "CNY",
        "cb_price": "1743.60",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Daniya kronasi",
        "code": "DKK",
        "cb_price": "1829.31",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Misr funti",
        "code": "EGP",
        "cb_price": "266.92",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Yevro",
        "code": "EUR",
        "cb_price": "13645.82",
        "nbu_buy_price": "13450.00",
        "nbu_cell_price": "13650.00",
        "date": "31.05.2024"
    },
    {
        "title": "Angliya funt sterlingi",
        "code": "GBP",
        "cb_price": "16043.59",
        "nbu_buy_price": "15800.00",
        "nbu_cell_price": "16500.00",
        "date": "31.05.2024"
    },
    {
        "title": "Islandiya kronasi",
        "code": "ISK",
        "cb_price": "91.52",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Yaponiya iyenasi",
        "code": "JPY",
        "cb_price": "80.41",
        "nbu_buy_price": "70.00",
        "nbu_cell_price": "90.00",
        "date": "31.05.2024"
    },
    {
        "title": "Koreya respublikasi voni",
        "code": "KRW",
        "cb_price": "9.17",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Quvayt dinori",
        "code": "KWD",
        "cb_price": "41133.74",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Qozog‘iston tengesi",
        "code": "KZT",
        "cb_price": "28.35",
        "nbu_buy_price": "15.00",
        "nbu_cell_price": "30.00",
        "date": "31.05.2024"
    },
    {
        "title": "Livan funti",
        "code": "LBP",
        "cb_price": "0.14",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Malayziya ringgiti",
        "code": "MYR",
        "cb_price": "2682.79",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Norvegiya kronasi",
        "code": "NOK",
        "cb_price": "1194.96",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Polsha zlotiysi",
        "code": "PLN",
        "cb_price": "3182.65",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Rossiya rubli",
        "code": "RUB",
        "cb_price": "140.36",
        "nbu_buy_price": "100.00",
        "nbu_cell_price": "150.00",
        "date": "31.05.2024"
    },
    {
        "title": "Shvetsiya kronasi",
        "code": "SEK",
        "cb_price": "1186.61",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Singapur dollari",
        "code": "SGD",
        "cb_price": "9338.34",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Turkiya lirasi",
        "code": "TRY",
        "cb_price": "390.59",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "Ukraina grivnasi",
        "code": "UAH",
        "cb_price": "311.64",
        "nbu_buy_price": "",
        "nbu_cell_price": "",
        "date": "31.05.2024"
    },
    {
        "title": "AQSh dollari",
        "code": "USD",
        "cb_price": "12619.83",
        "nbu_buy_price": "12580.00",
        "nbu_cell_price": "12660.00",
        "date": "31.05.2024"
    }
]

def currency_exchange():

    soum = int("Enter your soum: ")
    code = input("enter a currency code: ")

    for currency in data:
        if data["code"] == code:
            result = data["cb_curreny" ]


def current_price():
    code = input("Eneter a code: ").upper()
    for currency in data():
        if currency["code"] == code:
            text = "the price for ", currency[code], "is ", currency["cb_price"] 
            print(text)
            return show_menu()
    print("Wrong code")
    return current_price()

def currency_title():

    new_list = []

    code = input("Eneter a currency name: ").lower()
    for currency in data:
        if code in currency["title"].lower():
            new_list.append(currency["title"], currency["code"], currency["cb_price"])
            
    if new_list:
        for items in new_list:
            print(f"Title: {items[0]}, Code: {items[1]}, Exchange Rate: {items[2]}")
    else:
        print("Wrong title")
        return currency_title()

def show_menu():
    text = """
    1. Exchange the currency: 
    2. Other currency in soum:
    3. FromTo exchange: 
    4. Search with title: 
    5. Exit: 
    """
    print(text)

    user_input = int(input("Choose from menu: "))
    if user_input == 1:
        pass
    elif user_input == 2:
        current_price()
    elif user_input == 4:
        currency_title()
    else:
        print("Good bye !!!")
        return

show_menu()



# def currancy_exchange(money: float, currency: str) -> float:
#     for currency in data():
#         for key, value in currency.items():
#             if value["code"] == currency:
#                 changed_value = money / value["cb_price"]
#                 print(f"your converted money will be: ", changed_value)


# user_money = float(input("enter your money value: "))
# wanted_currency = input("enter a currency code: ")

# result = currancy_exchange(user_money, wanted_currency)
# print(result)


