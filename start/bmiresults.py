import os
from time import sleep

def simpan_bmi_di_datatxt(hasil):
    file_path = "history/data.txt"
    with open(file_path, "a", encoding='utf-8') as file:
        file.write(f"{hasil.replace('\n','')}\n")

def bmi_kurus(hasil_bmi) -> float:
    status_berat_badan = "KURUS"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan}"
    print(hasil)
    simpan_bmi_di_datatxt(hasil)
    sleep(5)
    os.system("cls")

def bmi_normal(hasil_bmi) -> float:
    status_berat_badan = "NORMAL"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan}✨"
    print(hasil)
    simpan_bmi_di_datatxt(hasil)
    sleep(5)
    os.system("cls")

def bmi_gemuk(hasil_bmi) -> float:
    status_berat_badan = "GEMUK"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan}"
    print(hasil)
    simpan_bmi_di_datatxt(hasil)
    sleep(5)
    os.system("cls")

def bmi_obesitas(hasil_bmi) -> float:
    status_berat_badan = "OBESITAS"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan}"
    print(hasil)
    simpan_bmi_di_datatxt(hasil)
    sleep(5)
    os.system("cls")
