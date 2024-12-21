import os
from time import sleep

from utils.calculators import hitung_dan_simpan_bmi
from utils.display_headers import tampilkan_header_utama
from data.reader import tampilkan_database_bmi

def pilih_menu() -> str:
    os.system('cls' if os.name == 'nt' else 'clear')
    tampilkan_header_utama()
    print(f"| [1] Hitung BMI{7*"\t"}|")
    print(f"| [2] Lihat Database{7*"\t"}|")
    print(f"| [3] Exit{8*"\t"}|")
    print(f"+{71*"-"}+")
    return int(input("Silakan pilih menu (1/2/3): "))

def main_bmi():
    while True:
        try:
            pilihan = pilih_menu()
            if pilihan == 1:
                hitung_dan_simpan_bmi()
            elif pilihan == 2:
                tampilkan_database_bmi()
                sleep(2)
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa. 👋\n")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih 1/2/3.")
                input("\nTekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            sleep(2)

if __name__ == "__main__":
    main_bmi()