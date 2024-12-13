import os
import pandas as pd
from tools import headers

def read_database():
    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar untuk semua platform
    headers.header_database()
    file_path = "bmr/database/dataframes.csv"

    try:
        content = pd.read_csv(file_path)
        print(content)
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"File kosong: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

    input("\nTekan Enter untuk melanjutkan...")  # Menunggu input pengguna sebelum melanjutkan