import matplotlib.pyplot as plt
import csv

vals={}
spamreader=""
with open('data2.csv',"r") as csvf:
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
plt.ylabel("Transmission Time (ms)")
plt.savefig('DOS_CAN2.png')
plt.title("Transmission Time V/S (During and without Attack)")
plt.show()