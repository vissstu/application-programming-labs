import argparse


def parsing_arguments():
    """
    Reads keyword, number of images, path to the folder, where you want to save images, path to the annotation file from terminal
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", type=str, help="Search word")
    parser.add_argument("number_of_images", type=int, help="Number of downloaded images")
    parser.add_argument("imgdir", type=str, help="The path to the folder with downloaded images")
    parser.add_argument("file_with_annotation", type=str, help="Path to the annotation file")
    arguments = parser.parse_args()
    return arguments