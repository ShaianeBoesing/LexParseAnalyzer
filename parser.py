# flake8: noqa

translation = {
    "A": "MAIN",
    "B": "FLIST",
    "C": "FLIST'",
    "D": "FDEF",
    "E": "PARLIST",
    "F": "PARLIST'",
    "G": "STMT",
    "H": "ATRIBST",
    "I": "ATRIBST'",
    "J": "PRINTST",
    "K": "RETURNST",
    "L": "IFSTMT",
    "M": "IFSTMT'",
    "N": "STMLIST",
    "O": "STMLIST'",
    "P": "EXPR",
    "Q": "EXPR'",
    "R": "NUMEXPR",
    "S": "NUMEXPR'",
    "T": "TERM",
    "U": "TERM'",
    "V": "FACTOR",
    "Ç": "FACTOR",
    "W": "FCALL",
    "X": "TESTE",
    "Y": "PARLISTCALL",
    "Z": "PARLISTCALL'",
}

ll1_table = [
#      ==    (      )     *     +    ,      -     ;     <     =    >     id   def    if   else  num  print return int   {     }     $
    [None, None, None, None, None, None, None, "G",  None, None, None, "G",  "B",  "G",  None, None, "G",  "G",  "G",  "G",  None, "∑"   ],    # A
    [None, None, None, None, None, None, None, None, None, None, None, None, "D'C", None, None, None, None, None, None, None, None, None, ],    # B
    [None, None, None, None, None, None, None, None, None, None, None, None, "D" , None, None, None, None, None, None, None, None, "∑" , ],    # C
    [None, None, None, None, None, None, None, None, None, None, None, None, "def'id'('E')'{'N'}",None, None, None, None, None, None, None, None, None, ],    # D
    [None, None, "∑" , None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "int'id'F", None, None, None, ],    # E
    [None, None, "∑" , None, None, ",'E", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ],    # F
    [None, None, None, None, None, None, None, ";" , None, None, None, "H';", None, "L" , None, None, "J';", "K';", "int'id';", "{'O'}", None, None, ],    # G
    [None, None, None, None, None, None, None, None, None, None, None, "id'='I",None, None, None, None, None, None, None, None, None, None, ],    # H
    [None, "V'U'S'Q",None,None, None, None, None, None, None, None, None, "id'X",None, None, None,"V'U'S'Q",None, None, None, None, None, None, ],    # I
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "print'P", None, None, None, None, None, ],    # J
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, "return", None, None, None, None, ],    # K
    [None, None, None, None, None, None, None, None, None, None, None, None, None, "if'('P')'G'M", None, None, None, None, None, None, None, None, ],    # L
    [None, None, None, None, None, None, None, "∑" , None, None, None, "∑" , None, "∑" ,["∑","else'G"], None, "∑", "∑", "∑", "∑", "∑", "∑", ],    # M
    [None, None, None, None, None, None, None, "G'O", None, None, None, "G'O", None, "G'O", None, None, "G'O", "G'O", "G'O", "G'O", None, None, ],    # N
    [None, None, None, None, None, None, None, "N", None, None, None,  "N", None,  "N", None, None, "N", "N", "N", "N", "∑", None, ],    # O
    [None, "R'Q", None, None, None, None, None, None, None, None, None, "R'Q", None, None, None, "R'Q", None, None, None, None, None, None, ],    # P
    ["=='R", None, "∑" , None, None, None, None, "∑",  "<'R", None, ">'R", None, None, None, None, None, None, None, None, None, None, None, ],    # Q
    [None, "T'S", None, None, None, None, None, None, None, None, None, "T'S", None, None, None, "T'S", None, None, None, None, None, None, ],    # R
    ["∑", None, "∑", None, "+'T'S",  None, "-'T'S", "∑", "∑",  None, "∑",  None, None, None, None, None, None, None, None, None, None, None, ],    # S
    [None, "Ç'U", None, None, None, None, None, None, None, None, None, "Ç'U", None, None, None, "Ç'U", None, None, None, None, None, None, ],    # T
    ["∑" , None, "∑" ,"*'Ç'U", "∑" , None, "∑" ,  "∑", "∑" , None, "∑" , None, None, None, None, None, None, None, None, None, None, None, ],    # U
    [None, "('R')",None, None, None, None, None, None, None, None, None, None, None, None, None, "num", None, None, None, None, None, None, ],    # V
    [None, "('R')",None, None, None, None, None, None, None, None, None, "id", None, None, None, "num", None, None, None, None, None, None, ],    # Ç
    [None, None, None, None, None, None, None, None, None, None, None, "id'('Y')", None, None, None, None, None, None, None, None, None, None, ],    # W
    ["U'S'Q","('Y')",None,"U'S'Q","U'S'Q", None,"U'S'Q","U'S'Q","U'S'Q", None,"U'S'Q", None, None, None, None, None, None, None, None, None, None, None, ],    # X
    [None, None, "∑" , None, None, None, None, None, None, None, None, "id'Z", None, None, None, None, None, None, None, None, None, None, ],    # Y
    [None, None, "∑" , None, None, ",'Y", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ],    # Z
]

bind_col_table = ["==", "(", ")", "*", "+", ",", "-", ";", "<", "=", ">", "id", "def", "if", "else", "num", "print", "return", "int", "{", "}", "$"]

ll1_table_dict = {}

for letter_index, letter in enumerate(translation.keys()):
    ll1_table_dict[letter] = {}
    for way,terminal in zip(ll1_table[letter_index], bind_col_table):
        if way is not None:
            ll1_table_dict[letter].update({terminal:way})

# for bind in ll1_table_dict:
#     print(f"{translation[bind]}:{ll1_table_dict[bind]}")


mocked_lexer_output = ["def", "id", "(", "int", "id", ",", "int", "id", ")", "{", "id", "=", "id", "+", "id", ";", "id" ,"=" ,"id" ,"*" ,"id", ";", "return", ";", "}", "$"]
mocked_lexer_output1 = ["if","(","id","==","id",")","print","(","id",")", ";", "else", ";", "$"]

# mocked_lexer_output = ["{","int","id",";","$"]

def is_lenguage_valid(lexer_output, tree=["A", "$"], prints = True):
    while len(lexer_output):
        if prints:
            printable_tree = [(translation[letter] if letter in translation else letter) for letter in tree[:-1]]
            print(f"{' '.join(printable_tree)} $ ||||||||||||||||| {' '.join(lexer_output)}")

        # Primeiro verifica se o que recebeu na arvore está presente na lista de Variáveis não terminais ou é $
        # Caso esteja presente passa para executar esse bloco de tradução de Variável para produção possível.
        if tree[0] in translation.keys() or tree[0] == "$":

            # Caso a arvore esteja em $ e o output do lexer não estiver zerado, quer dizer que ainda há terminais a serem eliminados, ou seja o programa é inválido.
            # Caso o primeiro output do lexer não estiver em um output permitido pela tabela ll(1), significa que o programa é inválido.
            if (tree[0] == "$" and len(lexer_output)> 1) or (not lexer_output[0] in ll1_table_dict[tree[0]]):
                return False

            # Remove a primeira variável da arvore para trabalho.
            origin = tree.pop(0)

            # Caso for uma lista, significa que há ambiguidade, ou seja precisa passar em mais de um caminho para o mesmo não terminal.
            if isinstance(ll1_table_dict[origin][lexer_output[0]], list):
                for possible_output in ll1_table_dict[origin][lexer_output[0]]:
                    aux_tree = tree[:] # arvore de auxilio para não modificar a original
                    aux_tree_to_print = tree[:] # arvore de auxilio para printar a correta caso seja uma arvore válida
                    aux_lexer_output_to_print = lexer_output[:] # lista de tokens auxiliar para printar caso seja o caminho correto
                    
                    # A cada não terminal ou terminal do caminho possível a partir da origin, se adiciona a arvore auxiliar para rodar a recorrencia
                    for variable in reversed(possible_output.split("'")):
                        aux_tree.insert(0, variable)
                        aux_tree_to_print.insert(0, variable)

                    is_valid = is_lenguage_valid(lexer_output, aux_tree, False) # Roda a recorrencia com a árvore atual e a lista de token do lexer atual
                    if is_valid:
                        is_lenguage_valid(aux_lexer_output_to_print, aux_tree_to_print, True) # Se for válido, rodará a função novamente printando o passo a passo do parser para leitura
                        return True

                else:
                    return False # Caso não há um retorno válido a partir da ambiguidade, significa que não é um programa válido

            # A cada não terminal ou terminal do caminho possível a partir da origin, se adiciona a arvore na ordem correspondente.
            for variable in reversed((ll1_table_dict[origin][lexer_output[0]]).split("'")):
                tree.insert(0, variable)

        elif tree[0] != lexer_output[0]:
            return False
        # while true necessário para remover terminais com tokens caso há multiplos tokens em sequencia a serem eliminados.
        while True:
            printable_tree1 = [(translation[letter] if letter in translation else letter) for letter in tree[:-1]]
            if len(tree) == 0: # Caso não há mais nada na árvore significa que acabou o parsing
                break
            if tree[0] == lexer_output[0]: # Caso a variavel mais a esquerda for igual ao token do lexer mais a esquerda se faz a eliminação
                if prints:
                    print(f"{' '.join(printable_tree1)} $ ||||||||||||||||| {' '.join(lexer_output)}")
                del tree[0], lexer_output[0]
            elif tree[0] == "∑": # Caso for a string vazia, se faz a eliminação
                if prints:
                    print(f"{' '.join(printable_tree1)} $ ||||||||||||||||| {' '.join(lexer_output)}")
                del tree[0]
            else: # Caso não eliminar nenhum token, significa que pode passar para proxima etapa do parsing
                break
    return True
