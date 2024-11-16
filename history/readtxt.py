import os
from time import sleep
from start import headers

def read_file():
    os.system("cls")
    file_path = "history/data.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            headers.header()
            content = file.readlines()
            nomor = 1  # Dimulai dari 1
            for index in content:
                print(f"{nomor}. {index.strip()}")  # Menghilangkan whitespace
                nomor += 1
    except FileNotFoundError:
        print("\n>>> File tidak ditemukan. Pastikan file 'data.txt' ada di folder 'history'.")
    sleep(5)
    os.system
