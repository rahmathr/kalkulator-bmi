def calculate_bmi(tinggi_badan, berat_badan):
  """"Proses Menghitung BMI"""
  konversi_meter = tinggi_badan / 100
  hasil_bmi = berat_badan / (konversi_meter**2)
  return hasil_bmi