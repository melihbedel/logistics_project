_NOTE: This repository is a reupload of a group project, the original is privated and I do not have owner rights_

# Logistics-App

The logistics app can:
1. Login/logout employee and give different command permissions based on the type of employee
2. Create Packages
2. Create Routes
3. Assign Package to suitable route
4. Find truck for a given route
5. Keep track on the deliveries' statutes
6. Show information for specific package
7. Show all packages, that are waiting to be assigned to routes
8. Show all routes that are in progress
9. Keep track of the application state

> **_NOTE:_**  When you test the program, the input_log file keeps track of every command and reuses it on the next run of the application. <br />
> If you want to test the application again, you have to manually clear the input_log.txt and time_log.txt files

### Input Example
```
CreatePackage Sydney Melbourne 45 test@test.com
Loginuser manager
CreatePackage Sydney Melbourne 45 test@test.com
CreateRoute 2023 10 10 06 00 Brisbane Sydney Melbourne
AssignTruck 1
AssignPackage 1
Createroute 2023 09 12 06 00 AliceSprings Adelaide Melbourne Sydney Brisbane
AssignTruck 2
CreatePackage AliceSprings Brisbane 23000 test@testt.com
CreatePackage Perth Melbourne 22 test@testtt.com
ViewUnassignedPackages
ViewRoutes
Adddays 28 0
ViewRoutesinprogress
ViewPackage 1
End
```

### Output Example
```No user is logged in. Please login first.
Manager successfully logged in.
Package #1 created!
Route #1 created!
Truck #1001 assigned to route #1.
Package #1 assigned to route #1.
Route #2 created!
Truck #1002 assigned to route #2.
Package #2 created!
Package #3 created!
----------
Packages waiting to be assigned:
1. Package #2
Weight: 23000kg
Start location: AliceSprings
Destination: Brisbane
2. Package #3
Weight: 22kg
Start location: Perth
Destination: Melbourne
----------
All routes in the system:
----------
Route #1
Status: pending
Current Location:Brisbane
-----
Location and time of arrival:
Brisbane (2023/10/10, 06:00)
Sydney (2023/10/11, 02:31)
Melbourne (2023/10/11, 23:03)
----------
Route #2
Status: pending
Current Location:AliceSprings
-----
Location and time of arrival:
AliceSprings (2023/09/12, 06:00)
Adelaide (2023/09/14, 04:26)
Melbourne (2023/09/16, 02:53)
Sydney (2023/09/18, 01:20)
Brisbane (2023/09/19, 23:47)
28 days and 0 hours added! 
Current time: 2023/09/12, 12:10
---------
Routes in progress:
----------
1. Route #2
Status: departed
Current Location:AliceSprings
-----
Location and time of arrival:
AliceSprings (2023/09/12, 06:00)
Adelaide (2023/09/14, 04:26)
Melbourne (2023/09/16, 02:53)
Sydney (2023/09/18, 01:20)
Brisbane (2023/09/19, 23:47)
----------
Package details
Package #1
Weight: 45kg
Start location: Sydney
Destination: Melbourne
Package status: assigned
Detailed information sent to test@test.com
----------
```
