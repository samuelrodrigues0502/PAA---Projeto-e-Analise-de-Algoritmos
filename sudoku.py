def gerar_sudoku(sudoku_str):
    matriz_sudoku = []
    linhas = sudoku_str.strip().split('\n')

    for linha in linhas:
        numeros = linha.split()
        if len(numeros) != 9:
            raise ValueError("Cada linha do Sudoku deve conter 9 números.")

        linha_sudoku = []
        for numero in numeros:
            try:
                valor = int(numero)
                linha_sudoku.append(valor)
            except ValueError:
                raise ValueError("Entrada inválida no Sudoku. Use números de 1 a 9 ou 0 para espaços em branco.")

        matriz_sudoku.append(linha_sudoku)

    if len(matriz_sudoku) != 9:
        raise ValueError("O Sudoku deve conter 9 linhas.")

    return matriz_sudoku

def ler_arquivo_para_string(nome_arquivo):
    conteudo = ""
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def verificaColocaNum(num, lin, col):
    #Verificação do quadrante 3x3
    linIniQuad = 3 * (lin // 3)
    colIniQuad = 3 * (col // 3)

    for i in range(linIniQuad, linIniQuad + 3):
        for j in range(colIniQuad, colIniQuad + 3):
            if matrizSudoku[i][j] == num:
                return False

    #Verificação da linha
    if num in matrizSudoku[lin]:
        return False

    #Verificação da coluna
    for i in range(9):
        if matrizSudoku[i][col] == num:
            return False

    return True

#Função principal responsável pela resolução do sudoku tilizando recursão
def resolve():
    existeZero = False
    lin, col = 0, 0

    #Função que verifica se há alguma célula "vazia"
    for i in range(9):
        for j in range(9):
            if matrizSudoku[i][j] == 0:
                lin, col = i, j
                existeZero = True

    #Se não existe o Sudoku já está resolvido
    if existeZero == False:
        return True
    #Laço que vai tentando preencher as células do Sudoku
    for num in range(1, 10):
        if verificaColocaNum(num, lin, col):
            matrizSudoku[lin][col] = num

            if resolve():
                return True
            #Caso a recursão não chegar em uma solução, a tentativa é anulada
            matrizSudoku[lin][col] = 0

    return False

def resolverSudoku(matrizSudoku):

    if resolve():
        print(17*'=')
        for linha in matrizSudoku:
            print(" ".join(map(str, linha)))
    else:
        print("Não há solução para o Sudoku.")

#arquivo = "C:\\Users\\samue\\Desktop\\IFMG\\SEMESTRE 6\\PAA\\sudokuteste.txt"
arquivo = input('Inisira o caminho do arquivo txt que contém o sudoku: ')
sudokuStr = ler_arquivo_para_string(arquivo)
matrizSudoku = gerar_sudoku(sudokuStr)

for linha in matrizSudoku:
    print(" ".join(map(str, linha)))

resolverSudoku(matrizSudoku)