#project 6
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print ('=' * 64)
print ('NIM \tNAMA \t\tN.MID \tN.UAS \tN.AKHIR \tSTATUS')
print ('-' * 64)
for data in nilai :
    nAkhir = ((data['mid']) + (data ['uas']*2))/3
    if (nAkhir >=60):
        statusmhs = 'LULUS'
    else:
        statusmhs = 'GAGAL'
    print (data['nim'], "\t", end='')
    print (data['nama'], end='')
    if (len(data['nama']) < 7):
        print ("\t\t", data['mid'], end='')
    else:
        print ("", "\t" , data['mid'], end='')
    print ("\t", data ['uas'], end='')
    print ("\t", round(nAkhir,1), end='')
    print("\t\t", statusmhs)
    
