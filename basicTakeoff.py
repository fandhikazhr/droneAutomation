# Connect to the Vehicle
import dronekit_sitl, sys
from dronekit import connect, VehicleMode
vehicle = connect('tcp:127.0.0.1:5760', wait_ready = True)

def arm_and_takeoff(aTargetAltitude):
  """
  Arms vehicle and fly to aTargetAltitude.
  """
  
  print "Basic pre-arm checks"
  # Don't try to arm until autopilot is ready
  while not vehicle.is_armable:
    print "Waiting for vehicle to initialise..."
    time.sleep(1)
    
    print "Arming motors"
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
      print "Waiting for arming..."
      time.sleep(1)
      
     print "Taking off !"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude
    
    While True:
      print "Altitude : ", vehicle.location.global_relative_frame.alt
      if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
        print "Reached target altitude"
        break
       time.sleep(1)
      
arm_and_takeoff(10)
