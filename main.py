import os
from datetime import datetime
from time import sleep
from typing import Optional

# Import modul-modul yang diperlukan
from start import bmi, user_inputs, headers
# from database import read_database

def pilih_menu() -> str:
    """
    Menampilkan menu utama dan meminta pilihan pengguna.

    Returns:
        str: Pilihan pengguna.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header()
    print(f"\n🗓️  {datetime.now().year}-{datetime.now().month}-{datetime.now().day}\n")

    print("A. START")
    print("B. DATABASE")
    print("C. EXIT\n")

    return input(">>> [A/B/C/D] : ").strip().upper()

def proses_bmi() -> None:
    """
    Memproses perhitungan BMI dengan input dari pengguna.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header()

    # Kumpulkan input pengguna
    nama = user_inputs.get_nama()
    jenis_kelamin = user_inputs.get_jenis_kelamin()
    berat_badan = user_inputs.get_berat_badan()
    usia = user_inputs.get_usia()
    tinggi_badan = user_inputs.get_tinggi_badan()

    # Hitung BMI
    try:
        hasil_bmi = bmi.kalkulator_bmi(tinggi_badan, berat_badan)

        # Kategorikan BMI
        if hasil_bmi < 18.5:
            bmi.bmi_kurus(hasil_bmi)
        elif hasil_bmi <= 25:
            bmi.bmi_normal(hasil_bmi)
        elif 25 < hasil_bmi <= 30:
            bmi.bmi_gemuk(hasil_bmi)
        else:  # hasil_bmi > 30
            bmi.bmi_obesitas(hasil_bmi)
    except Exception as e:
        print(f"Terjadi kesalahan dalam perhitungan BMI: {e}")
        sleep(3)

def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    while True:
        try:
            pilihan = pilih_menu()

            if pilihan == 'A':
                proses_bmi()
            elif pilihan == 'B':
                print("\nCOMING SOON 🚧")
                sleep(2)
            elif pilihan == 'C':
                print("\nTerima kasih! Sampai jumpa. 👋")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih A/B/C/D.")
                sleep(2)

        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            sleep(2)

if __name__ == "__main__":
    main()