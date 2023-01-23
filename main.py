path = input("What directory holds input.txt? ")
with open(path + "/input.txt", "r") as f:
    data = f.read().splitlines()

for line in data:
    lineData = line.split(" ")
    latitude = lineData[0].split(".")
    longitude = lineData[1].split(".")
    if latitude[1].__len__ != 2:
        latitude[1] = "0" + latitude[1]
    if longitude[1].__len__ != 2:
        longitude[1] = "0" + longitude[1]
    lineOut = f"[{latitude[0]}d{latitude[1]}m{latitude[2]}], [{longitude[0]}d{longitude[1]}m{longitude[2]}]"
    print(lineOut)

 