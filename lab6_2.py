s="()[]{}"
stack = [] 
is_valid = True 
for char in s:
    if char == "(" or char == "[" or char == "{":
        stack = stack + [char] #я добавил в список char вручную, прибавляя элемент без append
    else:
        if not stack: # если пришла закрывающая, а стопка пустая то ошибка
            is_valid = False
            break
        last = stack[-1] # смотрю какая скобка лежит на верху и убираю ее оттуда 
        stack = stack[:-1]
        if (char == "(" and  last != "(") or (char == "[" and  last != "[") or (char == "{" and  last != "{"):
            is_valid = False
            break
if stack:
    is_valid = False
print(is_valid)
                