# file objects
# my_file = open('C:\\ATS TRAINING\star.txt', 'r')
# my_file = open('C:\\Users\ATS TRAINING\star.txt', 'r')
# my_file = open("star.txt","r")
# my_file = open("star.txt", "a")
my_file = open("star.txt", "w")
my_file.write("Twinkle Twinkle Little Star!")
my_file.close()
# print(my_file.readlines())
my_file = open("star.txt","r")
print(my_file.read())