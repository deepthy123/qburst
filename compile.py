import subprocess
def compare(out,out1):
    r=open(out)
    r1=open(out1)
    r_line=r.readline()
    r1_line=r1.readline()
    while r_line!='' or r1_line!='':
       r_line=r_line.strip()
       r1_line=r1_line.strip()
       if(r_line!=r1_line):
           success=False
           break
       r_line=r.readline()
       r1_line=r1.readline()
    r.close()
    r1.close()
    return success

def compile(name,inp,out):
    f=open(inp,"r")
    f1=open("tout.txt","w")
    subprocess.call(["gcc", name,"-o","t"])
    subprocess.call(["./h"],stdin=f,stdout=f1)
    f.close()
    f1.close()
    return compare("tout.txt",out)
    

##def question():
##   this function to be added later   