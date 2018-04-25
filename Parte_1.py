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
    
    
    
# Escolha numero 1, adicionar item nao existente ****   FEITO   ***
    
    if escolha == 1:
        
        nome = input('Nome do produto: ')
        
        if nome not in estoque:
        
            a = True  
            while a:
                Qinicial = float(input('Quantidade inicial: '))
                
                if Qinicial < 0:
                    print('A quantidade inicial não pode ser negativa.')
                    
                else:
                    a = False
        
        else:
            print('Produto ja cadastrado')
        
                
                
        estoque[nome] = {'quantidade' : Qinicial}




# Escolha numero 2, remover item ****************       

    elif escolha == 2:
        
        nome = input('Nome do produto: ')
        
        if nome not in estoque:
            print('Elemento não encontrado')

            
# Escolha numero 3, alterar item ****************       

    elif escolha == 3:
        print('bunda')    
        
# Escolha numero 4, printar estoque *********   FEITO   ***   

    elif escolha == 4:
        
        for k in estoque:
            print('{0} : {1}'.format(k, estoque[k]['quantidade']))
    
    elif escolha == 0:
        i = 1
    
    else:
        print('Escolha inválida')
    
    
with open ('memoria.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)

print('Até mais')
