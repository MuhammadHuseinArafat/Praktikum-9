#project 7

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print ('=' * 71)
print ('NIM \tNAMA MAHASISWA \t\tTANGGAL LAHIR \t\tTEMPAT LAHIR')
print ('-' * 71)
for data in mhs:
    pecah = data.split(':')
    print (pecah[0], end='')
    print ("\t", pecah[1], end='')
    pecah2 = pecah[2].split('-')
    pecah2.reverse()
    boom = '/'.join(pecah2)
    if (len(pecah[1]) < 14):
        print ("\t\t", boom, end='')
    else:
        print("\t", boom, end='')
    print("\t\t", pecah[3])
