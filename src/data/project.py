"""
Contains Project class and associated code
"""

import json
import uuid


class Project:
    """
    A project with time
    """

    def __init__(self, project_id=None, **kwargs):
        self.id = project_id or uuid.uuid4().int
        self.name = ''
        self.git_link = ''
        self.contributors = {}
        self.hours_goal = 0
        self.created_date = None
        self.due_date = None
        self.technologies = set()
        self.pledges = {}

        # initialize fields from passed kwargs
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                raise ValueError('Unexpected kwd: {}'.format(k))

    @property
    def as_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'name': self.name,
            'git_link': self.git_link,
            'contrib': self.contributors,
            'created_date': self.created_date,
            'due_date': self.due_date,
            'hours_goal': self.hours_goal,
            'technologies': self.technologies,
            'pledges': self.pledges,
        })

    @classmethod
    def from_json(cls, json_s: str) -> 'Project':
        """
        Creates a project from passed json str.

        :param json_s: str
        :return: Project
        :raises ValueError if invalid data passed.
        """
        return cls(**json.loads(json_s))
