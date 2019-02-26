import random
import ru_local
prices = {'{}'.format(ru_local.AI_80): 33.00, '{}'.format(ru_local.AI_92): 41.00,
          '{}'.format(ru_local.AI_95): 44.50, '{}'.format(ru_local.AI_98): 50.00}
times = {'auto_1': None, 'auto_2': None, 'auto_3': None}
queue_1 = []
queue_2 = []
queue_3 = []

stazs1 = ""
stazs2 = ""
stazs3 = ""
st3 = ""
with open('azs.txt') as f_in:
    with open('azs1.txt', 'w') as f_out:
        for line in f_in:
            a = line.find(' ')
            b = line.find(' ', 2)
            num = line[:a]
            _max = line[a:b]
            mark = line[b:].replace('\n', '')
            st2 = '{}'.format(ru_local.AUTO)
            st2 += " " + num
            st2 += " " + '{}'.format(ru_local.MAX_LINE)
            st2 += " " + _max
            st2 += " " + '{}'.format(ru_local.GAS)
            st2 += " " + mark + " -> "
            if stazs1 == "":
                stazs1 = st2
            else:
                if stazs2 == "":
                    stazs2 = st2
                else:
                    stazs3 = st2


star1 = ""
star2 = ""
star3 = ""
with open('input.txt') as f_in1:
    with open('input1.txt', 'w') as f_out1:
        a = 0
        for line in f_in1:
            x = line.find(' ')
            y = line.find('{}'.format(ru_local.A))
            time = line[:x] + ' '
            hours = int(time[:time.find(':')])
            minutes = int(time[time.find(':')+1:])
            enother_time = hours * 60 + minutes
            litters = line[x:y - 1]
            mark1 = line[y:].replace('\n', '')

            st = ('{}'.format(ru_local.IN))
            st += ' ' + time
            st += ' ' + '{}'.format(ru_local.NEW_CLIENT)
            st += ' ' + time
            st += ' ' + mark1
            st += ' ' + litters
            if int(litters) % 10 == 0:
                refueling_time = int(int(litters) / 10 + random.randint(-1, 1))
                st += ' ' + str(refueling_time)
            elif int(litters) % 10 != 0:
                refueling_time = int((int(litters) // 10 + 1) + random.randint(-1, 1))
                st += ' ' + str(refueling_time)
            st += ' ' + '{}'.format(ru_local.STAND_IN_LINE)

            if mark1 == '{}'.format(ru_local.AI_80):
                if len(star1) < 3:
                    st += ' ' + '1 '
                    star1 += "*"
                    stazs1 += "*"
                else:
                    st += ' ' + '1 '
                    st += '{}'.format(ru_local.CANT)
            elif mark1 == '{}'.format(ru_local.AI_92):
                if len(star2) < 2:
                    st += ' ' + '2 '
                    star2 += "*"
                    stazs2 += "*"
                else:
                    st += ' ' + '3 '
                    if len(star3) < 4:
                        star3 += "*"
                        stazs3 += "*"
            elif mark1 == '{}'.format(ru_local.AI_95):
                if len(star3) < 4:
                    st += ' ' + '3 '
                    star3 += "*"
                    stazs3 += "*"
                else:
                    st += ' ' + '3 '
                    st += '{}'.format(ru_local.CANT)
            elif mark1 == '{}'.format(ru_local.AI_98):
                if len(star3) < 4:
                    st += ' ' + '3 '
                    star3 += "*"
                    stazs3 += "*"
                else:
                    st += ' ' + '3 '
                    st += '{}'.format(ru_local.CANT)
            st += ' ' + '\n'
            f_out1.write(st)
            f_out1.write(stazs1 + '\n')
            f_out1.write(stazs2 + '\n')
            f_out1.write(stazs3 + '\n')
            times.update()

            if mark1 == '{}'.format(ru_local.AI_80):
                if len(queue_1) < 3:
                    queue_1.append(enother_time)
                    times.update({'auto_1': queue_1})
                else:
                    pass
            elif mark1 == '{}'.format(ru_local.AI_92):
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
            elif mark1 == '{}'.format(ru_local.AI_95):
                if len(queue_3) < 4:
                    queue_3.append(enother_time)
                    times.update({'auto_3': queue_3})
                else:
                    pass
            elif mark1 == '{}'.format(ru_local.AI_98):
                if len(queue_3) < 4:
                    queue_3.append(enother_time)
                    times.update({'auto_3': queue_3})
                else:
                    pass

            if int(litters) % 10 == 0:
                refueling_time = int(int(litters) / 10 + random.randint(-1, 1))
                a = times.get('auto_1')
                if a is not None:
                    for i in a:
                        if enother_time - a[0] >= refueling_time:
                            a.remove(a[0])
                            b = {'auto_1': a}
                            times.update(b)
                c = times.get('auto_2')
                if c is not None:
                    for i in c:
                        if enother_time - c[0] >= refueling_time:
                            c.remove(c[0])
                            d = {'auto_2': c}
                            times.update(d)

                e = times.get('auto_3')
                if e is not None:
                    for i in e:
                        if enother_time - e[0] >= refueling_time:
                            e.remove(e[0])
                            f = {'auto_3': e}
                            times.update(f)
            elif int(litters) % 10 != 0:
                refueling_time = int((int(litters) // 10 + 1) + random.randint(-1, 1))
                a = times.get('auto_1')
                if a is not None:
                    for i in a:
                        if enother_time - a[0] >= refueling_time:
                            a.remove(a[0])
                            b = {'auto_1': a}
                            times.update(b)

                c = times.get('auto_2')
                if c is not None:
                    for i in c:
                        if enother_time - c[0] >= refueling_time:
                            c.remove(c[0])
                            d = {'auto_2': c}
                            times.update(d)

                e = times.get('auto_3')
                if e is not None:
                    for i in e:
                        if enother_time - e[0] >= refueling_time:
                            e.remove(e[0])
                            f = {'auto_3': e}
                            times.update(f)
            with open('azs1.txt') as f_in2:
                for line2 in f_in2:
                    f_out1.write(line2)

with open('input1.txt') as f_in3:
    text = f_in3.read()
    print(text)
