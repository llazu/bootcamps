#import mypackage.module1
# import mypackage.module2

# mypackage.module1.greet("Cedar")
# mypackage.module2.depart("Boredom")

#from mypackage import module1, module2

# module1.greet("Cedar")
# module2.depart("Boredom")

from mypackage.module1 import greet
from mypackage.mysubpackage.module3 import people

for person in people:
    greet(person) 