import os
from time import sleep

def jenis_kelamin(jenis_kelamin: str=["L,P"]):
  """
  Meminta input jenis kelamin dari pengguna.

  Parameters:
  jenis_kelamin (str, optional): Placeholder untuk input jenis kelamin pengguna. Default adalah ['L,P'].

  Returns:
  str: Jenis kelamin yang dimasukkan oleh pengguna.
  """
  jenis_kelamin = str(input("Jenis kelamin (L/P) : "))
  return jenis_kelamin

def pilihan_gender_1() -> str:
  """
  Placeholder function untuk pilihan gender 1.
  """
  pass

def pilihan_gender_2() -> str:
  """
  Menampilkan pesan untuk menggunakan huruf kapital dan mengulang input,
  kemudian membersihkan layar setelah 3 detik.
  """
  print("\nGunakan Huruf Kapital, Silahkan ulangi kembali! 😊")
  sleep(3)
  os.system('cls')

def pilihan_gender_3() -> str:
  """
  Menampilkan pesan kesalahan input dan meminta pengguna untuk memasukkan input yang benar,
  kemudian membersihkan layar setelah 3 detik.
  """
  print("\nInput yang anda masukkan salah! Silahkan input yang benar.")
  sleep(3)
  os.system('cls')