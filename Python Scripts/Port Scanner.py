import socket
from datetime import datetime

# Function to perform port scanning
def scan_ports(target_ip, start_port, end_port):
    print(f"\nScanning target: {target_ip}")
    print(f"Scanning ports from {start_port} to {end_port}")
    print(f"Start time: {datetime.now()}")
    print("=" * 50)

    # Loop through port range
    for port in range(start_port, end_port + 1):
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection attempt

        # Attempt to connect to the target IP and port
        result = sock.connect_ex((target_ip, port))

        # If the connection is successful (result 0), the port is open
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

        sock.close()

    print("=" * 50)
    print(f"Scan completed at {datetime.now()}")

# Function to ask user if they want to scan again or exit
def user_controls():
    while True:
        choice = input("\nDo you want to scan again? (y/n): ").strip().lower()
        if choice == 'y':
            return True  # Return True to allow another scan
        elif choice == 'n':
            print("Exiting the program.")
            return False  # Return False to exit the program
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")

# Main function
def main():
    print("Port Scanner Tool")
    print("Created by Michael Tran")
    print("=" * 50)

    while True:
        target_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))

        # Run the port scanner
        scan_ports(target_ip, start_port, end_port)

        # Ask user if they want to scan again or exit
        if not user_controls():
            break

if __name__ == "__main__":
    main()
