import cv2 
import matplotlib.pyplot as plt
import numpy as np 

#resmi içe aktar
img = cv2.imread("datai_team.jpg",0)

#BGR'den RGB'ye donustur
img_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img, cmap = "gray"), plt.axis("off"),plt.title("Orijinal") 

#erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
    
#sonucu rgb formatına donustur
result_rgb = cv2.cvtColor(result , cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(result_rgb, cmap = "gray"), plt.axis("off"),plt.title("Erozyon") 

#genişleme dilation
result2 = cv2.dilate(img , kernel, iterations = 1)
plt.figure(), plt.imshow(result2 , cmap = "gray"), plt.axis("off"), plt.title("Genişleme")

#white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(),plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise")

noise_img = whiteNoise + img 
plt.figure(),plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Img w White Noise")

#açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN,kernel)
plt.figure(),plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Acilma")

#black noise
blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(),plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise")
black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(),plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise w Img")
# kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE,kernel)
plt.figure(),plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("Kapama")

# gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,kernel)
plt.figure(),plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradient")




