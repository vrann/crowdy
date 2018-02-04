import json

from data.project import Project
from data.model import Model


def my_handler(event, context):
    data = json.loads(event['body'])
    message = 'Hello {} {}!'.format(data['first_name'],
                                    data['last_name'])

    return {
      "statusCode": 200,
      "body": json.dumps({'input': event,
                 'message' : message})
    };


def create_project(event, context):
    """
    Creates new project from passed information.
    :param event:
    :param context:
    :return: None
    """
    data = json.loads(event['body'])
    try:
        # Expected data values(and their defaults):
        #     id(generates new uuid4 if none passed)
        #     name('')
        #     git_link('')
        #     contributors({})
        #     hours_goal(0)
        #     due_date(None)
        #     pledges({})
        #
        # gives Project class the responsibility for handling
        # data validation for the new Project, rather than
        # duplicating that code here.
        model.store_project(Project(**data))
    except ValueError as e:
        print(e)
        return {
            'statusCode': 400,
            'body': json.dumps({'input': event, 'message': str(e)})
        }
    else:
        return {
            "statusCode": 200,
            'body': json.dumps({'input': event})
        }


def delete_project(event, context):
    """
    Deletes existing project of passed id.
    :param event:
    :param context:
    :return:
    """


def get_project_by_id(event, context):
    """
    Retrieves project of passed id.
    :param event:
    :param context:
    :return:
    """
    data = json.loads(event['body'])
    project_id = data['id']
    try:
        return {
            'statusCode': 200,
            'body': json.dumps(model.get_project_json(project_id))
        }
    except KeyError as e:
        return {
            'statusCode': 404,
            'body': json.dumps({'input': event, 'message': str(e)})
        }


model = Model()
