weight = 41.5
# Ground Shipping 
if weight <= 2:
  cost_ground = 1.50 * weight + 20
elif weight <= 6:
  cost_ground = 3 * weight + 20
elif weight <= 10: 
  cost_ground = 4 * weight + 20
else: 
 cost_ground = 4.75 * weight + 20
print("Ground Shipping: $" , cost_ground)
# Premium Ground Shipping 
cost_ground_premium = 125
print("Ground Shipping Premium: $", cost_ground_premium)
# Drone Shipping 
if weight <= 2:
  drone_ship = 4.5 * weight 
elif weight <= 6:
  drone_ship = 9 * weight 
elif weight <= 10: 
  drone_ship = 12 * weight 
else: 
 drone_ship = 14.25 * weight
print("Drone Shipping: $", drone_ship)
