import psutil
import time

# 获取名为"GRA5.exe"的进程
p = None
for proc in psutil.process_iter():
    if proc.name() == "GTA.exe":
        p = proc
        break

if p is None:
    print("未找到名为'GRA5.exe'的进程")
else:
    # 暂停进程
    p.suspend()
    print("进程已暂停")

    # 等待5秒钟
    time.sleep(5)

    # 恢复进程
    p.resume()
    print("进程已恢复")
