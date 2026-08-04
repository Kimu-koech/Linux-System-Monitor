import psutil
def get_process_count():
    return len(psutil.pids())


def get_process_names(limit=10):
    names=[]
    for process in psutil.process_iter(["name"]):
        if process.info["name"]:
            names.append(process.info["name"])
    return names[:limit]

def get_user_processes():
    count =0
    for process in psutil.process_iter(["username"]):
        if process.info["username"]:
            count +=1
    return  count





