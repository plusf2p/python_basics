for i in range(1, 101):
	tmp = i % 10
	if (tmp in [5, 6, 7, 8, 9, 0]) or (i in [11, 12, 13, 14]):
		sklon = 'ов'
	elif tmp in [2, 3, 4]:
		sklon = 'а'
	else:
		sklon = ''
	print(i, ' процент'+ sklon)
