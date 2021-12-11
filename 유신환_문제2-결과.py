import os
import sys
os.chdir('/Users/shinhwanyoo/유신환_sw프로그래밍입문_메인과제2' +
         os.path.join('')) 

with open("/Users/shinhwanyoo/problem2-2.txt","r") as file:
    lines = file.readlines()
    lines.insert(0, "")
    for i in range(1, len(lines)):
        print(i,":",lines[i])
        
sys.stdout = open("problem2-2-60083097.txt","w")

for i in range(1, len(lines)):
    print(i,":",lines[i])

sys.stdout.close()