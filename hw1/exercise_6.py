a = float(input('input beginning run (km) (> 0)    '))
b = float(input('input ending run (km)    '))
n = 1
an = a
while an < b and an > 0:
    an = an + an * 0.1
    n = n + 1
if an > 0:
    print('you have been running ', n, ' day(s)')
else:
    print ('you are wrong')
