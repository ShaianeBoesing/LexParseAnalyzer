# Integrantes: Marcus Vinicius (21201474), Matheus Lafeta (21202339) e Shaiane Boesing (21202341)


import argparse
import sys
import os
from lexer.lexer import lexer
from parser.parser import is_language_valid


def main():
    parser = argparse.ArgumentParser(description='Compila um arquivo de código fonte.')
    parser.add_argument('filename', type=str, help='Nome do arquivo a ser compilado')
    args = parser.parse_args()

    filename = args.filename
    filepath = './files/test-files/' + filename

    if not os.path.isfile(filepath):
        print(f"Erro: O arquivo '{filepath}' não foi encontrado.", file=sys.stderr)
        sys.exit(1)

    try:
        lexer_output = lexer(filepath)
        is_valid = is_language_valid(lexer_output)
        print(is_valid)
    except FileNotFoundError as e:
        print(f"Erro: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
