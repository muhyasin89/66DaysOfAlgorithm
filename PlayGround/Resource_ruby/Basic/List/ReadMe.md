array.include?(element) # preferred method
array.member?(element)
array.to_set.include?(element)
array.to_set.member?(element)
array.index(element) > 0
array.find_index(element) > 0
array.index { |each| each == element } > 0
array.find_index { |each| each == element } > 0
array.any? { |each| each == element }
array.find { |each| each == element } != nil
array.detect { |each| each == element } != ni
