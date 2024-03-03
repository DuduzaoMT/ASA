from pulp import *

prob = LpProblem("Noel_Problem",LpMaximize)

firstLine = input()
t,p,max = firstLine.split()  #t -> nº brinquedos,p->pacotes especiais,max -> nº max de brinquedos


brinquedos = {}
coeficientes_lucro = {}
max_capacidade = {}
exp1 = None
for i in range(int(t)):
    Line = input()
    lucro,capacidade = Line.split()
    brinquedos[f"brinquedo{i + 1}"] = LpVariable("brinquedo"+str(i + 1), 0, int(capacidade), LpInteger)
    coeficientes_lucro[f"brinquedo{i + 1}"] = int(lucro)
    max_capacidade[f"brinquedo{i + 1}"] = int(capacidade)
    exp1 += lpSum(brinquedos[f"brinquedo{i+1}"])

lista = [[] for _ in range(int(t)+1)] #posicao i é o boneco_i e posicao j é o pack j
exp2 = None
for w in range(int(p)):
    Line = input()
    i,j,k,l = Line.split()
    max_capacidade[f"brinquedo{w + int(t) + 1}"] = min(max_capacidade[f"brinquedo{int(i)}"],min(max_capacidade[f"brinquedo{int(j)}"],max_capacidade[f"brinquedo{int(k)}"]))
    maximiano = max_capacidade[f"brinquedo{w + int(t) + 1}"]
    brinquedos[f"brinquedo{w + int(t) + 1}"] = LpVariable(f"brinquedo{w + int(t) + 1}", 0, maximiano, LpInteger)
    coeficientes_lucro[f"brinquedo{w + int(t) + 1}"] = int(l)
    lista[int(i)].append(brinquedos[f"brinquedo{w + int(t) + 1}"])
    lista[int(j)].append(brinquedos[f"brinquedo{w + int(t) + 1}"])
    lista[int(k)].append(brinquedos[f"brinquedo{w + int(t) + 1}"])
    exp2 += lpSum(3*brinquedos[f"brinquedo{w + int(t) + 1}"])

for i in range(1,len(lista)):
    expressao = lpSum(packs for packs in lista[i])
    prob += lpSum(brinquedos[f"brinquedo{i}"]+expressao) <= max_capacidade[f"brinquedo{i}"]
  
# restrição de quantidade total
#exp1 = lpSum(brinquedos[f"brinquedo{x}"] for x in range(1,int(t)+1))
#exp2 = lpSum(3*brinquedos[f"brinquedo{x}"] for x in range(int(t)+1,len(brinquedos)+1))
prob += lpSum(exp1+exp2) <= int(max), "Restricao_Quantidade"

# função objetivo
prob += lpSum(coeficientes_lucro[x] * brinquedos[x] for x in brinquedos), "Funcao_Objetivo"

# Resolver o problema
prob.solve(GLPK(msg=0))

# Imprimir o valor máximo da função objetivo (lucro) se uma solução foi encontrada
if LpStatus[prob.status] == 'Optimal':
    print(value(prob.objective))