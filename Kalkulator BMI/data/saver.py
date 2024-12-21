def simpan_hasil_bmi(nama: str, jenis_kelamin: str, berat_badan: int, usia: int, tinggi_badan: int, bmi: int, status_berat_badan: str):
    file_path = "Kalkulator BMI/data/dataframe.csv"
    try:
        with open(file_path, "a", encoding='utf-8') as file:
            file.write(f"{nama},{jenis_kelamin},{berat_badan},{usia},{tinggi_badan},{int(bmi)},{status_berat_badan}\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan hasil BMI: {e}")