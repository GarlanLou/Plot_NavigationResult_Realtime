import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def parse_nmea_file(file_path):
    latitudes = []
    longitudes = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('$GPGGA'):
                data = line.split(',')
                latitude = float(data[2][:2]) + float(data[2][2:]) / 60.0
                if data[3] == 'S':
                    latitude = -latitude
                longitude = float(data[4][:3]) + float(data[4][3:]) / 60.0
                if data[5] == 'W':
                    longitude = -longitude
                latitudes.append(latitude)
                longitudes.append(longitude)
    return latitudes, longitudes

def update_plot(frame):
    latitudes, longitudes = parse_nmea_file(nmea_file)
    ax.clear()
    ax.plot(longitudes, latitudes, 'b.-', markersize=5, label='Track')
    ax.plot(longitudes[-1], latitudes[-1], 'r*', markersize=10, label='Current Position')
    ax.set_xlabel('Longitude (degrees)')
    ax.set_ylabel('Latitude (degrees)')
    ax.set_title('Real-time Navigation Positions')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.ticklabel_format(useOffset=False)
    ax.set_xlim(min(longitudes)-0.01, max(longitudes)+0.01)
    ax.set_ylim(min(latitudes)-0.01, max(latitudes)+0.01)
    ax.legend()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    nmea_file = os.path.join(script_dir, "rtk_tc_solution.txt")

    fig, ax = plt.subplots(figsize=(10, 6))

    while True:
        latitudes, longitudes = parse_nmea_file(nmea_file)
        if not latitudes or not longitudes:
            print("The NMEA file is empty. Waiting for data...")
            time.sleep(1)  # Wait for 1 second
        else:
            ani = FuncAnimation(fig, update_plot, interval=100, save_count=10)
            plt.show()
            break
