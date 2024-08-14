def calculate_bmi(tinggi_badan: int, berat_badan: int,) -> int:
  konversi_meter = tinggi_badan / 100
  hasil_bmi = berat_badan / (konversi_meter**2)
  return hasil_bmi