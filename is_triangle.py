def is_triangle(aa, bb, cc):
    if (aa > bb + cc) or (bb > aa + cc) or (cc > aa + bb):
        print "No"
    else:
        print "Yes"

a = int(raw_input("Enter a value for side 1:"))


b = int(raw_input("Enter a value for side 2:"))


c = int(raw_input("Enter a value for side 3:"))



is_triangle(a, b, c)
