-- Insert a new driver record
INSERT INTO Drivers
    (DriverID, UserName, Password, DriversName)
VALUES
    (1, 'driver1', 'password123', 'John Doe');

-- Insert a new shipping record associated with DriverID 1
INSERT INTO ShippingInfo
    (ShippingID, Date, Time, ShippingContainer, TransportationType, DriverID, VehicleNumber, Port, Status, Company)
VALUES
    (1, '2023-09-10', '08:00:00', 'Container123', 'Truck', 1, 'ABC123', 'Port A', 'In Progress', 'ABC Logistics');

-- Delete the driver with DriverID 1
DELETE FROM Drivers
WHERE DriverID = 1;

-- Delete the shipping record with ShippingID 1
DELETE FROM ShippingInfo
WHERE ShippingID = 1;
