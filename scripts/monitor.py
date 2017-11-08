#!/usr/bin/python
import time
import sys
import os

sys.path.append('/usr/local/lib/python2.7/site-packages/')
import psutil

def main():
    uptime = round(time.time() - psutil.boot_time())
    minutes, seconds = divmod(uptime, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    upt = str(days) + 'd ' + str(hours).zfill(2) + 'h ' + str(minutes).zfill(2) + 'm ' + str(seconds).zfill(2) + 's'

    av1, av5, av15 = os.getloadavg()
    load = "%.2f %.2f %.2f" \
           % (av1, av5, av15)

    mem = str(round((((psutil.virtual_memory().wired + psutil.virtual_memory().active) >> 20) / 1024), 1)) + 'G'

    swapfree = round(((psutil.swap_memory().used >> 20) / 1024), 2)
    swaptotal = round(((psutil.swap_memory().total >> 20) / 1024), 2)
    swp = str(swapfree) + 'G' + '/' + str(swaptotal) + 'G'

    cpuall = psutil.cpu_times_percent(1)
    cpuuser = cpuall.user
    cpusys = cpuall.system
    cpu = cpuuser + cpusys
    cpubar = round(cpu / 10)
    bar = '['
    for x in range(1, 11):
        if (x <= cpubar):
            bar = bar + '|'
        else:
            bar = bar + ' '
    bar = bar + ']'

    print('CPU: '
          + bar + ' '
          + str(cpu) + "%"
          + ' ' + load
          + ' Mem: ' + mem
          + ' Swp: ' + swp
          + ' Up: ' + str(upt)
          )


main()
