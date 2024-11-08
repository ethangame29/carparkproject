class Display:
    def __init__(self, id, car_park, message = "", is_on = False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id}: Welcome"

    def update(self, display_info):
        for key, value in display_info.items():
            print(f"{key}: {value}")