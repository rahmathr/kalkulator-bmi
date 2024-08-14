from time import sleep
from bmi_calculator.header import header

def berat_badan(berat_badan=0) -> int:
  while True:
    try:
      berat_badan = int(input("Berat badan (kg)    : "))
      return berat_badan
    except:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue

def usia(usia=0) -> int:
  while True:
    try:
      usia = int(input("Usia                : "))
      return usia
    except:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue

def tinggi_badan(tinggi_badan=0) -> int:
  while True:
    try:
      tinggi_badan = int(input("Tanggi badan (cm)   : "))
      return tinggi_badan
    except:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue