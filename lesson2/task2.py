import json

dict_to_json = {
    "item": "Fender Guitar",
    "quantity": "1",
    "price": "$ 2000",
    "buyer": "Maxim Evlampiev",
    "date": "01.03.2022"
    }


def write_order_to_json():
    with open('j_data.json', 'w') as f_n:
        f_n.write(json.dumps(dict_to_json))

    with open('j_data.json') as f_n:
        print(f_n.read())


write_order_to_json()
