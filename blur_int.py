"""
4190.308 Computer Architecture                                                          Spring 2023

Image blurring (int)

This module implements a function that blurs an image with a 3x3 filter (integer version)

@author:
    Jungi Hong <junn0103@snu.ac.kr>

@changes:
    2023/MM/DD Jungi Hong Comment
    
"""
def blur(image, height, width, channels, kernel_size=5):
    """
    Blurs an image with a kernel and returns the blurred image.

    Args:
        image:        image data (multi-level list)
        height:       image height
        width:        image width
        channels:     number of channels (BGR or BGRA)
        kernel_size:  size of blurring kernel

    Returns:
        A tuple containing the following elements:
        - blurred:    blurred image data
        - bheight:    blurred image height
        - bwidth:     blurred image width
        - bchannels:  blurred image channels

    """
    # create the kernel
    kernel = [[1 / (kernel_size ** 2) for i in range(kernel_size)] for j in range(kernel_size)]

    # create the output image
    bheight = height - kernel_size + 1
    bwidth = width - kernel_size + 1
    blurred = [[[0 for c in range(channels)] for x in range(bwidth)] for y in range(bheight)]

    # apply the kernel
    for c in range(channels):
        for y in range(bheight):
            for x in range(bwidth):
                fixed_value = 0  # fixed-point value for current pixel
                for i in range(kernel_size):
                    for j in range(kernel_size):
                        pixel_value = int(image[y + i][x + j][c]) << 8  # shift to left by 8 bits (multiply by 256)
                        kernel_value = kernel[i][j] * 256  # multiply kernel by 256 to convert it to fixed-point
                        fixed_value += pixel_value * kernel_value  # multiply and accumulate
                blurred[y][x][c] = (int(fixed_value) >> 16) & 0xFF  # shift back to right by 16 bits (divide by 256)

    return blurred, bheight, bwidth, channels
