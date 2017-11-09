#!/usr/bin/python
import time
import sys
import os

sys.path.append('/usr/local/lib/python2.7/site-packages/')
import psutil


def main():
    text_colour = str(6)
    load_colour = str(14)
    uptime_colour = str(14)
    mem_colour = str(4)
    swp_colour = str(4)
    cpu_colour = str(9)
    cpu_user_colour = str(2)
    cpu_sys_colour = str(1)

    uptime = round(time.time() - psutil.boot_time())
    minutes, seconds = divmod(uptime, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    upt = str(int(days)) + 'd ' + str(int(hours)).zfill(2) + ':' + str(int(minutes)).zfill(2) + ':' + str(
        int(seconds)).zfill(2)

    av1, av5, av15 = os.getloadavg()
    load = "%.2f %.2f %.2f" \
           % (av1, av5, av15)

    if av1 > 50 or av5 > 25:
        load_colour = str(9)

    mem = round((((psutil.virtual_memory().wired + psutil.virtual_memory().active) >> 20) / 1024), 1)
    if mem > 12:
        mem_colour = str(9)
    mem = str(mem) + 'G'

    swap_free = round(((psutil.swap_memory().used >> 20) / 1024), 2)
    swap_total = round(((psutil.swap_memory().total >> 20) / 1024), 2)
    if swap_total > 5:
        swp_colour = str(9)
    swp = str(swap_free) + 'G' + '/' + str(swap_total) + 'G'

    cpu_all = psutil.cpu_times_percent(1)
    cpu_user = cpu_all.user
    cpu_user_bar = round(cpu_user / 10)
    cpu_sys = cpu_all.system
    cpu = cpu_user + cpu_sys
    cpu_bar = round(cpu / 10)
    bar = '#[fg=colour4]['
    for x in range(1, 11):
        if x <= cpu_bar:
            if x <= cpu_user_bar:
                bar = bar + '#[fg=colour' + cpu_user_colour + ']|'
            else:
                bar = bar + '#[fg=colour' + cpu_sys_colour + ']|'
        else:
            bar = bar + ' '
    bar = bar + '#[fg=colour4]]'

    if cpu <= 30:
        cpu_colour = str(2)
    elif cpu <= 80:
        cpu_colour = str(11)
    elif cpu > 80:
        cpu_colour = str(1)

    print('#[fg=colour' + text_colour + ']CPU: '
          + str(bar) + ' #[fg=colour' + cpu_colour + ']'
          + (str(cpu) + '%%').rjust(6)
          + '  #[fg=colour' + load_colour + ']'
          + str(load)
          + '  #[fg=colour' + text_colour + ']Mem: #[fg=colour' + mem_colour + ']'
          + str(mem)
          + '  #[fg=colour' + text_colour + ']Swp: #[fg=colour' + swp_colour + ']'
          + str(swp)
          + '  #[fg=colour' + text_colour + ']Up: #[fg=colour' + uptime_colour + ']'
          + str(upt))


main()
