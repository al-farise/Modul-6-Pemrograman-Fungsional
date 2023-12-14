#Lengkapi kode dibawah ini untuk menjawab soal diatas ya


# TODO 0 : Import beberapa library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt


# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin disisipkan (overlay)
background_image = Image.open('./images/logo-umm.png')
overlay_image = Image.open('./images/task1.png')


# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert('RGB')


# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
resized_overlay_image = overlay_image.resize((400, 400))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - resized_overlay_image.width) // 2
y_center = (background_image.height - resized_overlay_image.height) // 2


# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(resized_overlay_image, (x_center, y_center))


# TODO 5 : Simpan gambar hasil edit
background_image.save('./images/task2.png')

# TODO 6 : Tampilkan
plt.imshow(background_image)
plt.axis('off')
plt.show()