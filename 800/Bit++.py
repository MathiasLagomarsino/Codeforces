def calculate(quant,solution):   
    if quant==0:
        return print(solution)
    operation=input() 

    if '+' in operation:
        solution+=1
        quant-=1
        return calculate(quant,solution)
    else:
        solution-=1
        quant-=1
        return calculate(quant,solution)

quant=input()
calculate(int(quant),0)