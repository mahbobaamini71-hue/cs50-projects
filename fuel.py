
def main():
    while True:
        fr = input('Fraction: X/Y    ')
        
        try:
            x, y = fr.split('/')
            x = int(x)
            y = int(y)
            if x > y:
                raise ValueError('X must be <= Y!')
            result = round(x / y * 100)
   
        except (ValueError, ZeroDivisionError): 
            pass  
   
        
        else:
            if result <= 1:
                print('E')  
            elif result >= 99:
                print('F')
            else:
                print(f'{result}%')
            break
    
    
if __name__ == "__main__":
    main()
