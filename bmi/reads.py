import os
from bmi import times
from bmi import headers
def read_file():
    os.system("cls")
    file_path = "bmi/data.txt"
    with open(file_path,"r",encoding='utf-8') as file:
        headers.header_riwayat()
        content = file.readlines()
        nomor = 0
        for index in content:
            print(f"{nomor}. {index}", end="")
            nomor += 1
    times.clearsleep()