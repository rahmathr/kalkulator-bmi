from bmi import times
def save_bmi_to_file(hasil: str):
    file_path = "bmi/data.txt"
    with open(file_path, "a", encoding='utf-8') as file:
        file.write(f"{hasil.replace("\n","")}\n")
def bmi_kurus(hasil_bmi) -> float:
    status_berat_badan = "Kurus"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori KURUS"
    print(hasil)
    save_bmi_to_file(hasil)
    times.clearsleep()
def bmi_normal(hasil_bmi) -> float:
    status_berat_badan = "Normal"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori NORMAL✨"
    print(hasil)
    save_bmi_to_file(hasil)
    times.clearsleep()
def bmi_gemuk(hasil_bmi) -> float:
    status_berat_badan = "Gemuk"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori GEMUK"
    print(hasil)
    save_bmi_to_file(hasil)
    times.clearsleep()
def bmi_obesitas(hasil_bmi) -> float:
    status_berat_badan = "Obesitas"
    bmi = f"{hasil_bmi:.2f}"
    hasil = f"\n>>> BMI anda sekitar {bmi}, yang termasuk dalam kategori OBESITAS"
    print(hasil)
    save_bmi_to_file(hasil)
    times.clearsleep()
