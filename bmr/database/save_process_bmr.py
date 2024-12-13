def simpan_proses_bmr(nama_lengkap: str, jenis_kelamin: str, berat_badan: int, usia: int, tinggi_badan: int, bmr: int, total_kalori: int):
    file_path = "bmr/database/dataframes.csv"
    try:
        with open(file_path, "a", encoding='utf-8') as file:
            file.write(f"{nama_lengkap},{jenis_kelamin},{berat_badan},{usia},{tinggi_badan},{int(bmr)},{int(total_kalori)}\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan hasil BMI: {e}")