# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
print('# Exemplo 01')
n = float(input('Digite um número: '))
cent = n * 100
mil = n * 1000
print('A medida em centimetros será {:.0f}, e em milimetros será {:.0f}.'.format(cent, mil))

print('# Exemplo 02')

n = float(input('Digite um número: '))
print('A medida em centimetros será {:.0f}, e em milimetros será {:.0f}'.format(n * 100, n * 1000))
