import collections

a = ['EM', 'BM', 'IX', 'CI', 'EX', 'DI', 'CX', 'DM', 'DX', 'BI', 'CE', 'JC', 'IX', 'JM', 'BM', 'EI', 'DI', 'EM', 'DM', 'EX', 'CX', 'CE', 'JC', 'CM', 'DX', 'BM', 'JX']

counts = collections.defaultdict(int)
for letters in a:
    counts[letters]+=1

print (counts)
hist = dict( (k, float(v)/len(a)) for k,v in counts.items())
print (hist)
print("test_branch_1")
print("that was easy")