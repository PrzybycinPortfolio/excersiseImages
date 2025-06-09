import numpy as np
import matplotlib.pyplot as plt

def draw_image(x,y):
    z = np.random.randint(0,255,(x,y,3)).astype('uint8')
    plt.imshow(z)
    plt.show()