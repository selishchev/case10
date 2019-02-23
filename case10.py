prices = {'АИ-80': 33.00, 'АИ-92': 41.00, 'АИ-95': 44.50, 'АИ-98': 50.00}
with open('azs.txt') as f_in:
    with open('azs1.txt', 'w') as f_out:
        for line in f_in:
            a = line.find(' ')
            b = line.find(' ', 2)
            num = line[:a]
            _max = line[a:b]
            mark = line[b:]
            f_out.write('Автомат №')
            f_out.write(num)
            f_out.write('  максимальная очередь:')
            f_out.write(_max)
            f_out.write('  Марки бензина: ')
            f_out.write(mark)
with open('input.txt') as f_in1:
    with open('input1.txt', 'w') as f_out1:
        for line in f_in1:
            x = line.find(' ')
            y = line.find(' ', 2)
            time = line[:x]
            minutes = line[x:y]
            mark1 = line[y:]
            f_out1.write('В ')
            f_out1.write(time)
            f_out1.write('  новый клиент:  ')
            f_out1.write(time)
            f_out1.write(mark1)
            f_out1.write(minutes)
            f_out1.write('встал в очередь к автомату №')
            f_out1.write('\n')
            with open('azs1.txt') as f_in2:
                for line2 in f_in2:
                    f_out1.write(line2)
