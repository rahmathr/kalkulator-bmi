# Referensi: https://hellosehat.com/health-tools/kebutuhan-kalori/
# Referensi: ChatGPT
# Menggunakan Paradigma Procedural

import os
from time import sleep
from bmi_calculator.calculator import calculate_bmi
from bmi_calculator.bmi_results import hasil_bmi_kurus,hasil_bmi_gemuk,hasil_bmi_normal,hasil_bmi_obesitas
from bmi_calculator.banner import banner

os.system('cls')

# Main
def main():
  while True:
    banner()
    
    jenis_kelamin = str(input("Jenis kelamin (L/P) : "))
    # Jika input yang dimasukan user tidak (L/P)
    if jenis_kelamin == "L" or jenis_kelamin == "P":
        pass
        
    elif jenis_kelamin == "l" or jenis_kelamin == "p":
        print("\nGunakan Huruf Kapital, Silahkan ulangi kembali! 😊")
        sleep(3)
        os.system('cls')
        continue
    else:
        print("\nInput yang anda masukkan salah! Silahkan input yang benar.")
        sleep(3)
        os.system('cls')
        continue

    berat_badan = int(input("Berat badan (kg)    : "))
    usia = int(input("Usia                : "))
    tinggi_badan = int(input("Tanggi badan (cm)   : "))

    hasil_bmi = calculate_bmi(tinggi_badan=tinggi_badan, berat_badan= berat_badan)

    # Menampilkan hasil BMI
    if hasil_bmi < 18.5:
      hasil_bmi_kurus(hasil_bmi=hasil_bmi)
      continue
    
    elif hasil_bmi >= 18.5 and hasil_bmi <= 25 :
      hasil_bmi_normal(hasil_bmi=hasil_bmi)
      continue
    
    elif hasil_bmi >= 25 and hasil_bmi <= 30:
      hasil_bmi_gemuk(hasil_bmi=hasil_bmi)
      continue
    
    elif hasil_bmi >= 30:
      hasil_bmi_obesitas(hasil_bmi=hasil_bmi)
      continue
  
if __name__ == '__main__':
  main()