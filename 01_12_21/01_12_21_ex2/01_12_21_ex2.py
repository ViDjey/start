def a(c, o, h):
    """Will find the minimum of three numbers"""
    c //= 2
    h //= 6
    if o >= c <= h:
        return c
    elif c >= o <= h:
        return o
    else:
        return h


kol_c = 0
kol_o = 0
kol_h = 0
tmp = 0
with open("input.txt", 'r') as f:
    for i in range(3):
        cim = f.read(1)
        if cim=='C' or cim=='O' or cim=='H':
            if cim == 'C':
                cim = f.read(1)
                if cim == '=':
                    cim = f.read(1)
                    while cim>='0' and cim<='9':
                        kol_c = kol_c*10 + int(cim)
                        cim = f.read(1)
                else:
                    tmp = 1        
            elif cim == 'O':
                cim = f.read(1)
                if cim == '=':
                    cim = f.read(1)
                    while cim>='0' and cim<='9':
                        kol_o = kol_o*10 + int(cim)
                        cim = f.read(1)
                else:
                    tmp = 1 
            elif cim == 'H':
                cim = f.read(1)
                if cim == '=':
                    cim = f.read(1)
                    while cim>='0' and cim<='9':
                        kol_h = kol_h*10 + int(cim)
                        cim = f.read(1)
                else:
                    tmp = 1 
            else:
                tmp = 1
        else:
            tmp = 1 
if  tmp == 1:
    print("input error in the file")
with open("output.txt", 'w') as file:
    file.write(f"Maximum number of alcohol molecules: {a(kol_c, kol_o, kol_h)}")
