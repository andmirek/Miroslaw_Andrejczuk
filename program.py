# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:03:03 2020

@author: rodzina
"""
#https://github.com/andmirek/Miroslaw_Andrejczuk
from datetime import datetime

def get_data(fname):
    """reads time from a file and returns list
       with g starting and ending time"""
    start = []
    endt = []
    with open(fname) as mfile:
        for line in mfile:
            if 'start' in line or line in ['\n']:
                continue
            line = line.strip('\n')
            start.append(dtime(line.split(",")[0]))
            endt.append(dtime(line.split(",")[1]))
    return start, endt


def dtime(intime):
    """convert time in am/pm to Hours:Minutes"""
    return datetime.strptime(intime, '%I:%M%p').strftime("%H:%M")


def conflict(mtimes, mtimee, mstart, mend):
    """return true if mtimes or mtimee is between mstart and mend
       mstart - start time
       mend   - end time
       mtimes,  mtimee - start/end time for testing"""
    if mstart <= mtimes < mend or mstart < mtimee <= mend:
        return True
    elif mtimes <= mstart and mtimee >= mend:
        return True
    else:
        return False


if __name__ == "__main__":
    FILEN = 'times'
    TSTART, TEND = get_data(FILEN)
    NMEET = len(TSTART)
    for i in range(NMEET):
        for j in range(i+1, NMEET):
            if conflict(TSTART[i], TEND[i], TSTART[j], TEND[j]):
                print "meeting ", i + 1, "in conflict with meeting ",\
 j + 1
