for i in range(int(input('No. of line: '))):
    mag_field, area = [int(i) for i in input('Magnetic field: ').replace(' ', '')], [int(i) for i in input('Area: ').replace(' ', '')]
    print(f'Magnetic flux: {sum(x*y for x,y in zip(mag_field, area))}')
