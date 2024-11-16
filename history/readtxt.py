import os
from time import sleep
from start import headers  # Pastikan ini sesuai dengan nama fungsi yang benar

def read_file() -> None:
    """
    Membaca dan menampilkan isi dari file data.txt.

    Menampilkan setiap entri dengan nomor urut. Jika file tidak ditemukan,
    akan menampilkan pesan kesalahan.
    """
    os.system("cls" if os.name == "nt" else "clear")  # Bersihkan layar dengan cara yang sesuai
    file_path = "history/data.txt"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            headers.header()  # Memanggil fungsi header
            content = file.readlines()
            for nomor, line in enumerate(content, start=1):  # Menggunakan enumerate untuk nomor urut
                print(f"{nomor}. {line.strip()}")  # Menghilangkan whitespace
    except FileNotFoundError:
        print("\n>>> File tidak ditemukan. Pastikan file 'data.txt' ada di folder 'history'.")

    sleep(5)  # Tunggu 5 detik sebelum keluar
    os.system("cls" if os.name == "nt" else "clear")  # Bersihkan layar setelah menampilkan isi file