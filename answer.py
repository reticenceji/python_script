import requests
import threading
import os
import os.path

#非常简单的爬虫，把所get到的内容保存下来
def pa(num,dir):
    print(num,"start")
    with open(dir+"/"+dir+"_{}.pdf".format(num),"wb") as fileobj:
        #这个网站URL特征，请不要拿这个网站做实验！
        r = requests.get("https://www.db-book.com/db6/practice-exer-dir/{}s.pdf".format(num))
        fileobj.write(r.content)
    print(num,"done")

dir = "Answers"
if not os.path.exists(dir):
    os.mkdir(dir)
threads = []
#多线程爬取
for i in range(26):
    t = threading.Thread(target=pa,args=(i+1,dir))
    threads.append(t)
    t.start()
#等待所有的线程结束
for t in threads:
    t.join()
print("All done")
