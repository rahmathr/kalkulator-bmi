import pandas as pd

def buat_data():
    list_nama = []
    list_jenis_kelamin = []
    list_berat_badan = []
    list_usia = []
    list_tinggi_badan = []
    list_bmi = []
    list_kategeri = []

    data = {
        "NAMA": [],
        "JENIS KELAMIN" : [],
        "BERAT_BADAN" : [],
        "USIA" : [],
        "TINGGI_BADAN" : [],
        "TINGGI BADAN" : [],
        "BMI" : [],
        "KATEGORI" : []
    }

    data = pd.DataFrame(data)
    print(data)

def read_data():
    pass
