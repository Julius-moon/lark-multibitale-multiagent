"""Check current permissions for the bot."""

import sys
sys.path.insert(0, '.')

from src.auth.app_auth import Credentials, get_token

# Load credentials
creds = Credentials()
bot = creds.get("manager")
print(f"Bot: {bot.name}")
print(f"app_id: {bot.app_id}")

# Get token and check permissions
token = get_token("manager")
print(f"app_access_token: {token[:20]}...")

# Check what scopes are available
print("\nPlease check the following in Feishu Open Platform:")
print("1. Go to https://open.feishu.cn/app/cli_a96674620b38dcc4")
print("2. Check '权限管理' -> '已添加权限'")
print("3. Ensure the following scopes are added:")
print("   - bitable:app")
print("   - base:record:create")
print("   - base:record:update")
print("   - base:record:delete")
print("\n4. After adding permissions, re-run: python src/main.py")