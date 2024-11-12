import os
from input_user import type_gender, user
from time import sleep
from headers import headers
from calculator_result import calculator, result
from read_data import read
os.system('cls')
if __name__ == "__main__":
  while True:
    headers.header()
    print("A. RIWAYAT")
    print("B. START\n")
    pilihan_pertama = str(input("Pilihan (A/B) : "))
    if pilihan_pertama == "A":
      read.read_file()
    elif pilihan_pertama == "B":
      os.system("cls")
      headers.header()
      jenis_kelamin =  type_gender.jenis_kelamin()
      if jenis_kelamin in ["L", "P"]:
          type_gender.pilihan_gender_1()
      elif jenis_kelamin in ["l", "p"]:
          type_gender.pilihan_gender_2()
      else:
          type_gender.pilihan_gender_3()
      berat_badan = user.berat_badan()
      usia = user.usia()
      tinggi_badan = user.tinggi_badan()
      hasil_bmi = calculator.calculate_bmi(tinggi_badan,berat_badan)
      if  hasil_bmi < 18.5:
          result.bmi_kurus(hasil_bmi)
      elif hasil_bmi <= 25:
          result.bmi_normal(hasil_bmi)
      elif hasil_bmi >= 25 and hasil_bmi <= 30:
          result.bmi_gemuk(hasil_bmi)
      elif hasil_bmi >= 30:
          result.bmi_obesitas(hasil_bmi)
      else:
          print("Hasil Tidak Ditemukan 🤖")
    else:
      print("\nPilihan Tidak Ditemukan, Input Yang Benar (A/B)")
      sleep(5)
      os.system("cls")