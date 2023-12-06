from astropy.io import fits


def calculate_star_flow(
        fits_file_path: str, star_coord: tuple[int, int], radius: int) -> float:
    image_data = fits.getdata(fits_file_path)
    exposure_time = fits.getval(fits_file_path, 'EXPTIME')
    
    x_star_coord, y_star_coord = star_coord

    total_energy = 0.0
    for y in range(y_star_coord - radius, y_star_coord + radius):
        for x in range(x_star_coord - radius, x_star_coord + radius):
            if (y - y_star_coord) ** 2 + (x - x_star_coord) ** 2 > radius ** 2:
                continue
            total_energy += image_data[y, x]

    return total_energy / exposure_time


def calculate_noise_flow(
        fits_file_path: str, star_coord: tuple[int, int], 
        inner_radius: int, outer_radius: int) -> float:
    image_data = fits.getdata(fits_file_path)
    exposure_time = fits.getval(fits_file_path, 'EXPTIME')

    x_star_coord, y_star_coord = star_coord

    pixel_count = 0
    total_noise_energy = 0.0
    for y in range(y_star_coord + inner_radius, y_star_coord + outer_radius):
        for x in range(x_star_coord + inner_radius, x_star_coord + outer_radius):
            if (y - y_star_coord) ** 2 + (x - x_star_coord) ** 2 < inner_radius ** 2 or \
                (y - y_star_coord) ** 2 + (x - x_star_coord) ** 2 > outer_radius ** 2:
                continue

            total_noise_energy += image_data[y, x]
            pixel_count += 1

    return total_noise_energy / (pixel_count * exposure_time)


def calculate_total_flow(
        fits_file_path: str, star_coord: tuple[int, int],
        inner_radius: int, outer_radius: int) -> float:
    return calculate_star_flow(fits_file_path, star_coord, inner_radius) - \
            calculate_noise_flow(fits_file_path, star_coord, inner_radius, outer_radius)

