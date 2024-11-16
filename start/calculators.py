def kalkulator_bmi(tinggi_badan: float, berat_badan: float) -> float:
    """
    Menghitung Body Mass Index (BMI) berdasarkan tinggi badan (dalam cm) dan berat badan (dalam kg).

    Parameters:
    tinggi_badan (float): Tinggi badan dalam satuan cm.
    berat_badan (float): Berat badan dalam satuan kg.

    Returns:
    float: Nilai BMI.

    Raises:
    ValueError: Jika tinggi_badan atau berat_badan kurang dari atau sama dengan nol.
    """
    if tinggi_badan <= 0 or berat_badan <= 0:
        raise ValueError("Tinggi badan dan berat badan harus lebih dari nol.")
    konversi_meter = tinggi_badan / 100
    return berat_badan / (konversi_meter**2)
