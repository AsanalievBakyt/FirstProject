
# i = 0
# # while i < len(numbers):
# #     if numbers[i] % 2 == 0:
# #         print(numbers[i])
# #     i += 1
# # print(sum(numbers))
# # i = 0
# # summ = 0
# while i < len(numbers):
#     summ += numbers[i]
#     i += 1
# print(summ)
#
# while i < len(numbers):
#     if numbers[i] > max_num and numbers[i] < max_num:
#         second = numbers[i]


# prev_num = 0
# i = 0
# neighbors = 1
# while i < len(numbers):
#     if numbers[i] == prev_sym:
#         count += 1
#     prev_sym = numbers[i]
#     i += 1
# print(prev_sym)


numbers = [1,7,6,8,8,9,9,4,5,5,5,5,8,9,12,14]
uniq_num =[]
# i = 0
# gt_ten = 0
# while i < len(numbers):
#     if numbers[i] > 10:
#         gt_ten += 1
#     i += 1
# print(gt_ten)

i = 0
while i < len(numbers):
    if numbers[i] not in uniq_num:
        uniq_num.append(numbers[i])
    i += 1
uniq_num.sort()
print(uniq_num)



