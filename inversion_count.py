# arquivo algoritmo de contagem de inversões

# divide meio (se par) ou meio + 1 (se impar)

# rec esq
# rec dir

# se apenas 1 elemento
# então: coloca num vetor onde o primeiro numero é o numero de inversões (começa em zero)

# se dois vetores existentes de mesmo lado então:
# Merge and Count: Va []  Vb []
# Vc []
# custo = length Va -1
# Ta = length(Va[])
# Tb = length(Vb[])
# i = 1
# j = 1
# terminou = False
# Vc[0] = Va[0] + Vb[0] 
# while(terminou == False):
#    if Va [i] =< Vb [j]: 
#       custo =- 1
#       Vc.append(Va[i])
#       i++
#   else:
#       Vc[0] = Vc[0] + custo
#       Vc.append(Vb[j])
#       j++
#   if(i > Ta and j > Tb):
#       terminou = True
#   elif(i > Ta):
#       while(Tb <= j):
#           Vc.append(Vb[j])
#           j++
#           terminou = True
#   elif(j > Tb):
#       custo = 0
#       while(Ta <= i):
#           Vc.append(Va[i])
#           i++
#           terminou = True
# return Vc[]