
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
      return None
   if int_list == None:
      raise ValueError
   max = int_list[0] - 1
   for i in range(len(int_list)):
      if int_list[i] > max:
         max = int_list[i]
   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   if len(int_list) <= 1:
      return [int_list[0]]
   return [int_list[-1]] + reverse_rec(int_list[:-1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   if low == high and int_list[high] != target:
      return None
   mid = (low + high + 1)//2
   if int_list[mid] == target:
      return mid
   if int_list[mid] < target:
      return bin_search(target, mid, high, int_list)
   if int_list[mid] > target:
      return bin_search(target, low, mid, int_list)
