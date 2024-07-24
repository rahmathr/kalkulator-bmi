# Referensi: https://hellosehat.com/health-tools/kebutuhan-kalori/
# Referensi: ChatGPT
# Menggunakan Paradigma Procedural

import os
import sapa
from time import sleep
os.system('cls')

# Main
def main():
  while True:
    sapa.opening()
    
    jenis_kelamin = str(input("Jenis kelamin (L/P) : "))
    # Jika input yang dimasukan user tidak (L/P)
    if jenis_kelamin == "L" or jenis_kelamin == "P":
        pass
        
    elif jenis_kelamin == "l" or jenis_kelamin == "p":
        print("\nGunakan Huruf Kapital, Silahkan ulangi kembali! 😊")
        sleep(3)
        os.system("cls")
        continue
    else:
        print("\nInput yang anda masukkan salah! Silahkan input yang benar.")
        sleep(3)
        os.system("cls")
        continue

    berat_badan = int(input("Berat badan (kg)    : "))
    usia = int(input("Usia                : "))
    tinggi_badan = int(input("Tanggi badan (cm)   : "))

    # Proses BMI
    konversi_meter = tinggi_badan / 100
    hasil_bmi = berat_badan / (konversi_meter**2)

    # Menampilkan hasil BMI
    if hasil_bmi < 18.5:
      print("")
      print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori KURUS")
      sleep(10)
      os.system('cls')
      continue
    
    elif hasil_bmi >= 18.5 and hasil_bmi <= 25 :
      print("")
      print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori NORMAL✨")
      sleep(10)
      os.system('cls')
      continue
    
    elif hasil_bmi >= 25 and hasil_bmi <= 30:
      print("")
      print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori GEMUK")
      sleep(10)
      os.system('cls')
      continue
    
    elif hasil_bmi >= 30:
      print("")
      print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori OBESITAS")
      sleep(10)
      os.system('cls')
      continue
  
if __name__ == '__main__':
  main()