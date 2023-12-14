#Lengkapi kode dibawah untuk menjawab soal diatas ya


# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import cv2


# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('./images/logo-umm.png')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert('L')


# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype('./fonts/ORION.TTF', 72)
text = 'Muhammad Salman Al Farisi 293'
# text_width, text_height = draw.textsize(text, font)
text_x = (gambarku.width - font.getlength(text)) // 2
text_y = 20
draw.text((text_x, 20), font=font, text=text)


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('./images/task1.png')

# TODO 5: Tampilkan hasil akhir gambar
image = cv2.imread('./images/task1.png')
plt_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(plt_image)
plt.axis('off')
plt.show()