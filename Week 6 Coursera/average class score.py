a = open('input.txt', 'r', encoding='utf8')
nine = []
ten = []
eleven = []

for list in a:
    b = list.rstrip('\n')
    x = b.split(' ')
    if x[2] == '9':
        nine.append(float(x[3]))
    elif x[2] == '10':
        ten.append(float(x[3]))
    else:
        eleven.append(float(x[3]))


def result(y):
    c = (sum(y) / len(y))
    return(c)


print(result(nine), result(ten), result(eleven))
