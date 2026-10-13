from datetime import datetime
from pathlib import Path
from multiprocessing import Process
import time

momento = datetime.now()
print(momento)

p_log_dir = Path("logs")
p_log = p_log_dir /"log.txt"



try:
    Path.mkdir(p_log_dir, parents=True)
    with open(p_log, "a") as log:
        log.write(f"<{datetime.now()}> - Carpetas Creadas\n")
except FileExistsError:
    with open(p_log, "a") as log:
        log.write(f"<{datetime.now()}> - Carpetas ya existe\n")
finally:
    with open(p_log, "a") as log:       
        log.write(f"<{datetime.now()}> - Programa arranca\n")
with open(p_log, "a") as log:
    while True:
        time.sleep(1)
        log.write(f"<{datetime.now()}> - Procesando Información\n")