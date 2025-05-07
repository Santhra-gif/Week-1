# Take user input and write it to a file
f = open('User_Sample.txt','w')
user_input = input("Your name ?:")
f.write(user_input)
f.close()

# Open the file to read it's contents
f = open('User_Sample.txt','r')
content = f.read()

# display 
print("")
print("Your name is .....")
print(content)