import ru_local

prices = {'{}'.format(ru_local.AI_80): 33.00, '{}'.format(ru_local.AI_92): 41.00, '{}'.format(ru_local.AI_95): 44.50, '{}'.format(ru_local.AI_98): 50.00}
with open('azs.txt') as f_in:
    with open('azs1.txt', 'w') as f_out:
        for line in f_in:
            a = line.find(' ')
            b = line.find(' ', 2)
            num = line[:a]
            _max = line[a:b]
            mark = line[b:]
            f_out.write('{}'.format(ru_local.AUTO))
            f_out.write(num)
            f_out.write('{}'.format(ru_local.MAX_LINE))
            f_out.write(_max)
            f_out.write('{}'.format(ru_local.GAS))
            f_out.write(mark)
with open('input.txt') as f_in1:
    with open('input1.txt', 'w') as f_out1:
        for line in f_in1:
            x = line.find(' ')
            y = line.find(' ', 2)
            time = line[:x]
            minutes = line[x:y]
            mark1 = line[y:]
            f_out1.write('{}'.format(ru_local.IN))
            f_out1.write(time)
            f_out1.write('{}'.format(ru_local.NEW_CLIENT))
            f_out1.write(time)
            f_out1.write(mark1)
            f_out1.write(minutes)
            f_out1.write('{}'.format(ru_local.STAND_IN_LINE))
            f_out1.write('\n')
            with open('azs1.txt') as f_in2:
                for line2 in f_in2:
                    f_out1.write(line2)