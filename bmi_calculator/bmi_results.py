import os
from time import sleep

def hasil_bmi_kurus(hasil_bmi) -> float:
  """
  Menampilkan hasil BMI dan mengkategorikannya sebagai 'KURUS'.

  Args:
      hasil_bmi (float): Nilai BMI yang dihitung.

  Returns:
      float: Nilai BMI yang diterima sebagai argumen.
  """
  print("")
  print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori KURUS")
  sleep(10)
  os.system('cls')

def hasil_bmi_normal(hasil_bmi) -> float:
  """
  Menampilkan hasil BMI dan mengkategorikannya sebagai 'NORMAL'.

  Args:
      hasil_bmi (float): Nilai BMI yang dihitung.

  Returns:
      float: Nilai BMI yang diterima sebagai argumen.
  """
  print("")
  print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori NORMAL✨")
  sleep(10)
  os.system('cls')

def hasil_bmi_gemuk(hasil_bmi) -> float:
  """
  Menampilkan hasil BMI dan mengkategorikannya sebagai 'GEMUK'.

  Args:
      hasil_bmi (float): Nilai BMI yang dihitung.

  Returns:
      float: Nilai BMI yang diterima sebagai argumen.
  """
  print("")
  print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori GEMUK")
  sleep(10)
  os.system('cls')

def hasil_bmi_obesitas(hasil_bmi) -> float:
  """
  Menampilkan hasil BMI dan mengkategorikannya sebagai 'OBESITAS'.

  Args:
      hasil_bmi (float): Nilai BMI yang dihitung.

  Returns:
      float: Nilai BMI yang diterima sebagai argumen.
  """
  print("")
  print (f"BMI anda sekitar {hasil_bmi:.2f}, yang termasuk dalam kategori OBESITAS")
  sleep(10)
  os.system('cls')