import os
from bmi import calculators, reads
from bmi import userinputs
from bmi import headers
from bmi import bmi
from bmi import times
from bmi import databases as db
os.system('cls')
if __name__ == "__main__":
  while True:
    headers.header()
    print("A. DATABASE")
    print("B. RIWAYAT")
    print("C. START\n")
    pilihan_pertama = str(input(">>> [A/B/C] : "))
    if pilihan_pertama in ["A","a"]:
      db.database()
    elif pilihan_pertama in ["B","b"]:
      reads.read_file()
    elif pilihan_pertama in ["C","c"]:
      os.system("cls")
      headers.header()
      nama = userinputs.nama()
      jenis_kelamin =  userinputs.jenis_kelamin()
      if jenis_kelamin in ["L","P"] or jenis_kelamin in ["l","p"]:
        berat_badan = userinputs.berat_badan()
        usia = userinputs.usia()
        tinggi_badan = userinputs.tinggi_badan()
        hasil_bmi = calculators.kalkulator_bmi(tinggi_badan,berat_badan)
        if  hasil_bmi < 18.5:
            bmi.bmi_kurus(hasil_bmi)
        elif hasil_bmi <= 25:
            bmi.bmi_normal(hasil_bmi)
        elif hasil_bmi >= 25 and hasil_bmi <= 30:
            bmi.bmi_gemuk(hasil_bmi)
        elif hasil_bmi >= 30:
            bmi.bmi_obesitas(hasil_bmi)
        else:
            print("Hasil Tidak Ditemukan 🤖")
      else:
        print("\nPilihan Tidak Ditemukan, Input Yang Benar (A/B)")
        times.clearsleep()
    else:
      print("\nPilihan Tidak Ditemukan, Input Yang Benar (A/B)")
      times.clearsleep()