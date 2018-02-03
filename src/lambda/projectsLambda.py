import json
def my_handler(event, context):
    data = json.loads(event['body'])
    message = 'Hello {} {}!'.format(data['first_name'],
                                    data['last_name'])

    return {
      "statusCode": 200,
      "body": json.dumps({'input': event,
                 'message' : message})
    };