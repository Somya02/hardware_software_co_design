import time
import matplotlib.pyplot as plt
from serial_communication import SerialCommunication

class DeviceMonitor:
    def __init__(self, port):
        self.serial_comm = SerialCommunication(port)
        self.data = []
        
    def monitor_data(self, duration=30):
        plt.ion()
        fig, ax = plt.subplots()
        start_time = time.time()
        
        while time.time() - start_time < duration:
            data = self.serial_comm.read_data()
            if data:
                self.data.append(float(data))  # Assuming numeric data
                ax.clear()
                ax.plot(self.data)
                plt.draw()
                plt.pause(0.01)
        
        plt.ioff()
        plt.show()

    def stop(self):
        self.serial_comm.close()

