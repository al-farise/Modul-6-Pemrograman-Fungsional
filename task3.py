from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# TODO 1: Buka gambar dengan Pillow
image = Image.open('./images/logo-umm.png')

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightened_image= enhancer.enhance(1.5)
enhancer = ImageEnhance. Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save('./images/task3.png')

# TODO 4: Tampilkan
plt.imshow(final_image)
plt.axis('off')
plt.show()