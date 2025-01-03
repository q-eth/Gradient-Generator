from PIL import Image
import math
import os

def hex_to_rgba(hex_color):
    """
    Преобразует шестнадцатеричный код цвета в формат RGBA.

    :param hex_color: Цвет в шестнадцатеричном формате (#RRGGBB или #RRGGBBAA)
    :return: Кортеж (R, G, B, A)
    """
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        a = 255
    elif len(hex_color) == 8:
        r, g, b, a = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16), int(hex_color[6:8], 16)
    else:
        raise ValueError("Invalid color format. Use #RRGGBB or #RRGGBBAA instead.")
    return (r, g, b, a)

def generate_gradient(width, height, colors, angle, output_path):
    """
    Генерирует изображение градиента с заданным углом наклона.

    :param width: Ширина изображения
    :param height: Высота изображения
    :param colors: Список цветов в формате [(hex_color, позиция), ...],
                   где hex_color — шестнадцатеричный цвет, позиция — число от 0 до 1
    :param angle: Угол наклона градиента в градусах
    :return: Изображение с градиентом
    """
    image = Image.new("RGBA", (width, height))
    pixels = image.load()

    colors = [(hex_to_rgba(color), position) for color, position in colors]
    colors = sorted(colors, key=lambda c: c[1])

    angle_rad = math.radians(angle)
    dx = math.cos(angle_rad)
    dy = math.sin(angle_rad)

    diag = math.sqrt(width**2 + height**2)

    for y in range(height):
        for x in range(width):

            position = ((x * dx + y * dy) / diag)

            position = max(0.0, min(1.0, position))

            for i in range(len(colors) - 1):
                color_start, pos_start = colors[i]
                color_end, pos_end = colors[i + 1]

                if pos_start <= position <= pos_end:

                    local_pos = (position - pos_start) / (pos_end - pos_start)

                    r = int(color_start[0] + (color_end[0] - color_start[0]) * local_pos)
                    g = int(color_start[1] + (color_end[1] - color_start[1]) * local_pos)
                    b = int(color_start[2] + (color_end[2] - color_start[2]) * local_pos)
                    a = int(color_start[3] + (color_end[3] - color_start[3]) * local_pos)

                    pixels[x, y] = (r, g, b, a)
                    break

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path, "PNG")
    print(f"Your gradient is saved as: {output_path}")

if __name__ == "__main__":

    width = 1920
    height = 1080

    colors = [
        ("#63008780", 0.0),
        ("#12014EC0", 0.5),
        ("#000000FF", 1.0),
    ]

    angle = 0

    output_path = "insert your path here with '\\' instead of '\'. For example: C:\\Users\\User\\Desktop\\gradient1.png"

    generate_gradient(width, height, colors, angle, output_path)