#Grupo TG018 - Joao Tomazio nr 78039 - Ricardo Costa nr 77978

from janela_sopa_letras import *

#==============================================================================#
#====================== TIPOS ABSTRATOS DE INFORMACAO =========================#
#==============================================================================#

#============ 1 - TIPO DIRECAO ==============#
#                                            #
# O tipo direcao e representado por strings, #
# contendo os pontos da rosa dos ventos,     #
#         N, S, E, W, NE, NW, SE, SW         #
#                                            #
#============================================#

# 1.1 - Reconhecedores

def e_direcao(arg):
    '''e_direcao : universal -> boolean
       e_direcao(arg) devolve True se arg for do tipo direcao, False caso contrario'''
    
    return arg in ("N", "S", "E", "W", "NE", "NW", "SE", "SW")

def e_norte(arg):
    '''e_norte : direcao -> boolean
       e_norte(arg) devolve True se arg for "N", False caso contrario'''
    
    return arg == "N"
    
def e_sul(arg):
    '''e_sul : direcao -> boolean
       e_sul(arg) devolve True se arg for "S", False caso contrario'''
    
    return arg == "S"
    
def e_leste(arg):
    '''e_leste : direcao -> boolean
       e_leste(arg) devolve True se arg for "E", False caso contrario'''
    
    return arg == "E"
    
def e_oeste(arg):
    '''e_oeste : direcao -> boolean
       e_oeste(arg) devolve True se arg for "W", False caso contrario'''
    
    return arg == "W"
    
def e_nordeste(arg):
    '''e_nordeste : direcao -> boolean
       e_nordeste(arg) devolve True se arg for "NE", False caso contrario'''
    
    return arg == "NE"
    
def e_noroeste(arg):
    '''e_noroeste : direcao -> boolean
       e_noroeste(arg) devolve True se arg for "NW", False caso contrario'''
    
    return arg == "NW"
    
def e_sudeste(arg):
    '''e_sudeste : direcao -> boolean
       e_sudeste(arg) devolve True se arg for "SE", False caso contrario'''
    
    return arg == "SE"
    
def e_sudoeste(arg):
    '''e_sudoeste : direcao -> boolean
       e_sudoeste(arg) devolve True se arg for "SW", False caso contrario'''
    
    return arg == "SW"

# 1.2 - Testes

def direcoes_iguais(d1, d2):
    '''direcoes_iguais : direcao x direcao -> boolean
       direcoes_iguais(d1, d2) devolve True se 'd1' = 'd2', False caso contrario'''
    
    return d1 == d2

# 1.3 - Outras Operacoes

def direcao_oposta(d):
    '''direcao_oposta : direcao -> direcao
       direcao_oposta(d) devolve a direcao oposta da introduzida, segundo a rosa dos ventos'''
    
    tuplo_direcoes = ("N", "S", "E", "W", "NE", "NW", "SE", "SW")
    tuplo_direcoes_opostas = ("S", "N", "W", "E", "SW", "SE", "NW", "NE")
    
    for i in range(len(tuplo_direcoes)): #corre tuplo_direcoes para encontrar o indice i da direcao introduzida, e apresenta tuplo_direcoes_opostas[i] que corresponde a direcao oposta da introduzida
        if tuplo_direcoes[i] == d:
            return tuplo_direcoes_opostas[i]
    
#=========== 2 - TIPO COORDENADA ============#
#                                            #
#  O tipo coordenada e representado por um   #
#  tuplo composto por 3 elementos, sendo os  #
#   dois primeiros inteiros positivos que    #
#   representam uma posicao na grelha, e o   #
#    terceiro uma direcao que representa a   #
#  direcao em que a palavra esta na grelha   #
#                                            #
#============================================#

# 2.1 - Construtor

def coordenada(l, c, d):
    '''coordenada : int x int x direcao -> coordenada
       coordenada(l, c, d) tem como valor a coordenada referente a posicao (l, c) e a direcao d, gerando um erro caso os argumentos sejam invalidos'''
    
    if not isinstance(l, int) or not isinstance(c, int) or not e_direcao(d): #testa tipos dos argumentos
        raise ValueError("coordenada: argumentos invalidos")
    
    elif l < 0 or c < 0: #testa o sinal dos argumentos que representam a posicao na grelha
        raise ValueError("coordenada: argumentos invalidos")
    
    else:
        return (l, c, d)
    
# 2.2 - Seletores
    
def coord_linha(c):
    '''coord_linha : coordenada -> int
       coord_linha(c) tem como valor a linha da coordenada'''
    
    return c[0]

def coord_coluna(c):
    '''coord_coluna : coordenada -> int
       coord_coluna(c) tem como valor a coluna da coordenada'''
    
    return c[1]

def coord_direcao(c):
    '''coord_direcao : coordenada -> direcao
       coord_direcao(c) tem como valor a direcao da coordenada'''
    
    return c[2]

# 2.3 - Reconhecedor

def e_coordenada(arg):
    '''e_coordenada : universal -> boolean
       e_coordenada(arg) tem o valor verdadeiro se arg for do tipo coordenada, falso caso contrario'''
    
    if not isinstance(arg, tuple): #testa se arg e um tuplo
        return False
    
    elif len(arg) != 3: #testa se arg e composto por 3 elementos
        return False
    
    elif not isinstance(arg[0], int) or not isinstance(arg[1], int) or not e_direcao(arg[2]): #testa o tipo dos elementos do argumento
        return False
    
    elif arg[0] < 0 or arg[1] < 0: #testa o sinal dos argumentos que representam a posicao na grelha
        return False
    
    else:
        return True
    
# 2.4 - Testes

def coordenadas_iguais(c1 , c2):
    '''coordenadas_iguais : coordenada x coordenada -> boolean
       coordenadas_iguais(c1 , c2) devolve o valor verdadeiro se as coordenadas c1 e c2 forem iguais e falso caso contrario'''
    
    return c1 == c2

# 2.5 - Outras Operacoes

def coordenada_string(c):
    '''coordenada_string : coordenada -> str
       coordenada_string(c) devolve a representacao externa de c: uma string iniciada por parentesis esquerdo '(' seguido pelo numero da linha e da coluna, separados por virgula e um espaco ', ', seguido por parentesis direito e traco ')-' , apos os quais se apresenta a direcao'''
    
    return "(" + str(coord_linha(c)) + ", " + str(coord_coluna(c)) + ")-" + coord_direcao(c) #aplica a representacao externa
    
#============= 3 - TIPO GRELHA ================#
#                                              #
# O tipo grelha corresponde a uma matriz m x n #
#  representada por uma lista de m elementos,  #
#  estes strings, compostos por n caracteres   #
#                                              #
#==============================================#

# 3.1 - Construtor

def grelha(lst):
    '''grelha : lista de strings -> grelha
       grelha(lst) devolve a propria lista introduzida, se esta for uma lista de strings de igual tamanho, levantando um erro em caso contrario'''
    
    if not isinstance(lst, list): #verifica se o argumento e uma lista
        raise ValueError("grelha: argumentos invalidos")
        
    elif lst == []: #verifica se a lista e vazia
        raise ValueError("grelha: argumentos invalidos")
        
    else:
        for i in lst: #verifica se todos os elementos da lista sao strings
            if not isinstance(i, str):
                raise ValueError("grelha: argumentos invalidos")
        
        for i in range(len(lst) - 1): #verifica se todas as strings tem o mesmo tamanho
            if len(lst[i]) != len(lst[i + 1]):
                raise ValueError("grelha: argumentos invalidos")
            
    return lst

# 3.2 - Seletores

def grelha_nr_linhas(g):
    '''grelha_nr_linhas : grelha -> int
       grelha_nr_linhas(g) devolve o numero de linhas da grelha g'''
    
    return len(g)

def grelha_nr_colunas(g):
    '''grelha_nr_colunas : grelha -> int
       grelha_nr_colunas(g) devolve o numero de colunas da grelha g'''
    
    return len(g[0])

def grelha_elemento(g, l, c):
    '''grelha_elemento : grelha x int x int -> str
       grelha_elemento(g, l, c) devolve o caracter que esta na posicao (l, c) da grelha g'''
    
    if not isinstance(l, int) or not isinstance(c, int): #verifica os tipos dos argumentos numericos
        raise ValueError("grelha_elemento: argumentos invalidos")
    
    elif not (0 <= l < grelha_nr_linhas(g)) or not (0 <= c < grelha_nr_colunas(g)): #verifica se l e c podem representar uma posicao nesta grelha
        raise ValueError("grelha_elemento: argumentos invalidos")
    
    return g[l][c]
        
def grelha_linha(g, c):
    '''grelha_linha : grelha x coordenada -> str
       grelha_linha(g, c) devolve a cadeia de caracteres que corresponde a linha definida segundo a direcao dada pela coordenada c, e que inclui a posicao dada pela mesma coordenada'''
     
    if coord_linha(c) >= len(g) or coord_coluna(c) >= len(g[0]) or not e_direcao(coord_direcao(c)): #verifica se a coordenada introduzida e valida nesta grelha
        raise ValueError("grelha_linha: argumentos invalidos")
    
    #inicializa os incrementos utilizados no ciclo de busca de linha
    incremento_linha = 0 
    incremento_coluna = 0
    
    texto = ""
    linha = coord_linha(c)
    coluna = coord_coluna(c)
    direcao = coord_direcao(c)
    
    #inicializa o estado da variavel auxiliar que permite saber se a direcao introuzida e simples. por direcao nao simples, considera-se as direcoes que se podem obter das direcoes simples atraves da funcao "direcao oposta"
    d_simples = False

    #condicoes para assinalar o inicio da busca e o incremento utilizado, dependendo da direcao introduzida
    if e_sul(direcao):
        linha = 0 #Encosta 'a primeira linha
        incremento_linha = 1
        d_simples = True
        
    elif e_leste(direcao):
        coluna = 0 #Encosta 'a primeira coluna
        incremento_coluna = 1
        d_simples = True
        
    elif e_sudeste(direcao): #dependendo da posicao, encosta ou 'a primeira linha ou 'a primeira coluna, ou ambas
        if linha > coluna:
            linha = linha - coluna
            coluna = 0
            
        elif linha < coluna:
            coluna = coluna - linha
            linha = 0
            
        else:
            linha = 0
            coluna = 0
            
        incremento_linha = 1
        incremento_coluna = 1
        d_simples = True
        
    elif e_sudoeste(direcao): #dependendo da posicao, encosta ou 'a primeira linha ou 'a ultima coluna coluna, ou ambas
        if linha > (grelha_nr_colunas(g) - 1 - coluna):
            linha = linha - (grelha_nr_colunas(g) - 1 - coluna)
            coluna = grelha_nr_colunas(g) - 1
                    
        elif linha < (grelha_nr_colunas(g) - 1 - coluna):
            coluna = coluna + linha
            linha = 0
                    
        else:
            linha = 0
            coluna = grelha_nr_colunas(g) - 1
            
        incremento_linha = 1
        incremento_coluna = -1
        d_simples = True
        
    if d_simples:
        while (0 <= linha < grelha_nr_linhas(g)) and (0 <= coluna < grelha_nr_colunas(g)):
            texto += grelha_elemento(g, linha, coluna)
            linha += incremento_linha
            coluna += incremento_coluna
        
        return texto
    
    else: #e' novamente chamada a funcao com o argumento da direcao oposta
        texto = grelha_linha(g, coordenada(linha, coluna, direcao_oposta(direcao)))
        
        return texto[::-1] #e' apresentada a linha (string) de tras para a frente

# 3.3 - Reconhecedor

def e_grelha(arg):
    '''e_grelha : universal -> boolean
       e_grelha(arg) tem o valor verdadeiro se arg for do tipo grelha e falso caso contrario.'''
    
    if not isinstance(arg, list): #verifica se o argumento e uma lista
        return False
      
    elif arg == []: #verifica se e uma lista vazia
        return False
        
    for i in arg: #verifica se todos os elementos da lista sao strings
        if not isinstance(i, str):
            return False
        
    for i in range(len(arg) - 1): #verifica se todas as strings tem o mesmo tamanho
        if len(arg[i]) != len(arg[i + 1]):
            return False
            
    return True

# 3.4 - Testes

def grelhas_iguais(g1, g2):
    '''grelhas_iguais : grelha x grelha -> boolean
       grelhas_iguais(g1, g2) devolve True se g1 e g2 forem iguais, False caso contrario'''
    
    return g1 == g2

#============= 4 - TIPO RESPOSTA ==============#
#                                              #
# O tipo resposta e representado por uma lista #
# de tuplos de dois elementos, o primeiro uma  #
#     palavra, e o segundo uma coordenada      #
#                                              #
#==============================================#

# Funcao auxiliar

def ordena_resposta(res):
    '''ordena_resposta : resposta -> resposta
       ordena_resposta(res) ordena os elementos da resposta por ordem alfabetica crescente, segundo as string contidas nos elementos'''
    
    lista_ord_alfabetica = []
        
    for i in range(resposta_tamanho(res)): #transforma a resposta numa lista
            lista_ord_alfabetica += [resposta_elemento(res, i)]
    
    for i in range(len(lista_ord_alfabetica)): #ordena a lista por bubblesort
        for j in range(len(lista_ord_alfabetica) - 1 - i):
            if lista_ord_alfabetica[j][0] > lista_ord_alfabetica[j + 1][0]:
                lista_ord_alfabetica[j], lista_ord_alfabetica[j + 1] = lista_ord_alfabetica[j + 1], lista_ord_alfabetica[j]
        
    return resposta(lista_ord_alfabetica) #volta a transformar a lista numa resposta 

# 4.1 - Construtor

def resposta(lst):
    '''resposta : lista de tuplos(string, coordenada) -> resposta
       resposta(lst) tem como valor a resposta que contem cada um dos tuplos que compoem a lista lst. Em caso de erro, o construtor gera um erro de valor'''
    
    if not isinstance(lst, list):
        raise ValueError("resposta: argumentos invalidos")
    
    for i in lst:
        if not isinstance(i, tuple): #verifica se cada elemento e um tuplo
            raise ValueError("resposta: argumentos invalidos")
            
        elif len(i) != 2: #verifica o tamanho de cada tuplo
            raise ValueError("resposta: argumentos invalidos")
                    
        elif not isinstance(i[0], str) or not e_coordenada(i[1]): #verifica o tipo dos elementos que constituem cada tuplo
            raise ValueError("resposta: argumentos invalidos")
    
    return lst

# 4.2 - Seletores

def resposta_elemento(res, n):
    '''resposta_elemento : resposta x int -> tuplo(string, coordenada)
       resposta_elemento(res, n) devolve o enesimo elemento da resposta res'''
    
    if not (0 <= n < len(res)): #verifica se o elemento existe na resposta
        raise ValueError("resposta_elemento: argumentos invalidos")
    
    return res[n]
    
def resposta_tamanho(res):
    '''resposta_tamanho : resposta -> int
       resposta_tamanho(res) devolve o numero de elementos da resposta res'''
        
    return len(res)

# 4.3 - Modificador

def acrescenta_elemento(r, s, c):
    '''acrescenta_elemento : resposta x string x coordenada -> resposta
       acrescenta_elemento(r, s, c) devolve a resposta r com mais um elemento, o tuplo (s, c)'''
    
    return r + [(s, c)]

# 4.4 - Reconhecedor

def e_resposta(arg):
    '''e_resposta : universal -> boolean
       e_resposta(arg) devolve True se arg for do tipo resposta, False caso contrario'''
    
    if not isinstance(arg, list): #verifica se o argumento e uma lista
        return False
       
    for i in arg:
        if not isinstance(i, tuple): #verifica se cada elemento da lista e um tuplo
            return False
            
        elif len(i) != 2: #verifica o tamanho de cada tuplo
            return False
                
        elif not isinstance(i[0], str) or not e_coordenada(i[1]): #verifica o tipo dos elementos que constituem cada tuplo
            return False
                         
    return True

# 4.5 - Testes

def respostas_iguais(r1, r2):
    '''respostas_iguais : resposta x resposta -> boolean
       respostas_iguais(r1, r2) devolve True se r1 e r2 contiverem os mesmos tuplos, False caso contrario'''
    
    if resposta_tamanho(r1) != resposta_tamanho(r2): #verifica se as respostas tem o mesmo tamanho
        return False
    
    #ordena as 2 respostas alfabeticamente 
    r1 = ordena_resposta(r1)
    r2 = ordena_resposta(r2)
    
    for i in range(resposta_tamanho(r1)):
        if (resposta_elemento(r1, i)[0] != resposta_elemento(r2, i)[0]) or \
           (not coordenadas_iguais(resposta_elemento(r1, i)[1], resposta_elemento(r2, i)[1])): #verifica se nas respostas ordenadas os elementos de igual indice i sao iguais
            return False
        
    return True

# 4.6 - Outras Operacoes

def resposta_string(res):
    '''resposta_string : resposta -> string
       resposta_string(res) devolve a representacao externa da resposta res: uma cadeia de caracteres iniciada pelo parentesis recto esquerdo '[' e que contem a descricao de cada elemento da resposta separados por virgulas e espaco ', ', terminando com o parentesis recto direito ']'. Cada elemento e representado por '<'PALAVRA':'COORDENADA'>', em que PALAVRA e a palavra encontrada e COORDENADA a coordenada onde se encontra a palavra'''
    
    texto = ""
    
    res = ordena_resposta(res) #ordena a resposta alfabeticamente
    
    for i in range(resposta_tamanho(res)): #aplica a representacao externa a cada elemento da resposta
        texto += "<" + resposta_elemento(res, i)[0] + ":" + coordenada_string(resposta_elemento(res, i)[1]) + ">, "
    
    return "[" + texto[:-2] + "]" #"[:-2]" para retirar o ", " a mais no texto 

#==============================================================================#
#============================ FUNCOES A IMPLEMENTAR ===========================#
#==============================================================================#

# Funcao auxiliar

def junta_respostas(r1, r2):
    '''junta_respostas : resposta x resposta -> resposta
       junta_respostas(r1, r2) devolve uma so resposta contendo os elementos de r1 e r2'''
        
    resposta_soma = r1
        
    for i in range(resposta_tamanho(r2)): #vai adicionando cada elemento de r2 'a resposta_soma
        resposta_soma = acrescenta_elemento(resposta_soma, resposta_elemento(r2, i)[0], resposta_elemento(r2, i)[1])        
    
    return resposta_soma

# Funcoes principais

def sopa_letras(fich):
    '''sopa_letras : string -> resposta
       sopa_letras(fich) tem como resultado a resposta ao puzzle descrito no ficheiro fich'''
    
    def converte_maiusculas(s):
            '''converte_maiusculas : str -> str
               converte_maiusculas(s) converte todas as letras minusculas de uma cadeia de caracteres para maiusculas'''
                
            dist = ord("a") - ord("A") #distancia na tabela ASCII entre as minusculas e as maiusculas
            
            texto_final = ""            
                
            for i in s:
                if "a" <= i <= "z": #transforma cada caracter que seja uma letra minuscula numa maiuscula
                    texto_final += chr(ord(i) - dist)
                        
                else: #mantem os caracteres que nao sejam letras minusculas
                    texto_final += i
                
            return texto_final     
    
    def organiza_sopa(l):
        '''organiza_sopa : list -> list
           organiza_sopa(l) devolve uma lista de strings em que cada string e composta por letras, ou seja, retira das cadeias todos os caracteres que nao correspondam a letras'''
        
        organizada = []
        texto = ""
        
        for s in l:
            for caracter in s:
                if caracter != " " and caracter != "\n": #filtra os caracteres indesejados
                    texto += caracter
                
            organizada += [converte_maiusculas(texto)] #aplica a funcao "converte_maiusculas" a cada string de letras
            texto = ""
            
        return organizada
    
    def organiza_palavreado(s):
        '''organiza_palavreado : str -> list
           organiza_palavreado(s) transforma uma cadeia de caracteres numa lista organizada de palavras'''
        
        s = converte_maiusculas(s) #aplica a funcao "converte_maiusculas" 'a string
        organizada = []
        texto = ""
        
        for caracter in s:
            if "A" <= caracter <= "Z": #adiciona as letras a uma string
                texto += caracter
            
            elif texto != "": #quando for verificado um caracter que nao seja uma letra, tranca a string e adiciona-a 'a lista
                organizada += [texto]
                texto = ""                
                
        return organizada
    
    ficheiro = open(fich, "r") #abre o ficheiro que contem as palavras chave e a grelha
    lst_linhas = ficheiro.readlines() #le o ficheiro
    ficheiro.close() # fecha-o
    
    palavreado = organiza_palavreado(lst_linhas[1][10:]) #obtem as palavras chave a procurar na sopa
    sopa = grelha(organiza_sopa(lst_linhas[2:])) # obtem a sopa em si, ou seja, constroi a grelha
    
    #tuplo composto por 4 respostas das palavras encontradas na grelha (procurar numa direcao obtem reposta para dois sentidos)
    tuplo_respostas = (\
    procura_palavras_numa_direcao(sopa, palavreado, "N"),\
    procura_palavras_numa_direcao(sopa, palavreado, "E"),\
    procura_palavras_numa_direcao(sopa, palavreado, "NE"),\
    procura_palavras_numa_direcao(sopa, palavreado, "NW"))
    
    resposta_final = resposta([])
    
    for i in range(len(tuplo_respostas)): #junta as 4 respostas numa resposta final
        resposta_final = junta_respostas(resposta_final, tuplo_respostas[i])
    
    janela = janela_sopa_letras(fich)
    janela.mostra_palavras(resposta_final)
    janela.termina_jogo()    
    
    return resposta_final
      
def procura_palavras_numa_direcao(grelha, palavras, direcao):
    '''procura_palavras_numa_direcao : grelha x list x direcao -> resposta
       procura_palavras_numa_direcao(grelha, palavras, direcao) tem como resultado a resposta que representa as coordenadas das palavras encontradas na grelha segundo uma direcao'''
    
    def palavras_num_sentido(grelha, palavras, direcao):
        '''palavras_num_sentido : grelha x list x direcao -> resposta
           procura_palavras_numa_direcao(grelha, palavras, direcao) tem como resultado a resposta que representa as coordenadas das palavras encontradas na grelha segundo um sentido'''
    
        resposta_dir = resposta([]) #cria uma resposta vazia
        
        if e_norte(direcao): #Fixa a ultima linha
            for coluna in range(grelha_nr_colunas(grelha)): #itera as colunas da grelha
                cadeia = grelha_linha(grelha, coordenada(grelha_nr_linhas(grelha) - 1, coluna, direcao)) #(grelha_nr_linhas(grelha) - 1) pois e fixada a ultima linha da grelha
            
                #Verifica se existe alguma palavra na linha da grelha criada como cadeia
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                        resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(grelha_nr_linhas(grelha) - 1 - posicao(cadeia, palavras[indice_palavra]), coluna, direcao))
                        del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
                        
        elif e_sul(direcao): #Fixa a primeira linha
            for coluna in range(grelha_nr_colunas(grelha)): #itera as colunas da grelha
                cadeia = grelha_linha(grelha, coordenada(0, coluna, direcao)) #0 pois e fixada a primeira linha da grelha
                
                #Verifica se existe alguma palavra na linha da grelha criada como cadeia
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                        resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(posicao(cadeia, palavras[indice_palavra]), coluna, direcao))
                        del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
        
        elif e_leste(direcao): #Fixa a primeira coluna
            for linha in range(grelha_nr_linhas(grelha)): #itera as linhas da grelha
                cadeia = grelha_linha(grelha, coordenada(linha, 0, direcao)) #0 pois e fixada a primeira coluna da grelha
                
                #Verifica se existe alguma palavra na linha da grelha criada como cadeia
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                        resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(linha, posicao(cadeia, palavras[indice_palavra]), direcao))
                        del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
                        
        elif e_oeste(direcao): #Fixa a ultima coluna
            for linha in range(grelha_nr_linhas(grelha)): #itera as linhas da grelha
                cadeia = grelha_linha(grelha, coordenada(linha, grelha_nr_colunas(grelha) - 1, direcao)) #(grelha_nr_colunas(grelha) - 1) pois e fixada a ultima coluna da grelha
                
                #Verifica se existe alguma palavra na linha da grelha criada como cadeia
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                        resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(linha, grelha_nr_colunas(grelha) - 1 - posicao(cadeia, palavras[indice_palavra]), direcao))
                        del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
                        
        elif e_nordeste(direcao): #Fixa ultima linha e primeira coluna respetivamente
            for coluna in range(grelha_nr_colunas(grelha) - 1, -1, -1): #itera as colunas da grelha
                cadeia = grelha_linha(grelha, coordenada(grelha_nr_linhas(grelha) - 1, coluna, direcao))
                
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(grelha_nr_linhas(grelha) - 1 - posicao(cadeia, palavras[indice_palavra]), coluna + posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
            
                    
            for linha in range(grelha_nr_linhas(grelha) - 2, -1, -1): #itera as linhas da grelha
                cadeia = grelha_linha(grelha, coordenada(linha, 0, direcao))
                
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(linha - posicao(cadeia, palavras[indice_palavra]), posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
                            
        elif e_noroeste(direcao): #Fixa ultima linha e ultima coluna respetivamente
            for coluna in range(grelha_nr_colunas(grelha)): #itera as colunas da grelha
                cadeia = grelha_linha(grelha, coordenada(grelha_nr_linhas(grelha) - 1, coluna, direcao))
                   
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(grelha_nr_linhas(grelha) - 1 - posicao(cadeia, palavras[indice_palavra]), coluna - posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
            
            for linha in range(grelha_nr_linhas(grelha) - 2, -1, -1): #itera as linhas da grelha
                cadeia = grelha_linha(grelha, coordenada(linha, grelha_nr_colunas(grelha) - 1, direcao))
                    
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(linha - posicao(cadeia, palavras[indice_palavra]), grelha_nr_colunas(grelha) - 1 - posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
        
        elif e_sudeste(direcao): #Fixa primeira linha e primeira coluna respetivamente
            for coluna in range(grelha_nr_colunas(grelha) - 1, -1, -1): #itera as colunas da grelha
                cadeia = grelha_linha(grelha, coordenada(0, coluna, direcao))
                
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(posicao(cadeia, palavras[indice_palavra]), coluna + posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
            
            for linha in range(1, grelha_nr_linhas(grelha)): #itera as linhas da grelha
                cadeia = grelha_linha(grelha, coordenada(linha, 0, direcao))
                
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenadas(linha + posicao(cadeia, palavras[indice_palavra]), posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
                 
        elif e_sudoeste(direcao): #Fixa primeira linha e ultima coluna respetivamente
            for coluna in range(grelha_nr_colunas(grelha)): #itera as colunas da grelha
                cadeia = grelha_linha(grelha, coordenada(0, coluna, direcao))
                
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenada(posicao(cadeia, palavras[indice_palavra]), coluna - posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
            
            for linha in range(1, grelha_nr_linhas(grelha)): #itera as linhas da grelha
                cadeia = grelha_linha(grelha, coordenada(linha, grelha_nr_colunas(grelha) - 1, direcao))
                            
                for indice_palavra in range(len(palavras) - 1, -1, -1):
                    if len(cadeia) >= len(palavras[indice_palavra]): #Verifica se a palavra tem espaco para existir na cadeia obtida
                        if palavras[indice_palavra] in cadeia: #se a palavra estiver na cadeia, adiciona-a 'a resposta em cunjunto com a coordenada que a localiza
                            resposta_dir = acrescenta_elemento(resposta_dir, palavras[indice_palavra], coordenadas(linha + posicao(cadeia, palavras[indice_palavra]), - posicao(cadeia, palavras[indice_palavra]), direcao))
                            del(palavras[indice_palavra]) #como a palavra foi encontrada, podemos elimina-la da lista
                           
        return resposta_dir

    def posicao(cadeia, palavra):
        '''posicao : str x str -> int
           posicao(cadeia, palavra) analisa a cadeia gerada por grelha_linha onde se sabe que a palavra esta inserida e devolve a posicao da palavra dentro dessa cadeia'''  
           
        for pos in range(len(cadeia) - len(palavra) + 1): #precorre as posicoes da cadeia desde 0 ate a ultima posicao onde a palavra tem espaco para existir
            if palavra == cadeia[pos : pos + len(palavra)]: #compara a palavra com um conjunto de caracteres comecados na posicao i do mesmo tamanho que a palavra
                return pos
      
    return junta_respostas(palavras_num_sentido(grelha, palavras, direcao), palavras_num_sentido(grelha, palavras, direcao_oposta(direcao))) #devolve 2 sentidos opostos que formam uma direcao
