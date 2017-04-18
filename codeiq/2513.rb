# 256 ruby solution

def sumOfTwoInArray(arr, target_sum)
  arr.each { |val| 
    if (arr.include? (target_sum - val) and (val != (target_sum - val)))
      return "yes" 
    end
  }
  "no"
end

input_length = gets.chomp.to_i
input_array = gets.chomp.split(' ').map(&:to_i)

puts sumOfTwoInArray(input_array, 256)
