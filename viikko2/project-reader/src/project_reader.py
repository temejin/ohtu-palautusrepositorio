from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_dict = tomli.loads(content)
        project_dict = content_dict['tool']['poetry']
        name = project_dict['name']
        desc = project_dict['description']
        dependencies = project_dict['dependencies']
        dev_dependencies = project_dict['group']['dev']['dependencies']
        authors = project_dict['authors']
        license = project_dict['license']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, dependencies, dev_dependencies, license, authors)
