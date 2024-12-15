def tampilan_header_utama():
    print(f"+{79*'-'}+")
    print(f"| Kalkulator Kebutuhan Energi\t\t\t\t\t\t\t|")
    print(f"+{79*'-'}+")
    print("| Hitung jumlah kalori yang dibakar tubuh Anda dalam keadaan istirahat total.\t|")
    print(f"+{79*'-'}+")

def tampilan_header_database():
    print(f"+{103*'-'}+")
    print(f"|\t\t\t\t\tBMR CALCULATOR | DATABASE\t\t\t\t\t|")
    print(f"+{103*'-'}+")

def tampilan_header_aktivitas_fisik():
    print(f"+{63*'-'}+")
    print(f"|\t\t\tTINGKAT AKTIVITAS FISIK\t\t\t|")
    print(f"+{63*'-'}+")
    aktivitas_pilihan = [
        "| [1] Hampir tidak pernah berolahraga\t\t\t\t|",
        "| [2] Jarang berolahraga\t\t\t\t\t|", 
        "| [3] Sering berolahraga atau beraktivitas fisik berat\t\t|"
    ]
    for pilihan in aktivitas_pilihan:
        print(pilihan)
    print(f"+{63*'-'}+")