#project 1
#Mengganti huruf 'u' menjadi huruf 'a'

def gantihuruf(teks, a, b):
    listkata = list (teks)
    for huruf in listkata :
    	if huruf == a :
    		listkata[listkata.index(a)]=b
    		ubah = ''.join(listkata)
    print (ubah)
    	

gantihuruf('matematika', 'e', 's')
