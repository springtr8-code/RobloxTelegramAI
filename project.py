import os
import json
import shutil

from memory import (
    save_current_project,
    get_projects_memory,
    save_projects_memory
)


PROJECTS_FOLDER = "Projects"


#--------------------------------------


def create_project(name):

    project_path = os.path.join(
        PROJECTS_FOLDER,
        name
    )

    if os.path.exists(project_path):
        return False


    os.makedirs(project_path)


    folders = [

        "Scripts",
        "GUI",
        "NPC",
        "Sounds",
        "Animations",
        "Models",
        "Assets"

    ]


    for folder in folders:

        os.makedirs(
            os.path.join(
                project_path,
                folder
            )
        )


    data = {

        "name":name,
        "progress":"0%",
        "status":"Waiting"

    }


    with open(
        os.path.join(
            project_path,
            "project.json"
        ),
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


    projects = get_projects_memory()

    projects[name] = {

        "progress":"0%",
        "status":"Waiting"

    }


    save_projects_memory(
        projects
    )


    save_current_project(
        name
    )


    return True


#--------------------------------------


def delete_project(name):

    path = os.path.join(
        PROJECTS_FOLDER,
        name
    )


    if not os.path.exists(path):
        return False


    shutil.rmtree(path)


    projects = get_projects_memory()


    if name in projects:
        del projects[name]


    save_projects_memory(
        projects
    )


    return True


#--------------------------------------


def get_projects():

    return list(
        get_projects_memory().keys()
    )