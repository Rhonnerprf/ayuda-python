'''
Valor de la costante pi mediante serie pi = 4 * 〈1-1/3+1/5-1/7+1/9-1/11〉.
'''

n = 1000
piValue = 0
for i in range(n):
    term = 4*((-1)**i)/(2*(i+1)-1)
    piValue = piValue + term 

print(piValue)
