import os
from time import sleep

def jenis_kelamin(jenis_kelamin: str = None) :
  if jenis_kelamin is None:
    jenis_kelamin = ["L,P"]
  return str(input("Jenis kelamin (L/P) : "))

def pilihan_gender_1() -> str:
  pass

def pilihan_gender_2() -> str:
  print("\nGunakan Huruf Kapital, Silahkan ulangi kembali! 😊")
  sleep(3)
  os.system('cls')

def pilihan_gender_3() -> str:
  print("\nInput yang anda masukkan salah! Silahkan input yang benar.")
  sleep(3)
  os.system('cls')