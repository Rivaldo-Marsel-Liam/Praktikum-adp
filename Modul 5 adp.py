print("================================================")
print("          PROGRAM MENGHITUNG NILAI MAHASISWA ADP          ")
print("================================================")

print("Nama     : Rivaldo Marsel Liam ")
print("NIM      : 2410431026 ")
print("Shift    : 1")
print("Modul    : 5\n")

jumlah = int(input("\nMasukkan jumlah mahasiswa praktikum ADP : "))

nama_mahasiswa = []
nilai_akhir = []


for i in range(jumlah):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama mahasiswa\t: ")
    pretest = float(input("Nilai Pretest\t: "))
    posttest = float(input("Nilai Posttest\t: "))
    makalah = float(input("Nilai Makalah\t: "))
    akhir = (pretest * 0.4) + (posttest * 0.4) + (makalah * 0.2)

    nama_mahasiswa.append(nama)
    nilai_akhir.append(akhir)

total = 0
for i in range(jumlah):
    total += nilai_akhir[i]
rata = total / jumlah

maks = nilai_akhir[0]
minim = nilai_akhir[0]
for i in range(jumlah):
    if nilai_akhir[i] > maks:
        maks = nilai_akhir[i]
    if nilai_akhir[i] < minim:
        minim = nilai_akhir[i]

nama_atas_rata = []
nilai_atas_rata = []
for i in range(jumlah):
    if nilai_akhir[i] > rata:
        nama_atas_rata.append(nama_mahasiswa[i])
        nilai_atas_rata.append(nilai_akhir[i])


print("\n================================================")
print("                HASIL NILAI                   ")
print("================================================")
print("\nDaftar Nilai Mahasiswa:")
print("+----+----------------------+-------------+")
print("| No | Nama Mahasiswa       | Nilai Akhir |")
print("+----+----------------------+-------------+")

for i in range(jumlah):
    print(f"| {i+1:2} | {nama_mahasiswa[i]:<20} | {nilai_akhir[i]:>11.2f} |")

print("+----+----------------------+-------------+")
print(f"\nRata-rata kelas: {rata:.2f}")
print(f"Nilai tertinggi: {maks:.2f}")
print(f"Nilai terendah : {minim:.2f}")

print("\nMahasiswa dengan nilai di atas rata-rata:")
print("+----+----------------------+-------------+")
print("| No | Nama Mahasiswa       | Nilai Akhir |")
print("+----+----------------------+-------------+")

for i in range(len(nama_atas_rata)):
    print(f"| {i+1:2} | {nama_atas_rata[i]:<20} | {nilai_atas_rata[i]:>11.2f} |")

print("+----+----------------------+-------------+")
print("\n================================================")
