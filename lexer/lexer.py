from lexer.DFA_table import transition_table, character_to_index


acceptance_state_action = {2: "id",
                           3: "id",
                           4: "if",
                           5: "whitespace",
                           6: "num",
                           8: "num",
                           9: "id",
                           10: "id",
                           11: "id",
                           12: "else",
                           13: "id",
                           14: "id",
                           15: "id",
                           16: "id",
                           17: "print",
                           18: "id",
                           19: "id",
                           20: "id",
                           21: "id",
                           22: "id",
                           23: "return",
                           24: "id",
                           25: "int",
                           26: "id",
                           27: "id",
                           28: "def",
                           29: ",",
                           30: ";",
                           31: "{",
                           32: "}",
                           33: "(",
                           34: ")",
                           35: "=",
                           36: "==",
                           37: "<",
                           38: ">",
                           39: "+",
                           40: "-",
                           41: "*"}

def lexer(file_name):
    output = []
    with open(file_name) as fd:
        file = fd.read()
        if file[len(file) -1] == '\n':
            file = file[:-1]

        # Main logic
        current_token_string = ''
        character_counter = 0
        last_acceptance_state = 0
        current_state = 1
        while character_counter < len(file):
            ch = file[character_counter]

            # Realize uma transição
            try:
                current_state = transition_table[current_state][character_to_index[ch]]
            except:
                print("Erro Léxico, caracter inválido econtrado: ", ch)
                exit(0)
                

            # O estado 0 implica a hora de tokenizar o input ou dar erro se o estado
            # atual não for de aceitação
            if current_state == 0:
                try:
                    if acceptance_state_action[last_acceptance_state] != "whitespace":
                        token = acceptance_state_action[last_acceptance_state]
                        output.append(token)
                        print(token)
                    current_state = 1
                    current_token_string = ""
                except:
                    print("Erro Léxico, token inválido encontrado: ", current_token_string)
                    exit(0)
            else:
                current_token_string += ch
                character_counter += 1

            # Se for um estado de aceitação, então ele é o mais novo estado de
            # aceitação, o que teria o maior input, respeitando o maximal munch
            if current_state in acceptance_state_action:
                last_acceptance_state = current_state


        # Matching the remaining token
        if current_state in acceptance_state_action:
            if acceptance_state_action[last_acceptance_state] != "whitespace":
                token = acceptance_state_action[last_acceptance_state]
                output.append(token)
                print(token)

    return output
