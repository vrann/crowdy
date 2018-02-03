import elasticsearch as es
import os

from .project import Project

ELASTIC_HOST = os.environ['ELASTIC_HOST']
PROJECTS_INDEX = 'projects'
PROJECTS_DOC_TYPE = 'project'


class Model:
    """
    Handles general data access and manipulation
    """
    def __init__(self):
        self.es = es.Elasticsearch([{'host': ELASTIC_HOST}])

    def store_project(self, project: Project):
        """
        Stores a passed project in db.
        :param project:  Project
        :return: None
        """
        self.es.create(
            index=PROJECTS_INDEX,
            doc_type=PROJECTS_DOC_TYPE,
            id=project.id,
            body=project.as_json
        )

    def get_project_json(self, project_id) -> str:
        """
        Gets a project as json from passed project id.
        :param project_id: uuid
        :return: str
        """
        return self.es.get(
            index=PROJECTS_INDEX,
            doc_type=PROJECTS_DOC_TYPE,
            id=project_id
        )

    def get_contributor_json(self, contrib_id):
        pass
