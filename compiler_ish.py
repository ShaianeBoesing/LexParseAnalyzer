from lexer import lexer
from parser import is_lenguage_valid

lexer_output = lexer('./arquivo.txt')
is_valid = is_lenguage_valid(lexer_output)
print(is_valid)