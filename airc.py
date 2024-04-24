import random
import os

def run_coin():
    # 生成一个1到6的随机整数，模拟掷骰子
    return random.randint(1, 6)

def generate_gua():
    """
    生成一个易经卦象
    """
    gua_list = []
    for _ in range(3):
        result = run_coin()
        if result % 2 == 0:
            gua_list.append("阴")
        else:
            gua_list.append("阳")
    return list(reversed(gua_list))

def get_gua_name(gua_list):
    """
    根据卦象列表返回对应的卦名
    """
    gsx = "".join(gua_list)
    if gsx == "阳阳阳":
        return "乾"
    elif gsx == "阴阴阴":
        return "坤"
    elif gsx == "阴阴阳":
        return "震"
    elif gsx == "阳阳阴":
        return "巽"
    elif gsx == "阴阳阴":
        return "坎"
    elif gsx == "阳阴阳":
        return "离"
    elif gsx == "阳阴阴":
        return "艮"
    elif gsx == "阴阳阳":
        return "兑"

def get_xy():
    return get_gua_name(generate_gua())

def get_sy():
    return get_gua_name(generate_gua())

def get_yx():
    return str(get_sy()) + "上" + str(get_xy()) + "下"

def find_block_in_file(bpath, bstart, bend):
    """
    在文件中查找指定的块
    """
    try:
        with open(bpath, "r", encoding="utf-8") as file:
            contents = file.read()
            start_index = contents.find(bstart)
            if start_index != -1:
                end_index = contents.find(bend, start_index + len(bstart))
                if end_index != -1:
                    return contents[start_index:end_index + len(bend)]
    except FileNotFoundError:
        print(f"文件 {bpath} 未找到。")
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
    return ""

def rc_r():
    tnum = get_tnum()  # 假设 get_tnum() 是一个有效的函数
    block_start = f"###{tnum}###"
    block_end = "###end###"
    return find_block_in_file("req_r_new.txt", block_start, block_end)

# 注意：由于原代码中并未定义 get_tnum() 和一些其他函数，这里假设这些函数已经被合适地实现了。
# 以下函数的实现需要根据实际情况进行补充。

if __name__ == "__main__":
    # 主程序入口
    print(rc_r())
