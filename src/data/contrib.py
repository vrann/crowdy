"""
Contains contributor class and associated code.
"""


class Contributor:
    """
    Contains information about a specific contributor.
    """

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.projects = kwargs.get('projects', {})
