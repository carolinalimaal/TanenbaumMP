mp = [['00000000' for c in range(4)] for b in range(8)] # Para gerar 8 bancos de 4 células cada

def MPcontroller(address): #Função para 'quebrar' o endereço entre banco e célula
    if 0 <= address <= 31:
        banco = address // 4 #Divisão inteira do endereço pelo nº de células por banco para descobrir qual é o banco desejado
        celula = address % 4 #Resto da divisão do endereço pelo nº de células por banco para descobrir qual é a célula desejada
        return banco, celula
    else:
        return False

def write(): #Função de escrita
    while True:
        address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2)
        banco, celula = MPcontroller(address) #Para as variáveis receberem os valores obtidos pela função MPcontroller
        data = input('INFORMAÇÃO DE 8 bits: ').zfill(8) 
        mp[banco][celula] = data
        print()
        opcao = input('Deseja continuar? [S]/[N]: ')
        if opcao in 'Nn':
            break
        
def runSimulation(): #Função para rodar todo o programa
    while True:
        address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2)
        if MPcontroller(address):
            banco, celula = MPcontroller(address)
            print(f'Conteúdo da célula {bin(address)[2:].zfill(5)} -> {mp[banco][celula]}')
        else:
            print('ENDEREÇO INVÁLIDO')

write() #Para escrever na memória
runSimulation() #Para ler a memória
