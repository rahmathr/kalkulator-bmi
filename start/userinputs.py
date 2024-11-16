def nama() -> str:
    while True:
        nama = input('Nama : ')
        if nama.isalpha():
            break
        else:
            print("\n>>> Input Harus Berupa Huruf!!\n")
    return nama

def jenis_kelamin() -> str:
    while True:
        jenis_kelamin = input("Jenis kelamin (L/P) : ").upper()
        if jenis_kelamin in ['L', 'P']:
            return jenis_kelamin
        else:
            print("\n>>> Input harus berupa 'L' atau 'P'!!\n")

def berat_badan() -> int:
    while True:
        try:
            berat_badan = int(input("Berat badan (kg) : "))
            return berat_badan
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")

def usia() -> int:
    while True:
        try:
            usia = int(input("Usia : "))
            return usia
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")

def tinggi_badan() -> int:
    while True:
        try:
            tinggi_badan = int(input("Tinggi badan (cm) : "))
            return tinggi_badan
        except ValueError:
            print("\n>>> Input Harus Berupa Angka!!\n")
