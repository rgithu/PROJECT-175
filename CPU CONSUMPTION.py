
import matplotlib.pyplot as plt
import psutil as p

bg_app_dict = {}

count = 0

for process in p.process_iter():
    count += 1
    
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        
        print("Name : ", name, "CPU Usage : ", cpu_usage)
        
        bg_app_dict.update({name : cpu_usage})
        
        keymax = max(bg_app_dict, key = bg_app_dict.get)
        print(keymax)
        
        keymin = min(bg_app_dict, key = bg_app_dict.get)
        
        bg_app_list = [keymax, keymin]
        print(bg_app_list)
        
        bg_app = bg_app_dict.values()
        
        max_bg_app = max(bg_app)
        print(max_bg_app)
        
        min_bg_app = min(bg_app)
        print(min_bg_app)
        
        max_min_bg_app_list = [max_bg_app, min_bg_app]
        print(max_min_bg_app_list)
        
plt.figure(figsize = (15, 7))
plt.xlabel("Applications")
plt.ylabel("CPU Usage")
plt.bar(bg_app_list, max_min_bg_app_list, width = 0.5, color = ("Pink", "Blue"))
plt.show()