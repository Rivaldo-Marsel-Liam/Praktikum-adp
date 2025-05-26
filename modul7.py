print("Nama     : Rivaldo Marsel Liam ")
print("NIM      : 2410431026 ")
print("Shift    : 1")
print("Modul    : 7\n")



def input_data_mahasiswa():
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    data_mahasiswa = []
    for i in range(jumlah):
        print(f"\nMahasiswa ke-{i+1}")
        nama = input("Nama: ")
        nim = input("NIM: ")
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        tugas = float(input("Nilai Tugas: "))
        data_mahasiswa.append([nama, nim, uts, uas, tugas])
    return data_mahasiswa

def hitung_rata(data, indeks):
    total = 0
    for mhs in data:
        total += mhs[indeks]
    return total / len(data)

def hitung_nilai_akhir(uts, uas, tugas):
    return 0.35 * uas + 0.35 * uts + 0.3 * tugas

def urutkan_data(data):
    n = len(data)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if data[j][5] < data[j+1][5]:  # Bandingkan nilai akhir
                # Tukar posisi
                data[j], data[j+1] = data[j+1], data[j]
    return data

def proses_data(data):
    for mhs in data:
        nilai_akhir = hitung_nilai_akhir(mhs[2], mhs[3], mhs[4])
        mhs.append(nilai_akhir)
    
    data_terurut = urutkan_data(data)
    
    for i in range(len(data_terurut)):
        data_terurut[i].append(i+1)
    
    return data_terurut

def tampilkan_tabel(data):
    rata_uts = hitung_rata(data, 2)
    rata_uas = hitung_rata(data, 3)
    rata_tugas = hitung_rata(data, 4)
    rata_akhir = hitung_rata(data, 5)
    
    print("\n{:<10} {:<10} {:<10} {:<10} {:<12} {:<12} {:<8}".format(
        "Nama", "NIM", "Nilai UTS", "Nilai UAS", "Nilai Tugas", "Nilai Akhir", "Peringkat"))
    print("-" * 80)
    
    for mhs in data:
        print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<12.2f} {:<12.2f} {:<8}".format(
            mhs[0], mhs[1], mhs[2], mhs[3], mhs[4], mhs[5], mhs[6]))
    
    print("-" * 80)
    print("{:<10} {:<10} {:<10.2f} {:<10.2f} {:<12.2f} {:<12.2f}".format(
        "", "", rata_uts, rata_uas, rata_tugas, rata_akhir))

def main():
    data = input_data_mahasiswa()
    data_proses = proses_data(data)
    tampilkan_tabel(data_proses)

main()