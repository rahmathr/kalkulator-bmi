import os
from datetime import datetime
from time import sleep

# Import modul-modul yang diperlukan
from start import bmi, user_inputs, headers
from database import read_databases

def pilih_menu() -> str:
    """
    Menampilkan menu utama dan meminta pilihan pengguna.

    Returns:
        str: Pilihan pengguna.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header()
    print(f"\n🗓️  {datetime.now().strftime('%Y-%m-%d')}\n")

    print("A. START")
    print("B. DATABASE")
    print("C. EXIT\n")

    return input(">>> [A/B/C] : ").strip().upper()

def proses_bmi() -> None:
    """
    Memproses perhitungan BMI dengan input dari pengguna.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header()

    # Kumpulkan input pengguna
    try:
        nama = user_inputs.get_nama_lengkap()
        jenis_kelamin = user_inputs.get_jenis_kelamin()
        berat_badan = user_inputs.get_berat_badan()
        usia = user_inputs.get_usia()
        tinggi_badan = user_inputs.get_tinggi_badan()

        # Hitung BMI
        hasil_bmi = bmi.kalkulator_bmi(tinggi_badan, berat_badan)

        # Kategorikan BMI
        if hasil_bmi < 18.5:
            bmi.bmi_kurus(hasil_bmi)
            simpan_proses_bmi(nama, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Kurus")
        elif hasil_bmi <= 25:
            bmi.bmi_normal(hasil_bmi)
            simpan_proses_bmi(nama, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Normal")
        elif 25 < hasil_bmi <= 30:
            bmi.bmi_gemuk(hasil_bmi)
            simpan_proses_bmi(nama, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Gemuk")
        else:  # hasil_bmi > 30
            bmi.bmi_obesitas(hasil_bmi)
            simpan_proses_bmi(nama, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Obesitas")

    except ValueError as e:
        print(f"Input tidak valid: {e}")
        sleep(2)
        proses_bmi()  # Memungkinkan pengguna untuk mencoba lagi
    except Exception as e:
        print(f"Terjadi kesalahan dalam perhitungan BMI: {e}")
        sleep(3)

# Simpan proses BMI
def simpan_proses_bmi(nama: str, jenis_kelamin: str, berat_badan: int, usia: int, tinggi_badan: int, hasil_bmi: float, status_berat_badan: str = None) -> None:
    file_path = "database/dataframe.csv"
    try:
        with open(file_path, "a", encoding='utf-8') as file:
            file.write(f"{nama},{jenis_kelamin},{berat_badan},{usia},{tinggi_badan},{hasil_bmi:.2f},{status_berat_badan}\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan hasil BMI: {e}")

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

if __name__ == "__main__":
    main()