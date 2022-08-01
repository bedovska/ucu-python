
def print_rectangle(nrows, ncols):
    zirochky = ""
    for _ in range(ncols):
        zirochky = zirochky + "*"
    for _ in range(nrows):
        print(zirochky)



print_rectangle(6, 9)



def print_rectangle_border(nrows, ncols):
    zirochky = ""
    for _ in range(ncols):
        zirochky = zirochky + "*"
    no_zirochky = "" 
    for i in range(ncols):
        if i == 0 or i == ncols-1:
            no_zirochky = no_zirochky + "*"
        else: 
            no_zirochky = no_zirochky + " "
    for i in range(nrows):
        if i == 0 or i == nrows-1:
            print(zirochky)
        else:
            print(no_zirochky)


print_rectangle_border(4,3)