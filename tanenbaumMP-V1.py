mp = [['00000000' for c in range(4)] for b in range(8)] # Para gerar 8 bancos de 4 células cada

def MPcontroller(address): #Função para 'quebrar' o endereço entre banco e célula
    banco = address // 4 #Divisão inteira do endereço pelo nº de células por banco para descobrir qual é o banco desejado
    celula = address % 4 #Resto da divisão do endereço pelo nº de células por banco para descobrir qual é a célula desejada
    return banco, celula

def write(): #Função de escrita
    address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2) #zfill completa com zeros à esquerda; int(--, 2) transforma de binário para decimal
    banco, celula = MPcontroller(address) #Para as variáveis receberem os valores obtidos pela função MPcontroller
    data = input('INFORMAÇÃO DE 8 bits: ').zfill(8) 
    mp[banco][celula] = data
    print()

def read(): #Função de leitura
    address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2) #zfill completa com zeros à esquerda; int(--, 2) transforma de binário para decimal
    banco, celula = MPcontroller(address)
    print(f'CONTEÚDO DA CÉLULA {bin(address)[2:].zfill(5)} -> {mp[banco][celula]}\n')

def showAll(): #Função de listar tudo
    for b in range(8): #8 bancos
        print(f'BANCO {bin(b)[2:].zfill(3)}')
        for c in range(4): #4 células
            print(mp[b][c])
        print()

def runSimulation(): #Função para rodar todo o programa
    while True:
        print('= SIMULADOR DE MEMÓRIA =')
        print('[W] WRITE')
        print('[R] READ')
        print('[L] LIST ALL ')
        opcao = input('')
        print()
        if opcao in 'Ww':
            write()
        if opcao in 'Rr':
            read()
        if opcao in 'Ll':
            showAll()

runSimulation()
