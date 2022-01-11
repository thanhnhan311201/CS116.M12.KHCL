# 1. float and in 
# x = 3
# print(type(x))
# print(x)
# print(x + 1)
# print(x + 1)
# print(x * 2)
# print(x**2)
# x += 1
# print(x)
# x *= 2
# print(x)
# print(x, x + 5, x*2, x**2)
# print(x%5, x /5, x//5)

# 2. boolean
# t = True
# f = False
# print(type(t))
# print(t and f)
# print(t or f)
# print(not t)
# print(t != f)

# 3.1. string
# hello = 'hello'
# world = 'world'
# print(hello)
# print(len(hello))
# hw = hello + ' ' + world
# print(hw)
# hw12 = '%s %s %d' % (hello, world, 12)
# print(hw12)

# 3.2. string
# s = 'hello'
# print(s.upper())
# print(s.capitalize())
# print(s.replace('l', '(ell) '))
# print(s.find('el'))
# print(' world '.strip())

# 4.1. list
# xs = [3, 2, 1]
# print(xs, xs[2])
# print(xs[-1])
# xs[2] = 'foo'
# print(xs)
# xs.append('bar')
# print(xs)
# x = xs.pop()
# print(x, xs)

# 4.2. list
# nums = list(range(5))
# print(nums)
# print(nums[2:4])
# print(nums[2:])
# print(nums[:2])
# print(nums[:])
# print(nums[:-1])
# nums[2:4] = [8, 9]
# print(nums)

# 5. dictionary
# d = {'cat': 'cute', 'dog': 'furry'}
# print(d['cat'])
# print('cat' in d)
# d['fish'] = 'wet'
# print(d['fish'])
# print(d.get('rat'))
# print(d.get('monkey', 'N/A'))
# print(d['monkey'])

# 6. set
# animals = {'cat', 'dog'}
# print('cat' in animals)
# print('fish' in animals)
# animals.add('fish')
# print('fish' in animals)
# print(len(animals))
# animals.add('cat')
# print(len(animals))
# animals.remove('cat')
# print(len(animals))

# 7. tuple
# t = (5, 6)
# print(type(t))
# a, b = t
# print(a, b)
# t2 = t + (7, 8)
# print(t2, t2[0])
# t[2] = 0

# 8. if
# temp = 60
# if temp > 100:
#     print('REALLY HOT')
# elif temp > 85:
#     print('HOT')
# elif temp >= 60:
#     print('Comfortable')
# else:
#     print('Cold')

# 9. for with list
# animals = ['cat', 'dog', 'monkey']
# for item in animals:
#     print(item)
# for index, item in enumerate(animals):
#     print("#%d: %s" % (index, item))

# 10.1. for with dictionary
# d = {'fish': 0, 'cat': 4, 'spider': 8}
# print(d['spider'])
# print(d.keys())
# print(d.values())
# for animals, legs in d.items():
#     print('A %s has %d legs' % (animals, legs))

# 10.2. for with dictionary
# nums = [0, 1, 2, 3, 4, 5, 6]
# even_square = {x: x ** 2 for x in nums if x % 2 == 0}
# print(even_square)

# 11. function
# def f(a, b=2, c=3):
#     print('a =', a)
#     print('b =', b)
#     print('c =', c)

# f(3, -1, 1.5)
# f(1)
# f(1, 2)
# f(a=0.5, c=4)

# 12. class
# class Greeter():
#     # Constructor
#     def __init__(self, name):
#         self.name = name # Create a instance variable

#     # Instance method
#     def greet(self, loud=False):
#         if loud:
#             print('HELLO, %s' % self.name)
#         else:
#             print('hello, %s' % self.name)
# g = Greeter("VietAI")
# g.greet()
# g.greet(loud=True)