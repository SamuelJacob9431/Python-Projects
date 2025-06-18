import time
from datetime import datetime

# Greeting based on current hour
def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good Morning! Don't forget to read the Newspaper."
    elif 12 <= hour < 17:
        return "Good Afternoon! Just in time for Siesta."
    elif 17 <= hour < 21:
        return "Good Evening! Tea, perhaps?"
    else:
        return "Good Night! Hope you have pleasant dreams."

def main():
    now = datetime.now()
    hour = now.hour
    formatted_time = now.strftime("%H:%M")

    greeting = get_greeting(hour)
    print(f"\n{greeting}\nCurrent Time: {formatted_time}\n")

    print("Stopwatch Starting! Press Ctrl+C to stop.\n")

    start_time = time.time()
    try:
        while True:
            elapsed = int(time.time() - start_time)
            mins, secs = divmod(elapsed, 60)
            hrs, mins = divmod(mins, 60)
            print(f"\r{hrs:02}:{mins:02}:{secs:02}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nStopwatch stopped.")

if __name__ == "__main__":
    main()


