print("Nama     : Rivaldo Marsel Liam ")
print("NIM      : 2410431026 ")
print("Shift    : 1")
print("Modul    : 3\n")
print("~~~~~ Game Tebak Angka BOM ~~~~~\n")

print("Pemain 1")
n = int(input("Pilih angka positif sampai : "))
k = int(input("Angka BOM!: "))

print("Deretan angka:")
for i in range(1, n + 1):
    if i % k == 0:
        print("BOM",end=" ") 
    else:
        print(i,end=" ")

print("\nPemain 2")
tebakan = 0
while tebakan < 1 or tebakan > n:  
    tebakan = int(input(f"Tebak angka dari 1 sampai {n}: "))
    if tebakan <1 or tebakan >n :
        print(f"Angka harus dalam rentang 1 sampai {n} \n")
    
if tebakan % k == 0:
    print(f"angka {tebakan} adalah BOM!, Anda kalah!\n")
else:
    print(f"angka {tebakan} bukan BOM!, Anda menang!\n")

print("~~~~~ Permainan Selesai ~~~~~")