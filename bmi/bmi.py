import os
from time import sleep

def kalkulator_bmi(tinggi_cm: float, berat_kg: float) -> float:
    """
    Menghitung Body Mass Index (BMI) berdasarkan tinggi badan (dalam cm) dan berat badan (dalam kg).

    Parameters:
    tinggi_cm (float): Tinggi badan dalam satuan cm.
    berat_kg (float): Berat badan dalam satuan kg.

    Returns:
    float: Nilai BMI.

    Raises:
    ValueError: Jika tinggi_cm atau berat_kg kurang dari atau sama dengan nol.

    Example:
    >>> kalkulator_bmi(170, 70)
    24.22
    """
    if tinggi_cm <= 0 or berat_kg <= 0:
        raise ValueError("Tinggi badan dan berat badan harus lebih dari nol.")

    tinggi_meter = tinggi_cm / 100  # Konversi tinggi badan dari cm ke meter
    return berat_kg / (tinggi_meter ** 2)

def tampilkan_hasil_bmi(hasil_bmi: float, status_berat_badan: str) -> None:
    """
    Fungsi umum untuk menampilkan hasil BMI.

    Args:
        hasil_bmi (float): Nilai BMI
        status_berat_badan (str): Status berat badan
    """
    # Tambahkan emoji sesuai kondisi
    emoji_map = {
        "KURUS": "🌱",  
        "NORMAL": "✨",
        "GEMUK": "⚠️",
        "OBESITAS": "🚨"
    }

    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\nBMI anda sekitar {bmi}, yang termasuk dalam kategori {status_berat_badan} {emoji_map.get(status_berat_badan, '')}"

    print(hasil)

    # Tunggu hingga pengguna menekan Enter
    input("\nTekan Enter untuk melanjutkan...")

    # Gunakan cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi-fungsi spesifik status BMI
def bmi_kurus(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori kurus"""
    tampilkan_hasil_bmi(hasil_bmi, "KURUS")

def bmi_normal(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori normal"""
    tampilkan_hasil_bmi(hasil_bmi, "NORMAL")

def bmi_gemuk(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori gemuk"""
    tampilkan_hasil_bmi(hasil_bmi, "GEMUK")

def bmi_obesitas(hasil_bmi: float) -> None:
    """Menampilkan hasil BMI untuk kategori obesitas"""
    tampilkan_hasil_bmi(hasil_bmi, "OBESITAS")