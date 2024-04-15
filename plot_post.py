import os
import matplotlib.pyplot as plt

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

def plot_navigation(latitudes, longitudes):
    plt.figure(figsize=(10, 6))
    plt.plot(longitudes, latitudes, 'b.', markersize=5, label='Positions')
    plt.xlabel('Longitude (degrees)')
    plt.ylabel('Latitude (degrees)')
    plt.title('Navigation Positions')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.ticklabel_format(useOffset=False)
    plt.xlim(min(longitudes)-0.01, max(longitudes)+0.01)
    plt.ylim(min(latitudes)-0.01, max(latitudes)+0.01)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 获取当前脚本文件所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构造NMEA文件的相对路径
    nmea_file = os.path.join(script_dir, "rtk_rrr_solution.txt")
    latitudes, longitudes = parse_nmea_file(nmea_file)
    plot_navigation(latitudes, longitudes)
