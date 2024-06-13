import brc_nanobind as m


DATA_PATH = r"data/measurements_100k.txt"
FIRST_10 = [
    ("Aalten", -93.8, -45.550000000000004, 49.2),
    ("Aarschot", -23.0, 20.62857142857143, 90.8),
    ("Aba", -91.4, -22.349999999999998, 52.3),
    ("Abakan", -94.1, -18.536363636363635, 74.7),
    ("Abano Terme", -73.8, -23.609090909090913, 89.6),
    ("Abasolo", -40.7, 8.51666666666667, 93.2),
    ("Abbots Langley", -77.3, -10.388888888888888, 58.5),
    ("Abbotsford", -95.5, -7.776470588235295, 90.6),
    ("Abdul Hakim", -97.5, 28.311111111111114, 92.8),
    ("Abdulino", -63.3, 18.1, 88.2),
]

LAST_10 = [
    ("Ḩās", -87.9, -1.680000000000001, 90.0),
    ("‘Abasān al Kabīrah", -45.1, 34.17777777777778, 95.2),
    ("‘Afrīn", -86.5, 6.927777777777777, 97.3),
    ("‘Alīābād-e Katūl", -85.6, -4.409999999999995, 96.9),
    ("‘Anbarābād", -77.2, -5.891666666666665, 95.2),
    ("‘Aqrah", -88.1, -14.381818181818181, 88.1),
    ("‘Izbat al Burj", -17.3, 31.46666666666667, 84.1),
    ("‘Ālī Shahr", -83.3, -2.3466666666666653, 75.9),
    ("’Aïn Roua", -97.5, -21.685714285714283, 92.5),
    ("’s-Gravenzande", -79.2, 0.8384615384615384, 94.3),
]


def test_add():
    assert m.add(1, 2) == 3


def test_nanobind_solution():
    data = m.get_weather_data(r"data/measurements_100k.txt")
    assert len(data) == 8838
    assert data[:10] == FIRST_10
    assert data[-10:] == LAST_10


def test_python_solution():
    data = m.get_weather_data_python(r"data/measurements_100k.txt")
    assert len(data) == 8838
    assert data[:10] == FIRST_10
    assert data[-10:] == LAST_10
