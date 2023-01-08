from common.base import sesion_factory
from Project import Project
from ProjectManager import ProjectManager


def populate_datebase():
    session = sesion_factory()

    ali = ProjectManager("Ali Dönmez")
    veli = ProjectManager("Veli Susmaz")

    iski = Project("İski E-Dönüşüm", "İski E Dönüşüm Sistemi", ali)

    catap = Project("Çanakkale Tarihi Eserler", "Çanakkale Tarihi Eserler Komutanlığı", veli)

    session.add(iski)
    session.add(catap)
    session.commit()
    session.close()


def query_project():
    session = sesion_factory()

    project_query = session.query(Project)
    session.close()
    return project_query.all()


def query_project_manager():
    sesion = sesion_factory()
    query_project_manager = sesion.query(ProjectManager)
    sesion.close()
    return query_project_manager.all()


if __name__ == '__main__':
    projects = query_project()

    if len(projects) == 0:
        populate_datebase()

    projects = query_project()

    for project in projects:
        print(f"Title: {project.title}  Desc: {project.description}, Manager: {project.project_manager.name}")
