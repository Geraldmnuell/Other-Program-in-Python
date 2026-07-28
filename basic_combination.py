# ALL BASIC PYTHON IN ONE PROGRAM
"""
MENGGABUNGKAN SEMUA BASIC PYTHON KE DALAM SATU PROGRAM
"""

def basic_syntax():
    print("=============== BASIC SYNTAX ===============")
    print(
        "Hello World, My name is Gerald Imanuel Manongga\n"
        "I' live in north minahasa\n"
        "I'am as Sam Ratulangi University Student\n"
        "From Faculty of Engineering\n"
        "and Study Program Informatics Batch 2025") # OUTPUT IS STRING
    print(1) # OUTPUT IS INTEGER
    print(6.7) # OUTPUT IS FLOAT
    print(True) # OUTPUT IS BOOLEAN
    print("============================================")

def variabel_dataTypes():
    print("=============== VARIABEL AND DATA TYPES ===============")
    name = "Gerald Imanuel Manongga"
    age = 19
    height = 167.67
    bool = False

    print(f"Halo nama saya {name}, Saya berumur {age} Tahun, \nTinggi badan saya adalah {height} cm, \nPernyataan di atas bernilai {bool}\n")

    print(type(name))
    print(type(age))
    print(type(height))
    print(type(bool))
    print("=======================================================")

def operators():
    print("=============== OPERATORS ===============")
    penjumlahan = 10 + 10
    pengurangan = 20 - 10
    perkalian = 10 * 10
    pembagian = 100 / 10 # BISA JUGA MENGGUNAKAN DUA GARIS MIRING //
    modulus = 10 % 4 # SISA PEMBAGIAN

    print("Penjumlahan :", penjumlahan)
    print("Pengurangan :", pengurangan)
    print("Perkalian :", perkalian)
    print("Pembagian :", pembagian)
    print("Modulus :", modulus)

    """
    Operator menggunakan variabel dan input user
    """

    print("===== MENU OPERASI (+, -, *, /, %) =====")
    operation = input("CHOOSE THE OPERATION FOR CAN DO IT! : ")
    x = int(input("\nINPUT YOUR FIRST NUMBER : "))
    y = int(input("INPUT YOUR SECOND NUMBER : "))

    if operation == "+":
        operator1 = x + y
        print(f"{x} + {y} = {operator1}")
    elif operation == "-":
        operator2 = x - y
        print(f"{x} - {y} = {operator2}")
    elif operation == "*":
        operator3 = x * y
        print(f"{x} * {y} = {operator3}")
    elif operation == "/":
        if y == 0:
            print("NOT DIVISION BY ZERO, PLEASE TRG AGAIN!")
        else:
            operator4 = x / y
            print(f"{x} / {y} = {operator4}")
    elif operation == "%":
        operator5 = x % y
        print(f"{x} % {y} = {operator5}")
    else:
        print("OPERATOR YANG DIMASUKKAN SALAH, SILAHKAN COBA LAGI")

    print("=========================================")

def conditional():
    print("=============== CONDITIONAL ===============")
    # PROGRAM NILAI MAHASISWA
    nilai_mahasiswa = int(input("Masukkan nilai mahasiswa : "))

    if nilai_mahasiswa >= 85 and nilai_mahasiswa <= 100:
        print(f"Nilai {nilai_mahasiswa} mendapatkan grade A")
    elif nilai_mahasiswa >= 80 and nilai_mahasiswa <= 84:
        print(f"Nilai {nilai_mahasiswa} mendapatkan grade B+")
    elif nilai_mahasiswa >= 75 and nilai_mahasiswa <= 79:
        print(f"Nilai {nilai_mahasiswa} mendapatkan grade B")
    elif nilai_mahasiswa >= 70 and nilai_mahasiswa <= 74:
        print(f"Nilai {nilai_mahasiswa} mendapatkan grade C+")
    elif nilai_mahasiswa >= 60 and nilai_mahasiswa <= 69:
        print(f"Nilai {nilai_mahasiswa} mendapatkan grade C")
    else:
        print(f"Nilai {nilai_mahasiswa} mendapatkan grade E / TIDAK LULUS")
    print("===========================================")

def looping():
    print("=============== FOR AND WHILE LOOP ===============")
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target1 = 5
    hasil = 0
    sum = 0

    hari_hari = [
        "SENIN",
        "SELASA",
        "RABU",
        "KAMIS",
        "JUMAT",
        "SABTU",
        "MINGGU"
    ]
    angka = 0

    print("===== PERKALIAN 5 =====")
    for i in number:
        print(f"{i} * {target1} = {i * target1}")
        sum = sum + i

    print("===== PENJUMLAHAN ANTAR INDEKS =====")
    for i in range(len(number) - 1):
        hasil = number[i] + number[i + 1]
        print(number[i], "+", number[i + 1], "=", hasil)
    print(f"Hasil penjumlahan dari kelompok bilangan {number} adalah {sum}")

    print("========== NAMA HARI ==========")
    for i in hari_hari:
        angka = angka + 1
        print(f"Hari ke-{angka} adalah hari {i}")

while True:
    print("~~~~~~~~~~ PILIHAN MENU ~~~~~~~~~~")
    print("1. BASIC SYNTAX")
    print("2. VARIABEL AND DATA TYPES")
    print("3. OPERATORS")
    print("4. CONDITIONAL (IF/ELIF/ELSE)")
    print("5. FOR AND WHILE LOOP")
    print("6. EXIT MENU")

    pilihan = int(input("SILAHKAN MEMILIH OPSI YANG TERSEDIA! : "))

    if pilihan == 1:
        basic_syntax()
    elif pilihan == 2:
        variabel_dataTypes()
    elif pilihan == 3:
        operators()
    elif pilihan == 4:
        conditional()
    elif pilihan == 5:
        looping()
    elif pilihan == 6:
        print("ANDA TELAH KELUAR DARI PILIHAN MENU")
        break
    else:
        print("TIDAK ADA PILIHAN MENU, COBA MEMILIH MENU PILIHAN YANG TERSEDIA!!")
