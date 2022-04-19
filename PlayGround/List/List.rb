require 'pp'

# make string "Hello World" and string "1122334455"
str1 = "Hello World"
int1 = "1122334455"

puts "Str: #{str1} Int: #{int1}"

# turn string into list
list_str = str1.split("")
list_int = int1.scan /\w/

pp list_str
pp list_int

# turn list char into list int
list_int = list_int.map(&:to_i)
pp list_int

# remove duplicate
list_int = list_int.uniq
pp list_int

# turn list into string
puts list_str.join("")

# check if 'space' inside list
puts list_str.include?(" ")

# check index space
ind_space = list_str.index(" ")
puts ind_space

# remove space in list
list_str.delete_at(ind_space)
pp list_str

# swap list
list_str[4], list_str[5] = list_str[5], list_str[4]
pp list_str

# make another list
list_int1 = [6,7,8,9,10]

# merge 2 list with same type
list_int = (list_int + list_int1).uniq
pp list_int

# cut list into 2 left and right
mid = (list_str.size / 2).round
left, right = list_str.each_slice(mid).to_a
pp left
pp right


# make hash map
firstHashMap = {1 =>"fist", 2 => "second", 3 => "third"}

# check if n in keys
puts firstHashMap.key?(1)

# get value of n
puts firstHashMap[1]

# check if n in values
puts firstHashMap.has_value?("third")

# itterate in hash
firstHashMap.each do |key, val|
    puts "Key: #{key} Value: #{val}"
end