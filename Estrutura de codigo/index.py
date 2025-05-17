# Só pra testar o git e github
c = 0
while True:
    try: 
     sexo = str(input('Qual teu sexo ? ')).upper()
     idade = int(input('Qual tua idade?'))
     c += 1
    except ValueError:
       print('Tente novamente ')
    if c == 3 :
       break
print(f'No total foram cadastradas {c} pessoas')    
