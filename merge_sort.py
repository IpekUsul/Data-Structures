def merge_sort(list):
  """
  Sorts a list in ascending order
  Returns a new sorted list

  Divide: Find the midpoint of the list and divide into sublists.
  Conquer: Recursively sort the sublists created in previous step.
  Combine: Merge the sorted sublists created in previous step.3

  takes 0(n log n) time
  
  """
  if len(list) <= 1:
    return list

 left_half, right_half= split(list)
 left= merge_sort(left_half)
 right= merge_sort(right_half)

return merge(left,right)

def split(list):
  """
  Divide the unsorted list at midpoint into sublists
  Returns two sublists -left and right
  Takes overall 0(log n) time
  """
mid=len(list)//2
left=list[:mid]  # from the very beginning of the list to midp.
right=list[mid:]  # from the midp. of the list to the very end.

return left, right

def merge(left, right):
  """
  Merges two lists(arrays), sorting them in the process
  Returns a new merged list
  runs in overall 0(n) time
  """

l=[]
i=0
j=0

while i < len(left) and j < len(right):
  if left[i] < right[j]:
    l.append(left[i])
    i+=1
  else:
    l.append(right[j])
    j= j+1

while i < len(left):
  l.append(left[i])
  i +=1

while j < len(right):
  l.append(right[j])
  j+=1

return l

def verify_sorted(list):
  n= len(list)

if n== 0 or n ==1:
  return True

return list[0]< list[1] and verify_sorted(list[1:])

alist=[54,26,98,65,74,88,60,98,21,17]
l=merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))









