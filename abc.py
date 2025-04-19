import easygui as gui
import subprocess

# 输入要ping的网站
website = gui.enterbox("请输入您要ping的网站")

if website:  # 确保用户输入不为空
    # 执行ping命令并捕获输出
    result = subprocess.getoutput(f"ping {website}")
    # 显示结果
    gui.msgbox(result)
else:
    gui.msgbox("未输入内容！")