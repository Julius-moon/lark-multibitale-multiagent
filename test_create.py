"""Check table schema to understand required fields."""

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

# Get table fields
base_token = "BDBawPzo4iKGUOkacc6cJc7mn8e"
table_id = "tblMbuT7TNyuizf0"

opt = RequestOptionBuilder().app_access_token(token).build()
request = ListAppTableFieldRequest.builder() \
    .app_token(base_token) \
    .table_id(table_id) \
    .build()

response = client.bitable.v1.app_table_field.list(request, opt)
print(f"Fields response:")
print(f"  Success: {response.success()}")
print(f"  Code: {response.code}")
print(f"  Message: {response.msg}")

if response.data and response.data.items:
    print(f"\nTable fields:")
    for field in response.data.items:
        print(f"  - {field.field_name} ({field.type})")

# Also try creating a record with minimal fields
print("\n\nTrying to create a test record...")
create_request = CreateAppTableRecordRequest.builder() \
    .app_token(base_token) \
    .table_id(table_id) \
    .request_body(AppTableRecord.builder().fields({"任务标题": "测试任务"}).build()) \
    .build()

create_response = client.bitable.v1.app_table_record.create(create_request, opt)
print(f"Create record response:")
print(f"  Success: {create_response.success()}")
print(f"  Code: {create_response.code}")
print(f"  Message: {create_response.msg}")
if create_response.data:
    print(f"  Record ID: {create_response.data.record.record_id}")