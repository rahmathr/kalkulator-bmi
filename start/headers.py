def header(title: str = "BMI CALCULATOR", width: int = 33) -> None:
    """
    Menampilkan header dengan teks yang dapat disesuaikan.

    Parameters:
    title (str): Teks judul untuk header. Default adalah 'Kalkulator BMI'.
    width (int): Lebar header. Default adalah 33.
    """
    if len(title) > width:
        title = title[:width - 3] + '...'  # Memotong judul jika terlalu panjang

    padding = max((width - len(title)) // 2, 0)  # Pastikan padding tidak negatif
    print(width * "*")
    print(f"{' ' * padding}{title}{' ' * padding}")
    print(width * "*")

def header_database(title: str = "BMI CALCULATOR | DATABASE", width: int = 100) -> None:
    """
    Menampilkan header untuk database dengan teks yang dapat disesuaikan.

    Parameters:
    title (str): Teks judul untuk header database. Default adalah 'Kalkulator BMI | DATABASE'.
    width (int): Lebar header. Default adalah 100.
    """
    if len(title) > width:
        title = title[:width - 3] + '...'  # Memotong judul jika terlalu panjang

    padding = max((width - len(title)) // 2, 0)  # Pastikan padding tidak negatif
    print(width * "*")  # Menggunakan '*' untuk garis atas
    print(f"{' ' * padding}{title}{' ' * padding}")  # Menggunakan spasi untuk padding
    print(width * "*")  # Garis bawah