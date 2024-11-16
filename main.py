import os
from time import sleep
from start import calculators
from start import userinputs
from start import headers
from start import bmiresults
from history import readtxt
if __name__ == "__main__":
  while True:
    os.system('cls')
    headers.header()
    print("A. START")
    print("B. HISTORY")
    print("C. DATABASE\n")
    pilihan_pertama = str(input(">>> [A/B/C] : "))
    if pilihan_pertama in ["A","A"]:
      os.system("cls")
      headers.header()
      nama = userinputs.nama()
      jenis_kelamin =  userinputs.jenis_kelamin()
      berat_badan = userinputs.berat_badan()
      usia = userinputs.usia()
      tinggi_badan = userinputs.tinggi_badan()
      hasil_bmi = calculators.kalkulator_bmi(tinggi_badan,berat_badan)
      if  hasil_bmi < 18.5:
          bmiresults.bmi_kurus(hasil_bmi)
      elif hasil_bmi <= 25:
          bmiresults.bmi_normal(hasil_bmi)
      elif hasil_bmi >= 25 and hasil_bmi <= 30:
          bmiresults.bmi_gemuk(hasil_bmi)
      elif hasil_bmi >= 30:
          bmiresults.bmi_obesitas(hasil_bmi)
      else:
            print("Hasil Tidak Ditemukan 🤖")
    elif pilihan_pertama in ["B","b"]:
      readtxt.read_file()
    elif pilihan_pertama in ["C","c"]:
      pass #COMING SOON
    else:
      print("\nPilihan Tidak Ditemukan, Input Yang Benar (A/B)")
      sleep(5)
      os.system("cls")