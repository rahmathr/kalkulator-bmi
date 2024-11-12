def berat_badan(berat_badan:int=0):
    while True:
      try:
        return int(input("Berat badan (kg)    : "))
      except Exception:
        print("")
        print(">> Input Harus Berupa Angka!!")
        print("")
        continue

def usia(usia:int=0):
  while True:
    try:
      return int(input("Usia                : "))
    except Exception:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue

def tinggi_badan(tinggi_badan:int=0):
  while True:
    try:
      return int(input("Tanggi badan (cm)   : "))
    except Exception:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue