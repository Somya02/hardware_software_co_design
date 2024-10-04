from serial_communication import SerialCommunication

class DeviceControl:
    def __init__(self, port):
        self.serial_comm = SerialCommunication(port)
    
    def send_command(self, command):
        self.serial_comm.send_command(command)
        response = self.serial_comm.read_data()
        return response
    
    def stop(self):
        self.serial_comm.close()
