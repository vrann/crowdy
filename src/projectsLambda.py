import json

from data.project import Project
from data.contrib import Contributor
from data.model import Model
from deco import aws_lambda


# ---------------------------------------------------------------------
# Project lambdas


@aws_lambda
def create_project(event, context):
    """
    Creates new project from passed information.

    Expected data values(and their defaults):
        id(generates new uuid4 if none passed)
        name('')
        git_link('')
        contributors({})
        hours_goal(0)
        due_date(None)
        pledges({})

    :param event:
    :param context:
    :return: None
    """
    data = json.loads(event['body'])
    #
    # gives Project class the responsibility for handling
    # data validation for the new Project, rather than
    # duplicating that code here.
    model.store_project(Project(**data))


@aws_lambda
def delete_project(event, context):
    """
    Deletes existing project of passed id.
    :param event:
    :param context:
    :return:
    """
    data = json.loads(event['body'])
    project_id = data['id']
    model.del_project(project_id)


@aws_lambda
def get_project_by_id(event, context):
    """
    Retrieves project of passed id.
    :param event:
    :param context:
    :return:
    """
    data = json.loads(event['body'])
    project_id = data['id']
    return {
        'statusCode': 200,
        'body': json.dumps(model.get_project_json(project_id))
    }


# ---------------------------------------------------------------------
# Contributor lambdas


@aws_lambda
def add_contributor(event, context):
    """
    Adds a new contributor to the db.

    Expected kwargs (defaults):
       id (generates new uuid)
       name ('')
       projects ({})
    """
    data = json.loads(event['body'])
    # create and store contributor created from passed data
    model.store_contributor(Contributor(**data))


@aws_lambda
def get_contributor(event, context):
    """
    Gets contributor identified by id passed in data.
    :param event:
    :param context:
    :return: json representation of contributor data.
    """
    data = json.loads(event['body'])
    contrib_id = data['id']
    return {
        'statusCode': 200,
        'body': json.dumps(model.get_contributor_json(contrib_id))
    }


@aws_lambda
def delete_contributor(event, context):
    """
    Deletes existing contributor of passed id.
    :param event:
    :param context:
    :return:
    """
    data = json.loads(event['body'])
    contrib_id = data['id']
    model.del_project(contrib_id)


@aws_lambda
def pledge_hours(event, context):
    """
    Adds passed number of hours as a commitment of passed contributor,
    to passed project.
    :param event:
    :param context:
    :return:
    """
    data = json.loads(event['body'])
    contrib_id = data['contrib_id']
    project_id = data['project_id']
    n_hours = data['hours']
    model.add_pledged_hours(contrib_id, project_id, n_hours)


model = Model()
