# prob = {'Aa' : {'Aa' : '0.5' , 'AA' : '0.25' , 'aa' : '0.25'} , 'AA' : {'AA' : '0.5' , 'Aa' : '0.5'} , 'aa' : {'aa' : '0.5' , 'Aa' : '0.5'} , 'Bb' : {'Bb' : '0.5' , 'BB' : '0.25' , 'bb' : '0.25'} , 'BB' : {'BB' : '0.5' , 'Bb' : '0.5'} , 'bb' : {'bb' : '0.5' , 'Bb' : '0.5'} }

import math

k = 7
n = 33

def Ber(gen,num_offspring):
  return (math.factorial(2**gen)/(math.factorial(num_offspring) * math.factorial((2**gen) - num_offspring)))*(0.25**num_offspring) * (1-0.25)**((2**gen) - num_offspring)

prob = 0.0
i = n
while i <= (2**k):
  prob += Ber(k,i)
  i += 1

print prob