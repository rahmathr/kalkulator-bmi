import os
from timesleep import times
from headers import header
def read_file():
    os.system("cls")
    file_path = "bmi/database/data.txt"
    with open(file_path,"r",encoding='utf-8') as file:
        header.header_riwayat()
        content = file.readlines()
        nomor = 0
        for index in content:
            print(f"{nomor}. {index}", end="")
            nomor += 1
    times.clearsleep()