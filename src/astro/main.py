from astropy.io import fits


def calculate_star_flow(
        fits_file_path: str, star_coord: tuple[int, int], radius: int) -> float:
    image_data = fits.getdata(fits_file_path)
    exposure_time = fits.getval(fits_file_path, 'EXPTIME')
    
    x_star_coord, y_star_coord = star_coord

    total_energy = 0.0
    for y in range(y_star_coord - radius, y_star_coord + radius):
        for x in range(x_star_coord - radius, x_star_coord + radius):
            if abs(y - y_star_coord) + abs(x - x_star_coord) > radius:
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
            if abs(y - y_star_coord) + abs(x - x_star_coord) < inner_radius or \
                abs(y - y_star_coord) + abs(x - x_star_coord) > outer_radius:
                continue

            total_noise_energy += image_data[y, x]
            pixel_count += 1

    return total_noise_energy / (pixel_count * exposure_time)


def calculate_flow(
        fits_file_path: str, star_coord: tuple[int, int],
        inner_radius: int, outer_radius: int) -> float:
    return calculate_star_flow(fits_file_path, star_coord, inner_radius) - \
            calculate_noise_flow(fits_file_path, star_coord, inner_radius, outer_radius)


def main() -> None:
    test_path = '/home/adel/Documents/Programming_Projects/Python_Projects/TkAstroPy/fits/fit0.fit'
    test_star_coord = (1091, 1036)
    test_inner_radius = 5
    test_outer_radius = 10

    star_flow = calculate_star_flow(test_path, test_star_coord, test_inner_radius)
    noise_flow = calculate_noise_flow(test_path, test_star_coord, 
                                      test_inner_radius, test_outer_radius)
    flow = calculate_flow(test_path, test_star_coord, test_inner_radius, test_outer_radius)
    
    print(f'{star_flow} - {noise_flow} = {flow}')


if __name__ == '__main__':
    main()

