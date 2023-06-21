""" def strcounter(string): #сложность O(n**2)
    for symbol in string:
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter +=1
        print(symbol, counter)

strcounter('abcddaab') """

""" def strcounter(string): #сложность O(m*n) n - числа ь - уник числа
    for symbol in set(string):
        counter = 0
        for sub_symbol in string:
            if symbol == sub_symbol:
                counter +=1
        print(symbol, counter)

strcounter('bcddaabac') """

#у множества set() нет порядка (123 == 312)

def strcounter(string): #сложность О(n)
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0)+1
    print(syms_counter)
  
strcounter('bcddaabac')
