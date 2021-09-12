arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
hash_map = {}

# number 1 = 3 times
def SumList(hash_map, arr)
    arr.each do |item|
        if hash_map.key?(item)
            hash_map[item] += 1
        else
            hash_map[item] = 1
        end
    end

    return hash_map
end

def PrintHashMap(hash_map)
    hash_map.each do |key, val|
        puts "number #{key} = #{val} times"
    end
    
end


hash_map = SumList(hash_map, arr)
PrintHashMap(hash_map)