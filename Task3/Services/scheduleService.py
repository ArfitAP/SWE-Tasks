from Utils.intervalsUtil import transformIntervalTimes


def getMaxNumberOfInterviews(start_times, end_times):

    interviewSlots, n = transformIntervalTimes(start_times, end_times)
    interviewSlots.sort(key=lambda x: x[1])

    res = 0
    end = min(map(lambda x: x[0], interviewSlots))

    for i in range(n):

        if interviewSlots[i][0] >= end:
            end = interviewSlots[i][1]
            res += 1

    return {
            "max_interviews": res
        }
