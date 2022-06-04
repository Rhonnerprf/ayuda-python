n = int(input("Digite un número entero de tres cifras: "))

primeraCifra = n // 100
ultimaCifra = n % 10
nnum = 10*primeraCifra + ultimaCifra
inv_nnum = ultimaCifra*10 + primeraCifra

print("nnum =",nnum)
print("inv_num =",inv_nnum)
