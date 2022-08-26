from pprint import pprint
from bson.objectid import ObjectId # for ObjectId to print readable format
from dateutil.parser import parse # for parse date string to datetime.datetime format simce python cant handle ISODate format

class Dataset:
    dataset1 = [
        {
            "_id": "62e5288f4d0440f7811d1928",
            "name": "United States",
            "capital": "Washington, D.C.",
            "continent": "North America",
            "language": "English",
            "population": 328239523,
        },
        {
            "_id": "62e5288f4d0440f7811d192b",
            "name": "Australia",
            "capital": "Canberra",
            "continent": "Australia",
            "language": "English",
            "population": 25681300,
        },
        {
            "_id": "62e5288f4d0440f7811d192c",
            "name": "Japan",
            "capital": "Tokyo",
            "continent": "Asia",
            "language": "Japanese",
            "population": 125960000,
        },
        {
            "_id": "62e5288f4d0440f7811d192d",
            "name": "Brazil",
            "capital": "Brasília",
            "continent": "South America",
            "language": "Portuguese",
            "population": 210147125,
        },
    ]

    dataset2 = [
        {"_id": 1, "grades": [85, 80, 80]},
        {"_id": 2, "grades": [88, 90, 92]},
        {"_id": 3, "grades": [85, 100, 90]},
    ]

    dataset3 = [
        {
            "_id": 4,
            "grades": [
                {"grade": 80, "mean": 75, "std": 8},
                {"grade": 85, "mean": 90, "std": 5},
                {"grade": 85, "mean": 85, "std": 8},
            ],
        }
    ]

    dataset4 = [
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "A",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
    ]

    dataset5 = [{"_id": 1, "colors": ["blue", "green", "red"]}]

    dataset6 = [{"_id": 1, "scores": [8, 9, 10]}]

    dataset7 = [
        {
            "_id": 1,
            "fruits": ["apples", "pears", "oranges", "grapes", "bananas"],
            "vegetables": ["carrots", "celery", "squash", "carrots"],
        },
        {
            "_id": 2,
            "fruits": ["plums", "kiwis", "oranges", "bananas", "apples"],
            "vegetables": ["broccoli", "zucchini", "carrots", "onions"],
        },
    ]

    dataset8 = [{"_id": 1, "votes": [3, 5, 6, 7, 7, 8]}]

    dataset9 = [
        {
            "_id": ObjectId("5234cc89687ea597eabee675"),
            "code": "xyz",
            "tags": ["school", "book", "bag", "headphone", "appliance"],
            "qty": [
                {"size": "S", "num": 10, "color": "blue"},
                {"size": "M", "num": 45, "color": "blue"},
                {"size": "L", "num": 100, "color": "green"},
            ],
        },
        {
            "_id": ObjectId("5234cc8a687ea597eabee676"),
            "code": "abc",
            "tags": ["appliance", "school", "book"],
            "qty": [
                {"size": "6", "num": 100, "color": "green"},
                {"size": "6", "num": 50, "color": "blue"},
                {"size": "8", "num": 100, "color": "brown"},
            ],
        },
        {
            "_id": ObjectId("5234ccb7687ea597eabee677"),
            "code": "efg",
            "tags": ["school", "book"],
            "qty": [
                {"size": "S", "num": 10, "color": "blue"},
                {"size": "M", "num": 100, "color": "blue"},
                {"size": "L", "num": 100, "color": "green"},
            ],
        },
        {
            "_id": ObjectId("52350353b2eff1353b349de9"),
            "code": "ijk",
            "tags": ["electronics", "school"],
            "qty": [{"size": "M", "num": 100, "color": "green"}],
        },
    ]

    dataset10 = [
        {
            "_id": 1,
            "results": [
                {"product": "abc", "score": 10},
                {"product": "xyz", "score": 5},
            ],
        },
        {
            "_id": 2,
            "results": [{"product": "abc", "score": 8}, {"product": "xyz", "score": 7}],
        },
        {
            "_id": 3,
            "results": [{"product": "abc", "score": 7}, {"product": "xyz", "score": 8}],
        },
        {
            "_id": 4,
            "results": [{"product": "abc", "score": 7}, {"product": "def", "score": 8}],
        },
    ]

    dataset11 = [
        {
            "_id": 5,
            "quizzes": [
                {"wk": 1, "score": 10},
                {"wk": 2, "score": 8},
                {"wk": 3, "score": 5},
                {"wk": 4, "score": 6},
            ],
        }
    ]

    dataset12 = [{"_id": 1, "scores": [0, 2, 5, 5, 1, 0]}]

    dataset13 = [
        {
            "_id": 0,
            "name": "Pepperoni",
            "size": "small",
            "price": 19,
            "quantity": 10,
            "date": parse("2021-03-13T08:14:30Z"),
        },
        {
            "_id": 1,
            "name": "Pepperoni",
            "size": "medium",
            "price": 20,
            "quantity": 20,
            "date": parse("2021-03-13T09:13:24Z"),
        },
        {
            "_id": 2,
            "name": "Pepperoni",
            "size": "large",
            "price": 21,
            "quantity": 30,
            "date": parse("2021-03-17T09:22:12Z"),
        },
        {
            "_id": 3,
            "name": "Cheese",
            "size": "small",
            "price": 12,
            "quantity": 15,
            "date": parse("2021-03-13T11:21:39.736Z"),
        },
        {
            "_id": 4,
            "name": "Cheese",
            "size": "medium",
            "price": 13,
            "quantity": 50,
            "date": parse("2022-01-12T21:23:13.331Z"),
        },
        {
            "_id": 5,
            "name": "Cheese",
            "size": "large",
            "price": 14,
            "quantity": 10,
            "date": parse("2022-01-12T05:08:13Z"),
        },
        {
            "_id": 6,
            "name": "Vegan",
            "size": "small",
            "price": 17,
            "quantity": 10,
            "date": parse("2021-01-13T05:08:13Z"),
        },
        {
            "_id": 7,
            "name": "Vegan",
            "size": "medium",
            "price": 18,
            "quantity": 10,
            "date": parse("2021-01-13T05:10:13Z"),
        },
    ]
