print(">>>>PROGRAM MENENTUKAN BILANGAN PRIMA DAN BUKAN BILANGAN PRIMA MENGGUNAKAN PERINTAH PENGULANGAN DAN RANGE<<<<")
nilai = [ ]
x = int(input("Masukkan angka : "))
while x != '' :
    nilai.append(int(x))
    x = input("Masukkan lagi angka anda :")
for a in nilai :
    for x in range(2, a):
        if a % x == 0:
            print(a, "bukan merupakan bilangan")
            break
    else:
        print(a, "merupakan bilangan prima")