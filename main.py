path = input("What directory holds input.txt? ")
with open(path + "/input.txt", "r") as f:
    data = f.read().splitlines()
    f.close()
f = open(path + "/output.txt", "w")
f.write("")
f.close()

def convert(line):  
    lineData = line.split(" ")
    latitude = []
    longitude = []
    #   Process line
    #   Remove Degree Symbol
    if lineData.__contains__("°"):
        latitude = lineData[0].split("°")
        longitude = lineData[1].split("°")
        latitude = lineData[0].split("'")
        longitude = lineData[1].split("'")
    elif lineData.__contains__('') or lineData.__contains__(' '):
        pass
    else:
        latitude = lineData[0].split(".", 2)
        longitude = lineData[1].split(".", 2)
        print(latitude, longitude)
        if len(latitude[0]) != 3:
            latitude[0] = "0" + latitude[0]
        if len(longitude[0]) != 3:
            longitude[0] = "0" + longitude[0]

        lineOut = f"[\"{latitude[0]}d{latitude[1]}m{latitude[2]}\", \"{longitude[0]}d{longitude[1]}m{longitude[2]}\"]"
        output = open(path + "/output.txt", "a")
        output.write(lineOut + "\n")

 

for line in data:
    if line.startswith('#') or line.startswith(" "):
        pass
    else: 
        convert(line)