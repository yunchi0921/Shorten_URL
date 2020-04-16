
#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
# 
#  http://aws.amazon.com/apache2.0/
# 
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Shorten')

encode= "base10"
id = 0


response = table.put_item(
   Item={
        'encode': encode,
        'id': id,
        'url': "https://docs.aws.amazon.com/zh_tw/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html"
        }
)

print("PutItem succeeded:")
print(json.dumps(response, indent=4))

