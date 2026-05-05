"""Test script to debug Base API permissions."""

import sys
sys.path.insert(0, '.')

from src.auth.app_auth import Credentials, get_token
from lark_oapi import Client
from lark_oapi.api.bitable.v1 import *
from lark_oapi.core.token import RequestOptionBuilder

# Load credentials
creds = Credentials()
bot = creds.get("manager")
print(f"Bot: {bot.name}")
print(f"app_id: {bot.app_id}")

# Get token
token = get_token("manager")
print(f"app_access_token: {token[:20]}...")

# Create client
client = Client.builder() \
    .app_id(bot.app_id) \
    .app_secret(bot.app_secret) \
    .enable_set_token(True) \
    .build()

# Test API call
base_token = "BDBawPzo4iKGUOkacc6cJc7mn8e"
table_id = "tblMbuT7TNyuizf0"

print(f"\nTesting Base API with:")
print(f"  base_token: {base_token}")
print(f"  table_id: {table_id}")

# List records (read operation)
opt = RequestOptionBuilder().app_access_token(token).build()
request = ListAppTableRecordRequest.builder() \
    .app_token(base_token) \
    .table_id(table_id) \
    .page_size(5) \
    .build()

response = client.bitable.v1.app_table_record.list(request, opt)
print(f"\nList records response:")
print(f"  Success: {response.success()}")
print(f"  Code: {response.code}")
print(f"  Message: {response.msg}")

if response.data:
    print(f"  Items count: {len(response.data.items) if response.data.items else 0}")