import matplotlib.colors as colors
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
#import astropy.units as u
#from astropy.coordinates import SkyCoord
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from astropy.visualization import ImageNormalize, SqrtStretch
from matplotlib.colors import LogNorm
import numpy as np

#import sunpy.map


image_file_1 = get_pkg_data_filename('aia.lev1.171A_2011-05-30T10 56 36.34Z.image_lev1.fits')
image_data_1 = fits.getdata(image_file_1, ext=0)
image_data_1 = image_data_1[1200:2200, 100:1100] 

image_file_2 = get_pkg_data_filename('aia.lev1.171A_2011-05-30T10 56 24.34Z.image_lev1.fits')
image_data_2 = fits.getdata(image_file_2, ext=0)
image_data_2 = image_data_2[1200:2200, 100:1100] 

image_data_3 = np.array(image_data_2 - image_data_1)

plt.imshow( image_data_3, cmap= 'gray',vmin=-100, vmax=100)


plt.title('AIA 171.0 Angstrom 2011-05-30 10:56:24')

plt.xlim(0,1000)
plt.ylim(0,1000)
plt.colorbar()
plt.savefig('difference_image.png')
plt.show()

