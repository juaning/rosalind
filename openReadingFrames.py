import re
strStartCodon = '(ATG)'
strEndCodon = '(TAG|TAA|TGA)'
lstEndCodon = ['TAG', 'TAA' , 'TGA']
dict = { 'TTT' : 'F', 'CTT' : 'L', 'ATT' : 'I', 'GTT' : 'V', 'TTC' : 'F', 'CTC' : 'L', 'ATC' : 'I', 'GTC' : 'V', 'TTA'  : 'L', 'CTA' : 'L', 'ATA' : 'I', 'GTA' : 'V','TTG' : 'L','CTG' : 'L'
        ,'ATG' : 'M','GTG' : 'V','TCT' : 'S','CCT' : 'P','ACT' : 'T','GCT' : 'A','TCC' : 'S','CCC' : 'P','ACC' : 'T','GCC' : 'A','TCA' : 'S','CCA' : 'P','ACA' : 'T','GCA' : 'A','TCG' : 'S'
        ,'CCG' : 'P','ACG' : 'T','GCG' : 'A','TAT' : 'Y','CAT' : 'H','AAT' : 'N','GAT' : 'D','TAC' : 'Y','CAC' : 'H','AAC' : 'N','GAC' : 'D','TAA' : 'Stop','CAA' : 'Q','AAA' : 'K','GAA' : 'E'
        ,'TAG' : 'Stop','CAG' : 'Q','AAG' : 'K','GAG' : 'E','TGT' : 'C','CGT' : 'R','AGT' : 'S','GGT' : 'G','TGC' : 'C','CGC' : 'R','AGC' : 'S','GGC' : 'G','TGA' : 'Stop','CGA' : 'R','AGA' : 'R'
        ,'GGA' : 'G','TGG' : 'W','CGG' : 'R','AGG' : 'R','GGG' : 'G'
        } 
strDNA = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
strRegex = r'(' + strStartCodon + '(.+)' + strEndCodon + ')'
strRegex = r'((ATG)[\w+](TAA|TAG|TGA))'
objRegex = re.compile(strRegex)
strCandidate = objRegex.findall(strDNA)
print strCandidate
# for strSingle in strCandidate:
#     i = 0
#     stop = len(strSingle)
#     strResult = ''
#     while i < stop:
#         strResult += dict[strSingle[i:i+3]]
#         i += 3
#     print strResult
i = 0
dnaLen = len(strDNA)
inWord = False
strResult = ''
while i < dnaLen:
    tri = strDNA[i:i+3]
#     print tri
    if tri == 'ATG':
        inWord = True
    if tri in lstEndCodon:
        inWord = False
#         print strResult
        strResult = ''
    if inWord:
        strResult = dict[tri]
    i += 3