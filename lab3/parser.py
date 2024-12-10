import argparse


def parser() -> argparse.Namespace:
	"""
	Creates an ArgumentParser object and adds command line arguments.
	Parses the arguments entered by the user and returns a Namespace with the results.
	:return: A Namespace object containing the values of the command-line arguments
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument( "-1im","--image1", default="C:\\test\\lab3\\cats.jpg", type=str, help="The path to 1 image file")
	parser.add_argument("-n","--output", default="C:\\test\\lab3", type=str, help="The path to save the image")
	arguments = parser.parse_args()
	return arguments