# #open the file
# output_file= open("names.txt", "w")
# #process the file
# output_file.write("Alex")
# output_file.write("Bob")
# output_file.write("Zoe")

# #close the file
# output_file.close()


# #open the file
# input_file= open("names.txt", "r")
# #process the file
# content = input_file.read()
# print(content)


# #close the file
# input_file.close()



# line = infile.readline()
# while line != "":
#     print(line)
#     line = infile.readline


# for line in infile:
#     total += int(line)


#open the file
outfile= open("numbers.txt", "a")
#process the file
num = 4

while num <= 10:
    outfile.write(str(num)+"\n")
    num +=1

#close the file
outfile.close()

#! this is the ! reading part
infile = open("numbers.txt", "r")

for line in infile:
    print(line.strip())


infile.close()





