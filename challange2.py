int1 = int(input("Masukkan angka awal : "))
int2 = int(input("Masukkan angka terakhir : "))

for i in range(int1, int2 + 1): 
    result =  i * 7
    print(f"7 * {i} = {result}")

angka1 = int(input("Masukkan angka awal : "))
angka2 = int(input("Masukkan angka terakhir : "))
hasil = 0

for i in range(angka1, angka2 + 1):
    hasil = hasil + i
print(f"Hasil penjumlahan dari angka {angka1} sampai angka {angka2} adalah {hasil}")

range1 = int(input("Berapa banyak angka? : "))
maxNum = int(input("Masukkan angka ke 1 : "))
minNum = maxNum

for i in range(2, range1 + 1):
    number = int(input(f"Masukkan angka ke {i} : "))
    if number > maxNum:
        maxNum = number
    
    if number < minNum:
        minNum = number

print("Angka terbesar adalah", maxNum)
print("Angka terkecil adalah", minNum)
