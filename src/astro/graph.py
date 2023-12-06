from astropy.io import fits


def get_data_for_x_graph(
        filepath: str, star_coord: tuple[int, int], radius: int) -> tuple[list, list]:
    image_data = fits.getdata(filepath)

    x_list = []
    y_list = []

    for y in range(star_coord[1] - radius, star_coord[1] + radius + 1):
        x_list.append(image_data[y, star_coord[0]])
        y_list.append(y)

    return (y_list, x_list)


def get_data_for_y_graph(
        filepath: str, star_coord: tuple[int, int], radius: int) -> tuple[list, list]:
    image_data = fits.getdata(filepath)

    x_list = []
    y_list = []

    for x in range(star_coord[0] - radius, star_coord[0] + radius + 1):
        x_list.append(image_data[star_coord[1], x])
        y_list.append(x)

    return (y_list, x_list)


def get_data_for_z_graph(
        filepath: str, star_coord: tuple[int, int], radius: int) -> tuple[list, list, list]:
    image_data = fits.getdata(filepath)

    x_list = [x for x in range(star_coord[0] - radius, star_coord[0] + radius + 1)]
    y_list = [y for y in range(star_coord[1] - radius, star_coord[1] + radius + 1)]
    z_list = []
 
    conversion = radius - star_coord[1]
    for y in y_list:
        z_list.append([])
        for x in x_list:
            z_list[y + conversion].append(image_data[y, x])
 
    return (z_list, y_list, x_list)

