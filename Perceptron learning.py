n = int(input("Number of features = "))
w = []
bias = float(input("Bias = "))
for i in range(n):
    w.append(float(input("W {} = ".format(i+1))))
l = float(input("n = "))
z = int(input("N of patterns = "))
p = [[]]
for i in range(z):
    p.append([])

    for j in range(n):
        p[i].append(float(input("P{} coordinate {} = ".format(i+1, j+1))))

    t = int(input("t{} = ".format(i+1)))
    p[i].append(t)


for i in range(z):
    suii = bias
    for j in range(n):
        suii = suii + (p[i][j] * w[j])
    if suii > 0:
        c_test = 1
    else:
        c_test = 0
    if c_test == p[i][-1]:
        print("P{} class = ".format(
            i+1), p[i][-1], " and test class = ", c_test, "so it's correctly classified")
    else:
        print("P{} class = ".format(i+1),
              p[i][-1], " and test class = ", c_test, "so it's misclassified.")
        bias = bias + l*(p[i][-1] - c_test)
        for j in range(n):
            w[j] = w[j] + l*(p[i][-1] - c_test)*p[i][j]
        print("New bias = " , bias)
        for j in range(n):
            print("New W{} = ".format(j+1), w[j])
        
