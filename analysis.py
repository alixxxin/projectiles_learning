import numpy as np
import math as m

# get data

file = open('projectiles.csv','r')

records = []

for line in file:
    data = line.split(",")
    data[0] = int(data[0])
    data[1] = float(data[1])
    data[2] = float(data[2])
    if (line=="0 , 0.0 , 0.0\n"):
        records.append({})
    records[-1][data[0]] = [data[1], data[2]]
        
# unit is m/ms
initial_velocity_x = []
initial_velocity_y = []

for record in records:
	[x,y] = record[1];
	initial_velocity_x.append(x)
	initial_velocity_y.append(y)


# build the Y matrix
Y = [[],[]]
for a in records:
	for j in range(1,len(a)):
		Y[0].append(a[j][0])
		Y[1].append(a[j][1])

Ymatrix = np.array(Y)
# print(Ymatrix)
# print(Ymatrix.shape)

# Building the X matrix
X = [[],[],[],[],[]]

for i in range(0, len(records)):
	vx = initial_velocity_x[i]
	vy = initial_velocity_y[i]

	for j in range(1, len(records[i])):
		X[0].append(vx*j)
		X[1].append(vy*j)
		X[2].append(j)
		X[3].append(j**2)
		X[4].append(1)


Xmatrix = np.array(X)
# print(Xmatrix)
# print(Xmatrix.shape)

XT = np.transpose(Xmatrix)
YT = np.transpose(Ymatrix)

[WT, a, b, c] = np.linalg.lstsq(XT, YT)
W = np.transpose(WT)

# print(W)


# solve the question

X2 = [[],[],[],[],[]]

vx = 0.707106781187
vy = 0.658106781187

for i in range(0, 100):
	X2[0].append(vx*i)
	X2[1].append(vy*i)
	X2[2].append(i)
	X2[3].append(i**2)
	X2[4].append(1)

X2matrix = np.array(X2)

res = np.dot(W, X2matrix)
print("============= result =============")
print(res)

i = 1
while (res[1][i] > 0):
	i += 1

print("First " + str(i) + " records y axis is above zero")

finalresult = np.array([res[1][0:i], res[0][0:i]])

print("============= final result =============")
print(finalresult)

outfile = open("result.txt", "w")
for i in range(0, i):
	outfile.write(str(i) + "," + str(finalresult[1][i]) + "," + str(finalresult[0][i]) + "\n")



# closing all files
file.close()
outfile.close()