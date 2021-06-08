from random import randint

def get_random_code(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

NAMA_BULAN = (
    (0, "--Bulan--"),
    (1, "Januari", "Jan"),
    (2, "Februari", "Feb"),
    (3, "Maret", "Mar"),
    (4, "April", "Apr"),
    (5, "Mei", "Mei"),
    (6, "Juni", "Jun"),
    (7, "Juli", "Jul"),
    (8, "Agustus", "Agu"),
    (9, "September", "Sep"),
    (10, "Oktober", "Okt"),
    (11, "Nopember", "Nov"),
    (12, "Desember", "Des"),
)


def dMy(tgl):
    return str(tgl.day) + ' ' + NAMA_BULAN[tgl.month][1] + ' ' + str(tgl.year)

def dMy_short(tgl):
    return str(tgl.day) + ' ' + NAMA_BULAN[tgl.month][2] + ' ' + str(tgl.year)