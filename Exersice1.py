tahun = int(input("Masukkan Tahun: "))
if (tahun % 400 == 0) and (tahun % 100 == 0):
    print("{0} Adalah Tahun Kabisat".format(tahun))
elif (tahun % 4 == 0) and (tahun % 100 != 0):
    print("{0} Adalah Tahun Kabisat".format(tahun))
else: print("{0} Bukan Tahun Kabisat".format(tahun))