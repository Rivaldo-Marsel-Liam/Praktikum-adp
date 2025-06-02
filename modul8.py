print("Nama     : Rivaldo Marsel Liam ")
print("NIM      : 2410431026 ")
print("Shift    : 1")
print("Modul    : 8\n")



import os

def buat_data_awal():
    """Membuat file data awal inventaris buku"""
    data_awal = [
        "ISBN,Judul Buku,Penulis,Stok,Harga Beli,Harga Jual",
        "978-602-8519-93-9,Bumi,Andrea Hirata,15,50000,75000",
        "978-602-0324-80-8,Laskar Pelangi,Andrea Hirata,8,45000,68000",
        "978-602-8519-42-7,5 cm,Donny Dhirgantoro,12,48000,72000",
        "978-979-780-858-1,Negeri 5 Menara,Ahmad Fuadi,5,52000,78000",
        "978-602-220-023-8,Pulang,Leila S. Chudori,10,55000,82000",
        "978-602-03-3476-1,Garis Waktu,Fiersa Besari,20,40000,60000",
        "978-602-424-694-5,Sepotong Hati yang Baru,Tere Liye,3,47000,71000",
        "978-602-03-2896-8,Marmut Merah Jambu,Raditya Dika,18,42000,63000",
        "978-602-291-592-2,Konspirasi Alam Semesta,Fiersa Besari,7,46000,69000",
        "978-602-03-2487-8,Rindu,Dee Lestari,6,51000,76000"
    ]
    
    with open("inventaris buku.txt", "w") as file:
        file.write("\n".join(data_awal))
    print("File data awal berhasil dibuat: inventaris buku.txt")

def baca_data():
    """Membaca data dari file dan menyimpannya dalam list of dictionaries"""
    buku = []
    
    try:
        with open("inventaris buku.txt", "r") as file:
            header = file.readline().strip().split(",")
            for line in file:
                if line.strip():
                    values = line.strip().split(",")
                    data_buku = {
                        header[0]: values[0],         # ISBN
                        header[1]: values[1],         # Judul Buku
                        header[2]: values[2],         # Penulis
                        header[3]: int(values[3]),    # Stok
                        header[4]: int(values[4]),    # Harga Beli
                        header[5]: int(values[5])     # Harga Jual
                    }
                    buku.append(data_buku)
        print("Data berhasil dibaca dari file.")
        return buku
    except FileNotFoundError:
        print("File inventaris buku.txt tidak ditemukan.")
        return None

def hitung_potensi_keuntungan(buku):
    """Menghitung potensi keuntungan untuk setiap buku"""
    for b in buku:
        b["Potensi Keuntungan"] = (b["Harga Jual"] - b["Harga Beli"]) * b["Stok"]
    return buku

def buat_laporan(buku):
    """Membuat file laporan inventaris dengan tambahan potensi keuntungan"""
    with open("laporan_inventaris.txt", "w") as file:
        header = list(buku[0].keys())
        file.write(",".join(header) + "\n")

        for b in buku:
            row = [
                b["ISBN"],
                b["Judul Buku"],
                b["Penulis"],
                str(b["Stok"]),
                str(b["Harga Beli"]),
                str(b["Harga Jual"]),
                str(b["Potensi Keuntungan"])
            ]
            file.write(",".join(row) + "\n")
    
    print("File laporan berhasil dibuat: laporan_inventaris.txt")

def analisis_inventaris(buku):
    """Melakukan analisis inventaris dan menampilkan hasilnya"""
    if not buku:
        print("Tidak ada data buku untuk dianalisis.")
        return
    
    # Buku dengan keuntungan tertinggi dan terendah
    buku_tertinggi = max(buku, key=lambda x: x["Potensi Keuntungan"])
    buku_terendah = min(buku, key=lambda x: x["Potensi Keuntungan"])
    
    total_inventaris = sum(b["Stok"] * b["Harga Beli"] for b in buku)
    
    buku_restock = [b for b in buku if b["Stok"] < 5]
    
    print("\n=== HASIL ANALISIS INVENTARIS ===")
    print(f"Buku dengan potensi keuntungan tertinggi: {buku_tertinggi['Judul Buku']} (Rp{buku_tertinggi['Potensi Keuntungan']:,})")
    print(f"Buku dengan potensi keuntungan terendah: {buku_terendah['Judul Buku']} (Rp{buku_terendah['Potensi Keuntungan']:,})")
    print(f"Total nilai inventaris: Rp{total_inventaris:,}")
    
    print("\nBuku yang perlu di-restock (stok < 5):")
    if buku_restock:
        for b in buku_restock:
            print(f"- {b['Judul Buku']} (Stok: {b['Stok']})")
    else:
        print("Tidak ada buku yang perlu di-restock.")

def main():
    if not os.path.exists("inventaris buku.txt"):
        buat_data_awal()
    
    data_buku = baca_data()
    
    if data_buku:
        data_buku = hitung_potensi_keuntungan(data_buku)
        buat_laporan(data_buku)
        analisis_inventaris(data_buku)

if __name__ == "__main__":
    main()