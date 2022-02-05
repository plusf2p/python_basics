list_cub = []
sum_of_dig = 0
sum_of_dig_plus = 0


def sum_of_dig_func(dig):
	tmp_sum = dig % 10
	dig = dig // 10
	while dig >= 1:
		tmp_sum += dig % 10
		dig = dig // 10
	return tmp_sum


for i in range(1, 1001):
	if i % 2 != 0:
		tmp = i ** 3
		list_cub.append(tmp)
		if sum_of_dig_func(tmp) % 7 == 0:
			sum_of_dig += tmp
		if sum_of_dig_func(tmp + 17) % 7 == 0:
				sum_of_dig_plus += tmp + 17

print('A: Сумма чисел списка: ', sum_of_dig)
print('B и C: Сумма чисел списка (+17): ', sum_of_dig_plus)
