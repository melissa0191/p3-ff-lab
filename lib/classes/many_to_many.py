class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.book_list = []
        self.flight_list = []

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._first_name = name
    

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._last_name = name
        
    def bookings(self):
        return self.book_list
    
    def flights(self):
        return self.flight_list

    def num_cheap_bookings(self):
        cheap = [booking.price for booking in self.book_list if booking.price < 1000]
        return len(cheap)

    def has_booked_flight(self, flight):
        return flight in self.flight_list


class Flight:
    all = []

    def __init__(self, airline):
        self.airline = airline
        self.booking_list = []
        self.customer_list = []
        
        Flight.all.append(self)

    @property
    def airline(self):
        return self._airline
    
    @airline.setter
    def airline(self, airline_parameter):
        if isinstance(airline_parameter, str) and 1 < len(airline_parameter):
            self._airline = airline_parameter

    
    def bookings(self):
        return self.booking_list
    
    def customers(self):
        return self.customer_list

    def average_price(self):
        if len([booking for booking in Booking.all if booking.flight is self]) == 0:
            return 0.0
        else:
            price = [booking.price for booking in self.booking_list]
            return round(sum(price) / len(price), 1)

    @classmethod
    def top_two_expensive_flights(cls):
        if len(Booking.all) == 0:
            return None
        else:
            cls.all.sort(reverse=True, key=lambda f: f.average_price())
            return cls.all[:2]


class Booking:    
    all = []

    def __init__(self, customer, flight, price):
        self.customer = customer
        self.flight = flight
        self.price = price

        self.flight.booking_list.append(self)

        if customer not in self.flight.customer_list:
            self.flight.customer_list.append(customer)

        customer.book_list.append(self)

        if flight not in customer.flight_list:
            customer.flight_list.append(flight)

        Booking.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_parameter):
        if (not hasattr(self, 'price')) and isinstance(price_parameter, int) and 500 <= price_parameter <= 3000:
            self._price = price_parameter

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if type(customer) == Customer:
            self._customer = customer

    @property
    def flight(self):
        return self._flight
    
    @flight.setter
    def flight(self, flight):
        if type(flight) == Flight:
            self._flight = flight
