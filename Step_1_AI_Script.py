import time

print("AI System Starting... 🚀")

while True:
    print("Executing Step 1... AI is Running 🚀")
    
    # Perform a dummy background task to keep Railway active
    with open("keep_alive.txt", "w") as f:
        f.write("AI is still active...\n")
    
    time.sleep(600)  # Runs every 10 minutes

