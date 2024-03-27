import json
import os

def update_settings(user_lst):
    with open('settings.json', 'r', encoding='utf8') as f:
        settings = json.load(f)
        settings['user_lst'] = user_lst
    with open('settings.json', 'w', encoding='utf8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)

def run_main():
    os.system('python main.py')

if __name__ == '__main__':
    user_lst = input("请输入要下载的用户名（多个用户用逗号分隔）: ")
    update_settings(user_lst)
    run_main()
