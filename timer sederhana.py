import time

def waktu(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("waktu habis!")

if __name__ == "__main__":
    try:
        total_time = int(input("masukkan waktu detik: "))
        if total_time > 0:
            waktu(total_time)
        else:
            print("pastikan inputan waktu lebih dari nol .")
    except ValueError:
        print("input tidak valid,jangan masukkan huruf.")
