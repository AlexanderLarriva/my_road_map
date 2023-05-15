def apply_diff(TargetSet, UpdateDict):
  if 'add' in UpdateDict:
    AddSet = UpdateDict['add']
    TargetSet.update(AddSet)
  # AddSet = UpdateDict.get("add")
  #print(AddSet)
  if 'remove' in UpdateDict:
    RemoveSet = UpdateDict['remove']
  # RemoveSet = UpdateDict.get("remove")
  #print(RemoveSet)
    TargetSet.difference_update(RemoveSet)


TargetSet = set("abcd")
# UpdateDict = {'remove': {'a', 'b'}}
UpdateDict = {'add': {'e', 'f'}}
apply_diff(TargetSet, UpdateDict)

print(TargetSet)