def split_chars(input):
    return [char for char in input]

# here's how you read an int as an input
x = int(input())

tests = []
for _ in range(x):
    _input = input()
    try:
        tests.append(list(map(int, split_chars(_input))))
    except:
        tests.append(None)


def check_pesel(input):
    if not input or len(input) != 11:
        print('N')
    
    a,b,c,d,e,f,g,h,i,j,k = input
    result = a + 3*b + 7*c + 9*d + e + 3*f + 7*g + 9*h + i + 3*j + k
    if result % 10 == 0:
        print('Y')
    else:
        print('N')

for i in range(x):
    check_pesel(tests[i])