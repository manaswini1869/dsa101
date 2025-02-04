import csv

f1 = './dataset1.csv'
f2 = './dataset2.csv'

def main():
    dinoSpeed = {}
    pedal = {'Bipedal': 2, 'quadrupedal': 4, 'Pedal': 0}  # Removed spaces
    g = 9.8

    # Read the first CSV file
    with open(f1, 'r') as file1:
        csvfile = csv.reader(file1, skipinitialspace=True)
        next(csvfile, None)
        for lines in csvfile:
            dinoSpeed[lines[0].strip()] = [lines[2]]
            if lines[1].strip() in pedal:
                dinoSpeed[lines[0].strip()].append(pedal[lines[1].strip()])

    with open(f2, 'r') as file2:
        csvfile = csv.reader(file2, skipinitialspace=True)
        next(csvfile, None)
        for lines in csvfile:
            if lines[0].strip() in dinoSpeed:
                dinoSpeed[lines[0].strip()].append(lines[1].strip())
                dinoSpeed[lines[0].strip()].append(lines[2].strip())
    for dino, stat in dinoSpeed.items():
        speed = ((float(stat[0]) * float(stat[2]) / stat[1])) * g
        dinoSpeed[dino] = speed
    dinoSpeed = dict(sorted(dinoSpeed.items(), key=lambda item: item[1]))
    print(dinoSpeed)
# Calling the main function
main()
