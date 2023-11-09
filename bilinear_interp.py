import numpy as np
from numpy.linalg import inv

def bilinear_interp(I, pt):
    """
    Performs bilinear interpolation for a given image point.

    Given the (x, y) location of a point in an input image, use the surrounding
    four pixels to conmpute the bilinearly-interpolated output pixel intensity.

    Note that images are (usually) integer-valued functions (in 2D), therefore
    the intensity value you return must be an integer (use round()).

    This function is for a *single* image band only - for RGB images, you will 
    need to call the function once for each colour channel.

    Parameters:
    -----------
    I   - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    pt  - 2x1 np.array of point in input image (x, y), with subpixel precision.

    Returns:
    --------
    b  - Interpolated brightness or intensity value (whole number >= 0).
    """
    #--- FILL ME IN ---

    if pt.shape != (2, 1):
        raise ValueError('Point size is incorrect.')

    #------------------
    xl=np.shape(I)[0]
    yl=np.shape(I)[1]

    x=pt[0][0]
    y=pt[1][0]
    xu=int(np.ceil(x))
    xd=int(np.floor(x))
    yu=int(np.ceil(y))
    yd=int(np.floor(y))

    if xu==xl:
        xu=xl-1
    if yu==yl:
        yu=yl-1
    if xd==xl-1:
        xd=xl-2
        xu=xl-1
    if yd==yl-1:
        yd=yl-2
        yu=yl-1 

    s=1/((xu-xd)*(yu-yd))
    f=np.array([[I[yd,xd],I[yu,xd],I[yd,xu],I[yu,xu]]])
    a=np.array([[xu*yu,-yu,-xu,1],[-xu*yd,yd,xu,-1],[-xd*yu,yu,xd,-1],[xd*yd,-yd,-xd,1]])
    c=np.array([[1],[x],[y],[x*y]])
    at=a@c
    bt=s*(f@at)
    b=round(bt.item())                
    return b
