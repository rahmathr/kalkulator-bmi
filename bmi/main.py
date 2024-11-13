import os
from time import sleep
from hasilkalkulator import hasil, kalkulator
from inputuser import user
from headers import header
from bacadata import baca
from timesleep import times
os.system('cls')
if __name__ == "__main__":
  while True:
    header.header()
    print("A. RIWAYAT")
    print("B. START\n")
    pilihan_pertama = str(input("Pilihan (A/B) : "))
    if pilihan_pertama in ["A","a"]:
      baca.read_file()
    elif pilihan_pertama in ["B","b"]:
      os.system("cls")
      header.header()
      nama = str(input('Nama\t\t\t: '))
      jenis_kelamin =  str(input("Jenis kelamin (L/P)\t: "))
      if jenis_kelamin in ["L","P"] or jenis_kelamin in ["l","p"]:
        berat_badan = user.berat_badan()
        usia = user.usia()
        tinggi_badan = user.tinggi_badan()
        hasil_bmi = kalkulator.kalkulator_bmi(tinggi_badan,berat_badan)
        if  hasil_bmi < 18.5:
            hasil.bmi_kurus(hasil_bmi)
        elif hasil_bmi <= 25:
            hasil.bmi_normal(hasil_bmi)
        elif hasil_bmi >= 25 and hasil_bmi <= 30:
            hasil.bmi_gemuk(hasil_bmi)
        elif hasil_bmi >= 30:
            hasil.bmi_obesitas(hasil_bmi)
        else:
            print("Hasil Tidak Ditemukan 🤖")
      else:
        print("\nPilihan Tidak Ditemukan, Input Yang Benar (A/B)")
        times.clearsleep()
    else:
      print("\nPilihan Tidak Ditemukan, Input Yang Benar (A/B)")
      times.clearsleep()