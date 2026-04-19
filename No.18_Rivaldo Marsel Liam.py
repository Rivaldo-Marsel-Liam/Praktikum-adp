def cek_tiga_selisih_sama(kelompok):
    i = 0
    while i < len(kelompok) - 2:
        if (kelompok[i+1] - kelompok[i]) == (kelompok[i+2] - kelompok[i+1]):
            return True
        i = i + 1
    return False

def proses_bilangan(arr):
    naik = []
    turun = []

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            naik.append(arr[i])
        elif arr[i] < arr[i-1]:
            turun.append(arr[i])
    return naik, turun

def validasi_kelompok(kelompok):
    if cek_tiga_selisih_sama(kelompok):
        return False
    if sum(kelompok) < 0:
        return False
    return True

#Program Utama
data = list(map(float, input("Masukkan bilangan(pisahkan dengan spasi): ").split()))

naik, turun = proses_bilangan(data)

hasil = {}

if naik and validasi_kelompok(naik):
    hasil["naik"] = naik

if turun and validasi_kelompok(turun):
    hasil["turun"] = turun

if hasil:
    print("Kelompok valid:")
    for k, v in hasil.items():
        print(f"{k}: {v}")
else:
    print("Tidak ada kelompok yang valid.")
