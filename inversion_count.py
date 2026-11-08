# arquivo algoritmo de contagem de inversões

# divide meio (se par) ou meio + 1 (se impar)
def divide(va):
    tamanho = len(va)
    if(tamanho % 2 == 0):
        p = tamanho // 2
    else:
        p = (tamanho // 2) + 1
    p + 1
    vb = va[:p]
    vc = va[p:]
    print(vb)
    print(vc)    
        
# rec esq
# rec dir

# se apenas 1 elemento
# então: coloca num vetor onde o primeiro numero é o numero de inversões (começa em zero)

# se dois vetores existentes de mesmo lado então:
# Função que roda Merge and Count a partir de um vetor A e um vetor B e retorna um vetor C
def merge_and_count(va, vb):
    vc = [0]
    ta = len(va) - 1
    tb = len(vb) - 1 
    custo = ta
    print("custo inicial:")
    print(custo)
    i = 1
    j = 1
    terminou = False
    vc[0] = va[0] + vb[0]

    while(terminou == False):
        if(va[i] <= vb[j]):
            custo -= 1
            vc.append(va[i])
            i += 1
        else:
            vc[0] += custo
            vc.append(vb[j])
            j += 1
        if (i > ta and j > tb):
            terminou = True
            break
        if (i > ta):
            print("A")
            while(j <= tb):
                vc.append(vb[j])
                j += 1
            terminou = True
            break
        if (j > tb):
            print("B")
            custo = 0
            while(i <= ta):
                vc.append(va[i])
                i += 1
            terminou = True
            break
    return vc

va = [1, 2, 4, 56, 200, 9, 7]
vb = [1, 1, 4]

divide(va)