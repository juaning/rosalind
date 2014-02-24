def getGeneration(gen, k):
    genValues = [1,1]
    for i in range(2, gen):
        genValues.append(genValues[i-1] + (k * genValues[i-2]))
    return genValues[gen-1]

print getGeneration(36,2) 