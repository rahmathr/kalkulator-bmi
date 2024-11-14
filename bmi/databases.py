from time import sleep
import pandas as pd
import os
def database():
    os.system("cls")
    data = {
        "Nama": [],
        "JenisKelamin" : [],
        "BeratBadan" : [],
        "Usia": [],
        "TinggiBadan" : [],
    }

    hasil_data = pd.DataFrame(data)
    print(hasil_data)

    sleep(5)
    os.system("cls")

database()


