path = input("What directory holds input.txt? ")
with open(path + "/input.txt", "r") as f:
    data = f.read().splitlines()
    f.close()
f = open(path + "/output.txt", "w")
f.write("")
f.close()

for line in data:
    if line.startswith('#'):
        pass
    lineData = line.split(" ")
    #   Process line
    #   Remove Degree Symbol
    if lineData.__contains__("°"):
        latitude = lineData[0].split("°")
        longitude = lineData[1].split("°")
        latitude = lineData[0].split("'")
        longitude = lineData[1].split("'")
    else:
        latitude = lineData[0].split(".", 2)
        longitude = lineData[1].split(".", 2)
    
    if len(latitude[1]) != 3:
        latitude[1] = "0" + latitude[1]
    if len(longitude[1]) != 3:
        longitude[1] = "0" + longitude[1]

    lineOut = f"[\"{latitude[0]}d{latitude[1]}m{latitude[2]}\", \"{longitude[0]}d{longitude[1]}m{longitude[2]}\"]"
    output = open(path + "/output.txt", "a")
    output.write(lineOut + "\n")

 