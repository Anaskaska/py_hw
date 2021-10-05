time_sec = int(input ("input your time in sec "))
while time_sec > 86400:
    time_sec = time_sec - 86400

minutes = time_sec // 60
seconds = time_sec % 60
hours = 0
if minutes >= 60:
    hours = minutes // 60
    minutes = minutes % 60

time = f'your time is (hh:mm:ss) {hours}:{minutes}:{seconds} '
print(time)
