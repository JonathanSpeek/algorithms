# iterative implementation of insertion sort in Ruby

def insertion_sort(an_array)
  size = an_array.length
  i = 0
  while i < size
    current = an_array[i]
    j = i
    while j > 0 && an_array[j - 1] > current
      an_array[j] = an_array[j - 1]
      j -= 1
    end
    an_array[j] = current
    i += 1
  end
  return an_array
end
