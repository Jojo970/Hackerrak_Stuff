array1 = [1,3,5,6,7,9]
array2 = [2,4,6,10,11]
pos1 = 0
pos2 = 0

new_array = []

while pos1 < len(array1) and pos2< len(array2):

  if array1[pos1] == array2[pos2]:
    if array1[pos1] in new_array:
      pos1 +=1
      pos2 +=1
    else:
      new_array.append(array1[pos1])
      pos1 += 1
      pos2 += 1

  elif array1[pos1] >array2[pos2]:
    if array2[pos2] in new_array:
      pos2 += 1
  
    else:
      new_array.append(array2[pos2])
      pos2 += 1

  else:
    if array1[pos1] in new_array:
      pos1 += 1
    else:
      new_array.append(array1[pos1])
      pos1 += 1


if pos1 == len(array1):
  for var in array2[pos2:]:
    if var in new_array:
      pass
    else:
      new_array.append(var)
else:
  for var in array1[pos1:]:
    if var in new_array:
      pass
    else:
      new_array.append(var)

print(new_array)