def es_bisiesto(year):
    if year%4 == 0:
        return True
    elif year%4 == 0 and year%100 == 0 and  year%400 == 0:
        return True
    else: 
        return False

def main():
    year = int(input("Inserte año: "))
    print(es_bisiesto(year))

if __name__=="__main__":main()

# Test
"""
bisiestos = [1800,1804, 1808, 1812, 1816, 1820, 1824, 1828, 1832, 1836, 1840, 1844, 1848, 1852, 1856, 1860, 1864, 1868, 1872, 1876, 1880, 1884, 1888, 1892, 1896, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
for i in bisiestos:
    print(es_bisiesto(i))
"""