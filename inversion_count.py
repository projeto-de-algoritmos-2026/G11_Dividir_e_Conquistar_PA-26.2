# arquivo algoritmo de contagem de inversões

# divide meio (se par) ou meio + 1 (se impar)

# rec esq
# rec dir

# se apenas 1 elemento
# então: coloca num vetor onde o primeiro numero é o numero de inversões (começa em zero)

# se dois vetores existentes de mesmo lado então:
# Merge and Count: Va []  Vb []
# vc []
# custo = length Va -1
# ta = length(Va[])
# tb = length(Vb[])
# i = 1
# j = 1
# terminou = False
# vc[0] = Va[0] + Vb[0] 
# while(terminou == False):
#    if Va [i] <= Vb [j]: 
#       custo =- 1
#       vc.append(Va[i])
#       i++
#   else:
#       vc[0] = vc[0] + custo
#       vc.append(Vb[j])
#       j++
#   if(i > ta and j > tb):
#       terminou = True
#   elif(i > ta):
#       while(tb <= j):
#           vc.append(Vb[j])
#           j++
#       terminou = True
#   elif(j > tb):
#       custo = 0
#       while(ta <= i):
#           vc.append(Va[i])
#           i++
#       terminou = True
# return vc[]

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

va = [1, 2, 5]
vb = [1, 1, 4]

vc = merge_and_count(va, vb)

print(vc)