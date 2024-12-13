def get_nama_lengkap() -> str:
    while True:
        nama_lengkap_input = input("Nama Lengkap : ").strip().title()
        if all(x.isalpha() or x.isspace() or x in "'-." for x in nama_lengkap_input):
            return nama_lengkap_input
        else:
            print("\n>>> Input Harus Berupa Huruf dan Spasi!!\n")

def get_usia() -> int:
    while True:
        try:
            usia_input = int(input("Usia anda : "))
            if 0 <= usia_input <= 120:
                return usia_input
            else:
                print("\n>>> Usia harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_jenis_kelamin() -> str:
    while True:
        jenis_kelamin_input = input("Apa jenis kelamin Anda? (L/P) : ").strip().upper()
        if jenis_kelamin_input in ["L","l"]:
            return jenis_kelamin_input
        else:
            print("\n>>> Input harus berupa 'L' atau 'P'!!\n")

def get_tinggi_badan() -> int:
    while True:
        try:
            tinggi_badan_input = int(input("Berapa tinggi Anda? (cm) : "))
            if 0 < tinggi_badan_input <= 300:
                return tinggi_badan_input
            else:
                print("\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_berat_badan() -> int:
    while True:
        try:
            berat_badan_input = int(input("Berapa berat badan Anda? (kg) : "))
            if 0 < berat_badan_input <= 300:
                return berat_badan_input
            else:
                print("\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_intensitas_aktivitas() -> int:
    while True:
        try:
            total_kalori = int(input("Pilih tingkat intensitas aktivitas fisik Anda : "))
            if total_kalori in (1,2,3):
                return total_kalori
            else:
                print("\n>>> Pilihan tidak valid. Harap pilih 1, 2, atau 3.\n")
        except:
            print("\n>>> Input Harus Berupa Angka!!\n")

        return total_kalori
