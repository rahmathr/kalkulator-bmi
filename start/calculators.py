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
    bmi = berat_kg / (tinggi_meter ** 2)  # Hitung BMI
    return bmi