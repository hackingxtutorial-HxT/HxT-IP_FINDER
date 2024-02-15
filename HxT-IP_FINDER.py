print ("\033[93m")
import socket

def get_ip_address(url):
    ip_address = socket.gethostbyname(url)
    return ip_address

def main():
    while True:
        url = input("ENTER THE URL: ")

        ip_address = get_ip_address(url)
        print(" ")
        print ("\033[96mCODED BY : hacking_x_tutorial\033[0m")
        print(" ")
        print("\033[96mSOCIAL MEDIA : https://sites.google.com/view/hachingxtutorial/home")
        print(" ")
        print("\033[91mDISCLAIMER - THIS TOOL IS ILLEGAL & IT'S ONLY FOR EDUCATION PURPOSE !  USE  IT AT YOUR OWN RISK , I AM NOT RESPONSIBLE FOR YOUR ACTION !\033[0m")
        print(" ")
        print("\033[97mIP Address:", ip_address)
        print(" ")
        next_url = input("DO YOU WANT ENTER ANOTHER URL? (y/n): ")
        if next_url.lower() != "y":
            break

if __name__ == "__main__":
    main()
