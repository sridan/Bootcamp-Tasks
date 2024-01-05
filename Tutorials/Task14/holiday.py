"""○ city_flight: The city they will be flying to. (You can create some
options for them. Remember each city will have different flight
costs.)
○ num_nights: The number of nights they will be staying at a hotel
○ rental_days: The number of days for which they will be hiring a
car.
"""
city_flight_cost = [i for i in range(250,300,25)] 
for i in range(len(city_flight_cost)):
  if len(city_flight_cost)!=-1:
    
    city_flight = input('Enter the city name you want to fly to:')
    flight_cost=city_flight_cost[i]
    print(f'{city_flight}-{flight_cost}')
    response=input('Do you want to continue to check for other flights(y/n)?')
    if response.lower()=='y':
        continue
    elif response.lower()=='n':
        break
    else:
        response=input('Please enter either y or n:')
        continue


num_nights = int(input('Please enter the number of nights:'))
rental_days = int(input('Please enter the number of days to rent:'))
#total_cost=0
def hotel_cost(num_nights):
    return 175*num_nights
hotel_cost = hotel_cost(num_nights)

def plane_cost(city_flight):
    return city_flight

def car_rental(rental_days):
    total_car_rental = num_nights*rental_days 
    return total_car_rental
total_car_rental = car_rental(rental_days)

def holiday_cost(hotel_cost,plane_cost,car_rental):
    total_cost = hotel_cost+plane_cost+car_rental
    return total_cost
total_holiday_cost = holiday_cost(rental_days)

print(f'City:{city_flight}')
print(f'No.of nights to stay:{num_nights}')
print(f'Number of days to rent:{rental_days}')
print(f'Hotel cost:{hotel_cost}')
print(f'car rental:{total_car_rental}')
print(f'Total holiday cost:{total_holiday_cost}')


