n = 5
strPerm = '5 1 4 2 3'
listPerm = strPerm.split(' ')
print listPerm
listMax = []
listMin = []
def findSubSequence(listSearch,listResult,listFinal,v,order):
    i = 0
    listLen = len(listSearch)
    if len(listResult) > len(listFinal):
        listFinal = listResult
        print listFinal
    if not listSearch:
        return
    print listResult,v,listSearch, order, len(listResult), len(listFinal)
    while i < listLen:
        compare = v < listSearch[i]
        if order == '<':
            if compare:
                listResult.append(listSearch[i])
                findSubSequence(listSearch[i+1:listLen],listResult,listFinal,listSearch[i],order)
            else:
                findSubSequence(listSearch[i+1:listLen],listResult,listFinal,v,order)
        elif order == '>':
            if not compare:
                listResult.append(listSearch[i])
                findSubSequence(listSearch[i+1:listLen],listResult,listFinal,listSearch[i],order)
                listResult.pop()
            else:
                findSubSequence(listSearch[i+1:listLen],listResult,listFinal,v,order)
        else:
            print 'Error no order'
            break
        i += 1
# for el in listPerm:
#     listMax = []
listMax.append(listPerm[0])
listTmp = []
listTmp.append(listPerm[0])
findSubSequence(listPerm[1:len(listPerm)],listTmp,listMax,listPerm[0],'>')
print listMax