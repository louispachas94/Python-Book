# storing your functions in modules

# import py file
#import pizza, works too below is just another way to write it out
from pizza import pizza_order
# ex. filename.function name(parameters)
pizza_order(19,'sau','tomato sauce','chicken')

# using as to give a fucntion an alias
from pizza import pizza_order as pi
pi(17,'cheese')

# using as to give a module/file an alias
import pizza as pii

# importing all functions in a module/file
from pizza import*