'''
Investigar que es una serie de Fibonacci y realizar un algoritmo que la represente.
'''

n_terminos = int(input("¿Cuántos términos de la serie de Fibonacci?: "))

term_1 = 0
term_2 = 1
term_3 = term_1 + term_2
print(term_1, term_2, term_3, end=" ")
for i in range(n_terminos - 3):
    term_1 = term_2
    term_2 = term_3
    term_3 = term_1 + term_2
    print(term_3, end=" ")
