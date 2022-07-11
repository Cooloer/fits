from astropy.io import fits
import numpy as np
# path = 'D:/workspace/deconv/unsupervisedMFBD-master/214ytc_13.fits'

# hdu = fits.open(path)
# img = hdu[0].data
# print(img.shape)

# path = 'D:/workspace/deconv/unsupervisedMFBD-master/sigori.fits'

# hdu = fits.open(path)
# img = hdu[0].data
# print(img.shape)

path = 'D:/workspace/deconv/unsupervisedMFBD-master/214ytc_13.fits'
hdu = fits.open(path)
img = hdu[0].data
print(img.shape)
imgzeros = np.zeros((img.shape[0]*10,img.shape[1],img.shape[2]))
for i in range(0,imgzeros.shape[0],10):
    imgzeros[i:i+10,:,:] = img[i//10]
s =fits.PrimaryHDU(imgzeros[:,276-64:276+64,144-64:144+64])
ah = fits.HDUList([s])
ah.writeto('C:/Users/99286/Desktop/214ytc13_200.fits')

print(147)
