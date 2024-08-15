def calculate_bmi(tinggi_badan: int, berat_badan: int,) -> float:
    """
    Menghitung Body Mass Index (BMI) berdasarkan tinggi dan berat badan.

    Args:
        tinggi_badan (int): Tinggi badan dalam sentimeter.
        berat_badan (int): Berat badan dalam kilogram.

    Returns:
        float: Nilai BMI yang dihitung.
    """
    konversi_meter = tinggi_badan / 100
    hasil_bmi = berat_badan / (konversi_meter**2)
    return hasil_bmi