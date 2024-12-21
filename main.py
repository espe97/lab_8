def сложение(u, v, b):
    n = max(len(u), len(v))
    u = [0] * (n - len(u)) + u  
    v = [0] * (n - len(v)) + v   
    w = []
    перенос = 0

    for i in range(n - 1, -1, -1):
        сумма = u[i] + v[i] + перенос
        w.insert(0, сумма % b)  
        перенос = сумма // b   

    if перенос > 0:
        w.insert(0, перенос)  

    return w


 
def вычитание(u, v, b):
    n = max(len(u), len(v))
    u = [0] * (n - len(u)) + u
    v = [0] * (n - len(v)) + v
    w = []
    займ = 0

    for i in range(n - 1, -1, -1):
        разность = u[i] - v[i] - займ
        if разность < 0:
            разность += b   
            займ = 1
        else:
            займ = 0
        w.insert(0, разность)

    
    while len(w) > 1 and w[0] == 0:
        w.pop(0)

    return w


 
def умножение(u, v, b):
    n, m = len(u), len(v)
    w = [0] * (n + m)   

    for i in range(n - 1, -1, -1):
        перенос = 0
        for j in range(m - 1, -1, -1):
            произведение = u[i] * v[j] + w[i + j + 1] + перенос
            w[i + j + 1] = произведение % b   
            перенос = произведение // b   
        w[i + j] += перенос   

     
    while len(w) > 1 and w[0] == 0:
        w.pop(0)

    return w


 
def быстрое_умножение(u, v, b):
    if len(u) == 1 or len(v) == 1:
        return умножение(u, v, b)   

    m = max(len(u), len(v)) // 2
    u_старшая, u_младшая = u[:-m], u[-m:]
    v_старшая, v_младшая = v[:-m], v[-m:]

    z0 = быстрое_умножение(u_младшая, v_младшая, b)   
    z1 = быстрое_умножение(сложение(u_старшая, u_младшая, b), сложение(v_старшая, v_младшая, b), b)
    z2 = быстрое_умножение(u_старшая, v_старшая, b)

     
    результат = сложение(сложение(z2 + [0] * (2 * m), вычитание(z1, сложение(z2, z0, b), b) + [0] * m, b), z0, b)
    return результат


 
def деление(u, v, b):
    n, m = len(u), len(v)
    if m == 0 or (m == 1 and v[0] == 0):
        raise ValueError("Деление на ноль невозможно")

    q = [0] * (n - m + 1)   
    r = u[:]   
     
    v = [0] * (n - m) + v

    for i in range(n - m + 1):
        q[i] = (r[i] * b + (r[i + 1] if i + 1 < n else 0)) // v[i]
        for j in range(m):
            r[i + j] -= q[i] * v[j]
        while r[i] < 0:
            q[i] -= 1
            for j in range(m):
                r[i + j] += v[j]

    return q, r


u = [4, 3, 2, 1]  
v = [7, 8, 9]      
b = 10
print(сложение(u, v, b))   


u = [4,3,2,1]
v= [7,8,9]
b= 10

print(вычитание(u,v,b))

u = [4,3,2,1]
v= [7,8,9]
b= 10

print(умножение(u,v,b))