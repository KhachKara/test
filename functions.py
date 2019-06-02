def cubeinfo(length, width, height):
    """
    Считает суммарную площадь сторон, суммарный периматр кромок и объем куба
    и возвращает эти значения в виде кортежа.
    :param length: лина куба
    :param width: ширины куба
    :param height: высота куба
    :return:    square — суммарная площадь поверхностей,
                perimeter — суммарный перметр кромок,
                volume —  объем куба
    """
    square = 2*length*width + 2*length*height + 2*width*height
    perimeter = 4*length + 4*width + 4*height
    volume = length * width * height
    return square, perimeter, volume
print(cubeinfo(1, 1, 1))

