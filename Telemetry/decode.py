import csv
f = open("log.log", "r")
contents = f.read()
lines = contents.split("\n")
sensors = []

for l in lines:
    #print(l)
    individual = l.split()
    if(len(individual)>0):
        sensoridx = 0;
        for i in range(0, len(individual)):
            if(individual[i] == "ID:"): sensoridx = i + 1
        sensor = individual[sensoridx]
        if not sensor in sensors:
            sensors.append(sensor)
            print(sensor)

with open('output.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for s in sensors:
        values = []
        times = []
        for l in lines:
            splitLine = l.split()
            if(len(splitLine)>0):
                sensoridx = 0;
                for i in range(0, len(splitLine)):
                    if(splitLine[i] == "ID:"): sensoridx = i + 1
                if(splitLine[sensoridx] == s):
                    print("here")
                    hexval = ""
                    lengthIdx = 0;
                    for i in range(0, len(splitLine)):
                        if(splitLine[i] == "DLC:"): lengthIdx = i + 1

                    payloadLength = int(splitLine[lengthIdx])
                    for n in range(lengthIdx+1, lengthIdx+1+payloadLength):
                        hexval+=splitLine[n]
                    times.append(splitLine[1])
                    values.append(hexval)
                    print(hexval)
        data_writer.writerow([s])
        data_writer.writerow(["Times"] +times)
        data_writer.writerow(["Values"]+values)

        #print(individual[1])
