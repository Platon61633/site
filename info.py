import pandas as pd
import os

def info(filename):
    table = pd.read_csv(os.path.join('./files',filename), delimiter=';')[['timestamp', 'vehicle_gps_position.alt', 'vehicle_gps_position.lat', 'vehicle_gps_position.lon', 'vehicle_air_data.baro_alt_meter']]
    timestamp = table['timestamp']

    delta_timestamp = [timestamp[i+1]-timestamp[i] for i in range(len(timestamp)-1)]

    alt = [table['vehicle_gps_position.alt'][i+1]-table['vehicle_gps_position.alt'][i] for i in range(len(table['vehicle_gps_position.alt'])-1)]
    lat = [table['vehicle_gps_position.lat'][i+1]-table['vehicle_gps_position.lat'][i] for i in range(len(table['vehicle_gps_position.lat'])-1)]
    lon = [table['vehicle_gps_position.lon'][i+1]-table['vehicle_gps_position.lon'][i] for i in range(len(table['vehicle_gps_position.lon'])-1)]

    velocity = [(((alt[i]**2+lat[i]**2+lon[i]**2)**0.5)/delta_timestamp[i]) for i in range(len(delta_timestamp))]

    acceleration =max([velocity[i]/delta_timestamp[i] for i in range(len(delta_timestamp))])
    basic = {}
    for columns in table.columns:
        basic = {**basic, **{columns+"_mean": table[columns].mean(), columns+'_max': table[columns].max(), columns+'_min': table[columns].min()}}


    # print('acceleration', 'max', max(acceleration))
    return {**basic, **{'acceleration': acceleration, 'velocity_max': max(velocity), 'velocity_mean': sum (velocity) / len (velocity),
    'delta_timestamp_min': min(delta_timestamp), 'delta_timestamp_max': max(delta_timestamp), 'delta_timestamp_mean': sum (delta_timestamp) / len (delta_timestamp),
    }}
