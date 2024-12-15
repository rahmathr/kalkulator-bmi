import pandas as pd

import os
from tools import headers

def read_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.header_database()
    file_path = "bmr/database/dataframes.csv"

    try:
        content = pd.read_csv(file_path)
        print(content)
        print(f"+{103*'-'}+")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"File kosong: {file_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")

    input("\nTekan Enter untuk melanjutkan...")