from random import randint


team1_title = '"Мастера кода"'
team2_title = '"Волшебники данных"'
team1_num = 6
team2_num = 6
allTasks = 55
completeTasks1 = randint(0, 10) + 45
completeTasks2 = randint(0,10) + 45
timeTeam1 = randint(0, 2000) + 10000
timeTeam2 = randint(0, 2000) + 10000
completeTasksTotal = completeTasks1 + completeTasks2
timeAvg = round((timeTeam1 + timeTeam2) / completeTasksTotal, 2)
timeAvgTeam1 = round(timeTeam1 / completeTasks1, 2)
timeAvgTeam2 = round(timeTeam2 / completeTasks2, 2)

winnerTimeAvg = timeAvgTeam2
if timeAvgTeam1 > timeAvgTeam2:
    winnerTimeAvg = timeAvgTeam1

if completeTasks1 > completeTasks2 or completeTasks1 == completeTasks2 and timeTeam1 < timeTeam2:
    result = 'Победа команды "Мастера кода"!'
    winnerTimeAvg = timeAvgTeam1
elif completeTasks1 < completeTasks2 or completeTasks1 == completeTasks2 and timeTeam1 > timeTeam2:
    result = 'Победа команды "Волшебники данных"!'
    winnerTimeAvg = timeAvgTeam2
else:
    result = 'Ничья!'

print('Команды, участвующие в соревновании: %s (кол-во участников %s) и %s (кол-во участников %s)' % (team1_title, team1_num, team2_title, team2_num))
print('Всего предстоит решить %s задач за максимальное время 200 минут' % (allTasks))

print('Кол-во задач, верно решенных командой {}: {}'.format(team1_title, completeTasks1))
print('Кол-во задач, верно решенных командой {}: {}'.format(team2_title, completeTasks2))
print('Время, за которое команда {} решила все задачи: {} секунд'.format(team1_title, timeTeam1))
print('Время, за которое команда {} решила все задачи: {} секунд'.format(team2_title, timeTeam2))

print(f'Команды верно решили {completeTasks1} и {completeTasks2} задач')
print(f'Сегодня было верно решено задач: {completeTasksTotal}, среднее время на задачу: {timeAvg} секунд')
print(f'Результат соревнования: {result} Среднее время выполнения заданий: {winnerTimeAvg} секунд')
