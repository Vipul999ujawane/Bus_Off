import matplotlib.pyplot as plt
import csv

vals={}
spamreader=""
with open('data.csv',"r") as csvf:
    spamreader = csv.reader(csvf, delimiter=',', quotechar='|')

    for row in spamreader:
        if(row[1] not in vals):
            vals[row[1]]=[]
        else:
            vals[row[1]].append((int(row[0]),int(row[2])))

for ids in vals:
    x=[]
    y=[]
    print(ids)
    for i in vals[ids]:
        x.append(i[0])
        y.append(i[1])
    if(ids=="578"):
        plt.plot(x,y,label="attacker")
        continue    
    plt.plot(x,y,label=ids)
        #print(x,y)
plt.legend()
plt.xlabel("Time (ms)")
plt.ylabel("Periodicity (ms)")
plt.savefig('DOS_CAN.png')
plt.show()