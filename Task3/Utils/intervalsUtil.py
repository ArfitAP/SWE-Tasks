
def transformIntervalTimes(start_times, end_times):

    n = max(len(start_times), len(end_times))
    res = []

    for i in range(n):
        res.append([start_times[i], end_times[i]])

    return res, n
