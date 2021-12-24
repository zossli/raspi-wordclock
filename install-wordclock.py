from crontab import CronTab
import re
cron = CronTab(user='root')

for job in cron.find_comment(re.compile('Wordclock')):
    cron.remove(job)

job = cron.new(command='sudo python /home/pi/wordclock/wordclock.py setTime')
job.minute.every(5)
job.set_comment("Wordclock: Run every 5 Minutes, to set new Time")
job2 = cron.new(command='sudo python /home/pi/wordclock/wordclock.py startup')
job2.every_reboot()
job2.set_comment("Wordclock: Run one time at every reboot, to set new Time") 

cron.write()
