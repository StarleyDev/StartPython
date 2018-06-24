print('----------------------------')
print('Bem vindo ao curso de Python')
print('----------------------------')
print('Calculando em Pyton')
anoNascimento = int(input('Digite ano de Nascimento: '))
ano = int(input('Digite o ano atual: '))
print('----------------------------')
idade = ano - anoNascimento
if anoNascimento > ano:
    print('Voce nao pode ter nascido esse ano!')
else:
    # Usar as chaves para colocar os valores da variavel #
    print('Voce tem hoje: {}'.format(idade)) 
