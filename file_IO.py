s="Sharad is a Good boy"

# Context manager to read and write file
# with open("test.txt","w") as f:
#     f.write(s)

#Writing a file
# fp=open("test.txt","w")
# fp.write(s)
# fp.close()

#Reading a file
# with open("test.txt","r") as f:
#    s=f.read()
#    print(s)

fp=open("test.txt","r")
s=fp.read()
print(s)
fp.close()

#Appending a file
with open("test.txt","a") as f:
    f.write("And He is a coder")
