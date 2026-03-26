# 
# write a program to accept 3 person weight from user. then findout & display heaviest person 
# steps 
#  1 accept 1st person weight
#  2 accept 2nd person weight
#  3 accept 3rd person weight 
#  if 1st person weight > 2nd person weight then
#    if 1st person weight > 3rd person weight 
#      print 1st person is heaviest person 
#     else 
#      print 3rd is heaviest person 
#   else 
#     if 2nd person weight > 3rd person weight 
        #  print 2nd person is heaviest
    #    else 
#          print 3rd person is heaviest

weight1 = float(input("Enter 1st person weight"))
weight2 = float(input("Enter 2nd person weight"))
weight3 = float(input("Enter 3rd person weight"))
if weight1>weight2:
    if weight1>weight3:
        print("1st person is heaviest")
    else:
        print("3rd person is heaviest")
else:
    if weight2>weight3:
        print("2nd person is heaviest")
    else:
        print("3rd person is heaviest")
