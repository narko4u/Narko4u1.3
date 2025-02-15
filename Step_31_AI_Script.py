import time
import subprocess

def main():
    print("Executing Step 31 AI Task... 🚀")
    # AI Script for Step 31
    print("Executing Step 31...")

    # Print a message to indicate restart countdown
    print("All steps executed. Restarting sequence in 10 minutes... 🔄")
    
    # Wait for 10 minutes before restarting
    time.sleep(600)  # 600 seconds = 10 minutes

    # Restart the process by executing Step 1 again
    print("Restarting the sequence now...")
    subprocess.run(["python", "Step_1_AI_Script.py"])

if __name__ == "__main__":
    main()
