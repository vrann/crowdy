"""
Contains contributor class and associated code.
"""
import uuid
import json


class Contributor:
    """
    Contains information about a specific contributor.
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', uuid.uuid4().int)
        self.name = kwargs.get('name', '')
        self.projects = kwargs.get('projects', {})
        for k, v in kwargs:
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                raise ValueError('Unexpected kwd received: {}'.format(k))

    @property
    def as_json(self):
        pass
