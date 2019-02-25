import random
prices = {'АИ-80': 33.00, 'АИ-92': 41.00, 'АИ-95': 44.50, 'АИ-98': 50.00}
times = {'auto_1': None, 'auto_2': None, 'auto_3': None}
queue_1 = []
queue_2 = []
queue_3 = []
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
        a = 0
        for line in f_in1:
            x = line.find(' ')
            y = line.find('А')
            time = line[:x]
            hours = int(time[:time.find(':')])
            minutes = int(time[time.find(':')+1:])
            enother_time = hours * 60 + minutes
            litters = line[x:y - 1]
            mark1 = line[y:]
            f_out1.write('В ')
            f_out1.write(time)
            f_out1.write('  новый клиент:  ')
            f_out1.write(time)
            f_out1.write(mark1)
            f_out1.write(litters)
            f_out1.write('встал в очередь к автомату №')
            f_out1.write('\n')
            times.update()



            if mark1 == 'АИ-80\n':
                if len(queue_1) < 3:
                    queue_1.append(enother_time)
                    times.update({'auto_1': queue_1})
                else:
                    pass
            elif mark1 == 'АИ-92\n':
                if len(queue_2) < len(queue_3):
                    if len(queue_2) < 2:
                        queue_2.append(enother_time)
                        times.update({'auto_2': queue_2})
                    else:
                        pass
                elif len(queue_2) >= len(queue_3):
                    if len(queue_3) < 4:
                        queue_3.append(enother_time)
                        times.update({'auto_3': queue_3})
                    else:
                        pass
            elif mark1 == 'АИ-95\n':
                if len(queue_3) < 4:
                    queue_3.append(enother_time)
                    times.update({'auto_3': queue_3})
                else:
                    pass
            elif mark1 == 'АИ-98\n':
                if len(queue_3) < 4:
                    queue_3.append(enother_time)
                    times.update({'auto_3': queue_3})
                else:
                    pass





            if int(litters) % 10 == 0:
                refueling_time = int(int(litters) / 10 + random.randint(-1, 1))
                a = times.get('auto_1')
                if a not in None:
                    for i in a:
                        if enother_time - a[0] >= refueling_time:
                            a.remove(a[0])
                            b = {'auto_1': a}
                            times.update(b)
                c = times.get('auto_2')
                if c not in None:
                    for i in c:
                        if enother_time - c[0] >= refueling_time:
                            c.remove(c[0])
                            d = {'auto_2': c}
                            times.update(d)

                e = times.get('auto_3')
                if e not in None:
                    for i in e:
                        if enother_time - e[0] >= refueling_time:
                            e.remove(e[0])
                            f = {'auto_3': e}
                            times.update(f)
            elif int(litters) % 10 != 0:
                refueling_time = int((int(litters) // 10 + 1) + random.randint(-1, 1))
                a = times.get('auto_1')
                if a not in None:
                    for i in a:
                        if enother_time - a[0] >= refueling_time:
                            a.remove(a[0])
                            b = {'auto_1': a}
                            times.update(b)

                c = times.get('auto_2')
                if c not in None:
                    for i in c:
                        if enother_time - c[0] >= refueling_time:
                            c.remove(c[0])
                            d = {'auto_2': c}
                            times.update(d)

                e = times.get('auto_3')
                if e not in None:
                    for i in e:
                        if enother_time - e[0] >= refueling_time:
                            e.remove(e[0])
                            f = {'auto_3': e}
                            times.update(f)
                print(times)
            with open('azs1.txt') as f_in2:
                for line2 in f_in2:
                    f_out1.write(line2)
