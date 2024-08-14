import os
from time import sleep
import bmi_calculator
import bmi_calculator.input_users

os.system('cls')

if __name__ == "__main__":
  while True:
    bmi_calculator.header()

    jenis_kelamin = bmi_calculator.input_users.jenis_kelamin()
    if jenis_kelamin == "L" or jenis_kelamin == "P":
      bmi_calculator.input_users.pilihan_gender_1
    elif jenis_kelamin == "l" or jenis_kelamin == "p":
      bmi_calculator.input_users.pilihan_gender_2()
      continue
    else:
      bmi_calculator.input_users.pilihan_gender_3()
      continue

    berat_badan = bmi_calculator.input_users.berat_badan()
    usia = bmi_calculator.input_users.usia()
    tinggi_badan = bmi_calculator.input_users.tinggi_badan()
    hasil_bmi = bmi_calculator.calculate_bmi(tinggi_badan= tinggi_badan, berat_badan=berat_badan)

    if hasil_bmi < 18.5:
      bmi_calculator.hasil_bmi_kurus(hasil_bmi=hasil_bmi)
      continue

    elif hasil_bmi >= 18.5 and hasil_bmi <= 25 :
      bmi_calculator.hasil_bmi_normal(hasil_bmi=hasil_bmi)
      continue

    elif hasil_bmi >= 25 and hasil_bmi <= 30:
      bmi_calculator.hasil_bmi_gemuk(hasil_bmi=hasil_bmi)
      continue

    elif hasil_bmi >= 30:
      bmi_calculator.hasil_bmi_obesitas(hasil_bmi=hasil_bmi)
      continue

    else:
      print("Hasil Tidak Ditemukan 🤖")