entrada = int(input())
dicio = {3600: 0, 60: 0, 1: 0}
for i in [3600, 60, 1]:
    dicio[i] = int(entrada / i)
    entrada -= dicio[i] * i
print("%d:%d:%d" % (dicio[3600], dicio[60], dicio[1]))