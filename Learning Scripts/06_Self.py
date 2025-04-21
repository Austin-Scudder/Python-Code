
"""

class Tweet:
    pass

a = Tweet()

a.message = '140 characters'

print(a.message)

b = Tweet()

b.message = "Something entirely Different"

print (b.message)
"""

"""
#causes an error
class Tweet: 
    def __init__():
        print('Hi')

a = Tweet()
"""
"""
#needs a self as the argument even if there are no other arguments.
class Tweet: 
    def __init__(self):
        print('Hi')

a = Tweet()
"""
class Tweet: 
    def __init__(self, message):
        self.x = message
        print('Hi')

a = Tweet("something Here")

print(a.x)

b = Tweet()
