import os
from time import sleep
from typing import Optional

# Import modul-modul yang diperlukan
from start import calculators, userinputs, headers, bmiresults
from history import readtxt

def pilih_menu() -> Optional[str]:
    """
    Menampilkan menu utama dan meminta pilihan pengguna.

    Returns:
        Optional[str]: Pilihan pengguna atau None jika keluar.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header()
    print("A. START")
    print("B. HISTORY")
    print("C. DATABASE")
    print("D. EXIT\n")

    return input(">>> [A/B/C/D] : ").strip().upper()

def proses_bmi() -> None:
    """
    Memproses perhitungan BMI dengan input dari pengguna.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header()

    # Kumpulkan input pengguna
    nama = userinputs.get_nama()
    jenis_kelamin = userinputs.get_jenis_kelamin()
    berat_badan = userinputs.get_berat_badan()
    usia = userinputs.get_usia()
    tinggi_badan = userinputs.get_tinggi_badan()

    # Hitung BMI
    hasil_bmi = calculators.kalkulator_bmi(tinggi_badan, berat_badan)

    # Kategorikan BMI
    try:
        if hasil_bmi < 18.5:
            bmiresults.bmi_kurus(hasil_bmi)
        elif hasil_bmi <= 25:
            bmiresults.bmi_normal(hasil_bmi)
        elif 25 <= hasil_bmi <= 30:
            bmiresults.bmi_gemuk(hasil_bmi)
        elif hasil_bmi > 30:
            bmiresults.bmi_obesitas(hasil_bmi)
        else:
            print("Hasil Tidak Ditemukan 🤖")
    except Exception as e:
        print(f"Terjadi kesalahan dalam perhitungan: {e}")
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
                readtxt.read_file()
            elif pilihan == 'C':
                print("COMING SOON 🚧")
                sleep(2)
            elif pilihan == 'D':
                print("Terima kasih! Sampai jumpa. 👋")
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