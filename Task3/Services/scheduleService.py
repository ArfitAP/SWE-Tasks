from Utils.intervalsUtil import transformIntervalTimes

"""
    Implementation of algorithm to get max number of non-overlaping interviews.
    Returning object containing max number of interviews
"""
def getMaxNumberOfInterviews(start_times, end_times):

    # Transform input data to shape that is easier to handle
    interviewSlots, n = transformIntervalTimes(start_times, end_times)

    # Sort interviews by end times ascending
    interviewSlots.sort(key=lambda x: x[1])

    # Initialize auxiliary variables
    res = 0
    end = min(map(lambda x: x[0], interviewSlots))

    # Foreach interview
    for i in range(n):

        # If interview does not overlap with any of previous
        if interviewSlots[i][0] >= end:

            # Update current end time and increase the number of possible interviews
            end = interviewSlots[i][1]
            res += 1

    return {
            "max_interviews": res
        }
