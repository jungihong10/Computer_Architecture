"""
4190.308 Computer Architecture                                                          Spring 2023

Image blending (int)

This module implements a function that blends two images together (integer version)

@author:
    Jungi Hong <junn0103@snu.ac.kr>

@changes:
    2023/MM/DD Your Name Comment

"""

def blend(img1, img2, height, width, channels, overlay, alpha):
    """
    Alpha-blends two images of size heightxwidth using fixed-point arithmetic.
    The image data must contain an alpha channel, i.e., 'channels' must be four.

    Args:
        img1:         image 1 data (multi-level list), BGRA
        img2:         image 2 data (multi-level list), BGRA
        height:       image height
        width:        image width
        channels:     number of channels (must be 4)
        overlay:      if 1, overlay the second image over the first
                      if 0, merge the two images
        alpha:        alpha blending factor (0.0-1.0)

    Returns:
        A tuple containing the following elements:
        - blended:    blended image data (multi-level list), BGRA
        - bheight:    blended image height (=height)
        - bwidth:     blended image width (=width)
        - bchannels:  blended image channels (=channels)

    """

    if channels != 4:
        raise ValueError('Invalid number of channels')

    # Initialize output image
    bheight = height
    bwidth = width
    bchannels = channels
    blended = [[[0 for c in range(bchannels)] for w in range(bwidth)] for h in range(bheight)]

    for r in range(height):
        for c in range(width):
            # Overlay mode
            if overlay:
                # Copy background alpha value
                blended[r][c][3] = img1[r][c][3]
                alphacombined = (img2[r][c][3] * alpha) >> 8  # Shift the fixed-point value to the integer position

                # Blend color channels
                for i in range(3):
                    channel1 = (img1[r][c][i] * (256 - alphacombined)) >> 8  # Shift the fixed-point value to the integer position
                    channel2 = (img2[r][c][i] * alphacombined) >> 8  # Shift the fixed-point value to the integer position
                    blended[r][c][i] = ((channel1 + channel2) << 8) >> 8  # Convert back to fixed-point and store in the output

            # Merge mode
            else:
                # Blend alpha values
                blended[r][c][3] = ((img1[r][c][3] * (256 - alpha)) + (img2[r][c][3] * alpha) + 127) >> 8

                # Blend color channels
                for i in range(3):
                    # Convert the 1.8-bit fixed-point values back to 8-bit format
                    img1_fixed = img1[r][c][i] << 1
                    img2_fixed = img2[r][c][i] << 1

                    # Calculate the blended color channel in fixed-point format
                    blended_fixed = ((img1_fixed * img1[r][c][3] * (256 - alpha)) + (img2_fixed * img2[r][c][3] * alpha) + 127) >> 16

                    # Convert the blended color channel back to 1.8-bit fixed-point format and store in output pixel
                    blended[r][c][i] = blended_fixed >> 1

    return blended, bheight, bwidth, bchannels

