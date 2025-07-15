# txt=open("file.txt")
# print(txt.read())
# txt.close() # need to close the file after reading

# with keyword is used to open and close the file automatically
# by default the mode is r(read)
# with open('file.txt') as file:
#     print(file.read())

# a - append new data to the end of the file
# with open('file.txt', 'a') as file:
#     file.write('\nThis is a new line')

# create new file and write data to it
with open('new_file.txt',mode='w') as file:
    file.write('Hello World')