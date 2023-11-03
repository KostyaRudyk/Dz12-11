
class Pearson:
   a = 5
   b = 4
   c = 4

   def t_(self):
       pass

class Student(Pearson):
    pass

test = Student()

print(type(test))
print(hasattr(test, 'd'))
print(getattr(test, 'b', -1))
print(callable(test.t_))
print(issubclass(Student, Pearson))
print(isinstance(test, Pearson))

