motif = ['N','-P' , 'SoT', '-P']
fasta = 'MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK'
isMotif = False
addresses = []
address = ''
first,second,third = False,False,False
cc = 0
for c in fasta:
    cc += 1
    if(c == 'N'):
        first = True
        address = cc
    if(first and c != 'P'):
        first = False
        second = True
    if(second and (c == 'S' or c == 'T')):
        second = False
        third = True
    if(third and c != 'P'):
        third = False
        addresses.append(address)
        print address
#     first = False
#     second = False
#     third = False
    
print '[%s]' % ', '.join(map(str, addresses))
