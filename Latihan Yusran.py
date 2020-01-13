data = []
buah = ['semangka']
lanjut = True
while(lanjut):
    inputbuah = input("Masukkan Buah = ")
    if inputbuah is ("="):
        lanjut = False
    else:
        data.extend(buah)
        data.append(inputbuah)
print(data)
lanjut2 = True
while (lanjut2):
    print("1. Remove")
    print("2. Pop")
    print("3. Mencari dengan Fungsi")
    print("4. Selesai")
    betul = input("masukkan inputan menu = ")
    if betul=="1":
        data.remove("semangka")
        print(data)
    elif betul=="2":
        data.pop()
        print(data)
    elif betul=="3":
        cari = input("Data yang ingin dicari: ")
        for x in range(len(data)):
                 if(data[x]==cari):
                     print("ketemu")
                     print("Data ditemukan pada index ke = ", x)
                 elif(x==(len(data)-1)):
                        print("Data tidak ditemukan")
    else :
        print("Selesai")
        lanjut2 = False
