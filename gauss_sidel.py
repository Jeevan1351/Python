# This is a program to find the solution to three simultaneous linear equation using Gauss-Sidel method

def input_coeff():
    lst = []
    for i in range(0,3,1):
        e = float(input())
        lst.append(e)
    return lst

def xinput():
    x = []
    print("Enter the coefficients of the x term : ")
    x = input_coeff()
    return x

def yinput():
    y = []
    print("Enter the coefficients of the y term : ")
    y = input_coeff()
    return y

def zinput():
    z = []
    print("Enter the coefficients of the z term : ")
    z = input_coeff()
    return z

def cinput():
    c = []
    print("Enter the constant term : ")
    c = input_coeff()
    return c

def compute(xc, yc, zc, ct):
    x, y, z = 0, 0, 0
    for i in range(1,11,1):
        x = (ct[0] - yc[0] * y - zc[0] * z) / xc[0]
        y = (ct[1] - xc[1] * x - zc[1] * z) / yc[1]
        z = (ct[2] - yc[2] * y - xc[2] * x) / zc[2]
    return x, y, z

def output(x, y, z):
    print(" x = {}\n y = {}\n z = {}".format(x, y, z))

def main():
    xc, yc, zc, ct = [], [], [], []
    xc = xinput()
    yc = yinput()
    zc = zinput()
    ct = cinput()
    x, y, z = compute(xc, yc, zc, ct)
    output(x, y, z)

main()

    
