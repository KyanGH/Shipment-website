CREATE TABLE Drivers
(
    DriverID INT PRIMARY KEY,
    UserName VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    DriversName VARCHAR(255)
);

CREATE TABLE ShippingInfo
(
    ShippingID INT PRIMARY KEY,
    Date DATE,
    Time TIME,
    ShippingContainer VARCHAR(255),
    TransportationType VARCHAR(255),
    DriverID INT,
    VehicleNumber VARCHAR(255),
    Port VARCHAR(255),
    Status VARCHAR(255),
    Company VARCHAR(255),
    FOREIGN KEY (DriverID) REFERENCES Drivers (DriverID)
);
