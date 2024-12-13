import os
from time import sleep
from datetime import datetime
from tools import calculators, headers
from database import read_databases

def pilih_menu() -> str:
    """
    Menampilkan menu utama dan meminta pilihan pengguna.
    Returns:
        str: Pilihan menu yang diinput pengguna
    """
    os.system("cls")
    headers.header()
    print(f"\n🗓️  {datetime.now().strftime('%Y-%m-%d')}\n")
    print("A. BMR")
    print("B. DATABASE")
    print("C. EXIT\n")
    return input(">>> (A/B/C) : ").strip().upper()

def main_bmr():
    """
    Fungsi utama untuk menjalankan program kalkulator BMR.
    Menangani navigasi menu dan menghandle berbagai kemungkinan kesalahan.
    """
    while True:
        try:
            pilihan = pilih_menu()
            if pilihan == 'A':
                calculators.hitung_kebutuhan_kalori()
            elif pilihan == 'B':
                read_databases.read_database()
                sleep(2)
            elif pilihan == 'C':
                print("\nTerima kasih! Sampai jumpa. 👋")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih A/B/C.")
                sleep(2)
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            sleep(2)

main_bmr()