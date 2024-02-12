
"""
    Method used to transform input data containing start times and end times in separate Arrays to single 2D Array.
    Result is Array in shape Nx2 were each item x represents single interview starting at x[0] and ending at x[1]
    Returning result and number of interviews N
"""
def transformIntervalTimes(start_times, end_times):

    n = max(len(start_times), len(end_times))
    res = []

    for i in range(n):
        res.append([start_times[i], end_times[i]])

    return res, n
