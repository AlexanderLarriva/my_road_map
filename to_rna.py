def to_rna(dnk):
  rnk = []
  code = {"G": "C", "C": "G", "T": "A", "A": "U"}
  for i in dnk:
    rnk.append(code[i]) 
  return "".join(rnk)





to_rna('ACGTGGTCTTAA')
print(to_rna('ACGTGGTCTTAA'))
print(type(to_rna('ACGTGGTCTTAA')))