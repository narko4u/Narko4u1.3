import time
import os
import subprocess

def step_31():
    print("Executing Step 31 AI Task... 🚀")

    # Ensure only ONE process is running at a time
    try:
        process_count = int(subprocess.getoutput("ps aux | grep '[s]tep_31' | wc -l"))
        if process_count > 1:
            print("Step 31 is already running. Exiting to prevent overload.")
            return
    except Exception as e:
        print(f"Error checking running processes: {e}")

    # Perform Step 31 Tasks
    try:
        # Example Task - Add your specific function here
        print("Executing Step 31...")
        time.sleep(5)  # Simulate a task (Adjust as needed)
    except Exception as e:
        print(f"Error in Step 31: {e}")

    # Ensure the script waits before restarting
    print("All steps executed. Restarting sequence in 10 minutes... 🔄")
    time.sleep(600)  # 10-minute delay before restarting

    # Restart the script properly
    print("Restarting the sequence now...")
    os.system("python main.py")  # Change "main.py" to your script's name

# Run Step 31
if __name__ == "__main__":
    step_31()
