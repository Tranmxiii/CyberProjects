import requests

# Function to get IP geolocation using the ipinfo.io API
def get_ip_geolocation(ip):
    url = f"http://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\nIP Information for {ip}:")
        print(f"IP: {data['ip']}")
        print(f"Location: {data['city']}, {data['region']}, {data['country']}")
        print(f"Org: {data['org']}")
    else:
        print(f"[!] Failed to retrieve information for IP: {ip}")

# User controls to either check another IP or exit
def user_controls():
    while True:
        choice = input("\nDo you want to check another IP? (y/n): ").strip().lower()
        if choice == 'y':
            return True  # Return True to allow another check
        elif choice == 'n':
            print("\nExiting the program. Goodbye!")
            return False  # Return False to exit the program
        else:
            print("[!] Invalid input. Please enter 'y' for Yes or 'n' for No.")

# Main function
def main():
    print("IP Geolocation Finder Tool")
    print("Created by Michael Tran")
    print("=" * 50)

    while True:
        ip = input("Enter the IP address to look up: ").strip()
        get_ip_geolocation(ip)

        # Ask user if they want to check another IP or exit
        if not user_controls():
            break

if __name__ == "__main__":
    main()
