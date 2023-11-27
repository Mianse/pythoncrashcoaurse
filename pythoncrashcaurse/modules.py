#a module is basically  a a file containing a set of functions to include your applications
#there are core python modules modules ypu can install using a pip package(including django) as well as custom modules


#core modules
import datetime

from datetime import date
from time import time

#pip modules
from camelcase import CamelCase

#today=datetime.date.today()
today=date.today()
timestamp=time()

c=CamelCase()
print(c.hump('hello there world'))


print(timestamp)
print(today)
