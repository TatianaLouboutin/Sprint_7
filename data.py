class TestDataCreateOrder:

    ORDER_BLACK_COLOR = {
        "firstName": "Татьяна ",
        "lastName": "Ерина",
        "address": "Учебная, 142",
        "metroStation": 7,
        "phone": "+7 901 3554 35 35",
        "rentTime": 1,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", ""]
    }

    ORDER_GREY_COLOR = {
        "firstName": "Кэтрин",
        "lastName": "Фокина",
        "address": "Яковлева, 22",
        "metroStation": 6,
        "phone": "+7 904 4777 35 35",
        "rentTime": 2,
        "deliveryDate": "2024-06-05",
        "comment": "Saske, come back to Konoha",
        "color": ["GREY", ""]
    }

    ORDER_WITHOUT_COLORS = {
        "firstName": "Натали",
        "lastName": "Воробей",
        "address": "Усова, 75",
        "metroStation": 5,
        "phone": "+7 909 3554 35 35",
        "rentTime": 3,
        "deliveryDate": "2024-06-07",
        "comment": "Saske, come back",
        "color": []
    }

    ORDER_TWO_COLORS = {
        "firstName": "Никита",
        "lastName": "Трифонов",
        "address": "Ленина, 69",
        "metroStation": 4,
        "phone": "+7 903 3555 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-06-26",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GRAY"]
    }

    LST_ORDERS = [ORDER_BLACK_COLOR, ORDER_GREY_COLOR, ORDER_WITHOUT_COLORS, ORDER_TWO_COLORS]