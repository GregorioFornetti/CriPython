
with open("teste.txt", 'r', encoding='utf-8') as teste:
    x = teste.read().split('\n')
    print(x[0])
    print(x[1])