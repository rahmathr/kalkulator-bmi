def get_nama() -> str:
    while True:
        nama_input = input('Nama : ')
        if all(x.isalpha() or x.isspace() for x in nama_input):
            return nama_input
        else:
            print("\n>>> Input Harus Berupa Huruf!!\n")

def get_jenis_kelamin() -> str:
    while True:
        jenis_kelamin_input = input("Jenis kelamin (L/P) : ").upper()
        if jenis_kelamin_input in ['L', 'P']:
            return jenis_kelamin_input
        else:
            print("\n>>> Input harus berupa 'L' atau 'P'!!\n")

def get_berat_badan() -> int:
    while True:
        try:
            berat_badan_input = int(input("Berat badan (kg) : "))
            if berat_badan_input > 0:  # Pastikan berat badan positif
                return berat_badan_input
            else:
                print("\n>>> Berat badan harus lebih dari 0!!\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_usia() -> int:
    while True:
        try:
            usia_input = int(input("Usia : "))
            if usia_input > 0:  # Pastikan usia positif
                return usia_input
            else:
                print("\n>>> Usia harus lebih dari 0!!\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")

def get_tinggi_badan() -> int:
    while True:
        try:
            tinggi_badan_input = int(input("Tinggi badan (cm) : "))
            if tinggi_badan_input > 0:  # Pastikan tinggi badan positif
                return tinggi_badan_input
            else:
                print("\n>>> Tinggi badan harus lebih dari 0!!\n")
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")
