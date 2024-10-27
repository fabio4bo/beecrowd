import os
import subprocess
import sys

HOME_USER = os.path.expanduser("~")
PROJECT_PATH = HOME_USER + "/development/beecrowd/"

# python new_file b ".java" 1000  1 "Hello World"
category = sys.argv[1]
ext_language = sys.argv[2]
problem_number = str(sys.argv[3])
level = sys.argv[4]
problem_name = sys.argv[5]


def set_category_path(arg):
    match arg:
        case "a":
            return PROJECT_PATH + "ad-hoc/"
        case "b":
            return PROJECT_PATH + "beginner/"
        case "c":
            return PROJECT_PATH + "computational-geometry/"
        case "d":
            return PROJECT_PATH + "data-structures-and-libraries/"
        case "g":
            return PROJECT_PATH + "graph/"
        case "m":
            return PROJECT_PATH + "mathematics/"
        case "p":
            return PROJECT_PATH + "paradigms/"
        case "s":
            return PROJECT_PATH + "sql/"
        case "t":
            return PROJECT_PATH + "strings/"
        case _:
            print("Type a category.")


def set_category_name(arg):
    match arg:
        case "a":
            return "Ad-hoc"
        case "b":
            return "Beginner"
        case "c":
            return "Computational Geometry"
        case "d":
            return "Data Structures and Libraries"
        case "g":
            return "Graph"
        case "m":
            return "Mathematics"
        case "p":
            return "Paradigms"
        case "s":
            return "SQL"
        case "t":
            return "Strings"
        case _:
            print("Do not do this my friend.")


def create_folder(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def create_file(file_path):
    header = (
        "BEE "
        f"{problem_number} - "
        f"{problem_name} - Level "
        f"{level} - "
        f"{set_category_name(category)}"
    )
    try:
        if ext_language == ".py":
            with open(file_path, "x") as file:
                file.write('"""\n')
                file.write(header)
                file.write('\n"""\n')
        elif ext_language == ".java":
            with open(file_path, "x") as file:
                file.write("/*\n")
                file.write("* " + header)
                file.write("\n*/\n")
        elif ext_language == ".cpp":
            with open(file_path, "x") as file:
                file.write("/*\n")
                file.write("* " + header)
                file.write("\n*/\n")
    except FileExistsError:
        print(f"The file '{file_path}' already exists.")


file_path = set_category_path(category) + problem_number + "/"
create_folder(file_path)

j = ""
if ext_language == ".java":
    j = "Bee"
file_abs_path = file_path + j + problem_number + ext_language
create_file(file_abs_path)

subprocess.run(["code", file_abs_path])
