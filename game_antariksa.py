import time
import random
import os
from termcolor import colored

# Variabel permainan
pemain = {"nama": "", "bahan_bakar": 100, "oksigen": 100, "inventaris": []}
daftar_planet = ["Mars", "Alpha Centauri", "Pluto", "Galaxia-9"]
planet_sekarang = None
permainan_selesai = False

# Peta planet (array 2D 5x5)
peta_planet = [
    ["🌋", "🪨", "💎", "🛸", "👽"],
    ["🌌", "🔮", "🚀", "🌑", "⚡"],
    ["🌀", "🌠", "🏠", "🔋", "❌"],
    ["🪐", "💀", "🔭", "🪙", "🌪"],
    ["👾", "🔫", "🧭", "💧", "🔑"]
]

# Fungsi animasi teks
def animasi_teks(teks, warna='white', delay=0.03):
    for karakter in teks:
        print(colored(karakter, warna), end='', flush=True)
        time.sleep(delay)
    print()

# Fungsi membersihkan layar
def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loading screen
def tampilkan_loading(teks="Memuat", durasi=2):
    bersihkan_layar()
    animasi_teks(teks, 'cyan')
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(durasi / 3)
    print("\n")

# Tampilkan header
def tampilkan_header():
    bersihkan_layar()
    print(colored("==============================================", 'cyan'))
    animasi_teks("🚀 PETUALANGAN ANTARIKSA 🚀", 'magenta', 0.05)
    print(colored("==============================================", 'cyan'))
    print(colored(f"Pemain: {pemain['nama']} | Bahan Bakar: {pemain['bahan_bakar']}% | Oksigen: {pemain['oksigen']}%", 'yellow'))
    print(colored("----------------------------------------------", 'cyan'))

# Tampilkan peta planet
def tampilkan_peta():
    tampilkan_header()
    animasi_teks(f"🗺 Peta Planet {planet_sekarang}:", 'cyan')
    for i, baris in enumerate(peta_planet):
        print(f"{i} | " + " ".join(baris))
    print("    0   1   2   3   4")

    animasi_teks("\n🔍 Simbol di peta:", 'white')
    print("👽: Alien | 💎: Harta | 🚀: Kapal | 🔋: Baterai")
    print("🌋: Gunung Meletus | 💧: Air | 💀: Mayat | 🔫: Senjata")
    print("🧭: Kompas | 🪙: Koin | 🏠: Markas | 🌪: Badai")

# Efek berdasarkan simbol
def kejadian_dari_simbol(simbol):
    if simbol == "👽":
        animasi_teks("👽 SERANGAN ALIEN! Kehilangan 30% oksigen!", 'red')
        pemain["oksigen"] -= 30
    elif simbol == "💎":
        animasi_teks("💎 Menemukan berlian! Ditambahkan ke inventaris.", 'yellow')
        pemain["inventaris"].append("💎 Berlian")
    elif simbol == "🚀":
        animasi_teks("🚀 Menemukan kapal rusak! +10% bahan bakar.", 'green')
        pemain["bahan_bakar"] += 10
    elif simbol == "🌋":
        animasi_teks("🌋 Gunung meletus! Kehilangan 40% oksigen!", 'red')
        pemain["oksigen"] -= 40
    elif simbol == "🔋":
        animasi_teks("🔋 Menemukan baterai! +15% bahan bakar.", 'green')
        pemain["bahan_bakar"] += 15
    elif simbol == "💧":
        animasi_teks("💧 Menemukan air segar! +20% oksigen.", 'cyan')
        pemain["oksigen"] += 20
    elif simbol == "🪙":
        animasi_teks("🪙 Menemukan koin kuno! Ditambahkan ke inventaris.", 'yellow')
        pemain["inventaris"].append("🪙 Koin")
    elif simbol == "💀":
        animasi_teks("💀 Kerangka astronot... suasana menyeramkan. Tidak ada efek.", 'magenta')
    elif simbol == "🔫":
        animasi_teks("🔫 Senjata alien ditemukan! Ditambahkan ke inventaris.", 'yellow')
        pemain["inventaris"].append("🔫 Senjata")
    elif simbol == "🔭":
        animasi_teks("🔭 Menemukan teleskop! Tidak ada efek langsung.", 'blue')
    elif simbol == "🧭":
        animasi_teks("🧭 Kompas antariksa ditemukan. Tidak terlalu berguna di sini.", 'blue')
    elif simbol == "🏠":
        animasi_teks("🏠 Markas kecil ditemukan. Tempat aman sementara.", 'green')
    elif simbol == "🌪":
        animasi_teks("🌪 Badai angkasa menghantam! Kehilangan 25% bahan bakar.", 'red')
        pemain["bahan_bakar"] -= 25
    elif simbol == "🌑":
        animasi_teks("🌑 Area gelap dan sunyi... tidak ada yang ditemukan.", 'white')
    elif simbol == "❌":
        animasi_teks("❌ Area terlarang. Cepat pergi dari sini!", 'red')
        pemain["oksigen"] -= 10
    else:
        animasi_teks("🤷 Tidak ada kejadian khusus di lokasi ini.", 'white')

# Jelajahi planet berdasarkan koordinat
def jelajahi_planet():
    global permainan_selesai, planet_sekarang

    tampilkan_peta()
    animasi_teks("\nPilih lokasi untuk dijelajahi (baris dan kolom 0-4)", 'white')

    try:
        baris = int(input("Baris (0-4): "))
        kolom = int(input("Kolom (0-4): "))
        
        if 0 <= baris < 5 and 0 <= kolom < 5:
            simbol = peta_planet[baris][kolom]
            tampilkan_header()
            animasi_teks(f"🚶 Menjelajahi titik ({baris}, {kolom}) dengan simbol {simbol}...", 'cyan')
            time.sleep(1)
            kejadian_dari_simbol(simbol)
        else:
            animasi_teks("❌ Koordinat tidak valid!", 'red')
    except ValueError:
        animasi_teks("❌ Input harus angka!", 'red')

    if pemain["oksigen"] <= 0:
        animasi_teks("💀 KEHABISAN OKSIGEN! GAME OVER.", 'red', 0.05)
        permainan_selesai = True
    elif pemain["bahan_bakar"] <= 0:
        animasi_teks("⛽ KEHABISAN BAHAN BAKAR! Terdampar...", 'red', 0.05)
        permainan_selesai = True

# Menu utama
def mulai_permainan():
    global planet_sekarang, permainan_selesai

    tampilkan_loading("🚀 Memulai Petualangan Antariksa")
    
    # Setup pemain
    bersihkan_layar()
    animasi_teks("Masukkan nama petualang antariksa:", 'yellow')
    pemain["nama"] = input(colored(">> ", 'green'))

    while not permainan_selesai:
        tampilkan_header()
        print(colored("1. Pergi ke planet baru", 'green'))
        print(colored("2. Jelajahi planet saat ini", 'blue'))
        print(colored("3. Cek inventaris", 'yellow'))
        print(colored("4. Lihat peta planet", 'magenta'))
        print(colored("5. Keluar dari permainan", 'red'))

        pilihan = input(colored("Pilih aksi (1-5): ", 'white'))

        if pilihan == "1":
            planet_sekarang = random.choice(daftar_planet)
            animasi_teks(f"🛸 Bepergian ke {planet_sekarang}...", 'cyan', 0.05)
            time.sleep(2)
            pemain["bahan_bakar"] -= 10
        elif pilihan == "2":
            if planet_sekarang:
                jelajahi_planet()
                input("\nTekan Enter untuk lanjut...")
            else:
                animasi_teks("⚠ Pilih planet dulu!", 'red')
        elif pilihan == "3":
            tampilkan_header()
            animasi_teks("🎒 INVENTARIS:", 'yellow')
            if pemain["inventaris"]:
                for item in pemain["inventaris"]:
                    print(f" - {item}")
            else:
                print(" (Kosong)")
            input("\nTekan Enter untuk lanjut...")
        elif pilihan == "4":
            if planet_sekarang:
                tampilkan_peta()
                input("\nTekan Enter untuk lanjut...")
            else:
                animasi_teks("⚠ 5Pilih planet dulu!", 'red')
        elif pilihan == "5":
            animasi_teks("👋 Terima kasih sudah bermain!", 'magenta')
            break
        else:
            animasi_teks("❌ Pilihan tidak valid!", 'red')
        
        time.sleep(1)

# Jalankan game
if __name__ == "__main__":
    mulai_permainan()
