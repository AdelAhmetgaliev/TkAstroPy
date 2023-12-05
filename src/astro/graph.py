from astropy.io import fits


def get_data_from_x_graph(
        filepath: str, star_coord: tuple[int, int], radius: int) -> tuple[list, list]:
    image_data = fits.getdata(filepath)

    x_list = []
    y_list = []

    for y in range(star_coord[1] - radius, star_coord[1] + radius):
        x_list.append(image_data[y, star_coord[0]])
        y_list.append(y)

    return (y_list, x_list)


def get_data_from_y_graph(
        filepath: str, star_coord: tuple[int, int], radius: int) -> tuple[list, list]:
    image_data = fits.getdata(filepath)

    x_list = []
    y_list = []

    for x in range(star_coord[0] - radius, star_coord[0] + radius):
        x_list.append(image_data[star_coord[1], x])
        y_list.append(x)

    return (y_list, x_list)


def get_data_from_z_graph(
        filepath: str, star_coord: tuple[int, int], radius: int) -> tuple[list, list, list]:
    image_data = fits.getdata(filepath)

    x_list = [x for x in range(star_coord[0] - radius, star_coord[0] + radius)]
    y_list = [y for y in range(star_coord[1] - radius, star_coord[1] + radius)]
    z_list = []

    for y in y_list:
        z_list.append([])
        for x in x_list:
            z_list[y - star_coord[1] + radius].append(image_data[y, x])

 
    return (z_list, y_list, x_list)

