

def add(xx: float, yy: float) ->float:
    print('xx and yy ', xx, yy)
    result = xx + yy
    xx = 1234
    return result

def subtract(xx: float, yy: float = 0.0) -> float:
    return xx - yy

def print_add(xx: float, yy: float) -> None:
    print (xx + yy)

diff = subtract(3)
print(diff)

diff = subtract(yy=1.1, xx=2.2)
print(diff)

aa=2.2
bb=3.3
z= add(aa, bb)
print('aa', aa)

favourites = ['burger', 'hotdog', 'fish and chips']

def add_chinese(my_list: list):
    my_list.append('egg fried rice')

    print(favourites)
    add_chinese(favourites)
    print(favourites)

def do_some_maths(xx: float, yy: float, my_operation: callable):
    return my_operation(xx, yy)

result_1 = do_some_maths(1.1, 2.2, add)
print('do something with add', result_1)

result_2 = do_some_maths(1.1, 2.2, subtract)
print('do something with subtract', result_2)

secret_op = add #no bracket

result_3 = do_some_maths(1.1, 2.2, secret_op)

print(secret_op)