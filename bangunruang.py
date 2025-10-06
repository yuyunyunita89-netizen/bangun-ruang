import math

print("Program Menghitung Luas Permukaan & Volume Bangun Ruang")
print("1. Kubus")
print("2. Balok")
print("3. Tabung")

pilih = int(input("Pilih bangun ruang (1/2/3): "))

if pilih == 1:
    # Kubus
    sisi = float(input("Masukkan panjang sisi kubus: "))
    luas_permukaan = 6 * sisi * sisi
    volume = sisi ** 3
    print("Luas Permukaan Kubus =", luas_permukaan)
    print("Volume Kubus =", volume)

elif pilih == 2:
    # Balok
    p = float(input("Masukkan panjang: "))
    l = float(input("Masukkan lebar: "))
    t = float(input("Masukkan tinggi: "))
    luas_permukaan = 2 * (p*l + p*t + l*t)
    volume = p * l * t
    print("Luas Permukaan Balok =", luas_permukaan)
    print("Volume Balok =", volume)

elif pilih == 3:
    # Tabung
    r = float(input("Masukkan jari-jari alas: "))
    t = float(input("Masukkan tinggi: "))
    luas_permukaan = 2 * math.pi * r * (r + t)
    volume = math.pi * r * r * t
    print("Luas Permukaan Tabung =", luas_permukaan)
    print("Volume Tabung =", volume)

else:
    print("Pilihan tidak valid")