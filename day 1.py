# Program untuk perkenalan dasar Python


def greeting():
    print("Selamat datang di program 30 day of code!")
def get_name():
    name = input("Siapa namamu? =  ")
    return name

def greet_user(name):
    print("Halo,", name, "! Senang bertemu denganmu.")

def main():
    greeting()  
    name = get_name()  
    greet_user(name)  

if __name__ == "__main__":
    main()
