# Creating a data base for a large company
# with relations between the tables

DROP TABLE OrderDetails;

DROP TABLE Orders;

DROP TABLE Customers;

DROP TABLE Employees;

DROP TABLE Products;

CREATE TABLE Products(
	ProductID INT PRIMARY KEY, 
	ProductName VARCHAR(100) NOT NULL,
	SupplierID INT NOT NULL, 
	CategoryID INT NOT NULL, 
	QuantityPerUnit INT NOT NULL, 
	UnitPrice FLOAT NOT NULL, 
	UnitsInStock INT, 
	UnitsOnOrder INT
);

CREATE TABLE Employees (
	EmpID INT PRIMARY KEY, 
	Last_Name VARCHAR(100) NOT NULL, 
	First_Name VARCHAR(100) NOT NULL, 
	Title VARCHAR(100) NOT NULL, 
	HireDate DATE NOT NULL, 
	Office INT NOT NULL, 
	Extension INT, 
	Reports_To INT FOREIGN KEY REFERENCES Employees(EmpID), 
	Year_Salary FLOAT NOT NULL,
);	

CREATE TABLE Customers (
	CustomerID INT PRIMARY KEY, 
	CompanyName VARCHAR(100) NOT NULL, 
	ContactName VARCHAR(100) NOT NULL, 
	[Address] VARCHAR(100) NOT NULL, 
	City VARCHAR(100) NOT NULL, 
	PostalCode VARCHAR(100) NOT NULL, 
	Country VARCHAR(100) NOT NULL, 
	Phone VARCHAR(100) NOT NULL, 
	Fax VARCHAR(100),
	/*CONSTRAINT City_Check Check City IN (*/
);

CREATE TABLE Orders (
	OrderID INT PRIMARY KEY, 
	OrderDate DATE NOT NULL, 
	CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID) NOT NULL, 
	EmployeeID INT FOREIGN KEY REFERENCES Employees(EmpID) NOT NULL, 
	ShipperID INT NOT NULL, 
	Freight FLOAT NOT NULL
);

CREATE TABLE OrderDetails (
	OrderID INT FOREIGN KEY REFERENCES Orders(OrderID), 
	ProductID INT FOREIGN KEY REFERENCES Products(ProductID), 
	UnitPrice FLOAT NOT NULL, 
	Quantity INT NOT NULL, 
	Discount FLOAT
	CONSTRAINT PK_OrderDetails PRIMARY KEY (OrderID,ProductID)
);



ALTER TABLE Employees	ADD	Bonus INT, NewSalary INT

ALTER TABLE Employees ALTER COLUMN Bonus Real
ALTER TABLE Employees ALTER COLUMN NewSalary Real


SELECT ProductName, UnitsInStock, UnitsOnOrder, UnitsOnOrder - UnitsInStock as dif
FROM Products
WHERE UnitsOnOrder > UnitsInStock
Order by dif Desc;

SELECT City, numOfCustomer = count(*), count(Distinct PostalCode)
FROM Customers
GROUP BY City
HAVING count(*)>=2
ORDER BY numofCustomer;

SELECT C.CustomerID, Count(Distinct O.OrderID) ,  Count(Distinct OD.ProductID)
FROM Customers AS C JOIN Orders AS O ON C.CustomerID = O.CustomerID	JOIN OrderDetails AS OD ON O.OrderID=OD.OrderID
GROUP BY C.CustomerID
ORDER BY 2 DESC
