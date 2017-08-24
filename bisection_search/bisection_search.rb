# char: a single character
# a_str: an alphabetized string
# prints: true if char is in a_str; false otherwise

def is_in(char, a_str)

  a_str = a_str.chars.sort(&:casecmp).join
  length = a_str.length
  mid = length / 2
  if a_str == ''
      p false
  elsif a_str.length == 1
      a_str == char
  elsif char == a_str[mid]
      p true
  elsif char < a_str[mid]
      is_in(char, a_str[0..(mid-1)])
  else
      is_in(char, a_str[(mid+1)..-1])
  end
end
