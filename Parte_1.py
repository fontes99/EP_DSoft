
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
    
    escolha = int(input('Faça sua escolha: '))  
    
    
    
    if escolha == 1:
        
        x = input('Nome do produto: ')
        
        a = True  
        while a:
            y = float(input('Quantidade inicial: '))
            if y < 0:
                print('A quantidade inicial não pode ser negativa.')
            else:
                a = False
                
                
        estoque[x] = {'quantidade' : y}
        print(estoque)
       

    elif escolha == 2:
        print('bunda')
        
    elif escolha == 3:
        print('bunda')    
        
    elif escolha == 4:
        print('bunda')
        
    elif escolha == 0:
        i = 1
    
    else:
        print('Escolha inválida')
    
    
with open ('memoria.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)

print('Até mais')
