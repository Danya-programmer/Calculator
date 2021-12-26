def decision(task):
    for i in task:
        if i == '+':
            num = task.split(i)
            return int(num[0]) + int(num[1])
        elif i == '-':
            num = task.split(i)
            return int(num[0]) - int(num[1])
        elif i == '/' or i == ':':
            num = task.split(i)
            return int(num[0]) / int(num[1])
        elif i == '*':
            num = task.split(i)
            return int(num[0]) * int(num[1])
        else:
            pass