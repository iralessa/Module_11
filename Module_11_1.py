# -*- coding: utf-8 -*-
from PIL import ImageDraw, Image, ImageFont

# Открываем изображение
img = Image.open('example.jpg')

# Показываем размеры и формат изображения
print("Размер исходного изображения -",img.size)

# Изменяем размер изображения и выводим на экран
r_img = img.resize((300, 200))
print("Изменили размер изображения -",r_img.size)
# Рисуем (Добавляем текст)
draw = ImageDraw.Draw(r_img)
text = "Это питон!"
# координаты верхнего левого угла текста на изображении
position = (30, 10)
# цвет текста
text_color = "green"
# Загружаем шрифт и размер
font = ImageFont.truetype("arial.ttf", 36)
# Рисуем текст с указанным шрифтом
draw.text(position, text, fill=text_color, font=font)
# Применяем эффекты (например, переворот) и сохраняем как новое изображение
f_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# Рисуем (Добавляем текст)
draw = ImageDraw.Draw(f_img)
text = "Это зеркальное изображение! "
# координаты верхнего левого угла текста на изображении
position = (50, 50)
# Цвет текста
text_color = "red"
# Загружаем шрифт и размер
font = ImageFont.truetype("arial.ttf", 52)
# Рисуем текст с указанным шрифтом
draw.text(position, text, fill=text_color, font=font)
# Сохраняем измененные изображения
r_img.save('r_example.jpg')
f_img.save('f_example.jpg')

# ИТОГ: Получилось два изображения:
# 1) r_example.jpg (изменили размер и добавили текст)
# 2) f_example.jpg(отоброзили зеркально и добавили текст)