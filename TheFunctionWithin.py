'''TheFunctionWithin'''
def function(numa, numb, numc, numd):
    '''TheFunctionWithin'''
    print(func1(func1(numa)))
    print(func2(func1(numa-numb)))
    print(func3(func1(numa+numb), func1(numa+numc), func2(func1(numd**2))))
    print(func4(func3(func1(numa+numb), func1(numa-numc), func2(func1(numd**2))), \
func2(func1(numa-numb)), func1((func1(func1(func1(func1(numc)))))), (numd**8)))

def func1(numa):
    '''Function1'''
    f_1 = 2*numa
    return f_1

def func2(numa):
    '''Function2'''
    f_2 = (3*(numa**4))-(numa**3)+(2*(numa**2))+10
    return f_2

def func3(numa, numb, numc):
    '''Function3'''
    f_3 = (((numc+numa)**2)-(numa*numb)+(numb**2))
    return f_3

def func4(numa, numb, numc, numd):
    '''Function4'''
    f_4 = ((numa**2)+(numb**2)-(numc**2))/((numd**2)-(2*numa*numd)+2*numa)
    return f_4

function(float(input()), float(input()), float(input()), float(input()))
