from file_utils import loadWithJSON

## Will load all Harrisonburg and Rockingham data into a list of lists
## Each element in the main list will contain a list of two items, the str:date and int:cases
harrisonburg_data = loadWithJSON('harrisonburg.json')
rockingham_data = loadWithJSON('rockingham.json')

## Print all elements in the list as an example
for data in rockingham_data:
     date = data[0]
     cases = data[1]
     print('On ' + date + ' there were ' + str(cases) + ' cases in Harrisonburg')
print()
print('When was the first positive COVID case in Rockingham County and Harrisonburg?')
for data in harrisonburg_data:
    date = data[0]
    cases = data[1]
    if cases > 0:
        print(date + ' in Harrisonburg')
        break
for data in rockingham_data:
    date = data[0]
    cases = data[1]
    if cases > 0:
        print(date + ' in Rockingham')
        break
print()
print('What day was the maximum number of cases recorded in Harrisonburg and Rockingham County?')


previous_day = 0
max = 0
day = None
for data in harrisonburg_data:
    date = data[0]
    cases = data[1]
    if max < (cases - previous_day):
        day = date
        max = (cases - previous_day)
    previous_day = cases
print(day + ' in Harrisonburg')

previous_day = 0
max = 0
day = None
for data in rockingham_data:
    date = data[0]
    cases = data[1]
    if max < (cases - previous_day):
        day = date
        max = (cases - previous_day)
    previous_day = cases

print(day + ' in Rockingham')
print()
print('What was the worst week in the city/county for new COVID cases? '
      'When was the rise in cases the fastest over a seven day period?')
i = 0
harrisonburg_cases = []
harrisonburg_dates = []
previous_day = 0
for data in harrisonburg_data:
    date = data[0]
    cases = data[1]
    harrisonburg_cases.append(cases - previous_day)
    harrisonburg_dates.append(date)
    previous_day = cases
movingavgs = []
weekavg=0
while i < (len(harrisonburg_cases) - 6):
    weekavg = sum(harrisonburg_cases[i : i + 7]) / 7
    movingavgs.append(weekavg)
    i += 1
max = 0
startH = None
for x, val in enumerate(movingavgs):
    if max < val:
        startH = x
        max = val
print('The worst week in Harrisonburg for new COVID cases was ' + harrisonburg_dates[startH] + ' through ' + harrisonburg_dates[startH + 6])

previous_day = 0
rockingham_cases = []
rockingham_dates = []
for data in rockingham_data:
    date = data[0]
    cases = data[1]
    rockingham_cases.append(cases - previous_day)
    rockingham_dates.append(date)
    previous_day = cases
movingavgs = []
weekavg = 0
i = 0
while i < len(rockingham_cases) - 7 + 1:
    weekavg = sum(rockingham_cases[i : i + 7]) / 7
    movingavgs.append(weekavg)
    i += 1
max = 0
startR = None
for x, val in enumerate(movingavgs):
    if max < val:
        startR = x
        max = val
print('The worst week in Rockingham for new COVID cases was ' + rockingham_dates[startR] + ' through ' + rockingham_dates[startR + 6])