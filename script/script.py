L = [100, 45, -55, 125]
def min_sp(L):
    if len(L) == 1:
        return L[0]
    return L[0] if L[0] < min_sp(L[1:]) else min_sp(L[1:])

print(min_sp(L))

def mirror(a, res=0):
    if a:
        res = res * 10 + a % 10
        a = a // 10
        return mirror(a, res)
    else:
        return res
    #return mirror(a // 10, res*10 + a % 10) if a else res

print(mirror(154865))

def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10)

print(equal(150, 6))

def e():
    n = 1

    while True:
        yield (1 + 1 / n) ** n
        n += 1

#-------------

USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)

auth = yesno == "Y"

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

if auth:
    username = input("Введите ваш username:")

def has_access(func):
    def wrapper():
        if username in USERS:
            print("Доступ разрешен")
            func()
        else:
            print("Доступ запрещен")
    return wrapper

@is_auth
@has_access
def from_db():
    print("some data from database")

from_db()
#------------

L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))

def chet_(x):
    return x % 2 == 0   # функция возвращает только True или False

result = filter(chet_, [-2, -1, 0, 1, -3, 2, -3] )

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]


data = [
   (82, 1.91),
   (68, 1.74),
   (90, 1.89),
   (73, 1.79),
   (76, 1.84)
]

print(list(sorted(data, key = lambda x: x[0] / x[1] ** 2)))
print(min(data, key = lambda x: x[0] / x[1] ** 2))


a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))