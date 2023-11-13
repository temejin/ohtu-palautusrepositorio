class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def prettyPrint(self, xs):
        return "\n".join([f"- {x}" for x in xs])

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n{self.prettyPrint(self.authors)}\n"
            f"\nDependencies:\n{self.prettyPrint(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n{self.prettyPrint(self.dev_dependencies)}"
        )
