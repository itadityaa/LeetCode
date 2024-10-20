def minimumRounds(tasks: list[int]) -> int:
    count_tasks = {}
    for i in tasks:
        if i not in count_tasks:
            count_tasks[i] = 1
        else:
            count_tasks[i] += 1

    # print(count_tasks)
    minRounds = 0
    for count_task in count_tasks.values():
        if count_task == 1:
            return -1
        remainder = count_task % 3
        rounds = count_task // 3
        if remainder == 1 or remainder == 2:
            rounds += 1
        minRounds += rounds

    return minRounds


print(minimumRounds([2, 2, 2, 3, 3]))
