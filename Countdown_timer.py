import time

my_time = int(input("Enter the time in seconds: "))
for x in reversed(range(0, my_time)):
    seconds = x % 60
    minutes = int((x/60) % 60)
    print(f"00:{minutes:02}:{seconds:02}")
    print(x)
    time.sleep(1)

print("Saa imeisha")