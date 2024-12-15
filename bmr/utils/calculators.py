import os
from time import sleep

from utils import user_inputs, display_headers
from data.saver import simpan_proses_bmr

def hitung_kebutuhan_kalori():
    os.system("cls")
    display_headers.tampilan_header_utama()
    
    global nama_lengkap, usia, jenis_kelamin, tinggi_badan, berat_badan
    
    try:
        nama_lengkap = user_inputs.input_nama_lengkap()
        usia = user_inputs.input_umur()
        jenis_kelamin = user_inputs.input_jenis_kelamin()
        tinggi_badan = user_inputs.input_tinggi_badan()
        berat_badan = user_inputs.input_berat_badan()
        
        if jenis_kelamin.upper() == "L":
            bmr_pria = hitung_bmr_pria(berat_badan, tinggi_badan, usia)
            display_headers.tampilan_header_aktivitas_fisik()
            total_kalori = user_inputs.input_intensitas_aktivitas()
            
            aktivitas_fungsi_pria = {
                1: aktivitas_ringan_pria,
                2: aktivitas_sedang_pria,
                3: aktivitas_berat_pria
            }
            
            aktivitas_fungsi_pria.get(total_kalori, lambda x: print("Pilihan tidak valid"))(bmr_pria)

        elif jenis_kelamin.upper() == "P":
            bmr_wanita = hitung_bmr_wanita(berat_badan, tinggi_badan, usia)
            display_headers.header_aktivitas_fisik()
            total_kalori = user_inputs.input_intensitas_aktivitas()
            
            aktivitas_fungsi_wanita = {
                1: aktivitas_ringan_wanita,
                2: aktivitas_sedang_wanita,
                3: aktivitas_berat_wanita
            }
            
            aktivitas_fungsi_wanita.get(total_kalori, lambda x: print("Pilihan tidak valid"))(bmr_wanita)

        else:
            print("Jenis kelamin tidak valid!")

    except ValueError as ve:
        print(f"\nKesalahan input: {str(ve)}")
    except Exception as e:
        print(f"\nTerjadi kesalahan tidak terduga: {str(e)}")

def hitung_bmr_pria(berat_badan: float, tinggi_badan: float, usia: int) -> float:
    try:
        bmr = 66.5 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
        return max(bmr, 0)
    except Exception as e:
        print(f"Kesalahan perhitungan BMR pria: {e}")
        return 0

def hitung_bmr_wanita(berat_badan: float, tinggi_badan: float, usia: int) -> float:
    try:
        bmr = 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
        return max(bmr, 0)
    except Exception as e:
        print(f"Kesalahan perhitungan BMR wanita: {e}")
        return 0

def proses_kalori(bmr: float, faktor_aktivitas: float, jenis_aktivitas: str):
    kalori_kebutuhan = bmr * faktor_aktivitas
    
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr:.0f} kkal")
    print(f"Total Kebutuhan Kalori ({jenis_aktivitas}): {kalori_kebutuhan:.0f} kkal")
    input("\nTekan Enter untuk melanjutkan...")

    simpan_proses_bmr(
        nama_lengkap=nama_lengkap,
        usia=usia,
        jenis_kelamin=jenis_kelamin,
        tinggi_badan=tinggi_badan,
        berat_badan=berat_badan,
        bmr=bmr,
        total_kalori=kalori_kebutuhan
    )

    os.system("cls")

def aktivitas_ringan_pria(bmr_pria: float):
    proses_kalori(bmr_pria, 1.2, "Aktivitas Ringan")

def aktivitas_sedang_pria(bmr_pria: float):
    proses_kalori(bmr_pria, 1.3, "Aktivitas Sedang")

def aktivitas_berat_pria(bmr_pria: float):
    proses_kalori(bmr_pria, 1.4, "Aktivitas Berat")

def aktivitas_ringan_wanita(bmr_wanita: float):
    proses_kalori(bmr_wanita, 1.2, "Aktivitas Ringan")

def aktivitas_sedang_wanita(bmr_wanita: float):
    proses_kalori(bmr_wanita, 1.3, "Aktivitas Sedang")

def aktivitas_berat_wanita(bmr_wanita: float):
    proses_kalori(bmr_wanita, 1.4, "Aktivitas Berat")