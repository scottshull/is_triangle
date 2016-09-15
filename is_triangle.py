def is_triangle(aa, bb, cc):
    if (aa > bb + cc) or (bb > aa + cc) or (cc > aa + bb):
        print "No"
    else:
        print "Yes"

print ("Enter a value for side 1:")
a = raw_input()
if a == '':
    a = "15"

print ("Enter a value for side 2:")
b = raw_input()
if b == '':
    b = "15"

print ("Enter a value for side 3:")
c = raw_input()
if c == '':
    c = "30"

is_triangle(a, b, c)
