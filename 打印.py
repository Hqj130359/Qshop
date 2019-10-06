
def random_code(len=6):
    import random
    sz=[]
    for i in range(10):
        sz.append(str(i))
    for i in range(ord('a'), ord('z') + 1):
        sz.append(chr(i))
    for i in range(ord('A'), ord('Z') + 1):
        sz.append(chr(i))

    valid_code = "".join([random.choice("".join(sz)) for i in range(len)])
    print(valid_code)
random_code()



# daxie()
# print(ord('a'))#97
# print(ord('z'))#122
# print(ord('A'))#65
# print(ord('Z'))#90
# print(chr(97))
