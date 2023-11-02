import random
import time

def random_list(size:int,max:int)->list:
    list=[]
    for i in range(0,size):
        list.append(random.randint(0,max))
    return list

class metriikka:
    aihtoja=0
    vertailuja=0
    def __init__(self, vaihtoja, vertailuja):
        self.vaihtoja=vaihtoja
        self.vertailuja=vertailuja
    def tulosta_metriikka():
        print("Operaatiot:")
        print("Vaihtoja:")

def lisays_lajittelu(lista:list)->list:
    apu=0
    i=0
    
    for j in range(1,len(lista)):
        apu=lista[j]
        for p in range(0,j):
            if lista[p]>lista[j]:
                o=j
                while o>p:
                    lista[o]=lista[o-1]
                    o-=1
                lista[p]=apu
                break
    return lista

            
                

def kuplalajittelu(lista:list)->list:
    temp=0
    for i in range(0,len(lista)):
        for i in range(0,len(lista)-1):
            if lista[i]>lista[i+1]:
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
    return lista

def liputettu_kuplalajittelu(lista:list):
    eiLajiteltu=True
    while eiLajiteltu:
        eiLajiteltu=False
        for i in range(0,len(lista)-1):
            if lista[i]>lista[i+1]:
                eiLajiteltu=True
                temp=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=temp
                
    return lista

def test_wrapper(listan_koko, luku_maks,funktio,tulosta=True):
    lista=random_list(listan_koko,luku_maks)
    print(f"Testataan {funktio.__name__} syötekoolla {listan_koko}...")
    aa=time.time_ns()
    if tulosta:
        print("Lista ennen:",lista)
    funktio(lista)
    if tulosta:
        print("Lista jälkeen",lista)
    la=time.time_ns()
    ajastin(aa,la)




def ajastin(aloitusaika,lopetusaika)->str:
    kesto=lopetusaika-aloitusaika
    if kesto<1000:
        print("kesto oli",kesto,"ns")
    elif kesto/1000<1000:
        print("kesto oli",kesto/1000 ,"us")
    elif kesto/1000000<1000:
        print("kesto oli",kesto/1000000,"ms")
    else:
        print("kesto oli",kesto/1000000000,"s")    


### Testialue

#test_wrapper(10000,1000,kuplalajittelu,False)
#test_wrapper(10000,1000,liputettu_kuplalajittelu,False)
test_wrapper(1000,1000,lisays_lajittelu,False)