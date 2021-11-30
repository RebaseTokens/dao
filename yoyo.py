import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)
    

def commit(sc):
    print('Commit')
    subprocess.call(['/root/Desktop/dao/autocommit.sh'])
  
    s.enter(30, 1, commit, (s,))
    
s.enter(1, 1, commit, (s,))
s.run()
