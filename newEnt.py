def check_row(row=list):
    row_sum=0.0
    for number in row:
        row_sum+=number
        if number < 0 :
            raise KeyError
    row_sum=row_sum/len(row)
    return row_sum
def normal_row(row,row_sum):
    import math
    import decimal    
    decimal.getcontext().prec = 100
    result = []
    for number in row:
        number=int(number)
        exp_number=math.exp(-1*row_sum)
        factorial_number=math.factorial(number)
        try:
            math_expectation=row_sum**number
            p_dist=((math_expectation)/factorial_number)*exp_number
        except:
            math_expectation=decimal.Decimal(row_sum)**decimal.Decimal(number)
            p_dist=((math_expectation)/factorial_number)*decimal.Decimal(exp_number)
        result.append(float(p_dist))
    return result
def calculate_entropy(old_row,new_row):
    import math
    old_new=0.0
    new_old=0.0
    for i in range(len(old_row)):
        try:
            old_new=old_new+(old_row[i]*math.log(old_row[i]/new_row[i]))
            new_old=new_old+(new_row[i]*math.log(new_row[i]/old_row[i]))
        except Exception as Error:
            old_new = old_new + 0.0
            new_old = new_old + 0.0
    return old_new,new_old

import csv

for i in range(1, 29):
    sats = []
    satsRes = 0
    # noises = []
    # noisesRes = 0
    hdop = []
    hdopRes = 0
    # vdop = []
    # vdopRes = 0
    # eph = []
    # ephRes = 0
    # epv = []
    # epvRes = 0

    with open(str(i)+'.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].split(';')[9] != 'vehicle_gps_position.satellites_used':
                sats.append(int(row[0].split(';')[9]))
            # if row[0].split(';')[8] != 'vehicle_gps_position.noise_per_ms':
            #     noises.append(int(row[0].split(';')[8]))
            # if row[0].split(';')[4] != 'vehicle_gps_position.eph':
            #     eph.append(float(row[0].split(';')[4]))
            # if row[0].split(';')[5] != 'vehicle_gps_position.epv':
            #     epv.append(float(row[0].split(';')[5]))
            if row[0].split(';')[6] != 'vehicle_gps_position.hdop':
                hdop.append(float(row[0].split(';')[6]))
            # if row[0].split(';')[7] != 'vehicle_gps_position.vdop':
            #     vdop.append(float(row[0].split(';')[7]))

    for i in range(1, len(sats)-5):
        old = normal_row([sats[i-1], sats[i], sats[i+1], sats[i+2], sats[i+3]], check_row([sats[i-1], sats[i], sats[i+1], sats[i+2], sats[i+3]]))
        new = normal_row([sats[i], sats[i+1], sats[i+2], sats[i+3], sats[i+4]], check_row([sats[i], sats[i+1], sats[i+2], sats[i+3], sats[i+4]]))
        old_new, new_old = calculate_entropy(old, new)
        res = abs(new_old)+abs(old_new)
        if satsRes < res:
            satsRes = res
    # for i in range(1, len(noises)-5):
    #     old = normal_row([noises[i-1], noises[i], noises[i+1], noises[i+2], noises[i+3]], check_row([noises[i-1], noises[i], noises[i+1], noises[i+2], noises[i+3]]))
    #     new = normal_row([noises[i], noises[i+1], noises[i+2], noises[i+3], noises[i+4]], check_row([noises[i], noises[i+1], noises[i+2], noises[i+3], noises[i+4]]))
    #     old_new, new_old = calculate_entropy(old, new)
    #     res = abs(new_old)+abs(old_new)
    #     if noisesRes < res:
    #         noisesRes = res
    # for i in range(1, len(eph)-5):
    #     old = normal_row([eph[i-1], eph[i], eph[i+1], eph[i+2], eph[i+3]], check_row([eph[i-1], eph[i], eph[i+1], eph[i+2], eph[i+3]]))
    #     new = normal_row([eph[i], eph[i+1], eph[i+2], eph[i+3], eph[i+4]], check_row([eph[i], eph[i+1], eph[i+2], eph[i+3], eph[i+4]]))
    #     old_new, new_old = calculate_entropy(old, new)
    #     res = abs(new_old)+abs(old_new)
    #     if ephRes < res:
    #         ephRes = res
    # for i in range(1, len(epv)-5):
    #     old = normal_row([epv[i-1], epv[i], epv[i+1], epv[i+2], epv[i+3]], check_row([epv[i-1], epv[i], epv[i+1], epv[i+2], epv[i+3]]))
    #     new = normal_row([epv[i], epv[i+1], epv[i+2], epv[i+3], epv[i+4]], check_row([epv[i], epv[i+1], epv[i+2], epv[i+3], epv[i+4]]))
    #     old_new, new_old = calculate_entropy(old, new)
    #     res = abs(new_old)+abs(old_new)
    #     if epvRes < res:
    #         epvRes = res
    for i in range(1, len(hdop)-5):
        old = normal_row([hdop[i-1], hdop[i], hdop[i+1], hdop[i+2], hdop[i+3]], check_row([hdop[i-1], hdop[i], hdop[i+1], hdop[i+2], hdop[i+3]]))
        new = normal_row([hdop[i], hdop[i+1], hdop[i+2], hdop[i+3], hdop[i+4]], check_row([hdop[i], hdop[i+1], hdop[i+2], hdop[i+3], hdop[i+4]]))
        old_new, new_old = calculate_entropy(old, new)
        res = abs(new_old)+abs(old_new)
        if hdopRes < res:
            hdopRes = res
    # for i in range(1, len(vdop)-5):
    #     old = normal_row([vdop[i-1], vdop[i], vdop[i+1], vdop[i+2], vdop[i+3]], check_row([vdop[i-1], vdop[i], vdop[i+1], vdop[i+2], vdop[i+3]]))
    #     new = normal_row([vdop[i], vdop[i+1], vdop[i+2], vdop[i+3], vdop[i+4]], check_row([vdop[i], vdop[i+1], vdop[i+2], vdop[i+3], vdop[i+4]]))
    #     old_new, new_old = calculate_entropy(old, new)
    #     res = abs(new_old)+abs(old_new)
    #     if vdopRes < res:
    #         vdopRes = res

    if (satsRes >= 1):
        if hdopRes < 70:
            answer="асинхр"
        else:
            answer="глуш"
    elif (satsRes >= 0.037):
        answer="синхр"
    else:
        answer="норм"
    print(answer)
    #print(satsRes)
    #print(hdopRes)