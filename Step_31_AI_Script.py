import time
import subprocess
import sys

def main():
    print("Executing Step 31 AI Task... 🚀")
    # AI Script for Step 31
    print("Executing Step 31...")

    # Print a message to indicate restart countdown
    print("All steps executed. Restarting sequence in 10 minutes... 🔄")

    # Wait for 10 minutes (600 seconds)
    time.sleep(600)

    # Restart the entire script cleanly without forking too many processes
    print("Restarting the sequence now...")
    subprocess.run([sys.executable, "Step_1_AI_Script.py"])

if __name__ == "__main__":
    main()
