
print("================================================")
print("          PROGRAM MENGHITUNG NILAI MAHASISWA ADP          ")
print("================================================")

print("Nama     : Rivaldo Marsel Liam ")
print("NIM      : 2410431026 ")
print("Shift    : 1")
print("Modul    : 5\n")
jumlah = int(input("\nMasukkan jumlah mahasiswa praktikum ADP : "))
data = []

for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama mahasiswa\t: ")
    pretest = float(input("Nilai Pretest\t: "))
    posttest = float(input("Nilai Posttest\t: "))
    makalah = float(input("Nilai Makalah\t: "))
    akhir = (pretest * 0.4) + (posttest * 0.4) + (makalah * 0.2)
    data.append([nama, akhir])

n = len(data)
total = 0
for i in range(n):
    total += data[i][1]
rata = total / n

maks = data[0][1]
minim = data[0][1]
for i in range(n):
    if data[i][1] > maks:
        maks = data[i][1]
    if data[i][1] < minim:
        minim = data[i][1]

atas_rata = []
for i in range(n):
    if data[i][1] > rata:
        atas_rata.append(data[i])

m = len(atas_rata)


print("\n================================================")
print("                HASIL NILAI                   ")
print("================================================")
print("\nDaftar Nilai Mahasiswa:")
print("+----+----------------------+-------------+")
print("| No | Nama Mahasiswa       | Nilai Akhir |")
print("+----+----------------------+-------------+")

for i in range(n):
    print(f"| {i+1:2} | {data[i][0]:<20} | {data[i][1]:>11.2f} |")

print("+----+----------------------+-------------+")
print(f"\nRata-rata kelas: {rata:.2f}")
print(f"Nilai tertinggi: {maks:.2f}")
print(f"Nilai terendah : {minim:.2f}")


print("\nMahasiswa dengan nilai di atas rata-rata:")
print("+----+----------------------+-------------+")
print("| No | Nama Mahasiswa       | Nilai Akhir |")
print("+----+----------------------+-------------+")

for i in range(m):
    print(f"| {i+1:2} | {atas_rata[i][0]:<20} | {atas_rata[i][1]:>11.2f} |")

print("+----+----------------------+-------------+")
print("\n================================================")
