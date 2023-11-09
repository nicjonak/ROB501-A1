# Billboard hack script file.
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

import matplotlib.pyplot as plt

def billboard_hack():
    """
    Hack and replace the billboard!

    Parameters:
    ----------- 

    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    # Bounding box in Y & D Square image - use if you find useful.
    bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
    Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])

    Iyd = imread(r'C:\Users\nicjo\Desktop\rob501_fall_2022_assignment_01\images\yonge_dundas_square.jpg')
    Ist = imread(r'C:\Users\nicjo\Desktop\rob501_fall_2022_assignment_01\images\uoft_soldiers_tower_light.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    #--- FILL ME IN ---

    # Let's do the histogram equalization first.

    # Compute the perspective homography we need...

    # Main 'for' loop to do the warp and insertion - 
    # this could be vectorized to be faster if needed!

    # You may wish to make use of the contains_points() method
    # available in the matplotlib.path.Path class!

    #------------------
    
    Iste=histogram_eq(Ist)
    H,A = dlt_homography(Iyd_pts,Ist_pts)
    for i in range(404,490):
      for j in range(38,354):
        coord=np.array([[i],
                        [j],
                        [1]])
        nc=H@coord
        nca=np.array([[nc[0,0]*nc[2,0]],
                      [nc[1,0]*nc[2,0]]])
        bn=bilinear_interp(Iste,nca)
        Ihack[j,i]=bn 

    # Visualize the result, if desired...
    # plt.imshow(Ihack)
    # plt.show()
    # imwrite(Ihack, 'billboard_hacked.png');

    return Ihack
