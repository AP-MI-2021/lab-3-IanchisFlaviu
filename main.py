def crescator(l):
    '''
    Ne afiseaza cea mai lunga subsecventa de numere crescatoare dintr-o lista de numere
    :param l:
    :return:
    '''
    list = []
    list_aux = []
    i=0
    while(i<len(l)-1):
        if (l[i]<=l[i+1]):
            list_aux.append(l[i])
        else:
            list_aux.append((l[i]))
            list.append(list_aux)
            list_aux = []
        i=i+1
    list_aux.append(l[i])
    list.append(list_aux)

    max = 0
    poz =-1
    for i in range(len(list)):
        if max < len(list[i]):
            max = len(list[i])
            poz = i
    return list[poz]

def test_crescator():
    assert crescator([1,2,3,2,4]) == [1,2,3]
    assert crescator([6,2,3,5,2,4]) == [2,3,5]
    assert crescator([7,3,2,4]) == [2,4]

def divizibil(l,k):
    list = []
    list_aux = []
    i = 0
    while (i<len(l)):
        if(l[i]%k==0):
            list_aux.append(l[i])
        else:
            list.append(list_aux)
            list_aux = []
        i = i+1
    list.append(list_aux)

    max = 0
    poz = -1
    for i in range(len(list)):
        if max < len(list[i]):
            max = len(list[i])
            poz = i
    return list[poz]

def test_divizibil():
    assert divizibil([5,10,2,3],5)==[5,10]
    assert divizibil([2,10,4,3,6,8],2)==[2,10,4]
    assert divizibil([100,10,3,6,8],2)==[100,10]

def medie(l, med):
    list = []
    med_aux = 0
    i = 0
    suma = 0
    while(i<len(l)):
        list_aux = l
        suma +=l[i]
        for j in range(i+1,len(l)):
            suma +=l[j]
        med_aux = suma/(len(l)-i+1)

        if (med_aux<med):
            print(l[i:len(l)])
            list.append(l[i:len(l)])

        else:

            while((suma>0) and (med_aux>med) and (len(list_aux)>1)):
                suma -= list_aux[len(list_aux)-1]
                list_aux=list_aux[i:len(list_aux)-1]
                print(len(list_aux))
                if (len(list_aux)!=0):
                    med_aux = suma/(len(list_aux))
                print(suma,"",len(list_aux))
            list.append(list_aux)
        list_aux = []
        suma = 0
        med_aux = 0
        i +=1

    max = 0
    poz = -1
    for i in range(len(list)):
        if max < len(list[i]):
            max = len(list[i])
            poz = i
    return list[poz]

def test_medie():
    assert medie([1,2,3,1,2],3) == [1,2,3,1,2]
    assert medie([3,3,3,111,222],3) == [3,3,3]
    assert medie([111,222,3,3,3],3) == [3,3,3]

def print_menu():
    print('1.Citirea listei')
    print('2.Determina cea mai lunga subsecventa de numere crescatoare')
    print('3.Determina cea mai lunga subsecventa de numere divizibile cu un numar dat')
    print('4.Determina cea mai lunga subsecventa a caror medie nu depaseste o valoare citita')
    print('0.Exit')


def main():
    test_crescator()
    test_divizibil()
    test_medie()
    print_menu()


    while True:
        opt = int(input('Dati optiunea '))
        if opt == 1:
            l = []
            nr = int(input('Dati lungimea listei de numere '))
            print('Introduceti elementele listei: ')
            for i in range(nr):
                el = int(input())
                l.append(el)
            print(l)
        elif opt == 2:
            print(crescator(l))
        elif opt == 3:
            k = int(input('Dati numarul '))
            print(divizibil(l,k))
        elif opt == 4:
            med = float(input('Dati un numar '))
            print(medie(l,med))
        elif opt == 0:
            break
        else:
            print('Optiune invalida')

main()