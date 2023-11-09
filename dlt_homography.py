import numpy as np
from numpy.linalg import inv, norm
from scipy.linalg import null_space

def dlt_homography(I1pts, I2pts):
    """
    Find perspective Homography between two images.

    Given 4 points from 2 separate images, compute the perspective homography
    (warp) between these points using the DLT algorithm.

    Parameters:
    ----------- 
    I1pts  - 2x4 np.array of points from Image 1 (each column is x, y).
    I2pts  - 2x4 np.array of points from Image 2 (in 1-to-1 correspondence).

    Returns:
    --------
    H  - 3x3 np.array of perspective homography (matrix map) between image coordinates.
    A  - 8x9 np.array of DLT matrix used to determine homography.
    """
    #--- FILL ME IN ---

    #------------------
    At=[]
    for i in range(0,4):
      xi=I1pts[0][i]
      yi=I1pts[1][i]
      ui=I2pts[0][i]
      vi=I2pts[1][i]
      ai=np.array([[-xi,-yi,-1,0,0,0,ui*xi,ui*yi,ui],
          [0,0,0,-xi,-yi,-1,vi*xi,vi*yi,vi]])
      At=At+[ai]
    AU=np.concatenate((At[0],At[1]),axis=0)
    AL=np.concatenate((At[2],At[3]),axis=0)
    A=np.concatenate((AU,AL),axis=0)
    ht=null_space(A)
    H=np.array([[ht[0][0],ht[1][0],ht[2][0]],
                [ht[3][0],ht[4][0],ht[5][0]],
                [ht[6][0],ht[7][0],ht[8][0]]])
    H=H*(1/H[2][2]) 
    return H, A
