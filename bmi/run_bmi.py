import os
from time import sleep

from tools import headers,calculators
from database import read_databases


def pilih_menu() -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.tampilkan_header_utama()
    print("| [1] Hitung BMI\t\t|")
    print("| [2] Lihat Database\t\t|")
    print("| [3] Exit\t\t\t|")
    print(f"+{31*"="}+")
    return int(input("Silakan pilih menu (1/2/3): "))

def main_bmi():
    while True:
        try:
            pilihan = pilih_menu()
            if pilihan == 1:
                calculators.hitung_dan_simpan_bmi()
            elif pilihan == 2:
                read_databases.tampilkan_database_bmi()
                sleep(2)
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa. 👋\n")
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

if __name__ == "__main__":
    main_bmi()