import sys
data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

    
i = 0
while i < len(content)-1:
    txt = content[i].rstrip("\n")
    
    i += 1
    pat = content[i].rstrip("\n")
        
    i += 1
    
    l = len(pat)
    for a in range(len(txt)):
        
        b = a+l

        if txt[a:b] == pat:
            print(f'O padrao foi encontrado na posicao {a}')
            
        if b == len(txt):
            break
            
