import os
temp=input("Enter the file path\n")
path="/".join(temp.split("\\"))+"/"     # "\\" bacause "\" give an error
n_name=input("Enter the new comon file name\n")
format=""
try:
    format=input("file format\n")
except:
    pass
i=1
for file in os.listdir(path):
    cur_name=path+file
    new_name=path+n_name+str(i)+format
    os.rename(cur_name,new_name)
    i+=1
