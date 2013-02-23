import re
import sys
import time

if  len(sys.argv) !=  2 :
    raise Exception("This script excepts a single argument. The StackExchange file.")

fileName = sys.argv[1]

kvRe = '(\w+)="(.*?)"'

f = open(fileName)
f.readline()
f.readline()
print "<add>"
for i, line in enumerate(f):
    if line == "</posts>" :
        continue
    print "<doc>"
    for field in re.findall(kvRe, line):
        key = field[0]
        value = field[1]
        if (key == "Body" or key == "Title" ) :
            value = re.sub("&lt;/?.+?&gt;|&[^q][#\w]+;"," ",value)
        elif key == "Tags" :
            value = re.sub("&#?\w+;"," ",value)
        elif (key == "CreationDate" or key == "LastActivityDate" or key == "LastEditDate" ) :
            value = value + "Z"
            if (key == "CreationDate"):
                t = time.strptime(value[0:-5], '%Y-%m-%dT%H:%M:%S')
                month = str(t[1])
                hour = str(t[3])
                minute = str(t[4])
                day_of_week = str(t[6]) #Monday is 0
                day_of_year = str(t[7]) #1 is Jan 1st
                print '<field name="%s">%s</field>' % ("CreationMonth",month)
                print '<field name="%s">%s</field>' % ("CreationHour",hour)
                print '<field name="%s">%s</field>' % ("CreationMinute",minute)
                print '<field name="%s">%s</field>' % ("CreationDayOfWeek",day_of_week)
                print '<field name="%s">%s</field>' % ("CreationDayOfYear",day_of_year)
                print '<field name="%s">%s</field>' % ("CreationDayOfWeek_Hour",day_of_week +"_"+ hour)
        if len(value) == 0 :
            continue
        print '<field name="%s">%s</field>' % (key, value )
    print "</doc>"
    if i > 1000000 :
        break;
print "</add>"
