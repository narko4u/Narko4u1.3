import time
import importlib

print("AI System Starting... 🚀")

steps = 31  # Total number of steps

while True:
    for i in range(1, steps + 1):
        script_name = f"Step_{i}_AI_Script"
        try:
            print(f"Executing {script_name}... 🚀")
            module = importlib.import_module(script_name)
            if hasattr(module, 'main'):
                module.main()  # Run script if it has a main function
            else:
                print(f"{script_name} does not have a main() function, skipping.")
        except Exception as e:
            print(f"Error executing {script_name}: {e}")

    print("All steps executed. Restarting sequence in 10 minutes... 🔄")
    time.sleep(600)  # Wait 10 minutes before running all steps again



