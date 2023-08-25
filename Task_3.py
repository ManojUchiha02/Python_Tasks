import re
import subprocess


def is_valid_ip(ip):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'
    pattern += r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip)


def is_pingable(ip):
    result = subprocess.run(["ping", "-c ", "1", ip], stdout=subprocess.PIPE)
    return result.returncode == 0


def ips():
    pinging_ips = []
    not_pinging_ips = []

    while True:
        user_choice = input("Do you want to enter an IP? (Yes/No): ").strip().lower()

        if user_choice == 'no' or user_choice == 'exit':
            break
        elif user_choice == 'yes':
            ip = input("Enter an IP address: ").strip()
            if is_valid_ip(ip):
                if is_pingable(ip):
                    pinging_ips.append(ip)
                    print("IP is pingable.")
                else:
                    not_pinging_ips.append(ip)
                    print("IP is not pingable.")
            else:
                print("Invalid IP format.")
        else:
            print("Invalid input. Please enter Yes or No.")

    with open("pinging_ips.txt", "w") as file:
        file.write("Pinging IPs:\n")
        for ip in pinging_ips:
            file.write(ip + '\n')

        file.write("\nNot Pinging IPs:\n")
        for ip in not_pinging_ips:
            file.write(ip + '\n')

    print("Pinging IPs:")
    for ip in pinging_ips:
        print(ip)

    print("\nNot Pinging IPs:")
    for ip in not_pinging_ips:
        print(ip)

ips()