def simpan_bmi_di_database(hasil: str) -> None:
    file_path = "database/dataframe.csv"
    try:
        with open(file_path,"a", encoding='utf-8') as file:
            pass
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan hasil BMI: {e}")
