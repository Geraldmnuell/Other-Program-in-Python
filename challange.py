import random

angka_rahasia = random.randint(1, 10)
tebakan = None
percobaan = 0

print("Saya sudah memilih angka 1 - 10, Coba tebak!")

while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan angka yang ingin di tebak : "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Angka Terlalu Kecil!")
    elif tebakan > angka_rahasia:
        print("Angka Terlalu Besar")
    else:
        print(f"Selamat kamu berhasil menebak angka {angka_rahasia} sebanyak {percobaan} kali percobaan!")