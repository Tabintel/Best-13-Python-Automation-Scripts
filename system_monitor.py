import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)

# Get memory usage
memory_usage = psutil.virtual_memory().percent

# Print system metrics
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")