from flask import Flask, render_template,request,redirect
import string
from math import floor
from urllib.parse import urlparse
str_encode=str.encode
from string import ascii_lowercase
from string import ascii_uppercase
import base64
import boto3
from boto3.dynamodb.conditions import Key, Attr
#import json
import decimal


app = Flask(__name__)
#host = 'http://localhost:5000/'
def toBase62(num,b=62):
    if b<=0 or b>62:
        return 0
    base=string.digits + ascii_lowercase +ascii_uppercase
    r=num%b
    res=base[r]
    q=floor(num/b)
    while q:
        r = q % b
        q = floor(q/b)
        res=base[int(r)]+res
    return res
def toBase10(num,b=62):
    base= string.digits+ascii_lowercase+ascii_uppercase
    limit = len(num)
    res=0
    for i in range(limit):
        res=b*res+base.find(num[i])
    return res

@app.route('/',methods=['GET', 'POST'])
def index():
    
    short_id=0
    if request.method == 'POST':
        original_url =request.form.get('url')
        if urlparse(original_url).scheme == '':
            url = 'http://'+original_url
        else:
            url = original_url
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('Shorten')
        response = table.query(
            Limit=1,
            ScanIndexForward=False,
            KeyConditionExpression=Key('encode').eq('base10')
        )
        for i in response['Items']:
            short_id=int(i['id'])
        response =table.put_item(
            Item={
                'encode':'base10',
                'id':short_id+1,
                'url':url,
                }
        )
        encoded_string=toBase62(short_id+1)
        return render_template('index.html',short_url=request.base_url+encoded_string)
        
    return render_template('index.html')
@app.route('/<short_url>')
def redirect_short_url(short_url):
    decoded = toBase10(short_url)
    url = request.base_url # fallback if no URL　is found
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Shorten')
    response = table.query(
        KeyConditionExpression=Key('encode').eq('base10') & Key('id').eq(decoded)
    )
    for i in response['Items']:
        url=i['url']
    return redirect(url)
    
if __name__=="__main__":
    app.run(debug=True)
