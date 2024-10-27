# r = read
# a = append
# w= write
# x = create

# f = open("names.txt")
# print(f.read())
# print(f.read(4)) give 4 characters of file

# print(f.readline()) read the line it reads first line
# print(f.readline()) read the line it reads second line

# for line in f:
#     print(line)

# f.close()

# f = open("names.txt","a")

# try:
#     f = open("names.txt")
#     print(f.read())
# except:
#     print("FIle doesnot exist")
# finally:
#     f.close()
# f.writelines("zainab")
# f.close()
# f = open("names.txt")
# print(f.read())
# f.close()

f = open("names.txt","w")
f.write("Zainab")
f.close()
