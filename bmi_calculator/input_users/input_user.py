def berat_badan(berat_badan:int=0):
  """
  Meminta pengguna untuk memasukkan berat badan dalam kilogram dan mengembalikan nilai yang dimasukkan.

  Args:
      berat_badan (int): Berat badan awal dalam kilogram. Defaultnya adalah 0.

  Returns:
      int: Berat badan yang dimasukkan oleh pengguna dalam kilogram.

  Raises:
      ValueError: Jika input yang dimasukkan bukan angka.
  """
  while True:
    try:
      berat_badan = int(input("Berat badan (kg)    : "))
      return berat_badan
    except:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue

def usia(usia:int=0):
  """
  Meminta pengguna untuk memasukkan usia dan mengembalikan nilai yang dimasukkan.

  Args:
      usia (int): Usia awal. Defaultnya adalah 0.

  Returns:
      int: Usia yang dimasukkan oleh pengguna.

  Raises:
      ValueError: Jika input yang dimasukkan bukan angka.
  """
  while True:
    try:
      usia = int(input("Usia                : "))
      return usia
    except:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue

def tinggi_badan(tinggi_badan:int=0):
  """
  Meminta pengguna untuk memasukkan tinggi badan dalam sentimeter dan mengembalikan nilai yang dimasukkan.

  Args:
      tinggi_badan (int): Tinggi badan awal dalam sentimeter. Defaultnya adalah 0.

  Returns:
      int: Tinggi badan yang dimasukkan oleh pengguna dalam sentimeter.

  Raises:
      ValueError: Jika input yang dimasukkan bukan angka.
  """
  while True:
    try:
      tinggi_badan = int(input("Tanggi badan (cm)   : "))
      return tinggi_badan
    except:
      print("")
      print(">> Input Harus Berupa Angka!!")
      print("")
      continue