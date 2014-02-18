def getGeneration(gen, k):
    if gen == 1 or gen == 2:
        return 1
    return getGeneration(gen-1) + (k * getGeneration(gen-2))

getGenertion(5,3) 