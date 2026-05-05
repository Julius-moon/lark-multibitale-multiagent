"""Test create with correct field names."""

import sys
sys.path.insert(0, '.')

from src.auth.app_auth import Credentials, get_token
from lark_oapi import Client
from lark_oapi.api.bitable.v1 import *
from lark_oapi.core.token import RequestOptionBuilder

# Load credentials
creds = Credentials()
bot = creds.get("manager")
token = get_token("manager")

# Create client
client = Client.builder() \
    .app_id(bot.app_id) \
    .app_secret(bot.app_secret) \
    .enable_set_token(True) \
    .build()

# Create record with correct field names
base_token = "BDBawPzo4iKGUOkacc6cJc7mn8e"
table_id = "tblMbuT7TNyuizf0"

opt = RequestOptionBuilder().app_access_token(token).build()

create_request = CreateAppTableRecordRequest.builder() \
    .app_token(base_token) \
    .table_id(table_id) \
    .request_body(AppTableRecord.builder().fields({"标题": "测试任务", "状态": "待处理"}).build()) \
    .build()

create_response = client.bitable.v1.app_table_record.create(create_request, opt)
print(f"Create record response:")
print(f"  Success: {create_response.success()}")
print(f"  Code: {create_response.code}")
print(f"  Message: {create_response.msg}")
if create_response.data and create_response.data.record:
    print(f"  Record ID: {create_response.data.record.record_id}")