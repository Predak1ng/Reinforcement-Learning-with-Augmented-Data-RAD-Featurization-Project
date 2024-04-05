import numpy as np
import os
import math

#Distance formula for 3d coordinates
def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2) + pow((z2 - z1), 2))

#Theta formula for 3d coordinates
def calc_theta(x1, y1, z1, x2, y2, z2):
    return ((math.acos(((x1 * x2) + (y1 * y2) + (z1 * z2)) / math.sqrt((pow(x1, 2) + pow(y1, 2) + pow(z1, 2)) * (pow(x2, 2) + pow(y2, 2) + pow(z2, 2))))) * (180 / math.pi))

def calc_centroid(x, y, z):
    sum_x = sum(x) / 20
    sum_y = sum(y) / 20
    sum_z = sum(z) / 20
    return [sum_x, sum_y, sum_z]

def train():
    directory = 'train'
    text_file = open("rad_d1_train.txt", "w")
    for filename in os.listdir(directory):
        #Initialization
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        theta1 = []
        theta2 = []
        theta3 = []
        theta4 = []
        theta5 = []
        x = []
        y = []
        z = []
        if filename.endswith('.txt'):

            #Starts loop for each file in train
            with open(os.path.join(directory, filename)) as f:

                #Finds T
                last_line = f.readlines()[-1]
                temp = ""
                for word in last_line:
                    if word != " ":
                       temp += word
                    else:
                        break
                T = int(temp)
                iterator = T
                start = 0
                finish = 20

                #Loops through T
                while iterator > 0:
                    kill = 0
                    f.seek(0)
                    lines = f.readlines()[start:finish]

                    #Loops through all 20 entries per T
                    for line in lines:
                        row = line.split()
                        if row[2] == "NaN" or row[3] == "NaN" or row[4] == "NaN":
                            kill = 1
                            break
                        x.append(float(row[2]))
                        y.append(float(row[3]))
                        z.append(float(row[4]))
                    if kill == 1:
                        break
                    #Calculates d and theta for each T
                    d1.append(distance(x[0], y[0], z[0], x[3], y[3], z[3]))
                    d2.append(distance(x[0], y[0], z[0], x[11], y[11], z[11]))
                    d3.append(distance(x[0], y[0], z[0], x[19], y[19], z[19]))
                    d4.append(distance(x[0], y[0], z[0], x[15], y[15], z[15]))
                    d5.append(distance(x[0], y[0], z[0], x[7], y[7], z[7]))
                    theta1.append(calc_theta(x[3], y[3], z[3], x[11], y[11], z[11]))
                    theta2.append(calc_theta(x[11], y[11], z[11], x[19], y[19], z[19]))
                    theta3.append(calc_theta(x[19], y[19], z[19], x[15], y[15], z[15]))
                    theta4.append(calc_theta(x[15], y[15], z[15], x[7], y[7], z[7]))
                    theta5.append(calc_theta(x[7], y[7], z[7], x[3], y[3], z[3]))
                    x.clear()
                    y.clear()
                    z.clear()
                    start += 20
                    finish += 20
                    iterator -= 1

                #Computes histogram per file
                histogram = []
                histogram.append(np.histogram(d1)[0])
                histogram.append(np.histogram(d2)[0])
                histogram.append(np.histogram(d3)[0])
                histogram.append(np.histogram(d4)[0])
                histogram.append(np.histogram(d5)[0])
                histogram.append(np.histogram(theta1)[0])
                histogram.append(np.histogram(theta2)[0])
                histogram.append(np.histogram(theta3)[0])
                histogram.append(np.histogram(theta4)[0])
                histogram.append(np.histogram(theta5)[0])

                #Normalizes histograms
                holder = [x / float(T) for x in histogram]
                holder = np.array(holder)
                holder = holder.flatten()
                result = []
                for i in holder:
                    result.append(round(i, 5))
                output = ""
                for i in result:
                    output = output + str(i) + " "
                #Write to file
                text_file.write(output)
                text_file.write("\n")

    text_file.close()

def test():
    directory = 'test'
    text_file = open("rad_d1_test.txt", "w")
    for filename in os.listdir(directory):
        #Initialization
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        theta1 = []
        theta2 = []
        theta3 = []
        theta4 = []
        theta5 = []
        x = []
        y = []
        z = []
        if filename.endswith('.txt'):

            #Starts loop for each file in train
            with open(os.path.join(directory, filename)) as f:

                #Finds T
                last_line = f.readlines()[-1]
                temp = ""
                for word in last_line:
                    if word != " ":
                       temp += word
                    else:
                        break
                T = int(temp)
                iterator = T
                start = 0
                finish = 20

                #Loops through T
                while iterator > 0:
                    kill = 0
                    f.seek(0)
                    lines = f.readlines()[start:finish]

                    #Loops through all 20 entries per T
                    for line in lines:
                        row = line.split()
                        if row[2] == "NaN" or row[3] == "NaN" or row[4] == "NaN":
                            kill = 1
                            break
                        x.append(float(row[2]))
                        y.append(float(row[3]))
                        z.append(float(row[4]))
                    if kill == 1:
                        break
                    #Calculates d and theta for each T
                    d1.append(distance(x[0], y[0], z[0], x[3], y[3], z[3]))
                    d2.append(distance(x[0], y[0], z[0], x[11], y[11], z[11]))
                    d3.append(distance(x[0], y[0], z[0], x[19], y[19], z[19]))
                    d4.append(distance(x[0], y[0], z[0], x[15], y[15], z[15]))
                    d5.append(distance(x[0], y[0], z[0], x[7], y[7], z[7]))
                    theta1.append(calc_theta(x[3], y[3], z[3], x[11], y[11], z[11]))
                    theta2.append(calc_theta(x[11], y[11], z[11], x[19], y[19], z[19]))
                    theta3.append(calc_theta(x[19], y[19], z[19], x[15], y[15], z[15]))
                    theta4.append(calc_theta(x[15], y[15], z[15], x[7], y[7], z[7]))
                    theta5.append(calc_theta(x[7], y[7], z[7], x[3], y[3], z[3]))
                    x.clear()
                    y.clear()
                    z.clear()
                    start += 20
                    finish += 20
                    iterator -= 1

                #Computes histogram per file
                histogram = []
                histogram.append(np.histogram(d1)[0])
                histogram.append(np.histogram(d2)[0])
                histogram.append(np.histogram(d3)[0])
                histogram.append(np.histogram(d4)[0])
                histogram.append(np.histogram(d5)[0])
                histogram.append(np.histogram(theta1)[0])
                histogram.append(np.histogram(theta2)[0])
                histogram.append(np.histogram(theta3)[0])
                histogram.append(np.histogram(theta4)[0])
                histogram.append(np.histogram(theta5)[0])

                #Normalizes histograms
                holder = [x / float(T) for x in histogram]

                #Conversions
                holder = np.array(holder)
                holder = holder.flatten()
                result = []
                for i in holder:
                    result.append(round(i, 5))
                output = ""
                for i in result:
                    output = output + str(i) + " "

                #Write to file
                text_file.write(output)
                text_file.write("\n")

    text_file.close()

def custom_train():
    directory = 'train'
    text_file = open("cust_d1_train.txt", "w")
    for filename in os.listdir(directory):
        #Initialization
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        theta1 = []
        theta2 = []
        theta3 = []
        theta4 = []
        theta5 = []
        x = []
        y = []
        z = []
        if filename.endswith('.txt'):

            #Starts loop for each file in train
            with open(os.path.join(directory, filename)) as f:

                #Finds T
                last_line = f.readlines()[-1]
                temp = ""
                for word in last_line:
                    if word != " ":
                       temp += word
                    else:
                        break
                T = int(temp)
                iterator = T
                start = 0
                finish = 20

                #Loops through T
                while iterator > 0:
                    kill = 0
                    f.seek(0)
                    lines = f.readlines()[start:finish]

                    #Loops through all 20 entries per T
                    for line in lines:
                        row = line.split()
                        if row[2] == "NaN" or row[3] == "NaN" or row[4] == "NaN":
                            kill = 1
                            break
                        x.append(float(row[2]))
                        y.append(float(row[3]))
                        z.append(float(row[4]))
                    if kill == 1:
                        break

                    #Calculates centroid from all 20 points
                    centroid = calc_centroid(x, y, z)

                    #Calculates d and theta for each T
                    d1.append(distance(centroid[0], centroid[1], centroid[2], x[3], y[3], z[3]))
                    d2.append(distance(centroid[0], centroid[1], centroid[2], x[11], y[11], z[11]))
                    d3.append(distance(centroid[0], centroid[1], centroid[2], x[19], y[19], z[19]))
                    d4.append(distance(centroid[0], centroid[1], centroid[2], x[15], y[15], z[15]))
                    d5.append(distance(centroid[0], centroid[1], centroid[2], x[7], y[7], z[7]))
                    theta1.append(calc_theta(x[3], y[3], z[3], x[11], y[11], z[11]))
                    theta2.append(calc_theta(x[11], y[11], z[11], x[19], y[19], z[19]))
                    theta3.append(calc_theta(x[19], y[19], z[19], x[15], y[15], z[15]))
                    theta4.append(calc_theta(x[15], y[15], z[15], x[7], y[7], z[7]))
                    theta5.append(calc_theta(x[7], y[7], z[7], x[3], y[3], z[3]))
                    x.clear()
                    y.clear()
                    z.clear()
                    start += 20
                    finish += 20
                    iterator -= 1

                #Computes histogram per file
                histogram = []
                histogram.append(np.histogram(d1)[0])
                histogram.append(np.histogram(d2)[0])
                histogram.append(np.histogram(d3)[0])
                histogram.append(np.histogram(d4)[0])
                histogram.append(np.histogram(d5)[0])
                histogram.append(np.histogram(theta1)[0])
                histogram.append(np.histogram(theta2)[0])
                histogram.append(np.histogram(theta3)[0])
                histogram.append(np.histogram(theta4)[0])
                histogram.append(np.histogram(theta5)[0])

                #Normalizes histograms
                holder = [x / float(T) for x in histogram]

                #Conversions
                holder = np.array(holder)
                holder = holder.flatten()
                result = []
                for i in holder:
                    result.append(round(i, 5))
                output = ""
                for i in result:
                    output = output + str(i) + " "

                #Write to file
                text_file.write(output)
                text_file.write("\n")

    text_file.close()

def custom_test():
    directory = 'test'
    text_file = open("cust_d1_test.txt", "w")
    for filename in os.listdir(directory):
        #Initialization
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        theta1 = []
        theta2 = []
        theta3 = []
        theta4 = []
        theta5 = []
        x = []
        y = []
        z = []
        if filename.endswith('.txt'):

            #Starts loop for each file in train
            with open(os.path.join(directory, filename)) as f:

                #Finds T
                last_line = f.readlines()[-1]
                temp = ""
                for word in last_line:
                    if word != " ":
                       temp += word
                    else:
                        break
                T = int(temp)
                iterator = T
                start = 0
                finish = 20

                #Loops through T
                while iterator > 0:
                    kill = 0
                    f.seek(0)
                    lines = f.readlines()[start:finish]

                    #Loops through all 20 entries per T
                    for line in lines:
                        row = line.split()
                        if row[2] == "NaN" or row[3] == "NaN" or row[4] == "NaN":
                            kill = 1
                            break
                        x.append(float(row[2]))
                        y.append(float(row[3]))
                        z.append(float(row[4]))
                    if kill == 1:
                        break

                    #Calculates centroid from all 20 points
                    centroid = calc_centroid(x, y, z)

                    #Calculates d and theta for each T
                    d1.append(distance(centroid[0], centroid[1], centroid[2], x[3], y[3], z[3]))
                    d2.append(distance(centroid[0], centroid[1], centroid[2], x[11], y[11], z[11]))
                    d3.append(distance(centroid[0], centroid[1], centroid[2], x[19], y[19], z[19]))
                    d4.append(distance(centroid[0], centroid[1], centroid[2], x[15], y[15], z[15]))
                    d5.append(distance(centroid[0], centroid[1], centroid[2], x[7], y[7], z[7]))
                    theta1.append(calc_theta(x[3], y[3], z[3], x[11], y[11], z[11]))
                    theta2.append(calc_theta(x[11], y[11], z[11], x[19], y[19], z[19]))
                    theta3.append(calc_theta(x[19], y[19], z[19], x[15], y[15], z[15]))
                    theta4.append(calc_theta(x[15], y[15], z[15], x[7], y[7], z[7]))
                    theta5.append(calc_theta(x[7], y[7], z[7], x[3], y[3], z[3]))
                    x.clear()
                    y.clear()
                    z.clear()
                    start += 20
                    finish += 20
                    iterator -= 1

                #Computes histogram per file
                histogram = []
                histogram.append(np.histogram(d1)[0])
                histogram.append(np.histogram(d2)[0])
                histogram.append(np.histogram(d3)[0])
                histogram.append(np.histogram(d4)[0])
                histogram.append(np.histogram(d5)[0])
                histogram.append(np.histogram(theta1)[0])
                histogram.append(np.histogram(theta2)[0])
                histogram.append(np.histogram(theta3)[0])
                histogram.append(np.histogram(theta4)[0])
                histogram.append(np.histogram(theta5)[0])

                #Normalizes histograms
                holder = [x / float(T) for x in histogram]

                #Conversions
                holder = np.array(holder)
                holder = holder.flatten()
                result = []
                for i in holder:
                    result.append(round(i, 5))
                output = ""
                for i in result:
                    output = output + str(i) + " "

                #Write to file
                text_file.write(output)
                text_file.write("\n")

    text_file.close()


if __name__ == '__main__':
    train()
    test()
    custom_train()
    custom_test()


