arr = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]

hash_map = {}

def sumList(arr,hashMap)
    arr.each do|item|
        if hashMap.key?(item)
            hashMap[item] += 1
        else
            hashMap[item] = 1
        end
    end
    return hashMap
end


def printHashMap(hashMap)
    hashMap.each do |key, val|
        puts "number: #{key} = #{val} times"
    end
end

hash_map = sumList(arr,hash_map)
printHashMap(hash_map)
