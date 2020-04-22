import time as tt
import serial

serialport = "/dev/ttyACM1"
baudRate = 9600

xs = []
ys = []

ser = serial.Serial(serialport, baudRate)
vals={}
yolo = tt.time()

while(tt.time()-yolo<100):
    line = ser.readline().decode()[:-1]
    #print(line)
    if ("<<START>>" in line):
        continue
    temp = line.split(', ')
    id = temp[0]
    time = temp[1]

    if(id not in vals):
        vals[id] = [int(time),0,0]
    else:
        last_time = vals[id][0]
        count = int(vals[id][1])
        freq = vals[id][2]
        
        vals[id][0] = int(time)
        vals[id][1] += 1
        vals[id][2] = int(int(time)-int(last_time))

    print("{},{},{}".format(vals[id][0],id,vals[id][2])) 