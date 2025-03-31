create database crime;
use crime;

CREATE TABLE Crime (
CrimeID INT PRIMARY KEY,
IncidentType VARCHAR(255),
IncidentDate DATE,
Location VARCHAR(255),
Description TEXT,
Status VARCHAR(20)
);
CREATE TABLE Victim (
VictimID INT PRIMARY KEY,
CrimeID INT,
Name VARCHAR(255),
ContactInfo VARCHAR(255),
Injuries VARCHAR(255),
FOREIGN KEY (CrimeID) REFERENCES Crime(CrimeID)
);
CREATE TABLE Suspect (
SuspectID INT PRIMARY KEY,
CrimeID INT,
Name VARCHAR(255),
Description TEXT,
CriminalHistory TEXT,
FOREIGN KEY (CrimeID) REFERENCES Crime(CrimeID)
);

INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status)
VALUES
(1, 'Robbery', '2023-09-15', '123 Main St, Cityville', 'Armed robbery at a convenience store', 'Open'),
(2, 'Homicide', '2023-09-20', '456 Elm St, Townsville', 'Investigation into a murder case', 'Under
Investigation'),
(3, 'Theft', '2023-09-10', '789 Oak St, Villagetown', 'Shoplifting incident at a mall', 'Closed');
INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status)
VALUES
(4, 'Assault', '2023-08-22', '321 Birch St, Metropolis', 'Physical altercation outside a bar', 'Open'),
(5, 'Fraud', '2023-07-18', '654 Pine St, Cityville', 'Online scam reported', 'Under Investigation'),
(6, 'Burglary', '2023-06-25', '987 Maple St, Townsville', 'Break-in at a residential home', 'Closed'),
(7, 'Vandalism', '2023-05-30', '741 Cedar St, Villagetown', 'Graffiti on public property', 'Open'),
(8, 'Arson', '2023-04-12', '852 Willow St, Metropolis', 'Deliberate fire at a warehouse', 'Under Investigation'),
(9, 'Kidnapping', '2023-03-09', '369 Aspen St, Cityville', 'Child abduction case', 'Open'),
(10, 'Drug Possession', '2023-02-15', '258 Spruce St, Townsville', 'Illegal substances found during a traffic stop', 'Closed'),
(11, 'Domestic Violence', '2023-01-28', '147 Redwood St, Villagetown', 'Police intervention in a domestic dispute', 'Under Investigation'),
(12, 'Car Theft', '2022-12-05', '369 Walnut St, Metropolis', 'Stolen vehicle reported', 'Open'),
(13, 'Cybercrime', '2022-11-20', '951 Digital St, Cityville', 'Phishing attack targeting multiple users', 'Under Investigation');
INSERT INTO Crime (CrimeID, IncidentType, IncidentDate, Location, Description, Status)
VALUES
(14, 'Robbery', '2023-10-10', '159 Chestnut St, Metropolis', 'Bank heist reported', 'Open'),
(15, 'Burglary', '2023-11-05', '753 Oak Ave, Townsville', 'Break-in at an electronics store', 'Open'),
(16, 'Fraud', '2023-12-15', '369 Elm Dr, Cityville', 'Credit card fraud detected', 'Open'),
(17, 'Vandalism', '2024-01-20', '951 Park St, Villagetown', 'Destruction of public property', 'Open'),
(18, 'Robbery', '2024-02-10', '357 Willow Rd, Metropolis', 'Armed robbery at a gas station', 'Open');


INSERT INTO Victim (VictimID, CrimeID, Name, ContactInfo, Injuries)
VALUES
(1, 1, 'John Doe', 'johndoe@example.com', 'Minor injuries'),
(2, 2, 'Jane Smith', 'janesmith@example.com', 'Deceased'),
(3, 3, 'Alice Johnson', 'alicejohnson@example.com', 'None');

alter table victim add age int check(age>0);
alter table suspect add age int check(age>0);
update Victim 
set age = 28 
where VictimID = 1;

update Victim 
set Age = 30 
where VictimID = 2;

update Victim 
set Age = 42 
where VictimID = 3;

INSERT INTO Victim (VictimID, CrimeID, Name, ContactInfo, Injuries, Age)
VALUES
(4, 4, 'Robert Brown', 'robertbrown@example.com', 'Broken arm', 32),
(5, 5, 'Emily Davis', 'emilydavis@example.com', 'Severe burns', 31),
(6, 6, 'Michael Wilson', 'michaelwilson@example.com', 'Concussion', 34),
(7, 7, 'Sarah Martinez', 'sarahmartinez@example.com', 'Minor cuts', 33),
(8, 8, 'David Lee', 'davidlee@example.com', 'None', 30),
(9, 9, 'Olivia White', 'oliviawhite@example.com', 'Leg fracture', 35),
(10, 10, 'William Harris', 'williamharris@example.com', 'Internal bleeding', 32),
(11, 11, 'Sophia Clark', 'sophiaclark@example.com', 'Bruised ribs', 31),
(12, 12, 'James Lewis', 'jameslewis@example.com', 'None', 33),
(13, 13, 'Charlotte Walker', 'charlottewalker@example.com', 'Head injury', 34);
INSERT INTO Victim (VictimID, CrimeID, Name, ContactInfo, Injuries, Age)
VALUES
(14, 14, 'Liam Turner', 'liamturner@example.com', 'Severe trauma', 45),
(15, 15, 'Emma Brown', 'emmabrown@example.com', 'Minor injuries', 32),
(16, 16, 'Noah Smith', 'noahsmith@example.com', 'Financial loss', 40),
(17, 17, 'Isabella Garcia', 'isabellagarcia@example.com', 'None', 29),
(18, 18, 'William Harris', 'williamharris@example.com', 'Gunshot wound', 36);


INSERT INTO Suspect (SuspectID, CrimeID, Name, Description, CriminalHistory, Age) 
VALUES 
(1, 1, 'Robber 1', 'Armed and masked robber', 'Previous robbery convictions', 35),
(2, 2, 'Unknown', 'Investigation ongoing', NULL, 40),
(3, 3, 'Suspect 1', 'Shoplifting suspect', 'Prior shoplifting arrests', 28),
(4, 4, 'Robert Brown', 'Involved in a bar fight', 'Prior assault charges', 32),
(5, 5, 'Emily Davis', 'Fraudulent transactions detected', 'Financial fraud cases', 31),
(6, 6, 'Michael Wilson', 'Break-in suspect', 'History of burglary', 34),
(7, 7, 'Sarah Martinez', 'Caught vandalizing public property', NULL, 33),
(8, 8, 'David Lee', 'Arson suspect seen near fire', 'Prior arson charges', 30),
(9, 9, 'Olivia White', 'Suspected in child abduction', 'Kidnapping attempt in 2020', 29),
(10, 10, 'William Harris', 'Drug possession and trafficking', 'Multiple drug offenses', 36),
(11, 11, 'Sophia Clark', 'Linked to a domestic violence case', NULL, 38),
(12, 12, 'James Lewis', 'Car theft suspect', 'Previous vehicle-related crimes', 27),
(13, 13, 'Charlotte Walker', 'Suspected in cybercrime', 'Past hacking offenses', 45),
(14, 14, 'Masked Bandit', 'Suspect seen fleeing the bank', 'Previous robbery arrests', 50),
(15, 15, 'Michael Wilson', 'Broke into the electronics store', 'Prior burglary convictions', 33),
(16, 16, 'Emma Brown', 'Suspected in credit card fraud', NULL, 31),
(17, 17, 'Unknown', 'Graffiti vandal caught on CCTV', NULL, 29),
(18, 18, 'William Harris', 'Possibly involved in gas station robbery', 'Armed robbery in 2020', 42);



select * from Crime;
select * from Victim;
select * from Suspect;

--1.Select all open incidents.
1.select * from Crime where Status='Open';
select c.CrimeID,c.IncidentType,c.IncidentDate,c.Location,c.Description,v.VictimID,v.name,v.ContactInfo,v.Injuries,v.age 
from Crime c 
join Victim v on c.CrimeID=v.CrimeID where Status='Open';

--2.Find the total number of incidents.
2.select count(crimeid) as total_number_of_incidents from crime;

--3.List all unique incident types.
3.select distinct incidenttype from Crime;

--4.Retrieve incidents that occurred between '2023-09-01' and '2023-09-10'.
4.select * from crime where IncidentDate between '2023-09-01' and '2023-09-10';

--5.List persons involved in incidents in descending order of age.
5. select * from Victim order by age desc;

--6.Find the average age of persons involved in incidents.
6. select injuries,avg(age) as average_Age from Victim group by Injuries;

--7.List incident types and their counts, only for open cases.
7. select incidenttype,status,count(IncidentType) as Count from Crime where status='Open' group by IncidentType,Status;

--8.Find persons with names containing 'Doe'.
8. select * from Victim join Crime on Crime.CrimeID=Victim.VictimID where name like '%doe%';

--9.Retrieve the names of persons involved in open cases and closed cases.
9. select v.victimid,v.name,v.contactinfo,v.injuries,v.age,c.Status
from victim v join Crime c on c.CrimeID=v.CrimeID 
where c.Status='Open' or c.Status='Closed';

--10.List incident types where there are persons aged 30 or 35 involved.
10. select v.name as victim_name,v.age,c.incidenttype from Victim v join Crime c on c.CrimeID=v.CrimeID where v.age=30 or v.age=35;

--11.Find persons involved in incidents of the same type as 'Robbery'.
11. select c.CrimeID,c.IncidentType,c.IncidentDate,c.Location,c.Description,v.VictimID,v.name,v.ContactInfo,v.Injuries,v.age 
from Crime c join Victim v on c.CrimeID=v.CrimeID 
where IncidentType='Robbery';

--12.List incident types with more than one open case.
12. select incidenttype,Count(incidenttype) as Count_of_incident from crime  where status='Open' group by IncidentType having count(incidenttype)>1;

--13.List all incidents with suspects whose names also appear as victims in other incidents.
13. select * from crime where crimeid in(select CrimeID from Suspect where Name in (select name from Victim));

--14.Retrieve all incidents along with victim and suspect details.
14. select c.incidenttype,c.incidentdate,c.location,c.status,v.name as victim_name,v.contactinfo,v.injuries,v.age,s.name as suspect_name,s.description,s.criminalhistory 
from Crime c join Victim v on v.CrimeID=c.CrimeID 
join Suspect s on s.CrimeID=c.CrimeID;

--15.Find incidents where the suspect is older than any victim.
15.select s.name as suspect_name,s.age as suspect_age,v.name as victim_name,v.age as victim_age 
from Suspect s 
join Victim v on s.CrimeID=v.CrimeID where s.age>v.age;

--16.Find suspects involved in multiple incidents
16.select Name,Description,CriminalHistory,CrimeID from suspect 
where name in 
(select name SuspectID from suspect group by name having count(name)>1) order by name;

--17.List incidents with no suspects involved.
17.select * from crime where crimeid not in(select crimeid from suspect);

--18.List all cases where at least one incident is of type 'Homicide' and all other incidents are of type 'Robbery'.
18.select CrimeID 
from Crime 
group by CrimeID
having count(case when IncidentType = 'Homicide' then 1 end) >= 1 and count(case when IncidentType NOT IN ('Homicide', 'Robbery') THEN 1 END) = 0;


--19.Retrieve a list of all incidents and the associated suspects, showing suspects for each incident, or 'No Suspect' if there are none.
19.select c.CrimeID, c.IncidentType, c.IncidentDate, c.Location, isnull(s.name,'No suspect') as SuspectName 
from Crime c 
left join Suspect s ON c.CrimeID = s.CrimeID order by c.CrimeID;

--20.List all suspects who have been involved in incidents with incident types 'Robbery' or 'Assault'
20.select s.crimeid,s.name,s.description,s.age,c.incidenttype 
from suspect s 
join Crime c on s.CrimeID=c.CrimeID where c.IncidentType='Assault' or c.IncidentType='Robbery'; 




