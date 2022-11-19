import time

year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()
print(f' year: {year} mon: {mon} mday: {mday} hour: {hour} min: {min} sec: {sec} wday: {wday} yday: {yday} isdst: {isdst}')