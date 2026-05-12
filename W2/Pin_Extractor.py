def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        # Split the poem into lines and iterate through each line
        lines = poem.split('\n')
        # enumerate function is used to get the index of the line and the line itself
        for line_index, line in enumerate(lines):
            words = line.split()
            # Check if the line has enough words to extract the character at the line index
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'
# example of extracting the list rather than a string
print(pin_extractor([poem, poem2, poem3]))
