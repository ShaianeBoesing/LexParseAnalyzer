import re

regex_list = ['if', '[a-h]+', ' ']

regex_action = {'if': "if",
                '[a-h]+': "id",
                ' ': "whitespace"}

# Para os Ids
current_token_string = ''

# Enforcing precedence
def first_match(token: str):
    for regex in regex_list:
        if re.fullmatch(regex, token):
            return regex
    else:
        return None

with open("arquivo.txt") as fd:
    file = fd.read()
    if file[len(file) - 1] == '\n':
        file = file[:-1]

    character_counter = 0
    tokens = []
    while character_counter < len(file):
        ch = file[character_counter]
        current_token_string += ch

        matched_regex = first_match(current_token_string)
        
        if matched_regex:
            next_ch = file[character_counter + 1] if character_counter + 1 < len(file) else None
            if next_ch is None or not first_match(current_token_string + next_ch):
                tokens.append(regex_action[matched_regex])
                current_token_string = ''
        
        character_counter += 1

    # Matching the remaining tokens
    if current_token_string:
        matched_regex = first_match(current_token_string)
        if matched_regex:
            tokens.append(regex_action[matched_regex])
        else:
            tokens.append("Error")

    for token in tokens:
        print(token)
