
#Bangun Datar.py
#Program Bangun Datar
#Aplikasi menghitung Luas dan keliling bangun datar

def persegi(s) :
    luas = s * s,"cm2"
    keliling = 4 * s,"cm"
    print("Luas =",  luas)
    print("Keliling =", keliling)

def persegi_panjang (p, l):
    luas = p * l,"cm2"
    keliling = 2 * (p + l),"cm"
    print("Luas =", luas)
    print("keliling =", keliling)

def segitiga(a, t):
    luas = a * t // 2,"cm2"
    keliling = 3 * a,"cm"
    print("Luas =", luas)
    print("keliling =", keliling)

def lingkaran(r):
    phi = 3
    luas = phi * r * r,"cm2"
    keliling = 2 * phi * r,"cm"
    print("Luas =", luas)
    print("keliling =", keliling)

bangun_datar = ["persegi", "persegi panjang", "segitiga", "lingkaran"]

while True:
    print("\n=== APLIKASI BANGUN DATAR ===")
    for i in range(len(bangun_datar)):
        print(i + 1, bangun_datar[i])
    print("5 keluar")

    pilihan = int(input("Masukkan pilihan: "))
        
    if pilihan == 1:
            s = int(input("Masukkan sisi:  "))
            persegi(s)

    elif pilihan == 2:
            p = int(input("Masukkan panjang: "))
            l = int(input("Masukkan lebar: "))
            persegi_panjang(p, l)

    elif pilihan == 3:
            a = int(input("Masukkan alas: "))
            t = int(input("Masukkan tinggi: "))
            segitiga(a, t)

    elif pilihan == 4:
            r = int(input("Masukkan jari-jari: "))
            lingkaran(r)

    elif pilihan == 5:
            print("Terima kasih telah menggunakan aplikasi Bangun Datar")
            break
    else:
            print("Pilihan tidak valid")
        