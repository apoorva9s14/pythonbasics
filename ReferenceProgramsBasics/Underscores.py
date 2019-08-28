#1. Explaining _, __, __x__

class C:
	_p=5
	
o=C()
# o.p  #Wrong
#o._p #Right
''' O/p
AttributeError: 'C' object has no attribute 'p'because it is an internal attribute, which is nonpublic
o._p will give the value 5

'''
class C:
    __p=5
o=C()
o.__p
''' O/p
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'C' object has no attribute '__p'
__p cannot be accessed from anywhere
'''
o._C__p
''' O/p 5
it can be accessed by _className__variable_name
'''
#__x__ is a builtin function