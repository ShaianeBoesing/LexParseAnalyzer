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
    [None, "R'Q", None, None, None, None, None, None, None, None, None, None, None, None, None, "R'Q", None, None, None, None, None, None, ],    # P
    ["=='R", None, "∑" , None, None, None, None, "∑",  "<'R", None, ">'R", None, None, None, None, None, None, None, None, None, None, None, ],    # Q
    [None, "T'S", None, None, None, None, None, None, None, None, None, None, None, None, None, "T'S", None, None, None, None, None, None, ],    # R
    ["∑", None, "∑", None, "+'T'S",  None, "-'T'S", "∑", "∑",  None, "∑",  None, None, None, None, None, None, None, None, None, None, None, ],    # S
    [None, "V'U", None, None, None, None, None, None, None, None, None, None, None, None, None, "V'U", None, None, None, None, None, None, ],    # T
    ["∑" , None, "∑" ,"*'V'U", "∑" , None, "∑" ,  "∑", "∑" , None, "∑" , None, None, None, None, None, None, None, None, None, None, None, ],    # U
    [None, "('R')",None, None, None, None, None, None, None, None, None, None, None, None, None, "num", None, None, None, None, None, None, ],    # V
    [None, None, None, None, None, None, None, None, None, None, None, "id'('Y')", None, None, None, None, None, None, None, None, None, None, ],    # W
    ["U'S'Q","('Y')",None,"U'S'Q","U'S'Q", None,"U'S'Q","U'S'Q","U'S'Q", None,"U'S'Q", None, None, None, None, None, None, None, None, None, None, None, ],    # X
    [None, None, "∑" , None, None, None, None, None, None, None, None, "id'Z", None, None, None, None, None, None, None, None, None, None, ],    # Y
    [None, None, "∑" , None, None, ",'Y", None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, ],    # Z
]

bind_col_table = ["==", "(", ")", "*", "+", ",", "-", ";", "<", "=", ">", "id", "def", "if", "else", "num", "print", "return", "int", "{", "}", "$"]

binds = {}

for letter_index, letter in enumerate(translation.keys()):
    binds[letter] = {}
    for way,terminal in zip(ll1_table[letter_index], bind_col_table):
        if way is not None:
            binds[letter].update({terminal:way})

for bind in binds:
    print(f"{bind}:{binds[bind]}")


mocked_lexer_output = ["def", "id", "(", "int", "id", ",", "int", "id", ")", "{", "id", "=", "id", "+", "id", ";", "id" ,"=" ,"id" ,"*" ,"id", ";", "return", ";", "}", "$"]

# mocked_lexer_output = ["{","int","id",";","$"]
tree = ["A", "$"]
while len(mocked_lexer_output):
    print(f"{''.join(tree)}   {''.join(mocked_lexer_output)}")
    if not mocked_lexer_output[0] in binds[tree[0]]:
        raise Exception("Parser error")
    origin = tree.pop(0)
    for variable in reversed((binds[origin][mocked_lexer_output[0]]).split("'")):
        tree.insert(0, variable)
    # print(tree)
    while True:
        if len(tree) == 0:
            break
        if tree[0] == mocked_lexer_output[0]:
            print(f"{''.join(tree)}   {''.join(mocked_lexer_output)}")
            del tree[0], mocked_lexer_output[0]
        elif tree[0] == "∑":
            print(f"{''.join(tree)}   {''.join(mocked_lexer_output)}")
            del tree[0]
        else:
            break

# def func1 ( int A , int B )
# {
#  C = A + B ;
#  D = B * C ;
# return ;
# }
