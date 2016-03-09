a = int(input("do x = "))
b = int(input("free one = "))
mod = int(input("posle gcd = "))
MOD = int(input("pervii mod = "))
m = int(input("del = ")) # число проверки ряда на делимость

def first(a,b,mod,MOD): # а - коэф перед Х; b - после равно; mod - делитель; MOD - начальный модуль
    i = 1
    n = 1
    while (b + n*mod) % a != 0:
        n+=1
    print(n) 
    
 
    for i in range (int((b + n*mod)/a),MOD,mod):
        
        print ("raw: ",i)

        if i % m == 0:
            print (i)

        
first(a,b,mod,MOD)  


    
        
        
         
