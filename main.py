import numpy as np
import matplotlib.pyplot as plt

# Configure the font settings
plt.rcParams['font.family'] = 'Times New Roman'

# Configure the parameters
time_steps = 100
time_delay = 1
headway_distance = 10
acceleration_threshold = 5
fixed_car_speed1 = 20
fixed_car_speed2 = 40
fixed_car_speed3 = 10

# Initialize the speed and position of the leading vehicle
front_car_speed = np.zeros(time_steps)
front_car_position = np.zeros(time_steps)
front_car_position[0] = 50

# Initialize acceleration
front_car_acceleration = np.zeros(time_steps)
car1_acceleration = np.zeros(time_steps)
car2_acceleration = np.zeros(time_steps)

# Set the speed change of the preceding vehicle: accelerate first, then decelerate.
for t in range(1, time_steps):
    if 10 <= t < 30:
        ideal_acceleration_front = fixed_car_speed1 - front_car_speed[t - 1]
    elif 30 <= t < 60:
        ideal_acceleration_front = fixed_car_speed2 - front_car_speed[t - 1]
    elif 60 <= t < 80:
        ideal_acceleration_front = fixed_car_speed3 - front_car_speed[t - 1]
    else:
        ideal_acceleration_front = -front_car_speed[t - 1]

    # Limit acceleration
    front_car_acceleration[t] = np.clip(ideal_acceleration_front, -acceleration_threshold, acceleration_threshold)

    # Update speed and location
    front_car_speed[t] = front_car_speed[t - 1] + front_car_acceleration[t]
    front_car_position[t] = front_car_position[t - 1] + front_car_speed[t]

# Initialize data for the two following vehicles
car1_position = np.zeros(time_steps)
car2_position = np.zeros(time_steps)
car1_speed = np.zeros(time_steps)
car2_speed = np.zeros(time_steps)

# The initial position is set to the distance between the vehicle and the one ahead minus a safety margin.
car1_position[0] = front_car_position[0] - headway_distance
car2_position[0] = car1_position[0] - headway_distance

# Simulate following behavior
for t in range(1, time_steps):
    if t >= time_delay:
        # Calculate the ideal acceleration for Car 1
        ideal_speed_car1 = front_car_speed[t - time_delay]
        ideal_acceleration_car1 = ideal_speed_car1 - car1_speed[t - 1]

        # Limit acceleration
        car1_acceleration[t] = np.clip(ideal_acceleration_car1, -acceleration_threshold, acceleration_threshold)

        # Update Speed and Position, Method 1 (Newell Car Following Model)
        car1_position[t] = front_car_position[t - time_delay] - headway_distance
        car1_speed[t] = front_car_speed[t - time_delay]

        # Update Speed and Position, Method 2
        #car1_speed[t] = car1_speed[t - 1] + car1_acceleration[t]
        #car1_position[t] = car1_position[t - 1] + car1_speed[t]

        # Calculate the position of Car 2, otherwise it will result in a null value.
        car2_position[1] = car1_position[0] - headway_distance

    if t >= 2 * time_delay:
        # Calculate the ideal acceleration for Car 2
        ideal_speed_car2 = car1_speed[t - time_delay]
        ideal_acceleration_car2 = ideal_speed_car2 - car2_speed[t - 1]

        # Limit acceleration
        car2_acceleration[t] = np.clip(ideal_acceleration_car2, -acceleration_threshold, acceleration_threshold)

        # Update Speed and Position, Method 1 (Newell Car Following Model)
        car2_position[t] = car1_position[t - time_delay] - headway_distance
        car2_speed[t] = car1_speed[t - time_delay]

        # Update Speed and Position, Method 2
        #car2_speed[t] = car2_speed[t - 1] + car2_acceleration[t]
        #car2_position[t] = car2_position[t - 1] + car2_speed[t]


# draw
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# location map
axs[0].plot(front_car_position, label='Front Car')
axs[0].plot(car1_position, label='Car 1')
axs[0].plot(car2_position, label='Car 2')
axs[0].set_title('Position')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Position')
axs[0].legend()

# speed map
axs[1].plot(front_car_speed, label='Front Car')
axs[1].plot(car1_speed, label='Car 1')
axs[1].plot(car2_speed, label='Car 2')
axs[1].set_title('Speed')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Speed')
axs[1].legend()

# acceleration map
axs[2].plot(front_car_acceleration, label='Front Car')
axs[2].plot(car1_acceleration, label='Car 1')
axs[2].plot(car2_acceleration, label='Car 2')
axs[2].set_title('Acceleration (Real-time Adjustment)')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Acceleration')
axs[2].legend()

plt.tight_layout()
plt.show()