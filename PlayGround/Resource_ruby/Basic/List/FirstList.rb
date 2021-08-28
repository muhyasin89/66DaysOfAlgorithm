require 'pp'

str1 = "Hello World! this is ruby"
int1 = 1234

list_int = int1.to_s.split("")
list_str = str1.split(" ")

puts str1 +  " end of str"
puts int1 

# puts list_int.inspect

# puts list_str.inspect
list_int.unshift("") 
pp list_int.reject(&:empty?).map(&:to_i)
pp list_str

list_int[0], list_int[1] = list_int[1], list_int[0]

pp list_int

pp list_str.sort_by(&:length)
pp list_str.sort {|a,b| a.length <=> b.length}
pp list_str.sort_by {|a| -a.length}

music = ["21.mp3", "10.mp3", "5.mp3", "40.mp3"]
pp music.sort
pp music.sort_by { |s| s.scan(/\d+/).first.to_i}


# hash = {1: "first", 2: "second", 3: "third"}
# hash = {a: 1, b: 2, c: 3}
hash = {"{": "}", "(": ")", "[": "]"}
pp hash.sort_by(&:last)

pp hash.key?(:"{")
pp hash.value?("}")

pp hash.member?("}")


def quick_sort(list)
    return [] if list.empty?
    groups = list.group_by { |n| n <=> list.first }
    less_than    = groups[-1] || []
    first        = groups[0]  || []
    greater_than = groups[1]  || []
    quick_sort(less_than) + first + quick_sort(greater_than)
  end
  
  p quick_sort [3, 7, 2, 1, 8, 12]