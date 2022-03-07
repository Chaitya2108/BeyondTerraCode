from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import socket
import argparse

try:
    def connectMyCopter():
        parser = argparse.ArgumentParser(description='commands')
        parser.add_argument('--connect')
        args = parser.parse_args()
        connection_string = args.connect
        vehicle = connect(connection_string, wait_ready=True)

        return vehicle

    def arm_and_takeoff(target_altitude):
        while not vehicle.is_armable:
            print("waiting for vehicle to become armable")
            time.sleep(1)
        vehicle.mode = VehicleMode("GUIDED")

        while vehicle.mode!="GUIDED":
            print("waiting for vehicle to enter guided")
            time.sleep(1)
        
        vehicle.armed=True
        while vehicle.armed==False:
            print("waiting to arm vehicle")
            time.sleep(1)
        
        vehicle.simple_takeoff(target_altitude)

        while True:
            print("Current Altitude: ", vehicle.location.global_relative_frame.alt)
            if vehicle.location.global_relative_frame.alt>target_altitude*0.95:
                break
            time.sleep(1)
        print("target alt reached")
        return None

    vehicle=connectMyCopter()
    print("taking off...")
    vehicle.mode=VehicleMode("GUIDED")
    arm_and_takeoff(2)
    vehicle.mode=VehicleMode("LAND")

    time.sleep(2)
    print("End of function")
    print("copter vers: ", vehicle.version)

    while True:
        time.sleep(2)

    vehicle.close()
except Exception():
    print("error")


