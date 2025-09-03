
# Text file modes
# "r"  Open for reading
# "w" Open for writing, truncating the file first
# "a" Open for writing, appending to the end of the file
# "r+" Open for reading and writing without truncting the file
# "w+" Open for writing and reading ,truncting the file
# "a+" Open for appending and reading




# Open file
my_file=open("messege.txt","r")


#methode 1
lines=my_file.readlines()
for line in lines:
    print(line,end="")

#methode 2
print(my_file.readline(), end="")
print(my_file.readline(), end="")
print(my_file.readline(), end="")

#methode 3
for line in my_file:
    print(line, end="")


#methode 4
print(my_file.read())

my_file.close()

#############################################
first_file=open("names.txt","a")

#methode 1
first_file.write("Bilal \n")
first_file.write("Samir \n")
first_file.write("Madir \n")
first_file.write("Lamin \n")

#methode 2
names=["Rachid \n","Omar\n","Samira\n","kamal\n","Iade\n","Aymen\n"]
for name in names:
    first_file.write(name)

#methode 3
all_names=["Rachid dohan \n","Omar iadir\n","Samira ktabi\n","kamal tidghi\n","Iade Rachidi\n","Aymen bouchri\n"]
first_file.writelines(all_names)


first_file.close()