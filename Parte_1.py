
import json


with open ('memoria.txt','r') as arquivo:
    conteudo = arquivo.read()
    estoque = json.loads(conteudo)
    
i = 0 

while i == 0:
    print('')
    print('Controle de estoque')
    print('0 - sair')
    print('1 - adicionar item')
    print('2 - remover item')
    print('3 - alterar item')
    print('4 - imprimir estoque')
    
    escolha = int(input('Fa�a sua escolha: '))  
    
    
    
    if escolha == 1:
        print('oi')
    
    elif escolha == 2:
        print('bunda')
        
    elif escolha == 3:
        print('bunda')    
        
    elif escolha == 4:
        print('bunda')
        
    elif escolha == 0:
        i = 1
    
    else:
        print('Escolha inv�lida')
        print('Sabe ler n�o? � de 0 a 4 Caba�o...')
    

with open ('Arquivo.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)

print('At� mais')

