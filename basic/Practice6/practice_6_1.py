# f = open('text.txt','r')
# print(f.read())
# f.close()
#
# f = open('text.txt','w')
# f.write("The Little Prince")
# f.close()
#
# f = open('text.txt','a')
# f.write("\nI am responsible for my rose\nthe little prince repeated sothat he would be sure to remember")
# f.close()

f = open('text.txt','r')
# print(f.read())
# print(f.readline())
lines = f.readlines()
print(lines)
#['The Little Prince\n', 'I am responsible for my rose\n', 'the little prince repeated sothat he would be sure to remember']

f.close()

