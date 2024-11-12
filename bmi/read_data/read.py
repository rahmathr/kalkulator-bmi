import os
from time import sleep
def read_file():
    os.system("cls")
    file_path = "bmi/database/data.txt"
    with open(file_path,"r",encoding='utf-8') as file:
        content = file.readlines()
        nomor = 0
        for index in content:
            print(f"{nomor}. {index}")
            nomor += 1
    sleep(5)
    os.system("cls")