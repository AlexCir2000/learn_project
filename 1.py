from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text = 'Ok')

if __name__ == '__main__':
    MyApp().run()

"""

from tkinter import *

wnd = Tk()
wnd.title('Window')
wnd.geometry('250x150')
wnd.resizable(False, False)
lbl = Label(wnd,text='Hello, everybody', font=('Arial Bold',20))
lbl.place(x=30, y=20)
btn = Button(wnd, text='Close', font=('Courier New Bold', 13), command=wnd.destroy)
btn.place(x=50, y=65, width=170, height=50)
wnd.mainloop()
"""
"""

from threading import *

def func(n):
    global L
    myLock.acquire()
    l = []
    for i in range(n):
        l.append(i)
    L.insert(n,l)

    print(n, L)
    myLock.release()


L=[]
T = []
myLock = Lock()
for i in (5,3,2,1,4,0):
    T.append(Thread(target=func, args=(i,)))
for t in T:
    t.start()
for t in T:
    t.join()

print(L)

"""
"""
class obj():
    def __init__(self):
        self.L1 = []
        self.L2 = []
    def __call__(self, n):
        for i in range(200):
            if type(n) == int:
                self.L1.append(n)
            if type(n) == str:
                self.L2.append(n)


a = obj()
s1 = Thread(target=a, args=(1,))
s2 = Thread(target=a, args=('Z'))
s1.start()
s2.start()
s1.join()
s2.join()
print(a.L1)
print(a.L2)

"""
"""
from threading import *
from time import sleep
def ins(a):
    global L

    while True:
        MyEvevnt.wait()
        MyEvevnt.clear()
        if len(L)<8:
            # MyLock.acquire()
            L.append(a)

            # MyLock.release()
            print(L)
        else:
            MyEvevnt.set()
            break

        MyEvevnt.set()
        sleep(0.3)

a1 = Thread(target=ins, args=('s'))
a2 = Thread(target=ins, args=('1'))
L=[]
MyLock = Lock()
MyEvevnt = Event()
MyEvevnt.set()
a1.start()
a2.start()
a1.join()
a2.join()

print('End', L)
"""

"""
from threading import *
from time import sleep
def func():
    global res
    i = 1
    while myevent.is_set():
        res += i**2
        print(res, end=' ')
        i += 1
        sleep(0.3)

a = Thread(target=func)
myevent = Event()
myevent.set()
res = 0
a.start()
sleep(5)
myevent.clear()
if a.is_alive():
    a.join()
print('\nEnd')
"""



"""
class MyError(Exception):
    def __init__(self):
        # super().__init__()
        self.L = []

    def __add__(self, n):
        self.L.append(chr(n))
        return self

def getMyError(n):
    try:
        if n <= ord('b'):
            getMyError(n + 1)
            raise MyError
    except MyError as error:
        raise error + n
def getList():
    try:
        getMyError(ord('a'))
    except MyError as error:
        return error.L

L = getList()
print(L)

# raise error + 'a'

print(ord('z'))
print(ord('a'))

"""

"""
import math


def func(a):
    try:
        a = float(a)
    except:
        raise TypeError(' Incorrect type')
    try:
        x = math.sin(a) / (a * (a - 1))
    except ZeroDivisionError:
        if a == 0:
            return -1
        else:
            raise ZeroDivisionError('Zero Division')
    return x

a = 3

try:
    print(func(a))
except Exception as error:
    print(error)

"""

"""
m = '5'
n = -10
try:
    if m>n:
        raise ArithmeticError
    for i in range(m,n+1):
        print(i, end=' ')
except TypeError as error:
    print(error.__class__.__name__)
except ArithmeticError:
    print('m>n')
"""
"""
def summa(*n):
    res = 0
    for i in n:
        try:
            res += i
        except TypeError as error:
            print('incorrect type:', i)
            print(error.__class__.__name__)
            for j in error.__class__.__mro__:
                print(j.__name__)
            continue
    return  res

print(summa(1,'3,',5,7,[1,2]))
"""
"""
from threading import *
from time import sleep


def calc(txt, op,time):
    global number
    for i in range(4):
        # MyLock.acquire()
        print('Blocked: ', txt)
        sleep(time)
        try:
            print(txt, ' read = ', number)
            if op:
                number += 1
            else:
                number -= 1
            print(txt, ' written ', number)
        finally:
            # MyLock.release()
            print('object released')
            print('--------------')


number = 0
MyLock = Lock()
a = Thread(target=calc, kwargs={'txt':'A', 'op':True, 'time':1})
b = Thread(target=calc, kwargs={'txt':'B', 'op':False, 'time':1})
b.start()
a.start()

a.join()
b.join()
print('End')
"""
"""
def func_a(count, time, text):
    for i in range(count):
        print(text,'a[',i,']')
        sleep(time)
def func_b():
    for i in range(5):
        print('b[',i,']')
        sleep(1)

t = Thread(target=func_a, args=(4,2,'Secondary thread '))
t.start()
sleep(0.1)
func_a(3,1,'Primary thread ')

if t.is_alive():
    t.join()
print('Hello')
"""

"""
error = Exception('First error')
error1 = ArithmeticError('Ariphmetic Error')
print(error1)
print(error1.__doc__)
print(error1.__class__.__bases__[0].__name__)
raise error
raise error

"""
"""
a = [10,20,30,40]
for i in [0,1,2,'three',4,3]:
    try:
        print('a['+str(i)+'] = ', end='')
        a[i] /= (i - 1)
        print(a[i])
    except (TypeError, IndexError) as error:
        print()
        print('Error class: ', error.__class__.__name__)
        print('Error doc: ', error.__doc__)
        print('Base class: ',error.__class__.__bases__[0].__name__)
        for k in error.__class__.__mro__:
            print(k.__name__, end=' - ')
    except ZeroDivisionError as error:
        print()
        print('Error class: ', error.__class__.__name__)
        print('Error doc: ', error.__doc__)
        for k in error.__class__.__mro__:
            print(k.__name__, end=' - ')
        a[i] = 0
"""
"""
class decor:
    def show_o(self):
        print()
        for i in self.__dict__:
            if not i.startswith('_') and i != 'show_o':
                print(i, self.__dict__[i])


class MyClass(decor):
    def __init__(self, n):
        self.L = [1,1]
        a = 1
        b = 1
        for i in range(n-2):
            a, b = b, a + b
            self.L.append(b)

    def __iter__(self):
        self.pos = -1
        return self

    def __next__(self):
        self.pos += 1
        return self.L[self.pos]


a = iter(MyClass(19))
try:
    while True:
        print(next(a), end=' ')
except:
    print('That''s all')
"""
"""
class MyClass(decor):
    def __init__(self, a):
        self.L = []
        if type(a) == list:
            for i in range(len(a)):
                if type(i) == int:
                    self.L.append(a[i])
        else:
            print('Incorrect input data')


    def __call__(self, n):
        sum = 0
        for i in range(len(self.L)):
            sum += self.L[i]*(n**i)
            print(self.L[i], ' * ', n, '**',i,' = ',self.L[i]*(n**i) , ' + ')
        return sum


a = MyClass([10,-5,12,2,6,-1,67])
print(' = ',a(4))

a. show_o()
"""
"""
class MyClass(decor):
    def __init__(self, a, b):
        self.L1 = a
        self.L2 = b


    def __iter__(self):
        self.pos = -1
        return self

    def __next__(self):
        self.pos += 1
        try:
            res = self.L1[self.pos] + self.L2[self.pos]
        except:
            res = self.L1[self.pos] if len(self.L1)>len(self.L2) else self.L2[self.pos]

        return res


a = iter(MyClass([1,2,3,4,5],[4,5,6,7]))

try:
    while True:
        print(next(a), end=' ')
except:
    print('no values')

a. show_o()
"""
"""
class MyClass(decor):
    def __init__(self,T):
        self.L = []
        if type(T) == list:
            for i in range(len(T)):
                self[i] = T[i]
        else:
            print('Incorrect input data')

    def __len__(self):
        return len(self.L)

    def __getitem__(self, item):
        return self.L[item][0]

    def __setitem__(self, key, value):
        if type(value) == str:
            self.L.insert(key, value)

a = MyClass([7,'31','27','ffff',5, 3.56, [1,2]])
M = [7,'31','27','ffff',5, 3.56, [1,2]]
for i in range(len(M)):
     a[i]= M[i]

for j in range(len(a)):
    print(a[j], end=' ')


a.show_o()
"""
"""
class MyClass(decor):
    def __init__(self):
        L =[]
        n =0
    def __eq__(self, k):
        if self.L[0] == k:
            print(self.L[0],' = ', k, ' True')
        else:
            print(self.L[0], ' = ', k, ' False')

    def __ne__(self, k):
        if self.L[1] != k:
            print(self.L[1],' != ', k, ' True')
        else:
            print(self.L[1], ' != ', k, ' False')

    def __gt__(self, k):
        if self.L[2] > k:
            print(self.L[2],' > ', k, ' True')
        else:
            print(self.L[2], ' > ', k, ' False')

    def __add__(self, k):
        self.n = self.n + k
        return MyClass()

    def __sub__(self, k):
        self.n = self.n - k
        return MyClass()

    def __rsub__(self, k):
        self.n = k - self.n
        return MyClass()

    def __mul__(self, k):
        self.n = self.n * k
        return MyClass()

    def __truediv__(self, k):
        self.n = self.n / k
        return MyClass()

    def show(self):
        print(self.n, end=' ')

obj1 = MyClass()
obj2 = MyClass()
obj1.L = [55, 66, 34, -2, 11]
obj2.L = [11, 33, -8, 2, 222]
obj1 == obj2.L[0]
obj1 != obj2.L[1]
obj1 > obj2.L[2]
# obj1.show()
obj1.show_o()
"""
"""
v = [1,2,3,4,5].__iter__()
for i in range(9):
    try:
        print(v.__next__())
    except StopIteration:
        print('no more')
"""
"""
class Fibs(decor):
    def __getitem__(self, item):
        a = 1
        b = 1
        for i in range(0, item-2):
            a, b = b, a+b
        return b

f = Fibs()
for k in range(1,16):
    print(f[k], end=" ")
f.show_o()
"""
"""
class MyClass():
    def __init__(self,n):
        self.val = n

    # def __str__(self):
    #     return str(self.val)

    def __add__(self, other):
        if type(other) == int:
            self.val += other
        else:
            self.val = 0
        return MyClass(self.val)

    def show_o(self):
        for i in self.__dict__:
            if not i.startswith('_') and i != 'show_o':
                print(i, self.__dict__[i])

a = MyClass(10)

print(a)
a.show_o()
b = a + 25
print(b)
a.show_o()
b.show_o()
c = a + 'Hello'
print(c)
a.show_o()
"""
"""
class MyClass(decor):
    p1 =0
    p2 = None
    def print_mro(self):
        k = 1
        for i in MyClass.__mro__:
            print("[" + str(k) + "]", i.__name__)
            k += 1

a = MyClass()
a. print_mro()
a.p1 = 0
"""
"""
class Binar:
    link1 = None
    link2 = None
    level = 0



def create_graph(a,n):
    a.link1 = Binar()
    a.link2 = Binar()
    a.level = n
    if n>0:
        create_graph(a.link1, n-1)
        create_graph(a.link2, n-1)

def print_graph(a):

    if a.link1 != None:
        print(a.link1, a.level, end=' ')
        print(a.link2, a.level, end=' ')
        print()
        print_graph(a.link1)
        print_graph(a.link2)
a = Binar()
create_graph(a,3)
print_graph(a)
"""
"""
class MyClass:
    num =0
    link = None
    def ins(self,k):
        a = self
        for i in range(k):
            # renumbering
            #a.num += 1
            a = a.link

        b = MyClass()
        b.link = a.link
        b.num = a.num
        a.link = b
        a.num = b.num + 1

    def del_obj(self,k):
        if k == 0:
            print('Can\'t delete 1 arg')
            return
        a = self
        for i in range(k-1):
            # a.num -= 1
            a = a.link
        a.link = a.link.link


    def show(self):
         a = self
         while a.link != None:
            print(a.num, end=' ')
            a = a.link


def func(n):
    a = MyClass()
    a.num = n
    if n>0:
        a.link = func(n-1)
    return a


res = func(9)
res.show()
print()
res.ins(8)
res.show()
print()
res.del_obj(4)
res.show()
"""
"""
class MyClass:
    def show_o(self):
        for i in self.__dict__:
            if not i.startswith('_') and i != 'show_o':
                print(i, self.__dict__[i])


def obj_sum(a,b):
    c = MyClass()
    c.p1 = []
    for i in range(max(len(a.p1),len(b.p1))):
        try:
            c.p1.append(a.p1[i]+b.p1[i])
        except:
            c.p1.append(a.p1[i] if len(a.p1)>len(b.p1) else b.p1[i])
    return c


a = MyClass()
b = MyClass()
a.p1 = [1,3,5,7,9]
b.p1 = [2,4,6,8,10,12,14]
c = obj_sum(a,b)
a.show_o()
b.show_o()
c.show_o()
"""
"""
class MyClass:
    p1 = 0


def create_objlist(n):
    obj_list = []
    for i in range(n):
        a = MyClass()
        a.p1 = 2 * i + 1
        obj_list.append(a)
    return obj_list

L = create_objlist(5)
for j in L:
    print(j.p1)

"""
#
"""
class class1:
    def __init__(self,L):
        k = 1
        for i in L:
            self.__dict__[k] = i
            k += 1
    def show_o(self):
        for i in self.__dict__:
            if not str(i).startswith('_') and i != 'show_o':
                print(i, self.__dict__[i])

def create_obj(obj):
    class class2:
        def __init__(self):
            k = 1
            for i in obj.__dict__.values():
                if type(i) == int:
                    self.__dict__[k] = i
                    k += 1
        def show_o(self):
            for i in self.__dict__:
                if not str(i).startswith('_') and i != 'show_o':
                    print(i, self.__dict__[i])
    return class2()

a = class1([1,7,4.55,35,'ddd',44,[1,2,3]])

a.show_o()
b = create_obj(a)
b.show_o()
"""
"""
def obj_create(L,s):
    if type(L) == list and type(s) == str:
        class Internal_Class:
            def __init__(self):
                for i in L:
                    self.__dict__[i] = 122

            def show_o(self):
                for i in self.__dict__:
                    if not i.startswith('_') and i != 'show_o':
                        print(i, self.__dict__[i])

        Internal_Class.__name__ = s
        return Internal_Class()
    else:
        print('Invalid arguments')
a = obj_create(['a','b','c'],'MyClass')
a.show_o()
"""
"""
class MyClass:
    "Show is go on"
    def __init__(self, a ):
        self.L = []
        for i in a:
            if type(i) == int:
                self.L.append(i)
    def show(self,L):
        for i in L:
            print(i)
    def sred(self, L):
        print(sum(L)/len(L))

    def show_o(self):
        for i in self.__dict__:
            if not i.startswith('_') and i != 'show_o':
                print(i, self.__dict__[i])

a = MyClass([1,5, 4, 4.44, 'asas', [1,2,3]])
a.show(a.L)
a.sred(a.L)
a.show_o()
print(a.L)
"""

"""
class MyClass:
    "Show is go on"
    def __init__(self, a , b):
        if type(a) == str and type(b) == int:
            self.txt = a
            self.num = b
        elif type(a) == int and type(b) == str:
            self.txt = b
            self.num = a
        elif type(a) == str and type(b) == str:
            self.txt = a + b
        elif type(a) == int and type(b) == int:
            self.num = a + b

    def show_o(self):
        for i in self.__dict__:
            if not i.startswith('_') and i != 'show_o':
                print(i, self.__dict__[i])

a = MyClass('sss', 5)
a.show_o()
b=MyClass(123, 'ssssss')
b.show_o()
c=MyClass(123, 321)
c.show_o()
d=MyClass('aaaaaa', 'ssssss')
d.show_o()
e=MyClass(1.64,'s')
e.show_o()


"""

"""
class MyClass:
    "Show is go on"
    def __init__(self, a =1 , b=1):
        self.p1 = a
        self.p2 = b


    def show_p(self):
        for i in MyClass.__dict__:
            if not i.startswith('_') and i != 'show_p':
                print(i, MyClass.__dict__[i])
    def show_o(self):
        for i in self.__dict__:
            if not i.startswith('_') and i != 'show_p':
                print(i, self.__dict__[i])
    p1c =0
    p2c =0

a = MyClass(5,'sss')

a.show_p()
a.show_o()
"""
"""
name = 'abrakadabra.txt'
f2 = open(name, 'wt')
s = ' isfOIoo OHHH lKH\nJHjhjhjgw83'
f2.write(s.upper())
f2.close()
"""

"""

from datetime import datetime
date1 = datetime.today()
date2 = datetime(1980,1,19,22,10,5)
delta = date1-date2
print(delta, delta.seconds)
"""
"""
def func(a,b):
    res = []
    ares = []
    print ('A+B=', a+b)
    res.append(a+b)
    ares.append(abs(a+b))
    print('A-B=', a - b)
    res.append(a - b)
    ares.append(abs(a - b))
    print('A*B=', a * b)
    res.append(a * b)
    ares.append(abs(a * b))
    print('A/B=', a / b)
    res.append(a / b)
    ares.append(abs(a / b))
    print(res)
    print(ares)
    print('max =', max(ares))
    print('min =', min(ares))

a = complex(1,2)
b = complex(8,-3)
func(a,b)
"""
"""
# a = int(input('Enter base: '))
a = ''
b = 135
c= oct(b)
a = list(reversed(c[2::]))
r= ''.join(i for i in a)
r = '0o'+r
print(r)
print(int(eval('0o207')))
print(int(eval(r)))
"""
"""
name = 'poem.txt'
f = open(name, 'wt+')
f.write('Some text \nwith end of strings\n')
f.seek(0)
print(f.tell(), '->', f.read(4))
f.seek(3,0)
# f.seek(f.tell()-3)
print(f.tell(), '->', f.read(3))
s = f.readline()
s += f.readline()
s += f.readline()
print(s)
f.close()
"""
"""
from datetime import time, date, datetime

mytime = time(12,23,56)
print(mytime, mytime.fromisoformat('01:20:56'), mytime.second)
mytime=mytime.replace(15, second=45)
print(mytime)

mydate = date(1980,1,19)
newdate = date.today()

print(newdate-mydate)


date = datetime.now()
print(date, date.date(), date.time())
"""
"""
import types
from fractions import Fraction
from decimal import Decimal
A=3+4j
print("A =", A)
print("Re(A) =", A.real)
print("Im(A) =", A.imag)
print("|A| =", abs(A))
B = -1+1j
print("B =", B)
C=complex(0,1)
print("C =", C)

print("A+B =", A+B)
print("A*C =", A*C)
print("A/B =", A/B)


a = Fraction(2,5)
b = Fraction(3,10)
print(a+b)
c = 1/3
print(3*c)
print(d)
print(type(b))
c = int(b,2)
print(type(c))
print(oct(c))
print(bin(a))
print(-1//5)
"""

"""
def func(n):
    for i in range(n):
        yield 2**i
for j in func(10):
    print(j//2)
"""
"""
def func(a:'множитель', n:'кол. членов'):
    "Сумма членов геометрической прогрессии"
    global s
    global summ
    print(s, end=' ')
    summ += s
    s *= a
    if n-1>0:
        func(a, n-1)

s = 1
summ = 0
print(func.__doc__, func.__annotations__)
func(5,8)
print('\n',summ)
"""
"""
def func(txt):
    print(txt[0], end=' ')
    if len(txt[2::]) > 0:
        func(txt[2::])


txt2 = ' aB Some Long String With Spaces ZYp'
func(txt2)
"""
"""
def func(fu,n):
    def ret(x):
        for i in range(n):
            x = fu(x)
        return x
    return ret

def f(x):
    return x*x

r = func(f,2)

print(r(5))
"""
"""
def sum(a,b):
    summa = 0
    max_list = True if len(a)>len(b) else False
    k = 0
    for i in range(max(len(a),len(b))):
        if max_list:
            summa += a[i] + b[k]
        else:
            summa += a[k] + b[i]
        if k == min(len(a),len(b))-1:
            k = 0
        else:
            k += 1
    return summa


"""

"""
def func(a:'annot')->'Annotation':
    "docs functions"
    print(a)
print(func.__doc__)
print(func.__annotations__)
"""

"""
def display(f, a, b):
    for k in range(a, b+1):
        print("{0:4}".format(f(k)), end=" ")
    print()

def mypow(n):
    return lambda x: x**n

def apply(f, h):
    def calc(x):
        return f(h(x))
    return calc

A= mypow(2)
B= mypow(3)
C=apply(lambda x: 2*x+1, lambda x: 2*x)

print("x ", end="")
display(lambda x: x,1,5)
print("A(x)", end="")
display(A,1,5)
print("B(x)", end="")
display(B,1,5)
print("C(x)", end="")
display(C,1,5)
"""
"""


num =10
L = lambda n: 2*n+1

for i in range(num):
    print((lambda n:2*n+1)(i))
"""
"""
txt = ' aB Some Long String With Spaces ZYd'
txt2 = ''
words = txt.split()
sword = words[::-1]
txt2 += ' '.join(i for i in sword)
print(txt2)
"""
"""
def max_elem(words):
    n =0
    maxim = 0
    for i in range(len(words)):
        if len(words[i])>maxim:
            n = i
            maxim = len(words[i])
    return n



txt = ' wewewewweaB Some Long String Without Spaces ZYd'
txt2 = ''
txt1 = ''
words = txt.split()
print(words)
n= max_elem(words)
print(n)
txt2 += ' '.join(words[i] for i in range(len(words)) if i != n)
print(txt2)
"""
"""
glas = 'aeijouwy'
glas += glas.upper()
soglas = 'bcdfghklmnpqrstvxz'
soglas += soglas.upper()
glas_list= list(glas)
soglas_list = list(soglas)
print(txt)

for i in txt:
    if i in glas_list:
        if i == 'Y':
            txt1 += 'a'
        else:
            txt1 += ''.join(glas_list[glas_list.index(i)+1])
    elif i in soglas_list:
        if i == 'Z':
            txt1 += 'b'
        else:
            txt1 += ''.join(soglas_list[soglas_list.index(i)+1])

    else:
        txt1 += ' '
print(txt1)
for i in txt1:
    if i in glas_list:
        if i == 'a':
            txt2 += 'Y'
        else:
            txt2 += ''.join(glas_list[glas_list.index(i)-1])
    elif i in soglas_list:
        if i == 'b':
            txt2 += 'Z'
        else:
            txt2 += ''.join(soglas_list[soglas_list.index(i)-1])

    else:
        txt2 += ' '
print(txt2)
"""
"""
i = 0
while len(txt) > i or len(txt2) > i:
    try:
        txt1 += txt[i]
        txt1 += txt2[i]
    except:
        txt1 += '*'
    i += 1
print(txt1)
"""
"""
for i in range(0,len(txt)-2,3):
    txt1 += txt[i+2] + txt[i+1] + txt[i]
ost = len(txt)%3 if len(txt)%3!=0 else -len(txt)
txt1+= txt[-ost:]
print(txt1)
"""
"""
txt = 'UppEr aNd lOWer cAsE'
print(txt)
txt1 =''
delta = ord('a')-ord('A')
for i in txt:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        txt1 += chr(ord(i)+delta)
    elif ord(i)>=ord('a') and ord(i)<=ord('z'):
        txt1 += chr(ord(i)-delta)
    else:
        txt1 += i
print(txt1)

for i in range(200):
    print(chr(i), end=' ')
"""
"""
txt = "
**** *  * *   * ***** **** *    *
*  * *  *  * *    *   *  * * *  *
**** ****   *     *   *  * *  * *
*    *  *   *     *   *  * *   **
*    *  *   *     *   **** *    *

"
print(txt)"""
"""
a = 'Number:{} text:{} num2:{}'
txt = a.format(123, 'Alex', 321)
print('Number {0} is {0:#x} and {0:#b}'.format(42))





num = 42002544
l=['p','f','s','z']
print(l)
txt = 'asd heeli world of tanks '+''.join(l)
print(txt.rjust(40,'_'))
txt1= txt.split('o',1)
print(txt1)

txt=f"Number is {num:*^ 9,d}"
"""

"""
a = {k: str(k) for k in range(20)}
b = {k: 2 * k for k in range(10, 30)}
nums = set(a.keys() & b.keys())
c = dict()
for i in nums:
    c[i] = {a[i]} | {b[i]}
print(a, b)
print(nums)
print(c)
"""
"""
b = dict()
txt = 'ABCABD'
c = set(txt)

for k in c:
  txt1 = ''
  a = list(txt)
  a.remove(k)
  txt1 = ''.join(j for j in a)
  b[k] = txt1

print(b)
"""
"""
# a=input('Enter words')
# b=int(input('Enter num2'))
a=([1,3],[3,5])

for i in range(1,51,2):
  a = a+[i,i+2]
print(a)
m=set(a)
print(m)
"""
"""
a=set()
b=set()
for s in m:
    if s%3==0:
        a.add(s)
    if s%4==0:
        b.add(s)
print((a|b))
print((a&b))
print((a|b)-(a&b))
"""
"""
while a//10 != 0:
    m.add(a%10)
    a //= 10
m.add(a%10)
while b//10 != 0:
    n.add(b%10)
    b //= 10
n.add(b%10)
print(m|n)
"""

"""
from random import *
a=set()
b=set()
while len(a)<5 or len(b)<10:
    rand = randint(0,30)
    if rand <=10 and len(a)<5:
        a.add(rand)
    elif rand >10 and len(b)<10:
        b.add(rand)
    else:
        pass
print(a,b)



A = dict(zip([1, 2, 3], ['K', 'L', 'M']))
B = dict.fromkeys([10, 20, 30], 'Z')
print("A==B:", A==B)
print("A!=B:", A!=B)
A.update(B)
print(A)
print((20,'Z') in A.items())
print(20 in A)
print('Z' in A)
print(5 not in A)
"""
"""
from random import *
def create_table(columns):
    res = [i for i in range(columns)]
    res1 = [i for i in range(columns)]
    return(res, list(reversed(res1)))

def func(a):
    return [max(a), a.index(max(a))]

a, b =create_table(10)
print(a,b)

c = [a[i//2] if i%2==0 else b[i//2] for i in range(2*len(a))]
print(c)

"""
"""
for i in range(0,2*len(a)-2,2):
    a.insert(i+1,a[i]+a[i+1])
print(a)"""
"""
a[0::2] = sorted(a[0::2])
a[1::2] = sorted(a[1::2], reverse=True)
print(a)
"""

"""
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j]<a[j+1]:
            s = a[j]
            a[j] = a[j+1]
            a[j+1] = s
print(a)
"""
"""
def create_table(rows,columns):
    res = []
    res = [[randint(1,12) for i in range(rows)] for j in range(columns)]
    return(res)
# rows = int(input("Enter rows "))
# columns = int(input("Enter columns "))
a = create_table(5,4)
print(a)
del_num = 0

for i in range(0,4):
    a[i].pop(del_num)
a.pop(del_num)
print(a)
"""
"""
def print_table(table):
    for i in range(len(table)):
        print(table[i])

res_x = 10
res_y = 10
k = 0
# res=[[0]*res_x]*res_y
res = [[0 for i in range(res_x)] for j in range(res_y)]
print(res)
k =0
while k<res_x//2 and k<res_y//2:
    res[k][k:res_x-k] = [l for l in range(k,10) if l<(res_x-k)]
    print(res)
    for m in range(k+1,res_y-k):
        res[m][-k-1] = 9
    res[res_y-k-1][res_x-k-1:k:-1] = [l for l in range(k,10) if l<(res_x-k-1)]

    for m in range(res_y-k-1,k,-1):
        res[m][k] = 0
    k+=1
print_table(res)

"""
"""
def create_zero(m,n):
    res = []
    for i in range(m):
        res.append([0]*n)
    print(res)
    return res

def
res_x = 10
res_y = 10
x=0
y=0
pos = []
count =0
while (x<res_x) and (y<res_y):
    for i in range(x,res_x-x):
        pos.append([i, x])
    for j in range(y+1, res_y-y):
        pos.append([j, res_y-y-1])
    for k in range(res_x -x - 2, x, -1):
        pos.append([k, res_x-x-1])
    for l in range(res_y -y - 1, y, -1):
        pos.append([y, l])
    x += 1
    y += 1
print_table(pos)
s=create_zero(res_x,res_y)
for m in range(len(pos)):
    print(pos[m][0], pos[m][1])
    s[pos[m][0]][pos[m][1]]=m
print_table(s)
"""

"""
from random import *

def create_table(rows,columns):
    res = []
    res = [[chr(randint(65,122)) for i in range(rows)] for j in range(columns)]
    return(res)
# rows = int(input("Enter rows "))
# columns = int(input("Enter columns "))
a = create_table(5,4)
print(a)
"""

"""
a = 1236549870
res = ()
res1 = ()
while a//10 > 0:
    res = res + (a%10,)
    res1 = (a%10,) + res1
    a //= 10
res = res + (a%10,)
res1 = (a%10,) + res1
print(res)
print(res1)
"""
"""
txt = str(a)
a=sorted(tuple(txt), reverse=True)
print(a)
b= a[::-1]
print(b)
"""

"""
n=15
a = [1,1]
for i in range(n-2):
    a.append(a[-1]+a[-2])
print(a)
a.reverse()
print(a)
b = (reversed(a))
print(b)"""
"""
A=tuple(k for k in range(1,21) if k%3!=0)
print(A)

B=[2**(k//2) if k%2==0 else 3**(k//2) for k in range(15)]
print(B)
C=[0 if k==0 or k==1 else k**2 for k in range(13) if not k in [2,5,7]]
print(C)"""
"""
try:
    x = float(input("Enter X "))
    y = float(input("Enter Y "))
    res = (True if x>y else False)
    if res:
        print("X>Y")
    elif x==y:
        print("Y=X")
    else:
        print('Y<X')

except:
    print('Bad input')

"""

"""
day = '0'
while day != '8':
    day = input("Enter num (1-7)")
    if day == '1':
        print("Monday")
    elif day == '2':
        print("Tuesday")
    elif day == '3':
        print("Wednesday")
    elif day == '4':
        print("Thursday")
    elif day == '5':
        print("Friday!")
    elif day == '6':
        print("Saturday")
    elif day == '7':
        print("Sunday")
    else:
        print('Bad input')"""

"""
m=[]
val = 0
for i in range(25):
    val += 3
    m.append(val)
print(m)
user = []
for j in range(3):
    user.append(int(input("Enter num")))
print(user)

while len(m)>0:
    if (user[0]== m[0]) and (user[1]== m[1]) and (user[2]== m[2]):
        print ('got equal')
        break
    m.pop(0)
else:
    print(('no entries'))"""
"""        


if (m[0]+m[1]>m[2]) and (m[0]+m[2]>m[1]) and (m[1]+m[2]>m[0]):
    print('Rectangle')
else:
    print('Not rectangle')"""
"""sum = int(input("Enter sum"))
res = 0
for j in range(1, sum+1):
    if j not in m:
        res += j
        print(j, end=', ')
print(res)
""""""
n = [1,23,456,789,0,1532]
m = [1,23,456,789,0,1532]

if len(n)== len(m):
    for i in range(len(n)):
        if n[i] != m[i]:
            print('Different')
            break
    else:
        print('Equvalent')
else:
    print('Diff length')




# a, b = (val[0], val[-1]) if type(val) == str else (val, type(val))
# print(a, b)
"""
"""def max2(n):
    m= list(2*k+1 for k in range(1,n+1))
    print(m)
    return sum(m)
n = input('Enter n')
n = int(n)
mas = [77,32,63,47,15,60,8,12,44]
print(max2(n))
"""
"""
n = input('Enter n')
n = int(n)

k=0
# b = input('Enter born year')
nums = list([5*k+3 for k in range(n+1)])
print(nums)
print(list(reversed(nums)))
"""
