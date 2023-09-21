def is_valid_ip_address(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            if not 0 <= int(part) <= 255:
                return False
        except ValueError:
            return False
    return True

def main():
    ip_address = input("Enter an IP address: ")
    if is_valid_ip_address(ip_address):
        print("Valid IP address")
    else:
        print("Invalid IP address")

if __name__ == '__main__':
    main()
