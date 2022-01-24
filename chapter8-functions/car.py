def car(manufacture, models, **car_info):
    car_info['manufacture'] = manufacture
    car_info['model'] = models
    return car_info