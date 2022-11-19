import time

year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()
data = f' year: {year} mon: {mon} mday: {mday} hour: {hour} min: {min} sec: {sec} wday: {wday} yday: {yday} isdst: {isdst}'

print(data)

file = open("date-info.txt", "w")
file.write(data)
file.close()