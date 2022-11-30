import re
from character_service import listChararcters

path=(listChararcters)[6]['episode']

for j in path:
    print(j)
    tup = re.findall('[0-9]+', j)
    s=''.join(tup)
    print(s)

