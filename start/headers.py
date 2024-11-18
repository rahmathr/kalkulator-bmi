def header(title: str = "BMI CALCULATOR", width: int = 33) -> None:
    """
    Menampilkan header dengan teks yang dapat disesuaikan.

    Parameters:
    title (str): Teks judul untuk header. Default adalah 'Kalkulator BMI'.
    width (int): Lebar header. Default adalah 30.
    """
    padding = ((width - len(title)) // 2) - 1
    print(width * "*")
    print(f"{padding * '>'} {title} {padding * '<'}")
    print(width * "*")