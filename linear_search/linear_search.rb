# iterative implementation of linear search in Ruby

def linear_search(item, an_array)
    i = 0
    while i < an_array.length
        if item == an_array[i]
            return "#{item} found at position #{i}"
        end
        i += 1
    end
    return "#{item} not found in the list"
end