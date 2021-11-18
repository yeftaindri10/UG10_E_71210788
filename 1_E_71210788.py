print("====Kalkulator Akar dan Pangkat====")
print("Pilihan menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat") 

pil = int(input("Masukkan menu yang anda pilih : "))

if pil == 1 : 
    bil = int(input("Masukkan bilangan yang ingin dipangkatkan : "))
    print("Hasil dari pemangkatan bilangan", bil, "dengan 2 (Kuadrat) adalah", (bil**2))
elif pil == 2:
    bil = int(input("Masukkan bilangan yang ingin dipangkatkan : "))
    print("Hasil dari pemangkatan bilangan", bil, "dengan 3 (Kubik) adalah", (bil**3)) 
elif pil == 3:
    bil = int(input("Masukkan bilangan yang ingin dipangkatkan : "))
    print("Hasil akar kuadrat dari bilangan", bil, "adalah", float(bil**(1/2)))
else:
    print("Pilihan menu yang dimasukkan tidak sesuai!")

