#Definição e criação da MP
num_celulas = 32
num_bancos = 8
celula_por_banco = 4
mp = [['00000000' for c in range(celula_por_banco)] for b in range(num_bancos)] # Para gerar 8 bancos de 4 células cada

# Função para 'quebrar' o endereço entre banco e célula
def MPcontroller(address): 
    if 0 <= address < num_celulas: #2^5 -> varia de 0 até 31
        banco = address // celula_por_banco #Divisão inteira do endereço pelo nº de células por banco para descobrir qual é o banco desejado
        celula = address % celula_por_banco #Resto da divisão do endereço pelo nº de células por banco para descobrir qual é a célula desejada
        return banco, celula
    
# Função de escrita
def write(): 
    while True:
        address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2)
        if 0 <= address < num_celulas:
            banco, celula = MPcontroller(address) #Para as variáveis receberem os valores obtidos pela função MPcontroller
            data = input('INFORMAÇÃO DE 8 bits: ').zfill(8)[:8] #O [:8] serve para deixar o dado com o tamanho de 8bits, retirando, caso ultrapasse, os menos significantes.
            mp[banco][celula] = data
            print()
            opcao = input('Deseja continuar? [S]/[N]: ')
            if opcao in 'Nn':
                break
        else:
            print('ENDEREÇO INVÁLIDO.')
        
# Função para rodar todo o programa
def runSimulation(): 
    while True:
        address = int(input('ENDEREÇO DE 5 bits: ').zfill(5), 2)
        if MPcontroller(address):
            banco, celula = MPcontroller(address)
            print(f'Conteúdo da célula {bin(address)[2:].zfill(5)} -> {mp[banco][celula]}')
        else:
            print('ENDEREÇO INVÁLIDO')
        opcao = input('Deseja continuar? [S]/[N]: ')
        if opcao in 'Nn':
            break

write() #Para escrever na memória
runSimulation() #Para ler a memória
