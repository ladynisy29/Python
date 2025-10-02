# f = open("demofile.txt")
# # print(f.read())
# # print(f.read())
# # print(f.readline())

# for x in f:
#     print(x)
# f.close()

# with  open("demofile.txt", "w") as f:
#     f.write("\nNow the file has more content!")
# with open("demofile.txt") as f:
#     print(f.read())

# with open("myfile.txt","x") as f:
#     pass

# with open("myfile.txt","w") as f:
#     f.write("Nisy will be great")

import os
os.remove("myfile.txt")