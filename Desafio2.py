vet = []
pares = []
d1 = []
d2 = float('inf')
num= int(input("Digite um numero: "))

while(num != 0):
    vet.append(num)
    num= int(input("Digite um numero: "))
vet.sort()
for i in range(len(vet) - 1):
    d1 = abs(vet[i] - vet[i + 1]) 
    if d1 < d2:  
        d2 = d1
        pares= [(vet[i], vet[i + 1])] 
    elif d1 == d2:  
        pares.append((vet[i], vet[i + 1]))  
print(pares)
