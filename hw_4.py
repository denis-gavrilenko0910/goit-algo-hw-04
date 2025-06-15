import timeit
import random


def gen_data(size):
  return [random.randint(0, 10000) for _ in range(size)]

def insertion_sort(data_lst):
  for i in range(1, len(data_lst)):
    key = data_lst[i]
    j = i -1 
    while j >= 0  and key < data_lst[j] :
      data_lst[j+1] = data_lst[j]
      j -= 1 
    data_lst[j+1] = key
  return data_lst

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
  merged = []
  left_index = 0
  right_index = 0

  # Сначала объедините меньшие элементы
  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      merged.append(left[left_index])
      left_index += 1
    else:
      merged.append(right[right_index])
      right_index += 1

  # Если в левой или правой половине остались элементы 
	# добавьте их к результату
  while left_index < len(left):
    merged.append(left[left_index])
    left_index += 1

  while right_index < len(right):
    merged.append(right[right_index])
    right_index += 1

  return merged

def time_mes(sort_fn, data):
  start_time = timeit.default_timer()
  sort_fn(data[:])
  end_time = timeit.default_timer() - start_time

  return end_time

def main():
  sorting_fn = [insertion_sort, merge_sort, sorted]
  header = "{:<20} | {:<20} | {:<20} | {:<20} | {:<20}".format("Sorting Algorithm", "Data 10", "Data 100", "Data 1000", "Data 10,000")

  print(header)
  print("-" * len(header))

  for el in sorting_fn:
    row = "{:<20}".format(el.__name__)
    for sz in [10, 100, 1000, 10000]:
      sort_time = time_mes(el, gen_data(sz))
      row += " | {:<20.5f}".format(sort_time)
    print(row)

main()


