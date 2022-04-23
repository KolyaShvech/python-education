
"""
Create class Transport with several inheriting classes from him.
"""

class Transport:
    """
    Create class Transport with parameters: moving_env, max_speed, type_of_fuel, year.
    """
    def __init__(self, moving_env, seats, year):
        self.moving_env = moving_env
        self.seats = seats
        self.year = year
        self.type_of_fuel = None

    def __str__(self):
        info = f"envirement = {self.moving_env}, max seats = {self.seats},\
 year of production = {self.year}"
        return info

    def moves(self, moving_env):
        """
        Create method go with parameter moving_env
        """
        self.moving_env = moving_env
        print(f"Transport moves by {self.moving_env} ")

    @staticmethod
    def refueled():
        """
        Create method refueled with parameter fuel_of_type.
        """
        print("This transport now at the filling station.")

    @staticmethod
    def repair():
        """
        Create method repair.
        """
        print("Transport is broken and it now under repair.")

    @staticmethod
    def stay():
        """
        Create staticmethod stay.
        """
        print("Transport now staying.")


class Engine:
    """
    Create class Engine with parameters: power, fuel_cons, volume.
    """
    def __init__(self, power, volume, serial_id):
        self.power = power
        self.volume = volume
        self.__serial_id = serial_id

    @property
    def serial(self):
        """
        Create Property method for serial id engine.
        """
        return self.__serial_id

    @serial.setter
    def serial(self, serial_id):
        self.__serial_id = serial_id

    def __str__(self):
        info_engine = f"power = {self.power}, volume = {self.volume} mm."
        return info_engine

    @staticmethod
    def start():
        """
        Create staticmethod start.
        """
        print("Engine is starting.")

    @staticmethod
    def stopped():
        """
        Create staticmethod stopped.
        """
        print("Engine stopped.")

    @classmethod
    def __verify(cls, volum):
        """
        Create Class method for volum.
        """
        return volum if isinstance(volum, int) else volum.volume

    def __ge__(self, other):
        volum = self.__verify(other)
        return self.volume >= volum


class Car(Transport, Engine):
    """
    Create class Car which inherited from Transport class and Engine class with all
    parameters both classes.
    """
    def __init__(self, moving_env, seats, year, power, volume, serial_id, gov_number):
        super().__init__(moving_env, seats, year)
        super().__init__(power, volume, serial_id)
        self.moving_env = moving_env
        self.seats = seats
        self.year = year
        self.power = power
        self.volume = volume
        self.__serial_id = serial_id
        self.gov_number = gov_number
        self.speed = None

    @property
    def serial(self):
        """
        Create Property method for serial id engine.
        """
        return self.__serial_id

    @serial.setter
    def serial(self, serial_id):
        self.__serial_id = serial_id

    def __str__(self):
        info_car = f"moving enviroment = {self.moving_env}, year = {self.year},\
power = {self.power}, volume = {self.volume}, state number = {self.gov_number}"
        return info_car

    def accident(self, gov_number, speed):
        """
        Create method accident with parameters gov_number, speed.
        """
        self.gov_number = gov_number
        self.speed = speed
        print(f"Car with govement number {self.gov_number}, by {self.speed}\
km in hour had an accident.")

    @classmethod
    def __verify(cls, seat):
        """
        Create Class method for seat.
        """
        return seat if isinstance(seat, int) else seat.seats

    def __le__(self, other):
        seat = self.__verify(other)
        return self.seats <= seat

    def sail(self, gov_number, year, power, volume):
        """
        Create method sail with parameters gov_number,year, power, volume, type_of_fuel.
        """
        self.gov_number = gov_number
        self.year = year
        self.power = power
        self.volume = volume
        print(f"Car with govement number {self.gov_number} put on sale.\n"
              f"Parameter car:\n year: {self.year}\n power: {self.power}\n volume: {self.volume}\n")

    def __iadd__(self, seat):
        self.seats += seat
        print(f"Added seats at This car. Now {self.seats} seats.")

    def __isub__(self, seat):
        self.seats -= seat
        print(f"Subtract seats at This car. Now {self.seats} seats.")


class Boat(Engine, Transport):
    """
    Create class Boat which inherited from class Engine and Transport. This class used all
    parameters from both classes.
    """
    def __init__(self, power, volume, serial_id, moving_env, seats, year, name):
        super().__init__(power, volume, serial_id)
        super().__init__(moving_env, seats, year)
        self.power = power
        self.volume = volume
        self.__serial_id = serial_id
        self.moving_env = moving_env
        self.seats = seats
        self.year = year
        self.name = name

    @property
    def serial(self):
        """
        Create Property method for serial id engine.
        """
        return self.__serial_id

    @serial.setter
    def serial(self, serial_id):
        self.__serial_id = serial_id

    @staticmethod
    def dropped_anchor():
        """
        Create staticmethod dropped_anchor.
        """
        print("Boat is stopped and dropped anchor.")

    def caught_in_storm(self, name):
        """
        Create method caught_in_storm with parameters type_of_fuel, name, displacement.
        """
        self.name = name
        print(f"The boat with the name {self.name} ran out of fuel and stopped.\
 A storm broke out and the boat began to sink.")

    def signal_sos(self, name):
        """
        Create method signal_sos with parameters name.
        """
        self.name = name
        print(f"The boat named by {self.name} give a signal SOS!")

    def __iadd__(self, seat):
        self.seats += seat
        print(f"Added seats at This car. Now {self.seats} seats.")

    def __isub__(self, seat):
        self.seats -= seat
        print(f"Subtract seats at This car. Now {self.seats} seats.")


class ElectricScooter(Transport):
    """
    Create class ElectricScooter which inherited by Transport class.
    """
    def __init__(self,moving_env, seats, year, battery, distance):
        super().__init__(moving_env, seats, year)
        self.moving_env = moving_env
        self.seats = seats
        self.year = year
        self.battery = battery
        self.distance = distance

    def discharched_battery(self, battery):
        """
        Create method discharched_battery with parameter battery.
        """
        if 50 <= battery <= 100:
            print(f"Level charging high equel {self.battery} %, you can ride.")
        elif 15 <= battery <= 49:
            print(f"Level charging equel {self.battery} %, will be carrifull follow by charge.")
        else:
            print(f"Scooter soon will be discharged level battery equel {self.battery} %.")

    @classmethod
    def __verify(cls, batter):
        return batter if isinstance(batter, int) else batter.battery

    def __eq__(self, other):
        batter = self.__verify(other)
        return self.battery == batter

    @staticmethod
    def the_fall():
        """
        Create staticmethod the fall.
        """
        print("The scooter is falls.")

    @staticmethod
    def take_the_delivery():
        """
        Create staticmethod take the delivery.
        """
        print("Scooter delivery order.")


class Plane(Transport):
    """
    Create class Plane which inherit be Transport class.
    """
    def __init__(self, moving_env, seats, year, appointment, load_capa, height):
        super().__init__(moving_env, seats, year)
        self.moving_env = moving_env
        self.seats = seats
        self.year = year
        self.appointment = appointment
        self.load_capa = load_capa
        self.height = height
        self.name = "Molly Green"

    @classmethod
    def __verify(cls, seat):
        """
        Create Class method for seat.
        """
        return seat if isinstance(seat, int) else seat.seats

    def __le__(self, other):
        seat = self.__verify(other)
        return self.seats <= seat

    def overloading(self, appointment, load_capa):
        """
        Create method overloading with parameters appointment, load_capa.
        """
        self.appointment = appointment
        self.load_capa = load_capa
        if load_capa != "over":
            print(f"The {self.appointment} plane  {self.load_capa}loading and can not flying.")
        else:
            print(f"The {self.appointment} plane {self.load_capa} and may fly.")

    def autopilot(self, height):
        """
        Create staticmethod autopilot. This method turned on then height = 10000 m.
        """

        self.height= height
        if height == 10000:
            print(f"Now height {self.height} m and pilot turned on autopilot.")
        elif height < 10000:
            print(f"Your height {self.height} m, your height must be lower.")
        else:
            print(f"Now {self.height} m less then needing for autopilot, pilot can not turn on.")

    def __iadd__(self, seat):
        self.seats += seat
        print(f"Added seats at this plane and passenger {self.name}. Now {self.seats} seats.")

    def __isub__(self, seat):
        self.seats -= seat
        print(f"Subtract seats at This car. Now {self.seats} seats.")


# trans = Transport("air", 100, 1998)
# print(trans.__str__())
# trans.moves("water")


# eng = Engine(210, 2100, "44223677")
# print(eng.serial)
# eng.stopped()
# eng1 = Engine(110, 1600, "eeiow575835fgs7")
# print(eng >= eng1)

# car = Car("ground", 4, 2012, 180, 2200, "tyu677840yt", "AX5412BE")
# print(car.__str__())
# car.sail("AX9810KA", 2018, 240, 3000)
# car.accident("BC1290ES", "200")
# car.__iadd__(1)
# print(car.seats)
# car.__isub__(3)
# print(car.seats)
# car1 = Car("ground", 9, 2012, 180, 2200, "ty5ttwv6840yt", "AX9081TH")
# print(car <= car1)
# print(car >= car1)

# boat = Boat(800, 5600, "qwe1234123lk", "water", 10, 2013, "Romanda")
# boat.stay()
# boat.caught_in_storm("Romanda")
# print(boat.seats, boat.power, boat.name)
# print(boat.serial)

# scoot = ElectricScooter("ground", 1, 2020, 60, 30)
# scoot.moves("ground")
# scoot.battery = 12
# scoot.discharched_battery(12)
# sco = ElectricScooter("ground", 1, 2020, 12, 30)
# print(scoot == sco)

# plane = Plane("air", 200, 1999, "passanger", "full", 10000)
# plane.autopilot(9999)
# plane.autopilot(10000)
# plane.__iadd__(1)
# print(plane.seats)
#
# pln = Plane("air", 150, 2000, "passenger", "full", 8000)
# print(plane <= pln)
