def kalkulator_bmi(tinggi_badan: int, berat_badan: int,) -> float:
    konversi_meter = tinggi_badan / 100
    return berat_badan / (konversi_meter**2)