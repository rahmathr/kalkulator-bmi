def get_nama_lengkap() -> str:
    while True:
        nama_lengkap_input = input('Nama Lengkap: ').strip().capitalize()
        # Memeriksa apakah nama hanya terdiri dari huruf, spasi, dan karakter tambahan yang valid
        if all(x.isalpha() or x.isspace() or x in "'-." for x in nama_lengkap_input):
            return nama_lengkap_input
        else:
            print("\n>>> Input Harus Berupa Huruf dan Spasi!!\n")

def get_jenis_kelamin() -> str:
    while True:
        jenis_kelamin_input = input("Jenis kelamin (L/P) : ").strip().upper()
        if jenis_kelamin_input in ['L', 'P']:
            return jenis_kelamin_input
        else:
            print("\n>>> Input harus berupa 'L' atau 'P'!!\n")

def get_berat_badan() -> int:
    while True:
        try:
            berat_badan_input = int(input("Berat badan (kg) : "))
            if 0 < berat_badan_input <= 300:  # Pastikan berat badan positif dan masuk akal
                return berat_badan_input
            else:
                print("\n>>> Berat badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_usia() -> int:
    while True:
        try:
            usia_input = int(input("Usia : "))
            if 0 < usia_input <= 120:  # Pastikan usia positif dan masuk akal
                return usia_input
            else:
                print("\n>>> Usia harus lebih dari 0 dan kurang dari atau sama dengan 120!!\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_tinggi_badan() -> int:
    while True:
        try:
            tinggi_badan_input = int(input("Tinggi badan (cm) : "))
            if 0 < tinggi_badan_input <= 300:  # Pastikan tinggi badan positif dan masuk akal
                return tinggi_badan_input
            else:
                print("\n>>> Tinggi badan harus lebih dari 0 dan kurang dari atau sama dengan 300!!\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")