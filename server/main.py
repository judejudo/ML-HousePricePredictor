
nums=[1,2,3,4]
output_list = []
list_of_numbers = []

for index, number in  enumerate(nums):
    if index == 0:
        output_list.append(number)
        list_of_numbers.append(number)
    else:
        sum_value = number + sum(list_of_numbers)
        output_list.append(sum_value)
        list_of_numbers.append(number)

print(output_list)