import os
man=[]
other=[]
try:
    os.chdir('C:/Users/dears/Documents/GitHub/Python/Head First Py/Chapter-3')
    data = open('sketch.txt')
    data.seek(0)
    for line in data:
        try:
            (role,line_spoken)=line.split(':',1)
            line_spoken=line_spoken.strip()
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print("File is Missing")

try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
    man_file.close()
    other_file.close()
    

except IOError:
    print("No files to Render Output")