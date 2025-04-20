import os
import sys
import shutil

from copystatic import copy_files_recursive
from generate_page import (
    generate_pages_recursive,
)


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    base_path = "/"
    if sys.argv[1] != "":
        base_path = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        base_path,
    )


if __name__ == "__main__":
    main()
