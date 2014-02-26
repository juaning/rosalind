import re
import urllib2
strRegex = r"(?=(N[^P][ST][^P]))"
objRegex = re.compile(strRegex)
ids = ['Q924A4', 'Q9QSP4', 'P40308','Q15UL9','P81448_EMBP_CRIGR','P10761_ZP3_MOUSE', 'Q2YCH6', 'P04141_CSF2_HUMAN', 'P04441_HG2A_MOUSE', 'Q3BN23', 'P00750_UROT_HUMAN', 'A6WKC3']
fastas = {}
for id in ids:
    rawContent =  urllib2.urlopen('http://www.uniprot.org/uniprot/'  + id + '.fasta').read()
    oneLineStr = ''.join(rawContent.split('\n')[1:])
    fastas[id] = oneLineStr
    
for k, fasta in fastas.iteritems():
    first,second,third,isMotif = False,False,False,False
    addresses = []
    address = ''
    cc = 0
    r = objRegex.finditer(fasta)
    foundIt = False
    for i in r:
        foundIt = True
        addresses.append(i.start() + 1)
    if foundIt:
        print k
        print '%s' % ' '.join(map(str, addresses))
        foundIt = False
