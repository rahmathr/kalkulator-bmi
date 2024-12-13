import pandas as pd
from tools import headers
import os

def tampilkan_database_bmi():
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.tampilkan_header_database()
    file_path = "bmi/database/dataframe.csv"

    try:
        content = pd.read_csv(file_path)
        print(content)
        print(f"+{87*"="}+")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"File kosong: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

    input("\nTekan Enter untuk melanjutkan...")