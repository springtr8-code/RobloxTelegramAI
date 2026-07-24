import json
import os


MEMORY_FOLDER = "Memory"

CURRENT_PROJECT = os.path.join(
    MEMORY_FOLDER,
    "current_project.json"
)

USER_MEMORY = os.path.join(
    MEMORY_FOLDER,
    "user_memory.json"
)

PROJECTS_MEMORY = os.path.join(
    MEMORY_FOLDER,
    "projects_memory.json"
)


#--------------------------------------------------


def read_json(path):

    if not os.path.exists(path):
        return {}

    try:
        with open(path,"r",encoding="utf-8") as file:
            return json.load(file)

    except:
        return {}


#--------------------------------------------------


def write_json(path,data):

    with open(path,"w",encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent = 4,
            ensure_ascii = False
        )


#--------------------------------------------------


def save_current_project(name):

    data = {

        "name":name

    }

    write_json(
        CURRENT_PROJECT,
        data
    )


#--------------------------------------------------


def get_current_project():

    return read_json(
        CURRENT_PROJECT
    )


#--------------------------------------------------


def save_user_memory(data):

    write_json(
        USER_MEMORY,
        data
    )


#--------------------------------------------------


def get_user_memory():

    return read_json(
        USER_MEMORY
    )


#--------------------------------------------------


def save_projects_memory(data):

    write_json(
        PROJECTS_MEMORY,
        data
    )


#--------------------------------------------------


def get_projects_memory():

    return read_json(
        PROJECTS_MEMORY
    )