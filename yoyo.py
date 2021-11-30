import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)

def wonder(sc):
    print('Wonderland - TIME')
    with open('/root/Desktop/dao/time.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')
    

    with open('/root/Desktop/dao/time.json', 'w') as file:
      file.write(filedata)
  
    s.enter(1, 1, commit, (s,))
    

def commit(sc):
    print('Commit')
    subprocess.call(['/root/Desktop/dao/autocommit.sh'])
  
    s.enter(30, 1, wonder, (s,))
    
s.enter(1, 1, wonder, (s,))
s.run()
