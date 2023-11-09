import schedule
import time

# Define a function to be executed
def sample_task():
    print("This task will be done at regular intervals.")

# Schedule the task to run every 1 hour
schedule.every().hour.do(sample_task)

# Execute the scheduled task indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)