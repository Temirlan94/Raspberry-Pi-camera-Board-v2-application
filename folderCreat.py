import os
for j in range (0,10):
    for i in range(1,9):
        os.makedirs(os.path.join(str(j) + str(i),'Top'))
        os.makedirs(os.path.join(str(j) + str(i),'Front'))
os.mkdir('default')