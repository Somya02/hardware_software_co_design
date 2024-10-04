import argparse
from device_monitor import DeviceMonitor
from device_control import DeviceControl

def main():
    parser = argparse.ArgumentParser(description="Embedded Serial Utility")
    parser.add_argument('--mode', type=str, required=True, help="Mode: 'monitor' or 'control'")
    parser.add_argument('--port', type=str, required=True, help="Serial port (e.g., COM3, /dev/ttyUSB0)")
    parser.add_argument('--command', type=str, help="Command to send in control mode")
    
    args = parser.parse_args()
    
    if args.mode == 'monitor':
        monitor = DeviceMonitor(args.port)
        print(f"Starting data monitoring on port {args.port}...")
        monitor.monitor_data()
        monitor.stop()
    
    elif args.mode == 'control':
        if not args.command:
            print("Please provide a command with --command.")
        else:
            control = DeviceControl(args.port)
            print(f"Sending command: {args.command}")
            response = control.send_command(args.command)
            print(f"Response: {response}")
            control.stop()
    
    else:
        print("Invalid mode. Use 'monitor' or 'control'.")

if __name__ == "__main__":
    main()

