import re
#talha
# Define the regular expressions for each token type
ID_REGEX = r'\b[a-zA-Z]+\w*\b'
CONST_REGEX = r'\b\d+(\.\d+)?\b'
PUNCT_REGEX = r'[;:,]'
LOGIC_REGEX = r'==|!=|<=|>=|<|>'
ARITH_REGEX = r'[+\-*/=]'
PAREN_REGEX = r'[()\[\]{}]'

# Define a function to identify the token type for a given token
def identify_token(token):
    if token in KEYWORDS:
        return 'Keyword'
    elif re.match(ID_REGEX, token):
        return 'Identifier'
    elif re.match(CONST_REGEX, token):
        return 'Constant'
    elif re.match(PUNCT_REGEX, token):
        return 'Punctuation'
    elif re.match(LOGIC_REGEX, token):
        return 'Logical Operator'
    elif re.match(ARITH_REGEX, token):
        return 'Arithmetic Operator'
    elif re.match(PAREN_REGEX, token):
        return 'Parenthesis'
    else:
        return 'Invalid'

# Define the list of keywords
KEYWORDS = ['int', 'float', 'double', 'false', 'await', 'else', 'import', 'pass', 'None', 'break',
            'except', 'in', 'raise', 'True', 'class', 'finally', 'is', 'return', 'and', 'continue',
            'for', 'lambda', 'try', 'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del',
            'global', 'not', 'with', 'async', 'elif', 'if', 'or', 'yield']

# Read a line of code from the console input or a file input
line = input(' :> Hello talha, this your code \n Enter a line of code: ')

# Split the line into tokens based on whitespace and the specified single character tokens
tokens = re.findall(r'\w+|[;:,]|[()\[\]{}]|[+\-*/=]|[<>=!]=?', line)

# Identify the type of each token and group them by type
token_groups = {}
for token in tokens:
    token_type = identify_token(token)
    if token_type not in token_groups:
        token_groups[token_type] = []
    token_groups[token_type].append(token)

# Print the results for each token type
for token_type in token_groups:
    print(f'{token_type}s({len(token_groups[token_type])}): {", ".join(token_groups[token_type])}')
