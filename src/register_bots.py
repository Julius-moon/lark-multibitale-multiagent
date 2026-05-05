#!/usr/bin/env python3
"""
独立注册三个Bot的脚本
用法: python register_bots.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.config_loader import get_bot_config
from src.auth.app_auth import register_bot  # 假设队长有这个函数

def main():
    bots = ['manager', 'editor', 'reviewer']
    for bot_name in bots:
        bot = get_bot_config(bot_name)
        print(f"正在注册 {bot['name']} Bot...")
        # 调用队长写的注册函数（如果函数名不同，需要调整）
        try:
            register_bot(bot['app_id'], bot['app_secret'])
            print(f"✅ {bot['name']} 注册成功")
        except Exception as e:
            print(f"❌ {bot['name']} 注册失败: {e}")

if __name__ == "__main__":
    main()