import serial
import time

class SerialCommunication:
    def __init__(self, port, baudrate=9600, timeout=1):
        """
        Initializes the serial communication with the given port and baudrate.
        
        :param port: The serial port (e.g., COM3 or /dev/ttyUSB0)
        :param baudrate: Baud rate for communication, default is 9600
        :param timeout: Timeout for reading from the serial port, default is 1 second
        """
        try:
            self.ser = serial.Serial(port, baudrate, timeout=timeout)
            time.sleep(2)  # Give time for the connection to initialize
        except serial.SerialException as e:
            print(f"Error opening serial port {port}: {e}")
            self.ser = None

    def send_command(self, command):
        """
        Sends a command over the serial port.
        
        :param command: The command to send to the device
        """
        if self.ser and self.ser.is_open:
            try:
                self.ser.write(command.encode('utf-8'))
            except serial.SerialException as e:
                print(f"Failed to send command: {e}")
        else:
            print("Serial port is not open.")

    def read_data(self):
        """
        Reads data from the serial port if available.
        
        :return: The data read from the serial port as a string, or None if no data is available
        """
        if self.ser and self.ser.is_open:
            try:
                if self.ser.in_waiting > 0:
                    data = self.ser.readline().decode('utf-8').strip()
                    return data
            except serial.SerialException as e:
                print(f"Failed to read data: {e}")
        return None

    def close(self):
        """
        Closes the serial connection.
        """
        if self.ser and self.ser.is_open:
            try:
                self.ser.close()
            except serial.SerialException as e:
                print(f"Failed to close serial port: {e}")
