def city_country(city,country,population=''):
    if population:
        full=city+','+country+','+str(population)
    else:
        full=city+','+country
    return full
