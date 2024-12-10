from working_with_a_picture import read_image, display_img, save_image, comawd_images
from image import histogram_of_channels, show_hist
from parser import parser


def main():
	arg = parser()
	try:
		original_image = read_image(arg.image1)
		print(f"Image size 1: {original_image.shape}")
		b, g, r = histogram_of_channels(original_image)
		show_hist(b, g, r)

		display_img(original_image, "Image1")

		combined=comawd_images(original_image,800,700)
		display_img(combined,"Image comad")


		save_image(combined, arg.output)
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()
