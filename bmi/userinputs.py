def nama():
  nama = str(input('Nama : '))
  return nama
def jenis_kelamin():
  jenis_kelamin = str(input("Jenis kelamin (L/P) : "))
  return jenis_kelamin
def berat_badan():
  while True:
    try:
      berat_badan = int(input("Berat badan (kg) : "))
      return berat_badan
    except ValueError:
      print(">>> \nInput Harus Berupa Angka!!")
      continue
def usia():
  while True:
    try:
      usia = int(input("Usia : "))
      return usia
    except ValueError:
      print(">>> \nInput Harus Berupa Angka!!")
      continue
def tinggi_badan():
  while True:
    try:
      tinggi_badan = int(input("Tanggi badan (cm) : "))
      return tinggi_badan
    except ValueError:
      print(">>> \nInput Harus Berupa Angka!!")
      continue