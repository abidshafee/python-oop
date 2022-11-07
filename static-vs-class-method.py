# static method doesn't need to instantiate object to call it,
# so we never need the object as a first argument in the static method -
# in class is just like regular function; so e can pass any argument we -
# prefer in the static method
from object_representation import myItem


class InheritedCl(myItem):
    pass


