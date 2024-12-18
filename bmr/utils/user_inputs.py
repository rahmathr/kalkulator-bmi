def input_nama_lengkap() -> str:
    while True:
        nama_lengkap = input("Nama Lengkap : ").strip().title()
        if all(x.isalpha() or x.isspace() or x in "'-." for x in nama_lengkap):
            return nama_lengkap
        else:
            print("\n>>> Input Harus Berupa Huruf dan Spasi!!\n")

def input_umur() -> int:
    while True:
        try:
            umur = int(input("Umur : "))
            if 0 <= umur <= 120:
                return umur
            else:
                print("\n>>> Usia harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

def input_jenis_kelamin() -> str:
    while True:
        jenis_kelamin = input("Apa jenis kelamin Anda? (L/P) : ").strip().upper()
        if jenis_kelamin in ["L","l"]:
            return jenis_kelamin
        else:
            print("\n>>> Input harus berupa 'L' atau 'P'!!\n")

def input_tinggi_badan() -> int:
    while True:
        try:
            tinggi_badan = int(input("Berapa tinggi Anda? (cm) : "))
            if 0 < tinggi_badan <= 300:
                return tinggi_badan
            else:
                print("\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

def input_berat_badan() -> int:
    while True:
        try:
            berat_badan = int(input("Berapa berat badan Anda? (kg) : "))
            if 0 < berat_badan <= 300:
                return berat_badan
            else:
                print("\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

def input_intensitas_aktivitas() -> int:
    while True:
        try:
            total_kalori = int(input("Pilih tingkat intensitas aktivitas fisik Anda : "))
            if total_kalori in (1,2,3):
                return total_kalori
            else:
                print("\n>>> Pilihan tidak valid. Harap pilih 1, 2, atau 3.\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")
