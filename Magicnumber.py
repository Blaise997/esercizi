# edit the functions prototype and implementation
def foo(a, b, c, *args):
    return len(args)

def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")

# Example usage:
extra_args_count = foo(1, 2, 3, 4, 5, 6)
print("Number of extra arguments in foo:", extra_args_count)



magic_check = bar(1, 2, 3, magicnumber=7)
print("Magic number check:", magic_check)
