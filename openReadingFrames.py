import re
def insertInList(l,v):
    if v not in l:
     l.append(v)
def getTranslateStr(strToLook):
    strLen = len(strToLook)
    i = 0
    tri = ''
    strResult = ''
    while i < strLen:
        if i+3 < strLen:
            tri = strToLook[i:i+3]
            if tri in lstEndCodon:
                return strResult
            else:
                strResult += dicc[tri]
        i += 3
    return False
def translate(strDNA,list):
    dnaLen = len(strDNA)
    for i in range(3):
        inWord = False
        strResult = ''
        strGen = ''
        while i < dnaLen:
            if i+3 < dnaLen:
                tri = strDNA[i:i+3]
                if tri == 'ATG':
                    strResult = getTranslateStr(strDNA[i:dnaLen])
                    if strResult:
                        insertInList(list,strResult)
                    strResult = ''
            i += 3
lstEndCodon = ['TAG', 'TAA' , 'TGA']
list = []
dicc = {'TTT' : 'F', 'CTT' : 'L', 'ATT' : 'I', 'GTT' : 'V', 'TTC' : 'F', 'CTC' : 'L', 'ATC' : 'I', 'GTC' : 'V', 'TTA'  : 'L', 'CTA' : 'L', 'ATA' : 'I', 'GTA' : 'V','TTG' : 'L','CTG' : 'L','ATG' : 'M','GTG' : 'V','TCT' : 'S','CCT' : 'P','ACT' : 'T','GCT' : 'A','TCC' : 'S','CCC' : 'P','ACC' : 'T','GCC' : 'A','TCA' : 'S','CCA' : 'P','ACA' : 'T','GCA' : 'A','TCG' : 'S','CCG' : 'P','ACG' : 'T','GCG' : 'A','TAT' : 'Y','CAT' : 'H','AAT' : 'N','GAT' : 'D','TAC' : 'Y','CAC' : 'H','AAC' : 'N','GAC' : 'D','TAA' : 'Stop','CAA' : 'Q','AAA' : 'K','GAA' : 'E','TAG' : 'Stop','CAG' : 'Q','AAG' : 'K','GAG' : 'E','TGT' : 'C','CGT' : 'R','AGT' : 'S','GGT' : 'G','TGC' : 'C','CGC' : 'R','AGC' : 'S','GGC' : 'G','TGA' : 'Stop','CGA' : 'R','AGA' : 'R','GGA' : 'G','TGG' : 'W','CGG' : 'R','AGG' : 'R','GGG' : 'G'}
diccReverse = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
strDNA = 'GCACTTCGCAATTGGCTTTTACCTCACGGTTGAAGAGTATTCCGAGTTTCGTGACCCCATATTGGGCATAACTGGCAATGGTTTGCCCGCTTGGTTTGCTCGATCGTACAGGGTCAGTCCATATCAACAGGACCAGCACACGATTTAAATATGGTGATGTGCTGAAGGTAGCATAGGGGTTAGAACATGATGTGCACTAATCTCTAGCGTTGCCACTTCGGACTGGATAGGACGCAGGCTACTGTGCAGCCGAGGAAATTGCGCGTTCCGAAACATAACATGAGTGATGCCCTTCTTGGCTGTTTCTCTTTGAATAGACTCATCGGGCCCCCCTGCGAGAGATTAGATTTCGATGTCGTACTCTTGCTGAGTTGAGAACCAAGACTATCAATGCGTAGCTCTGCTGGGAATGTCAGATTATCTACAATAGCTATTGTAGATAATCTGACATTGGATGTGTCGGCGGCTCCCGCAAAATCCAGCCGGCGGATCTAGTGATCAGACGGGCCTGACAAACCTACGCCATGTTTAGACAGGCGGGAGCGTCGCAACACTGCCAGGCGGTTGAGCCGTTCTATACGGATGCGCTTTACCGCCGCTGGAACGCAGAGATATACTACGGTCACGAGTAATTTGTCAGCACGATTGCAGGTAAACTGACCGGGATAGAGATCATGACTGGGTAGCAACAAGTCGCGACGTTCTGGACGCGCCGGGTTCGTTTGCGTCCTAATCACACATCAAGGAAAATAGCACTGTGAGGTGTCCATAGTAACTTCTTAACTGCACATTCTGCTTGTCGACCCTCACTTCTTCATCTTAGCATGAAGCAAAGAAATGGCAGACACCGTTAGGGACAT'
strReverseDNA = ''
for c in strDNA:
    strReverseDNA += diccReverse[c]
translate(strDNA,list)
translate(strReverseDNA[::-1],list)
for e in list:
    print e