string1 = input("Enter the word: ")

# opening a text file
file1 = open("hi.txt", "r")

# setting flag and index to 0
flag = 0
index = 0

# Loop through the file line by line
for line in file1:
    index += 1
    # checking string is present in line or not
    if string1 in line:
        flag=1
        print(" Sring", string1,"found in Line" ,index)

		
# checking condition for string found or not
if flag == 0:
    print('String', string1 , 'Not Found')
else:
    pass

# closing text file	
file1.close()
