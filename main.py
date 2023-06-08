import datetime

def ppp(data):
    f = data.split("\n")
    r = len(f)
    for i in range(0,4*r-4,4):
        f[i:i+1] = f[i].split("*")
    f.pop()
    return f

def rewrite(data,r):
    f = open('server.txt',"w")
    f.write("")
    f.close()
    for i in range(0,r,4): 
        f = open('server.txt',"a")
        reg = f"{data[i]}*{data[i+1]}*{data[i+2]}*{data[i+3]}\n"
        f.write(reg)
    f.close()

def ppp2(data):
    f = data.split("\n")
    r = len(f)
    for i in range(0,2*r-2,2):
        f[i:i+1] = f[i].split("*")
    return f

def find(us):
    f = open("workers.txt","r")
    f2 = f.read()
    f2 = ppp2(f2)
    for i in range(len(f2)):
        if f2[i]==us:
            return f2[i-1]


print("       Login/out\n")
f = open("server.txt","w")
f.close()
while True:
    username = input("Enter your ID: ")
    name = find(username)
    time = datetime.datetime.now()
    year = time.year
    month =  time.month
    day = time.day
    second =  time.second
    minute = time.minute
    hour = time.hour
    f = open("server.txt","r")
    f2 = f.read()
    f.close()
    f2 = ppp(f2)
    r = len(f2)
    a = False
    for i in range(r):
        if f2[i]==username:
            thour = hour - int(f2[i+1])
            tminute = minute - int(f2[i+2])
            tsecond = second - int(f2[i+3])
            if tminute < 0 :
                thour -= 1
                tminute += 60
            if tsecond < 0 :
                tminute -= 1
                tsecond += 60
            f2.pop(i)
            f2.pop(i)
            f2.pop(i)
            f2.pop(i)
            r = len(f2)
            rewrite(f2, r)
            f = open(f"{name}.txt","a")
            reg = f"Logged out: {hour}:{minute}:{second}\nWorked for {thour}:{tminute}:{tsecond}\n"
            f.write(reg)
            f.close()
            a = True
            break
    if a==False:
        f = open(f"{name}.txt","a")
        reg = f"On {year}/{month}/{day}:\nLogged in: {hour}:{minute}:{second}\n"
        f.write(reg)
        f.close()
        f = open("server.txt","a")
        reg = f"{username}*{hour}*{minute}*{second}\n"
        f.write(reg)
        f.close()
