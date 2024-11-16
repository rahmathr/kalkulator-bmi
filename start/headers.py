def header(title: str = "Kalkulator BMI") -> None:
    """
    Menampilkan header dengan teks yang dapat disesuaikan.

    Parameters:
    title (str): Teks judul untuk header. Default adalah 'Kalkulator BMI'.
    """
    # Saran-saran perbaikan:

    # 1. Gunakan konstanta untuk lebar header
    HEADER_WIDTH = 30

    # 2. Gunakan f-string untuk perhitungan padding
    print(HEADER_WIDTH * "=")
    print(f"{(HEADER_WIDTH - len(title)) // 2 * '-'} {title} {(HEADER_WIDTH - len(title)) // 2 * '-'}")
    print(HEADER_WIDTH * "=")

    # Alternatif lain yang lebih fleksibel:
    def header(title: str = "Kalkulator BMI", width: int = 30) -> None:
        """
        Menampilkan header dengan teks yang dapat disesuaikan.

        Parameters:
        title (str): Teks judul untuk header. Default adalah 'Kalkulator BMI'.
        width (int): Lebar header. Default adalah 30.
        """
        padding = (width - len(title)) // 2
        print(width * "=")
        print(f"{padding * '-'} {title} {padding * '-'}")
        print(width * "=")