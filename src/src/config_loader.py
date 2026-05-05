"""
三Bot配置加载器
从 config.yaml 读取三个独立Bot的凭证
"""
import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

def get_bot_config(bot_name):
    """根据 bot 名称（manager/editor/reviewer）返回其 app_id 和 app_secret"""
    config = load_config()
    bot = config['bots'][bot_name]
    return {
        'app_id': bot['app_id'],
        'app_secret': bot['app_secret'],
        'name': bot['name']
    }

def get_lark_config():
    config = load_config()
    return config['lark']

def get_llm_config():
    config = load_config()
    return config['llm']

def get_workflow_config():
    config = load_config()
    return config['workflow']