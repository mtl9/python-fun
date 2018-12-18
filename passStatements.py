# The pass statement does nothing.
# It can be used when a statement is required syntactically but the program requires no action.
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# for creating minimal classes
class MyEmptyClass:
    pass


# Another place pass can be used is as a place-holder
# for a function or conditional body when you are working on new code,
# allowing you to keep thinking at a more abstract level.
def initlog(*args):
    pass   # Remember to implement this!
