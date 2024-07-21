# Integrantes: Marcus Vinicius (21201474), Matheus Lafeta (21202339) e Shaiane Boesing (21202341)

from lexer.lexer import lexer
from parser.parser import is_lenguage_valid

lexer_output = lexer('./files/arquivo.txt')
is_valid = is_lenguage_valid(lexer_output)
print(is_valid)