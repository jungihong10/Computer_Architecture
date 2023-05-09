"""
4190.308 Computer Architecture                                                          Spring 2023

Image blurring (float)

This module implements a function that blurs an image with a 3x3 filter (floating point version)

@author:
    Jungi Hong <junn0103@snu.ac.kr>

@changes:
    2023/MM/DD Your Name Comment

"""

def blur(image, height, width, channels, kernel_size=5):
    """
    Blurs an image with a kernel and returns the blurred image.

    Args:
        image:        image data (multi-level list)
        height:       image height
        width:        image width
        channels:     number of channels (RGB)
        kernel_size:  size of blurring kernel

    Returns:
        A tuple containing the following elements:
        - blurred:    blurred image data
        - bheight:    blurred image height
        - bwidth:     blurred image width
        - bchannels:  blurred image channels

    """
    # creating the kernel
    kernel = [[1 / (kernel_size ** 2) for i in range(kernel_size)] for j in range(kernel_size)]

    # creating the output image
    bheight = height - kernel_size + 1
    bwidth = width - kernel_size + 1
    blurred = [[[0.0 for c in range(channels)] for x in range(bwidth)] for y in range(bheight)]

    # applying the kernel
    for c in range(channels):
        for y in range(1, bheight):
            for x in range(1, bwidth):
                for i in range(kernel_size):
                    for j in range(kernel_size):
                        blurred[y-1][x-1][c] += image[y + i - 1][x + j - 1][c] * kernel[i][j]

    # convert the blurred image data from float to int
    for y in range(bheight):
        for x in range(bwidth):
            for c in range(channels):
                blurred[y][x][c] = int(blurred[y][x][c])

    return blurred, bheight, bwidth, channels
