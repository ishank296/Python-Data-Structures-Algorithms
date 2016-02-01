arr = [5,32,7,6,12]

#sorted method creates a new list and returns it to caller
#sorted(iterable,cmp=None,key=None,reverse=False) --> new sorted list
sorted_arr = sorted(arr)
print sorted_arr

#The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes
sorted_str =  sorted("This is a test string from Andrew".split(), key=str.lower)
print sorted_str


#using indices as key in tuples
student_tuples = [('john','A',15),
                  ('jane','B',12),
                  ('dave','B',10)
                 ]
print sorted(student_tuples,key = lambda x:x[2]) # sort by age


#using name attribute with objects
class Student(object):
    
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __repr__(self):
        return repr((self.name,self.grade,self.age))
    
    def weighted_grade(self):
        return 'CDA'.index(self.grade)/float(self.age)
        
    
student_objects = [
                  Student('john','A',15),
                  Student('jane','D',25),
                  Student('dave','C',12)
                  ]
print sorted(student_objects,key = lambda x:x.age)



#Operator Module Functions
from operator import itemgetter, attrgetter, methodcaller

print sorted(student_tuples, key=itemgetter(2))  
print sorted(student_objects, key=attrgetter('age'))  
print sorted(student_objects,key=methodcaller('weighted_grade'))    
        
    



#list.sort() method. modifies list in-place (returns None to avoid confusion)
#sort() method can be used only with lists (not with any iterables as in case of sorted)
arr.sort()
print arr