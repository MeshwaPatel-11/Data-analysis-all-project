f = open("example1.txt", "r")

# print(f.read())
# print(f.read(5))
# print(f.readline())

#create new file and add text into the file
# f=open("example2.txt","a")
# f.write("Now the file has more content!")
# f.close()

# f = open("example2.txt","r")
# print(f.read())


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())