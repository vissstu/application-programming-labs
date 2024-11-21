import csv
import os


def create_annotation(imgdir: str, file_with_annotation: str) -> None:
    """
    Creating annotations with absolute and relative paths to images
    """
    with open(file_with_annotation, mode='w', encoding='utf-8') as annotation:
        writer = csv.writer(annotation)
        name_of_the_paths = ['Relative path', 'Absolute path']
        writer.writerow(name_of_the_paths)

        for file in os.listdir(imgdir):
            relative_path = os.path.relpath(file, imgdir)
            absolute_path = os.path.abspath(file)
            writer.writerow([relative_path, absolute_path])