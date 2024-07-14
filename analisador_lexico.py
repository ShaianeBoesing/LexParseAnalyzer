import re

regex_list = [r'if',
              r'[a-h]+',
              r' ']

regex_action = {'if': "if",
                '[a-h]+': "id",
                ' ': "whitespace"}

# Enforcing precedence
def first_match(token: str):
    for regex in regex_list:
        if re.fullmatch(regex, token):
            return regex
    else:
        return None

# Para os Ids
current_token_string = ''

with open("arquivo.txt") as fd:
    file = fd.read()
    if file[len(file) -1] == '\n':
        file = file[:-1]

    character_counter = 0
    was_matched = False
    while character_counter < len(file):
        ch = file[character_counter]

        current_token_string += ch
        matched_regex = first_match(current_token_string)

        if matched_regex is None and was_matched:
            matched_regex = first_match(current_token_string[:-1])
            print(regex_action[matched_regex])

            current_token_string = ''
            character_counter -= 1
            was_matched = False
        elif matched_regex is not None and not(was_matched):
            was_matched = True

        character_counter += 1

    # Matching the remaining tokens
    if first_match(current_token_string) != None:
        print(regex_action[first_match(current_token_string)])
    else:
        print("Error")