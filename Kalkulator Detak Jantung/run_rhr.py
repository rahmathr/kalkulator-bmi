import os

from utils.display_headers import tampilan_header_utama

def pilih_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    tampilan_header_utama()
    print(f"| [1] Hitung RHR{8*"\t"} |")
    print(f"| [2] Lihat Database{8*"\t"} |")
    print(f"| [3] Exit{9*"\t"} |")
    print(f"+{80*"-"}+")
    return int(input("Silahkan pilih menu (1/2/3): "))

def main():
    while True:
        try:
            pilihan:str = pilih_menu()
            if pilihan == 1:
                pass
            elif pilihan == 2:
                pass
            elif pilihan == 3:
                print("\nTerima kasih! Sampai jumpa. 👋")
                break
            else:
                print("\nPilihan Tidak Valid. Silakan pilih 1/2/3.")
                input("\nTekan enter untuk melanjutkan...")
        except:
            pass

if __name__ == "__main__":
    main()