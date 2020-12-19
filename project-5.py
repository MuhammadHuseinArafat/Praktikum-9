#project 5
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print ('=' * 50)
print ('NIM \tNAMA \t\tN.MID \tN.UAS')
print ('-' * 50)
for data in nilai :
    print (data['nim'], "\t", end='')
    print (data['nama'], end='')
    if (len(data['nama']) < 7):
        print ("\t\t", data['mid'], end='')
    else:
        print ("", "\t" , data['mid'], end='')
    print ("\t", data ['uas'])
    
