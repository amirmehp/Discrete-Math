from dimal import *

def error(text):
    print(f"\033[91m\033[4mErr: {text}\033[0m")
    exit(1)
def help_menu():
    print("+------------[HELP]------------+")
    print("|help|to show this help message|")
    print("|menu|to show the options menu |")
    print("|exit|to quit the app          |")
    print("+------------------------------+")
def get_matrices(n):
    i = 1
    matrices = []
    if n in [1, 2]:
        while i <= n:
            print(f"\033[1mFor the Matrix({i}): \033[0m")
            rows = int(input("Enter the number of rows of your matrix: "))
            cols = int(input("Enter the number of columns of your matrix: "))
            m = [[0]*cols]*rows

            for row in range(0, rows):
                for col in range(0, cols):
                    cell = int(input(f"Enter the value for cell[{row}][{col}] (only ones and zeros): "))
                    if cell not in (0, 1):
                        error("Only Ones and Zeros are accepted")
                    m[row][col] = cell

            matrices.append(m)
            i+=1

    else:
        error("The number of matrices can only be 1 or 2")
    return matrices

help_menu()
i = 1
funcs = [
    "Bool Multiply",
    "Bool Sum",
    "Draw Matrix Graph",
    "Identity Matrix",
    "Is Matrix Antisymetric",
    "Is Matrix Connected",
    "Is Matrix Symetric",
    "Is Matrix Transitive",
    "Is Subgraph",
    "Join Matrix",
    "Meet Matrix",
    "Node Degree",
    "Path Length",
    "Symetric Closure",
    "Transmitive Closure",
    "Transpose Matrix"
]

for func in funcs:
    print(f"\033[96m\033[1m{i}) {func}\033[0m")
    i += 1

while True:
    in1 = input("Dismall>")
    match(in1):
        case "exit":
            exit(0)
        case "menu":
            i = 1
            for func in dir(dimall):
                if func[0] != "_":
                    print(f"\033[96m\033[1m{i}) {func.replace('_', ' ').title()}\033[0m")
                    i += 1
        case "help":
            help_menu()
        case "1":
            m1, m2 = get_matrices(2)
            if len(m1[0]) != len(m2):
                error("Number of Columns of the First matrix are not equal to the Number of Rows of the Second matrix")
            else:
                for row in bool_multiply(m1, m2):       
                    print(row)

        case "2":
            n1 = int(input("First Number: "))
            n2 = int(input("Second Number: "))
            if n1 not in [1, 0]:
                error(f"Wrong value: `{n1}`, it should be either 1 or 0")
            if n2 not in [1, 0]:
                error(f"Wrong value: `{n2}`, it should be either 1 or 0")
            
            print(bool_sum(n1, n2))

        case "3":
             m = get_matrices(1)[0]
             draw_matrix_graph(m)
        case "4":
            n = int(input("Enter the number of rows and cols: "))
            for row in identity_matrix(n):
                print(row)
        case "5":
            m = get_matrices(1)[0]
            if is_matrix_antisymetric(m):
                print("The Matrix is Antisymetric")
            else:
                print("The Matrix is NOT Antisymetric") 

        case "6":
            m = get_matrices(1)[0]
            if is_matrix_connected(m):
                print("The Matrix is Connected")
            else:
                print("The Matrix is NOT Connected") 

        case "7":
            m = get_matrices(1)[0]
            if is_matrix_symetric(m):
                print("The Matrix is Symetric")
            else:
                print("The Matrix is NOT Symetric") 

        case "8":
            m = get_matrices(1)[0]
           if is_matrix_transitive(m):
                print("The Matrix is Transitive")
            else:
                print("The Matrix is NOT Transitive") 

        case "9":
            m1, m2 = get_matrices(2)
            if is_subgraph(m):
                print("The Matrix is Subgraph")
            else:
                print("The Matrix is NOT Subgraph") 

        case "10":
            m1, m2 = get_matrices(2)
            print(join_matrix(m1, m2))

        case "11":
            m1, m2 = get_matrices(2)
            print(meet_matrix(m1, m2))

        case "12":
            m = get_matrices(1)[0]
            index = int(input("Enter the node index: "))
            print(node_degree(m, index))

        case "13":
            print("Enter the Adjacency Matrix: ")
            m = get_matrices(1)[0]
            
            print("\033[1mFor the Weight Matrix: \033[0m")
            rows = len(m)
            cols = len(m[0])
            
            w = [[0]*cols]*rows

            for row in range(0, rows):
                for col in range(0, cols):
                    cell = int(input(f"Enter the value for cell[{row}][{col}]: "))
                    w[row][col] = cell


                    
            path = []
            length = int(input("Enter your path length: "))
            for i in range(0, length):
                path.append(int(input(f"Enter Path Node ({i}):")))
                
            print(path_length(m, w, path))

        case "14":
            m = get_matrices(1)[0]
            print(symetric_closure(m))

        case "15":
            m = get_matrices(1)[0]
            print(transmitive_closure(m))

        case "16":
            m = get_matrices(1)[0]
            print(transpose(m))
            
        case default:
            print(f"Err: Invalid Input `{in1}`")
