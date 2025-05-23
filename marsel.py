print("Nama     : Rivaldo Marsel Liam ")
print("NIM      : 2410431026 ")
print("Shift    : 1")
print("Modul    : 6\n")

print("Masukkan ukuran matriks A ")
baris_A = int(input("Masukkan Jumlah baris: "))
kolom_A = int(input("Masukkan Jumlah kolom: "))

print("\nMasukkan elemen-elemen matriks A:")
A = []
for i in range(baris_A):
    baris = []
    for j in range(kolom_A):
        elemen = float(input(f"A[{i}][{j}]: "))
        baris.append(elemen)
    A.append(baris)

print("\nMasukkan ukuran matriks B ")
baris_B = int(input("Masukkan Jumlah baris: "))
kolom_B = int(input("Masukkan Jumlah kolom: "))

print("\nMasukkan elemen-elemen matriks B:")
B = []
for i in range(baris_B):
    baris = []
    for j in range(kolom_B):
        elemen = float(input(f"B[{i}][{j}]: "))
        baris.append(elemen)
    B.append(baris)


while True:
    print("\nMenu Kalkulator Matriks:")
    print("1. Penjumlahan matriks")
    print("2. Pengurangan matriks")
    print("3. Perkalian matriks")
    print("4. Determinan matriks A")
    print("5. Invers matriks A")
    print("6. Transpose matriks A")
    print("7. Keluar")

    pilihan = input("Silahkan Pilih operasi (1-7): ")

    if pilihan == '1':
        if baris_A == baris_B and kolom_A == kolom_B:
            hasil = []
            for i in range(baris_A):
                baris = []
                for j in range(kolom_A):
                    baris.append(A[i][j] + B[i][j])
                hasil.append(baris)
            print("\nHasil Penjumlahan:")
            for baris in hasil:
                print(baris)
        else:
            print("Ukuran matriks tidak cocok untuk penjumlahan.")

    elif pilihan == '2':
        if baris_A == baris_B and kolom_A == kolom_B:
            hasil = []
            for i in range(baris_A):
                baris = []
                for j in range(kolom_A):
                    baris.append(A[i][j] - B[i][j])
                hasil.append(baris)
            print("\nHasil Pengurangan:")
            for baris in hasil:
                print(baris)
        else:
            print("Ukuran matriks tidak cocok untuk pengurangan.")

    elif pilihan == '3':
        if kolom_A == baris_B:
            hasil = []
            for i in range(baris_A):
                baris = []
                for j in range(kolom_B):
                    total = 0
                    for k in range(kolom_A):
                        total += A[i][k] * B[k][j]
                    baris.append(total)
                hasil.append(baris)
            print("\nHasil Perkalian:")
            for baris in hasil:
                print(baris)
        else:
            print("Ukuran matriks tidak cocok untuk perkalian.")

    elif pilihan == '4':
        print("\nHitung Determinan Matriks A dan B:")

        if baris_A == kolom_A:
            if baris_A == 2:
                det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
                print("Determinan Matriks A:", det_A)
            elif baris_A == 3:
                det_A = (A[0][0]*((A[1][1]*A[2][2]) - (A[1][2]*A[2][1]))
                         - A[0][1]*((A[1][0]*A[2][2]) - (A[1][2]*A[2][0]))
                         + A[0][2]*((A[1][0]*A[2][1]) - (A[1][1]*A[2][0])))
                print("Determinan Matriks A:", det_A)
            else:
                print("Determinan Matriks A hanya didukung untuk 2x2 atau 3x3.")
        else:
            print("Matriks A bukan matriks persegi.")

        if baris_B == kolom_B:
            if baris_B == 2:
                det_B = B[0][0]*B[1][1] - B[0][1]*B[1][0]
                print("Determinan Matriks B:", det_B)
            elif baris_B == 3:
                det_B = (B[0][0]*((B[1][1]*B[2][2]) - (B[1][2]*B[2][1]))
                         - B[0][1]*((B[1][0]*B[2][2]) - (B[1][2]*B[2][0]))
                         + B[0][2]*((B[1][0]*B[2][1]) - (B[1][1]*B[2][0])))
                print("Determinan Matriks B:", det_B)
            else:
                print("Determinan Matriks B hanya didukung untuk 2x2 atau 3x3.")
        else:
            print("Matriks B bukan matriks persegi.")

    elif pilihan == '5':
        print("\nHitung Invers Matriks A dan B:")

        if baris_A == 2 and kolom_A == 2:
            det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            if det == 0:
                print("Matriks A tidak memiliki invers.")
            else:
                invers = [
                    [ A[1][1]/det, -A[0][1]/det],
                    [-A[1][0]/det,  A[0][0]/det]
                ]
                print("Invers Matriks A:")
                for baris in invers:
                    print(baris)
        else:
            print("Invers Matriks A hanya didukung untuk matriks 2x2.")

        if baris_B == 2 and kolom_B == 2:
            det = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            if det == 0:
                print("Matriks B tidak memiliki invers.")
            else:
                invers = [
                    [ B[1][1]/det, -B[0][1]/det],
                    [-B[1][0]/det,  B[0][0]/det]
                ]
                print("Invers Matriks B:")
                for baris in invers:
                    print(baris)
        else:
            print("Invers Matriks B hanya didukung untuk matriks 2x2.")

    elif pilihan == '6':
        print("\nTranspose Matriks A:")
        transpose_A = []
        for j in range(kolom_A):
            baris = []
            for i in range(baris_A):
                baris.append(A[i][j])
            transpose_A.append(baris)
        for baris in transpose_A:
            print(baris)

        print("\nTranspose Matriks B:")
        transpose_B = []
        for j in range(kolom_B):
            baris = []
            for i in range(baris_B):
                baris.append(B[i][j])
            transpose_B.append(baris)
        for baris in transpose_B:
            print(baris)


    elif pilihan == '7':
        print("Terima kasih telah menggunakan kalkulator matriks.")
        break

    else:
        print("Pilihan tidak valid.")
