import csv
from math import factorial, e
import numpy as np
import os

def kl_divergence(a, b):
    return sum(a[i] * np.log(a[i]/b[i]) for i in range(len(a)))

def normal_row(arr):
    norm = []
    for i in range(0, len(arr)):
        norm.append(((e**(-sum(arr)/len(arr)))*((sum(arr)/len(arr))**arr[i]))/((factorial(arr[i]))))
    return norm
def entropy(filename):
    file = os.path.join("./files",filename)
    sats = []
    timestamps = []
    satsRes = 0
    firstTime = 0 

    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].split(';')[9] != 'vehicle_gps_position.satellites_used':
                sats.append(int(row[0].split(';')[9]))
            if row[0].split(';')[0] != 'timestamp':
                timestamps.append(int(row[0].split(';')[0]))

    for i in range(1, len(sats)-5):
        old = [sats[i-1], sats[i], sats[i+1], sats[i+2], sats[i+3]]
        new = [sats[i], sats[i+1], sats[i+2], sats[i+3], sats[i+4]]
        new_old = kl_divergence(normal_row(new), normal_row(old))
        old_new = kl_divergence(normal_row(old), normal_row(new))
        res = abs(new_old)+abs(old_new)
        if res >= 1 and firstTime == 0:
            firstTime = timestamps[i]
        if satsRes < res:
            satsRes = res
    # print(firstTime)
    # print(timestamps[-1])
    # print(timestamps[0])
    # print(satsRes)
    answer=""
    if (satsRes >= 1):
        answer="Глушение/Асинхронная атака"
    elif (satsRes >= 0.04):
        answer="Синхронная атака"
    else:
        answer="Нормальный полёт"
    return answer