# rc.py
import random
import os
def run_coin():
    ran_con1 = random.randint(2, 3)
    ran_con2 = random.randint(2, 3)
    ran_con3 = random.randint(2, 3)
    return ran_con1 + ran_con2 + ran_con3

fdata = ""
def set_fdata_mem():
    global fdata
    fdata = open("yixiang.txt", "r", encoding="utf-8")
set_fdata_mem()

def rr():
    lis1 = []
    for _ in range(3):
        result = run_coin()
        if result % 2 == 0:
            # print(result,"yin--")
            # print("yin--")
            # lis1 = lis1 + str(result)+"yin--"
            # lis1 = lis1 + str(result) + "yin--"
            # lis1.append("阴--")
            lis1.append("阴")
        else:
            # print(result,"yang—")
            # print("yang—")
            # lis1 = lis1 + str(result)+"yang--"
            # lis1 = lis1 + str(result) + "yang--"
            # lis1.append("阳—")
            lis1.append("阳")
    return list(reversed(lis1))
def get_xy():
    gsx = ""
    for i in rr():
        # print(i)
        gsx = gsx+str(i)
        if gsx == "阳阳阳":
            xy = "乾"
        if gsx == "阴阴阴":
            xy = "坤"
        if gsx == "阴阴阳":
            xy = "震"
        if gsx == "阳阳阴":
            xy = "巽"
        if gsx == "阴阳阴":
            xy = "坎"
        if gsx == "阳阴阳":
            xy = "离"
        if gsx == "阳阴阴":
            xy = "艮"
        if gsx == "阴阳阳":
            xy = "兑"
    return xy
def get_sy():
    gss = ""
    for i in rr():
        # print(i)
        gss = gss+str(i)
        if gss == "阳阳阳":
            sy = "乾"
        if gss == "阴阴阴":
            sy = "坤"
        if gss == "阴阴阳":
            sy = "震"
        if gss == "阳阳阴":
            sy = "巽"
        if gss == "阴阳阴":
            sy = "坎"
        if gss == "阳阴阳":
            sy = "离"
        if gss == "阳阴阴":
            sy = "艮"
        if gss == "阴阳阳":
            sy = "兑"
    return sy
def get_yx():
    yixiang =  str(get_sy()) + "上" + str(get_xy()) + "下"
    return yixiang
# print(get_yx())
def get_tl():
    yx = str(get_yx())
    global fdata
    fdata.seek(0)
    for line in fdata.readlines():
        if yx in line:
            return line
# print(get_tl())
# print(tarline)
def get_tnum():
    tnum = str(get_tl()).split("-")[0]
    return tnum
# print(get_tnum())

def find_block(bpath,bstart,bend):
    found = False
    btarget = []
    with open(bpath,"r",encoding="utf-8") as f:
        for line in f.readlines():
            if bstart in line:
                found = True
                continue
            if found and bend in line:
                break
            if found:
                btarget.append(line)
    return  '\n'.join(btarget)

def rc_r():
    b_content = find_block("req_r_new.txt","###"+get_tnum()+"###","###end###")
    return b_content

# print(rc_r())

##