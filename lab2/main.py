from iterator import ImageIterator
from downloader import download_images
from annotation import create_annotation
from parsing import parsing_arguments


def main():
    arguments = parsing_arguments()
    try:
        download_images(arguments.keyword, arguments.number_of_images, arguments.imgdir)
        create_annotation(arguments.imgdir,arguments.file_with_annotation)
        my_iterator = ImageIterator(arguments.file_with_annotation)
        for image in my_iterator:
            print(image)
    except Exception as error:
        print(f"Error: {error} ")


if __name__=="__main__":
    main()