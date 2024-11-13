def berat_badan(berat_badan:int=0):
    while True:
      try:
        return int(input("Berat badan (kg)\t: "))
      except Exception:
        print("") 
        print(">> Input Harus Berupa Angka!!")
        print("")
        continue

def usia(usia:int=0):
  while True:
    try:
      return int(input("Usia\t\t\t: "))
    except Exception:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue

def tinggi_badan(tinggi_badan:int=0):
  while True:
    try:
      return int(input("Tanggi badan (cm)\t: "))
    except Exception:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue