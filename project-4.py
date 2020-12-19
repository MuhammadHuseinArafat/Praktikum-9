#project 4
import random
def shuffleString(kata, n):
    listkata = []
    while (len(listkata) < n):
        acakKata = random.sample(kata, len(kata))
        acakUrut = ''.join(acakKata)
        if(acakUrut not in listkata):
            listkata.append(acakUrut)

    print(listkata)

shuffleString('kamu', 7)
