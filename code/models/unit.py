class Unit():
    def __init__(self, unit_type, serial_number, hours_run, customer, id=None):
        self.unit_type = unit_type
        self.serial_number = serial_number
        self.hours_run = hours_run
        self.customer = customer
        self.id = id