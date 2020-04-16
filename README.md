# Shorten_URL

## Using Python flask and dynamoDB making shorten URL service on AWS lambda

Before you can access DynamoDB programmatically or through the AWS CLI, you must configure your credentials to enable authorization for your applications.

[Configure Your Credentials](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.DynamoWebService.html#SettingUp.DynamoWebService.ConfigureCredentials)

### Create a Table

You can test if you connect your AWS account to CreateTable using following command.

`$ python3 ShortenCreateTable.py` 

And put item into your table!

`$ python3 ShortenItemOps.py`

### Set virtual environment

`$ pipenv install zappa boto3 flask`
`$ pipenv shell`

### Deploy by zappa

zappa is a service help us deploy our application on aws .

`$ zappa init`

After serverl questions you will get zappa_settings.json.

```
{
    "dev": {
        "app_function": "app.app",
        "aws_region": "us-east-1",
        "profile_name": "default",
        "project_name": "shorten",
        "runtime": "python3.6",
        "s3_bucket": "zappa-i3tc588p0"
    }
}
```

If it's ok feel free to deploy your application.

`$ zappa deploy dev`

If nothing is wrong , you will get aws endpoint to your application.
Enhoy:)