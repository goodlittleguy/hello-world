import bisect
def grade(score,breakpoints = [60,80,90],grades = "CBA"):
    line = bisect.bisect_left(breakpoints,score)
    return grades[line]
'''现在我们来试用一下'''
a = [grade(score) for score in [60,70,80]]
print(a)
