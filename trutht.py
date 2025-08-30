class TokenType:
    LPAR = 'LPAR'
    RPAR = 'RPAR'
    AND = 'AND'
    OR = 'OR'
    THEN = 'THEN'
    VAR = 'VAR'

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

def lexer(expression):
    tokens = []  
    i = 0
    while i < len(expression):
        if expression[i] == " ":
            i += 1
            continue
        if expression[i] == '(':
            tokens.append(Token(TokenType.LPAR, expression[i]))
            i += 1
        elif expression[i] == ')':
            tokens.append(Token(TokenType.RPAR, expression[i]))
            i += 1
        elif expression[i].isalpha(): # TODO: Couldn't turn these `if`s into a switch, or maybe I shouldn't :))) 
            start = i
            while i < len(expression) and expression[i].isalpha():
                i += 1
            word = expression[start:i]  
            if word == "and":
                tokens.append(Token(TokenType.AND, word))
            elif word == "or":
                tokens.append(Token(TokenType.OR, word))
            elif word == "then":
                tokens.append(Token(TokenType.THEN, word))
            else:
                tokens.append(Token(TokenType.VAR, word))
        else:
            i += 1 
    return tokens

def parser(tokens, start=0, end=None):
    if end is None:
        end = len(tokens)
    i = start
    ast = None

    def parse_operand_at(idx):
        tok = tokens[idx]
        if tok.token_type == TokenType.LPAR:
            depth = 0
            for j in range(idx, end):
                if tokens[j].token_type == TokenType.LPAR:
                    depth += 1
                elif tokens[j].token_type == TokenType.RPAR:
                    depth -= 1
                    if depth == 0:
                        return parser(tokens, idx+1, j), j
            raise ValueError("Unmatched paren")
        else:
            return tok.value, idx

    while i < end:
        tok = tokens[i]

        if tok.token_type in (TokenType.AND, TokenType.OR, TokenType.THEN):
            if ast is None:
                left, left_end = parse_operand_at(i-1)
            else:
                left = ast  

            right, right_end = parse_operand_at(i+1)
            node_key = {TokenType.AND: "and",
                        TokenType.OR:  "or",
                        TokenType.THEN:"then"}[tok.token_type]
            ast = {node_key: {"lval": left, "rval": right}}
            i = right_end + 1
            continue

        elif tok.token_type == TokenType.LPAR:
            subtree, j = parse_operand_at(i)
            ast = subtree
            i = j + 1
            continue

        elif tok.token_type == TokenType.RPAR:
            i += 1
            continue

        else:
            i += 1

    return ast

def evaluate(node, env):
    if isinstance(node, str):
        return bool(env[node])
    if not isinstance(node, dict):
        print("Uknown identifier:", node)
        exit(1)
    if "not" in node:
        return not evaluate(node["not"], env)

    for op in ("and","or","then"):
        if op in node:
            left = node[op]["lval"]
            right = node[op]["rval"]
            L = evaluate(left, env) 
            R = evaluate(right, env)
            if op == "and": return L and R
            if op == "or":  return L or R
            if op == "then": return (not L) or R

    raise ValueError("unknown node: %r" % node)



def evaluate_value(value, env):
    if isinstance(value, str):
        return env[value]
    return evaluate(value, env)


def generate_truth_table(expression):
    variables = sorted(set(token.value for token in lexer(expression) if token.token_type == TokenType.VAR))
    
    n = len(variables)
    truthtable = lambda n: [[(v>>i)&1 for i in range(n-1,-1,-1)] for v in range(1<<n)] if n>0 else [[]]
    # Some cool magic I found from the StackOverFlow:))))

    header = variables + [expression]
    print(" | ".join(header))
    print("-" * (len(" | ".join(header))))
    
    for combination in truthtable(n):
        env = dict(zip(variables, [bool(x) for x in combination]))

        tokens = lexer(expression)
        parsed = parser(tokens)

        try:
            result = evaluate(parsed, env)

            row = combination + [int(result)]

            print(" | ".join(str(x) for x in row))
        
        except Exception as e:
            print(f"Error evaluating {expression}: {e}")

def main():
    variables = {}
    results = {}
    while True:
        tokens = []
        expression = input("Type some expression: ")
        match(expression):
            case "exit":
                exit(0)
            case "help":
                print("-----------------------------------------")
                print("var <ret>        | to define variables")
                print("<expression><ret>| to evaluate expression")
                print("exit <ret>       | to exit")
                print("-----------------------------------------")
            case default:
                generate_truth_table(expression)


if __name__ == "__main__":
    main()
