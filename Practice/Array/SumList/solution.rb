arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
hash_map = {}

def SumList(arr, hash_map)
    arr.each do |item|
        if hash_map.key?(item)
            hash_map[item] += 1
        else
            hash_map[item] = 1
        end
    end

    return hash_map
end

def printHashMap(hash_map)
    hash_map.each do |key, val|
        puts "number #{key} = #{val} times"
    end
end

hash_map = SumList(arr, hash_map)
printHashMap(hash_map)