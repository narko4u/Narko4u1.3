import time
import os

print("AI System Starting... 🚀")

steps = 31  # Total number of steps

while True:
    for i in range(1, steps + 1):
        script_name = f"Step_{i}_AI_Script.py"
        if os.path.exists(script_name):
            print(f"Executing {script_name}... 🚀")
            os.system(f"python {script_name}")  # Runs each step
        else:
            print(f"Skipping {script_name} (not found).")

    print("All steps executed. Restarting sequence in 10 minutes... 🔄")
    time.sleep(600)  # Wait 10 minutes before running all steps again


