print ("Enter a value for side 1:")
1 = raw_input()
if 1 == '':
    1 = "15"

print ("Enter a value for side 2:")
2 = raw_input()
if 2 == '':
    2 = "15"

print ("Enter a value for side 3:")
3 = raw_input()
if 3 == '':
    3 = "30"

def is_triangle(1, 2, 3):
    if (1 > 2 + 3) or (2 > 1 + 3) or (3 > 1 + 2):
        print "No"
    else:
        print "Yes"
