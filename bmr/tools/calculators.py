import os
from time import sleep
from tools import user_inputs,headers
from database.save_process_bmr import simpan_proses_bmr

def hitung_kebutuhan_kalori():
    os.system("cls")
    headers.header()
    try:
        global nama_lengkap,usia,jenis_kelamin,tinggi_badan,berat_badan
        nama_lengkap = user_inputs.get_nama_lengkap()
        usia = user_inputs.get_usia()
        jenis_kelamin = user_inputs.get_jenis_kelamin()
        tinggi_badan = user_inputs.get_tinggi_badan()
        berat_badan = user_inputs.get_berat_badan()
        if jenis_kelamin == "L":
            bmr_pria = hitung_bmr_pria(berat_badan, tinggi_badan, usia)
            headers.header_aktivitas_fisik()
            total_kalori = user_inputs.get_intensitas_aktivitas()
            aktivitas_fungsi_pria = {
                1: aktivitas_ringan_pria,
                2: aktivitas_sedang_pria,
                3: aktivitas_berat_pria
            }
            aktivitas_fungsi_pria[total_kalori](bmr_pria)

        elif jenis_kelamin == "P":
            bmr_wanita = hitung_bmr_wanita(berat_badan, tinggi_badan, usia)
            headers.header_aktivitas_fisik()
            total_kalori = user_inputs.get_intensitas_aktivitas()
            aktivitas_fungsi_wanita = {
                1: aktivitas_ringan_wanita,
                2: aktivitas_sedang_wanita,
                3: aktivitas_berat_wanita
            }
            aktivitas_fungsi_wanita[total_kalori](bmr_wanita)

    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")


def hitung_bmr_pria(berat_badan: float, tinggi_badan: float, usia: int) -> float:
    """Menghitung Basal Metabolic Rate (BMR) untuk pria."""
    return 66.5 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)

def hitung_bmr_wanita(berat_badan: float, tinggi_badan: float, usia: int) -> float:
    """Menghitung Basal Metabolic Rate (BMR) untuk wanita."""
    return 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)

def aktivitas_ringan_pria(bmr_pria: float):
    """Menghitung kebutuhan kalori untuk pria dengan aktivitas ringan."""
    kalori_kebutuhan = bmr_pria * 1.2
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr_pria:.0f} kkal")
    print(f"Total Kebutuhan Kalori (Aktivitas Ringan): {kalori_kebutuhan:.0f} kkal")
    simpan_proses_bmr(nama_lengkap=nama_lengkap,usia=usia,jenis_kelamin=jenis_kelamin,tinggi_badan=tinggi_badan,berat_badan=berat_badan,bmr=bmr_pria,total_kalori=kalori_kebutuhan)
    sleep(7)
    os.system("cls")

def aktivitas_sedang_pria(bmr_pria: float):
    """Menghitung kebutuhan kalori untuk pria dengan aktivitas sedang."""
    kalori_kebutuhan = bmr_pria * 1.3
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr_pria:.0f} kkal")
    print(f"Total Kebutuhan Kalori (Aktivitas Sedang): {kalori_kebutuhan:.0f} kkal")
    simpan_proses_bmr(nama_lengkap=nama_lengkap,usia=usia,jenis_kelamin=jenis_kelamin,tinggi_badan=tinggi_badan,berat_badan=berat_badan,bmr=bmr_pria,total_kalori=kalori_kebutuhan)
    sleep(7)
    os.system("cls")

def aktivitas_berat_pria(bmr_pria: float):
    """Menghitung kebutuhan kalori untuk pria dengan aktivitas berat."""
    kalori_kebutuhan = bmr_pria * 1.4
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr_pria:.0f} kkal")
    print(f"Total Kebutuhan Kalori (Aktivitas Berat): {kalori_kebutuhan:.0f} kkal")
    simpan_proses_bmr(nama_lengkap=nama_lengkap,usia=usia,jenis_kelamin=jenis_kelamin,tinggi_badan=tinggi_badan,berat_badan=berat_badan,bmr=bmr_pria,total_kalori=kalori_kebutuhan)
    sleep(7)
    os.system("cls")

def aktivitas_ringan_wanita(bmr_wanita: float):
    """Menghitung kebutuhan kalori untuk wanita dengan aktivitas ringan."""
    kalori_kebutuhan = bmr_wanita * 1.2
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr_wanita:.0f} kkal")
    print(f"Total Kebutuhan Kalori (Aktivitas Ringan): {kalori_kebutuhan:.0f} kkal")
    sleep(7)
    os.system("cls")

def aktivitas_sedang_wanita(bmr_wanita: float):
    """Menghitung kebutuhan kalori untuk wanita dengan aktivitas sedang."""
    kalori_kebutuhan = bmr_wanita * 1.3
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr_wanita:.0f} kkal")
    print(f"Total Kebutuhan Kalori (Aktivitas Sedang): {kalori_kebutuhan:.0f} kkal")
    sleep(7)
    os.system("cls")

def aktivitas_berat_wanita(bmr_wanita: float):
    """Menghitung kebutuhan kalori untuk wanita dengan aktivitas berat."""
    kalori_kebutuhan = bmr_wanita * 1.4
    print(f"\nKebutuhan Kalori Anda:")
    print(f"BMR: {bmr_wanita:.0f} kkal")
    print(f"Total Kebutuhan Kalori (Aktivitas Berat): {kalori_kebutuhan:.0f} kkal")
    sleep(7)
    os.system("cls")