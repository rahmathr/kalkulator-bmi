import os
from time import sleep
from typing import Union  # Tambahkan import untuk type hinting

def simpan_bmi_di_datatxt(hasil: str) -> None:
    """
    Menyimpan hasil BMI ke file data.txt

    Args:
        hasil (str): Hasil perhitungan BMI yang akan disimpan
    """
    # Pastikan direktori 'history' ada
    os.makedirs('history', exist_ok=True)

    file_path = "history/data.txt"
    with open(file_path, "a", encoding='utf-8') as file:
        file.write(f"{hasil.replace('\n','')}\n")

def tampilkan_hasil_bmi(hasil_bmi: float, status_berat_badan: str) -> None:
    """
    Fungsi umum untuk menampilkan hasil BMI

    Args:
        hasil_bmi (float): Nilai BMI
        status_berat_badan (str): Status berat badan
    """
    # Tambahkan emoji sesuai kondisi
    emoji_map = {
        "KURUS": "",
        "NORMAL": "✨",
        "GEMUK": "⚠️",
        "OBESITAS": "🚨"
    }

    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan} {emoji_map.get(status_berat_badan, '')}"

    print(hasil)
    simpan_bmi_di_datatxt(hasil)

    # Tunggu sebentar dan bersihkan layar
    sleep(5)

    # Gunakan cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi-fungsi spesifik status BMI dapat disederhanakan
def bmi_kurus(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori kurus"""
    tampilkan_hasil_bmi(hasil_bmi, "KURUS")

def bmi_normal(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori normal"""
    tampilkan_hasil_bmi(hasil_bmi, "NORMAL")

def bmi_gemuk(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori gemuk"""
    tampilkan_hasil_bmi(hasil_bmi, "GEMUK")

def bmi_obesitas(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori obesitas"""
    tampilkan_hasil_bmi(hasil_bmi, "OBESITAS")