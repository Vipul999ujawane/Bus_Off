
import serial

serialport = "/dev/ttyACM0"
baudRate = 9600

xs = []
ys = []

ser = serial.Serial(serialport, baudRate)
vals={}
while(1):
    line = ser.readline().decode()[:-1]
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
        vals[id][2] = int((freq*count + int(time)-int(last_time))/(count+1))

    print(id,vals[id][2]) 