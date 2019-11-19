import os
try:
    os.chdir('C:/Users/dears/Documents/GitHub/Python/Head First Py/Chapter-3')
    data = open('sketch.txt')
    data.seek(0)

    for everyline in data:
        try:
                (role, linespoken) = everyline.split(':',1)
                print(role, end=' ')
                print('said :',end=' ')
                print(linespoken,end=' ')
        except:
            pass
    data.close()
except IOError:
    print('File not Found')

