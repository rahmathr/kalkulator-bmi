import os
from time import sleep

from database.save_process_bmi import simpan_hasil_bmi
from tools import user_inputs,headers

def hitung_dan_simpan_bmi() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    headers.tampilkan_header_utama()
    try:
        nama_lengkap = user_inputs.input_nama_lengkap()
        jenis_kelamin = user_inputs.input_jenis_kelamin()
        berat_badan = user_inputs.input_berat_badan()
        usia = user_inputs.input_umur()
        tinggi_badan = user_inputs.input_tinggi_badan()
        hasil_bmi = hitung_bmi(tinggi_badan, berat_badan)
        if hasil_bmi < 18.5:
            tampilkan_bmi_kurus(hasil_bmi)
            simpan_hasil_bmi(nama_lengkap, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Kurus")
        elif hasil_bmi <= 25:
            tampilkan_bmi_normal(hasil_bmi)
            simpan_hasil_bmi(nama_lengkap, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Normal")
        elif 25 < hasil_bmi <= 30:
            tampilkan_bmi_gemuk(hasil_bmi)
            simpan_hasil_bmi(nama_lengkap, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Gemuk")
        else:
            tampilkan_bmi_obesitas(hasil_bmi)
            simpan_hasil_bmi(nama_lengkap, jenis_kelamin, berat_badan, usia, tinggi_badan, hasil_bmi, "Obesitas")
    except ValueError as e:
        print(f"Input tidak valid: {e}")
        sleep(2)
        hitung_dan_simpan_bmi()
    except Exception as e:
        print(f"Terjadi kesalahan dalam perhitungan BMI: {e}")
        sleep(3)

def hitung_bmi(tinggi_cm: float, berat_kg: float) -> float:
    if tinggi_cm <= 0 or berat_kg <= 0:
        raise ValueError("Tinggi badan dan berat badan harus lebih dari nol.")
    tinggi_meter = tinggi_cm / 100
    return berat_kg / (tinggi_meter ** 2)

def tampilkan_hasil_bmi(hasil_bmi: float, status_berat_badan: str) -> None:
    emoji_map = {
        "KURUS": "🌱",
        "NORMAL": "✨",
        "GEMUK": "⚠️",
        "OBESITAS": "🚨"
    }
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\nBMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan} {emoji_map.get(status_berat_badan, '')}"
    print(hasil)
    input("\nTekan Enter untuk melanjutkan...")
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_bmi_kurus(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "KURUS")

def tampilkan_bmi_normal(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "NORMAL")

def tampilkan_bmi_gemuk(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "GEMUK")

def tampilkan_bmi_obesitas(hasil_bmi: float) -> None:
    tampilkan_hasil_bmi(hasil_bmi, "OBESITAS")