"""
4190.308 Computer Architecture                                                          Spring 2023

Image blending (float)

This module implements a function that blends two images together (floating point version)

@author:
    Jungi Hong <junn0103@snu.ac.kr>

@changes:
    2023/MM/DD Your Name Comment

"""

def blend(img1, img2, height, width, channels, overlay, alpha):
    """
    Alpha-blends two images of size heightxwidth. The image data must contain an alpha
    channel, i.e., 'channels' must be four

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
    blended = [[[0.0 for c in range(bchannels)] for w in range(bwidth)] for h in range(bheight)]

    for r in range(height):
        for c in range(width):
            # Overlay mode
            if overlay:
                # Copy background alpha value
                blended[r][c][3] = img1[r][c][3]
                alphacombined=img2[r][c][3] *alpha 

                # Blend color channels
                for i in range(3):
                    blended[r][c][i] = int((((1 - (alphacombined/255.0))*(img1[r][c][i]/255.0)) + (alphacombined/255.0* (img2[r][c][i]/255.0)))*255)

            # Merge mode
            else:
                # Blend alpha values
                blended[r][c][3] = int(img1[r][c][3]*(1-alpha) + img2[r][c][3]* alpha)
                

                # Blend color channels good
                for i in range(3):
                    blended[r][c][i] =  int(((img1[r][c][i]*img1[r][c][3]*(1.0-alpha))+ (img2[r][c][i]*img2[r][c][3]*(alpha*1.0)))/255.0)
                    
              

    return blended, bheight, bwidth, bchannels
