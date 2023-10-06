# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import pytest
import allure

# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    json_dir_path = 'allure-results'
    html_dir_path = './Report/html'
    pytest.main(['-sv','./TestCase/test_live_class.py','--clean-alluredir','--alluredir',json_dir_path])
    os.system(r'allure generate ./allure-results -o ./Report/html -c')
    # cmd = 'allure generate{{}}-o{{}}-c'.format(json_dir_path,html_dir_path)
    # os.system(cmd)
    # allure open ./Report/html
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
