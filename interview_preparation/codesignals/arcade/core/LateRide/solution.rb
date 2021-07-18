a = 808

def solution(n)
    # puts(n % 60)
    # puts(n / 60)
    hour = n / 60
    minute = n % 60

    result = hour.to_s + minute.to_s
    str_list = result.chars
    int_list = str_list.map(&:to_i)

    return int_list.inject(0){|sum,x| sum + x }

end


puts solution(a)