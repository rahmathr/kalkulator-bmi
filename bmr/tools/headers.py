def header() -> None:
    """
    Menampilkan header utama untuk kalkulator BMR.
    """
    print(f"{35*'='}")
    print(f"{10*' '}BMR CALCULATOR{10*' '}")
    print(f"{35*'='}")

def header_database() -> None:
    """
    Menampilkan header untuk halaman database BMR.
    """
    print(f"{90*'='}")
    print(f"{30*' '}BMR CALCULATOR | DATABASE{30*' '}")
    print(f"{90*'='}")

def header_aktivitas_fisik() -> None:
    """
    Menampilkan header dan pilihan tingkat aktivitas fisik.
    """
    print(f"{65*'='}")
    print(f"{20*' '}TINGKAT AKTIVITAS FISIK{20*' '}")
    print(f"{65*'='}")
    aktivitas_pilihan = [
        "1. Hampir tidak pernah berolahraga",
        "2. Jarang berolahraga", 
        "3. Sering berolahraga atau beraktivitas fisik berat"
    ]
    for pilihan in aktivitas_pilihan:
        print(pilihan)
    print(f"{65*'='}")