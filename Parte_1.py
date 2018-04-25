
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
    
    
    
# Escolha numero 1, adicionar item nao existente ************   FEITO   *******
    
    if escolha == 1:
        
        nome = input('Nome do produto: ')
        
        if nome not in estoque:
        
            a = True  
            while a:
                Qinicial = float(input('Quantidade inicial: '))
                
                if Qinicial < 0:
                    print('A quantidade inicial n�o pode ser negativa.')
                    
                else:
                    a = False
        
        else:
            print('Produto ja cadastrado')
        
                
                
        estoque[nome] = {'quantidade' : Qinicial}




# Escolha numero 2, remover item ****************************   FEITO   *******     

    elif escolha == 2:
        
        nome = input('Nome do produto: ')
        
        if nome not in estoque:
            print('Elemento n�o encontrado')
        
        else:
            del estoque[nome]

            
# Escolha numero 3, alterar item ****************************   FEITO   *******      

    elif escolha == 3:
        
        nome = input('Nome do produto: ')
        
        if nome in estoque:    
            quan = float(input('Altera��o na Quantidade: '))
            
            resultado = estoque[nome]['quantidade'] + quan
            
            estoque[nome]['quantidade'] = resultado
            
            print('Novo estoque de {0} : {1}'.format(nome, estoque[nome]['quantidade']))
        
        else:
            print('Elemento n�o encontrado')
        
# Escolha numero 4, printar estoque *************************   FEITO   *******   

    elif escolha == 4:
        
        for k in estoque:
            print('{0} : {1}'.format(k, estoque[k]['quantidade']))

# Escolha numero 0, Interromper programa ********************   FEITO   *******   

    elif escolha == 0:
        i = 1
    
    else:
        print('Escolha inv�lida')
    
    
with open ('memoria.txt','w') as arquivo:
    conteudo = json.dumps(estoque, sort_keys=True, indent=4)
    arquivo.write(conteudo)

print('At� mais')
