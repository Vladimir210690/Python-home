
while True:
    a = float(input("Введите первое число: "))
    i = input("Введите знак операции: ")
    b = float(input("Введите второе число: "))
    if i == '+':
        print(a + b)
    elif i == '-':
        print(a - b)
    elif i == '*':
        print(a * b)
    elif i == '/':
        if b == 0:
            print("Ошибка! Нельзя делить на ноль.")
        else:
            print(a / b)

        
    
    
    




   
        
      
        
        
