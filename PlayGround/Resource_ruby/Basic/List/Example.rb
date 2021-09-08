require 'pp'

# make string "Hello World" and string "1122334455"
str1 = "Hello World"
int1 = "1122334455"

# turn string into list
list_str1 = str1.scan /\w/
list_int1 = int1.scan /\w/

pp list_str1
pp list_int1

# turn list char into list int
pp int1.each_char.map(&:to_i)
list_int1 = list_int1.map(&:to_i)
pp list_int1

# turn list into string
pp list_str1.join('')

# remove duplicate
list_int1 = list_int1.uniq
pp list_int1

# check index d
ind_d = list_str1.index('d')
pp ind_d

# remove d in list
list_str1.delete_at(ind_d)
pp list_str1

# swap list
list_str1[4], list_str1[5] = list_str1[5], list_str1[4]
pp list_str1

# make another list
list_int2 = [6,7,8,9,10]

# merge 2 list with same type
list_int1 = (list_int1+list_int2).uniq
pp list_int1

# check if 'k' inside list
pp list_int1.include? 10

# cut list into 2 left and right
left, right = list_str1.each_slice((list_str1.size/2).round).to_a
pp left
pp right

# make hash map
firstHashMap = { 1 => "first", 2 => "second", 3 => "three" }

# check if n in keys
puts firstHashMap.key?(1)

# get value of n
puts firstHashMap[1]

# check if n in values
puts firstHashMap.has_value?("first")

# itterate in hash
firstHashMap.each do |key, value|
    puts "Key #{key}  Value #{value}"
end