A = '1234567'
print(A[1::2])


Name = "Michael Jackson"
print(Name.find('el'))


tuple1 = ("A", "B", "C")
print(tuple1[-1])


A = ((11, 12), [21, 22])
print(A[1])


A = ((11, 12), [21, 22])
print(A[0][1])


print('1, 2, 3, 4'.split(', '))


# Concatenate the following lists
A = [1, 'a']
B = [2, 1, 'd']
print("A and B concatination : ", A+B)

# How do you cast the list 'A' to the set 'a'?
# a = set(A)


# Consider the Set: V ={'A','B'}, what is the result of V.add('C')?

V = {'A', 'B'}
V.add('C')
print(V)


# Consider the Set: V={'A','B','C' }, what is the result of V.add('C')?

V = {'A', 'B', 'C'}
V.add('C')
print(V)


for n in range(3):
    print(n+1)


A = ['1', '2', '3']
for a in A:
    print(2*a)


class Points(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p1 = Points(1, 2)
p1.print_point()


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p2 = Points(1, 2)
p2.x = 2
p2.print_point()
