import psutil
from tkinter import *
from tkinter import ttk



def battery_sensor():
    """Calculates estimated battery life remaining, and returns percent, total time left, and power_plugged"""
    percent, secsleft, power_plugged = psutil.sensors_battery()

    hours_left = secsleft // 3600
    minutes_left = secsleft % 3600 // 60
    total_time_left = f"{hours_left}h{minutes_left} min"


    return percent, total_time_left, power_plugged

def ram_usage():
    """Unpacks, calculates and returns Total, Remaining, Percent, Used, free and total_and_usage RAM statistics"""
    total, remaining, percent_util, used, free = psutil.virtual_memory()
    total_in_mb = total // (1024 ** 2)
    remaining_in_mb = remaining // (1024**2)
    used_in_mb = used // (1024 ** 2)
    total_and_usage = f"{used_in_mb}MB / {total_in_mb}MB"

    return total_in_mb, remaining_in_mb, percent_util, used_in_mb, free, total_and_usage

def cpu_usage():
    """Returns CPU utilization as a float"""
    cpu_utilization = psutil.cpu_percent()
    return cpu_utilization

def disk_usage():
    """Calculates disk usage and returns percent, free and total_and_usage string in GB"""
    total, used, free, percent = psutil.disk_usage("/")
    total_in_gb = total / (1024 ** 3)
    used_in_gb = used / (1024 ** 3)
    free_in_gb = free / (1024 ** 3)
    total_and_usage = f"{used_in_gb:.2f}GB / {total_in_gb:.2f}GB"

    return percent, free_in_gb, total_and_usage


def update_label(label, function, index=None):
    """Updates the label each second, takes label name and function as args
    """
    
    updated_text = function()

    if index is not None:
        label.config(text=updated_text[index])
    else:
        label.config(text=updated_text)

    root.after(1000, update_label, label, function, index)



#Her bygger jeg appen

root = Tk()
root.title("System monitor v0.1")
frame = ttk.Frame(root, padding=10)
frame.grid()

#Lager labels og plaserer de i rammen med grid

#for CPU relaterte labels og buttons
cpu_description_label = ttk.Label(frame, text="CPU USAGE PERCENT:")
cpu_label = ttk.Label(frame, text="Loading..")
cpu_label.grid(column=0, row=1)
cpu_description_label.grid(column=0, row=0)

#for batteri relaterte labels og buttons
batterypercent_description_label = ttk.Label(frame, text="Battery percentage:").grid(column=1, row=0)
batterysecsleft_description_label = ttk.Label(frame, text="Estimated battery life:").grid(column=2, row=0)
batterypercent_label = ttk.Label(frame, text="")
batterysecsleft_label = ttk.Label(frame, text="")
batterypercent_label.grid(column=1, row=1)
batterysecsleft_label.grid(column=2, row=1)

#RAM relaterte Labels og buttons
ram_total_description_label = ttk.Label(frame, text="RAM usage:").grid(column=0, row=2)
ram_used_and_total_label = ttk.Label(frame, text="")
ram_used_and_total_label.grid(column=0, row=3)

#Disk relaterte labels of buttons
disk_total_description_label = ttk.Label(frame, text="Disk usage:").grid(column=1, row=2)
disk_used_and_total_label = ttk.Label(frame, text="")
disk_used_and_total_label.grid(column=1, row=3)


#caller update label funksjonen
update_label(cpu_label, cpu_usage)
update_label(batterypercent_label, battery_sensor, 0)
update_label(batterysecsleft_label, battery_sensor, 1)
update_label(ram_used_and_total_label, ram_usage, -1)
update_label(disk_used_and_total_label, disk_usage, -1)


root.mainloop()
