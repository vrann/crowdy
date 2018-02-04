import elasticsearch as es
import os

from .project import Project
from .contrib import Contributor

ELASTIC_HOST = os.environ['ELASTIC_HOST']
PROJECTS_INDEX = 'projects'
PROJECTS_DOC_TYPE = 'project'
CONTRIB_INDEX = 'contributors'
CONTRIB_DOC_TYPE = 'contrib'


class Model:
    """
    Handles general data access and manipulation
    """
    def __init__(self):
        self.es = es.Elasticsearch([{'host': ELASTIC_HOST}])

    # -----------------------------------------------------------------
    # PROJECT METHODS

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

    def del_project(self, project_id):
        """
        Deletes project identified by passed id.
        :param project_id: uuid
        :return:
        """
        self.es.delete(
            index=PROJECTS_INDEX,
            doc_type=PROJECTS_DOC_TYPE,
            id=project_id
        )

    # -----------------------------------------------------------------
    # CONTRIBUTOR METHODS

    def store_contributor(self, contrib: 'Contributor'):
        """
        Stores passed contributor in db.
        :param contrib: Contributor
        :return: None
        """
        self.es.create(
            index=CONTRIB_INDEX,
            doc_type=CONTRIB_DOC_TYPE,
            id=contrib.id,
            body=contrib.as_json
        )

    def get_contributor_json(self, contrib_id):
        pass
