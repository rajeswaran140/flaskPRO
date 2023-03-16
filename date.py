from datetime import datetime
current_date = datetime.now()

print('Day: ' + str (current_date.day))
print('Month: ' + str (current_date.month))
print ('Year: ' + str(current_date.year))
print ('Time: ' + str(current_date.time()))

timezone = current_date.astimezone().tzinfo
print('Timezone:', timezone)
