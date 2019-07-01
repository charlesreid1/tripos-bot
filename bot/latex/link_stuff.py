import subprocess
import glob

last = 256
maxx = 365

for i in range(maxx-last):
    source = "%03d.jpg"%(i+1)
    target = "%03d.jpg"%(last+i+1)
    print(" ".join(['ln','-fs',source,target]))
    subprocess.call(['ln','-fs',source,target])

