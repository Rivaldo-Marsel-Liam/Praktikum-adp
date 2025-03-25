print("Tugas 1 Praktikum ADP")
print("Nama = Rivaldo Marsel Liam")
print("Nomor BP = 2410431026")
print("Shift = 1")

print("===== PROGRAM PEMBELIAN TIKET PESAWAT =====")



r = 0
c = 0
while r < 4 or c < 4:
    print("\n Masukkan jumlah baris dan kolom kursi (minimal 4x4):")
    r = int(input("Jumlah baris: "))
    c = int(input("Jumlah kolom: "))
    if r < 4 or c < 4:
        print("Ukuran minimal bioskop adalah 4x4! Silakan masukkan ulang.")

nomor_kursi = 1
i = 0
while i < r:
    j = 0
    while j < c:
        print(f"{nomor_kursi}", end=" ")
        j += 1
        nomor_kursi += 1
    print()
    i += 1

while True:
    pesanan = int(input("\nMasukkan nomor kursi yang ingin dipesan (0 untuk selesai): "))

    if pesanan == 0:
        print("\n Terima kasih telah memesan tiket!")
        break
    elif pesanan < 1 or pesanan > r * c:
        print("\nNomor kursi tidak valid. Silakan masukkan nomor yang sesuai.")
    else:
        nomor_kursi = 1
        print(f"\n Kursi {pesanan} berhasil dipesan")

    nomor_kursi = 1
    i = 0
    while i < r:
        j = 0
        while j < c:
            if nomor_kursi == pesanan:
                print(" X", end=" ")
            else:
                print(f"{nomor_kursi}", end=" ")
            j += 1
            nomor_kursi += 1
        print()

        i+=1  