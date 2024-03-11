# MediCareHub
An MySQL 8.0 project for our Sophomore Database Project
TED UNIVERSITY
FACULTY OF ENGINEERING
DEPARTMENT OF COMPUTER ENGINEERING

CMPE 232
2024 Spring












MEDICAREHUB


MediCareHub is a comprehensive approach to the hospital management system. It can include features such as patient registration, appointment scheduling, taking an online appointment, showing results such as radiology or blood tests, medical records management, billing, and inventory management for medical supplies. It would aim to streamline the workflow within the hospital, enhance communication between departments, and improve overall efficiency in healthcare management.


Group Members:
 Duygu Can Gündoğan
Alp Eren Çakmak
Melisa Yurtekin
Yelda Sıla Mumcu




Abstract
The goal of this project is to develop a new comprehensive and dynamic approach to a Hospital Management System which will be named “MediCareHub”. In this project, we will provide various aspects of healthcare administration. The system will encompass patient registration, appointment scheduling(including online appointments), display medical tests, medical records management, invoice, pharmacy, staff, inventory control, and room and prescription. In this project, we aim to streamline hospital workflows, foster improved communication between departments, enhance overall efficiency, and toggle the simple choices in healthcare management. Staff and patients will utilize the application and lead to more organized and effective healthcare services.


Introduction

MediCareHub is a full-featured software program created to help hospitals and other medical facilities manage and coordinate many healthcare procedures more effectively. In order to optimize patient care, administrative duties, and overall hospital operations, this system incorporates several subsystems.

Patient Management System:
Handles patient information, including personal details, medical background and current conditions of the patients.
Manages admission, invoices and room allocations through the “Patient” and “Room” entities. 
Have the insurance details about the patient with the “Insurance” entity.                         
Employee and Department Management System
Handles staff information on employee roles, joining dates, and separations including nurses, doctors and other employees.
Organizes employees into departments through the “Department” entity.
Medical Record and Prescription System
Maintains electronic health records, prescriptions, and assigned medications for patients.
Manages medical backgrounds and current conditions through the “Medical_History” entity.
Facilitates prescriptions and medication details through the “Medicine” and “Prescription” entities.

Appointment Scheduling System
Handles the scheduling of appointments between doctors and patients.
Records appointment details in the “Appointment” entity, including scheduled dates and times.


Invoice and Finance System
Manages invoice details for patients, including room costs, test costs, and medication costs.
Handles financial transactions through the “Invoice” entity, considering insurance coverage and patient balances
Lab and Test Results System
Manages laboratory tests through the Lab entity, associating patients, doctors, and Lab technicians.
Calculates test costs and keeps records of tests performed.


By offering a comprehensive platform that guarantees that effective patient care, faster appointment procedures, and precise invoicing and financial management, MediCareHub is predicted to completely transform the way healthcare is administered. Through features including rapid access to thorough patient information, faster appointment scheduling, and secure data access restrictions, the initiative seeks to improve patient experiences and optimize medical staff workflows. The financial components of the system are made to integrate several expenses, account for insurance information, and manage patient balances in order to produce appropriate invoices. Administrators will be able to make well-informed decisions because of extensive reporting and analytics features that provide them with insights into patient satisfaction, staff performance, and data trends. In order to maintain data integrity and system stability, regular maintenance procedures will be put in place along with a scalable architecture that guarantees adaptation to expanding data needs. This will eventually promote a more effective and patient-centered healthcare environment. In order to maintain data integrity and system stability, regular maintenance procedures will be put in place along with a scalable architecture that guarantees adaptation to expanding data needs. This will eventually promote a more effective and patient-centered healthcare environment. In order to enhance the project's comprehension and synchronize it with pragmatic demands, conversations were held with “Güven Hastanesi”, who offered significant perspectives derived from their proficiency in the healthcare field.


Requirements

Room Entity:

Attributes: Room_ID (Primary Key), Room_Type, Patient_ID (Foreign Key), Room_Cost
Relationship: Patient (Many-to-One)

Lab Entity:

Attributes: Lab_ID (Primary Key), Patient_ID (Foreign Key), Lab_Techinican_ID (Foreign Key), Doctor_ID (Foreign Key), Test_Cost, Date
Relationships: Patient (Many-to-One), Lab_Technician (Many-to-One), Doctor (Many-to-One)

Invoice Entity:

Attributes: Invoice_ID (Primary Key), Date, Room_Cost (Reference: Room), Test_Cost (Reference: Lab), Other_Charges, Total, Patient_ID (Reference: Patient), Policy_Number (Reference: Insurance), Medicine_Cost (Reference: Medicine)
Relationships: Patient (Many-to-One), Insurance (Many-to-One), Medicine (Many-to-One)

Insurance Entity:

Attributes: Policy_Number (Primary Key), Patient_ID (Reference: Patient), Ins_Code, End_Date, Provider, Plan, Coop_Pay, Coverage, Dental, Optical, Maternity
Relationship: Patient (One-to-One)

Medicine Entity:

Attributes: Medicine_ID (Primary Key), M_Name, M_Quantity, Medicine_Cost
Relationship: Prescription (Many-to-One)

Prescription Entity:

Attributes: Prescription_ID (Primary Key), Patient_ID (Reference: Patient), Medicine_ID (Reference: Medicine), Date, Dosage, Doctor_ID (Reference: Doctor)
Relationships: Patient (Many-to-One), Medicine (Many-to-One), Doctor (Many-to-One)

Patient Entity:

Attributes: Patient_ID (Primary Key), Patient_Fname, Patient_Lname, Phone, Blood_Type, Email, Gender, Condition, Admisson_Date, Discharge_Date, Address
Relationships: Room (One-to-Many), Lab (One-to-Many), Invoice (One-to-Many), Insurance (One-to-One), Prescription (One-to-Many), Appointment (One-to-Many), Nurse (One-to-Many), Medical_History (One-to-One)

LoginPageDoctor Entity:

Attributes: User_id (Primary Key), Doctor_ID (Reference: Doctor), Username, Password
Relationship: Doctor (One-to-One)

LoginPagePatient Entity:

Attributes: User_id (Primary Key), Patient_ID (Reference: Patient), Username, Password
Relationship: Patient (One-to-One)
Medical_History Entity:

Attributes: Record_ID (Primary Key), Patient_ID (Reference: Patient), Pre_Conditions
Relationship: Patient (One-to-One)

Appointment Entity:

Attributes: Appointment_ID (Primary Key), Scheduled_On, Date, Time, Doctor_ID (Reference: Doctor), Patient_ID (Reference: Patient)
Relationships: Doctor (Many-to-One), Patient (Many-to-One)

Nurse Entity:

Attributes: Nurse_ID (Primary Key), Dept_ID (Reference: Department), Patient_ID (Reference: Patient), Emp_ID (Reference: Staff)
Relationships: Department (Many-to-One), Patient (Many-to-One), Staff (Many-to-One)

Staff Entity:

Attributes: Emp_ID (Primary Key), Emp_FName, Emp_LName, Date_Joining, Date_Separation, Emp_Type, Email, Address, Dept_ID (Reference: Department), SSN
Relationships: Department (Many-to-One), Doctor (One-to-One), Nurse (Many-to-One), WageSlip (One-to-One)

Doctor Entity:

Attributes: Doctor_ID (Primary Key), Emp_ID (Reference: Staff), Specialization, Dept_ID (Reference: Department)
Relationship: Staff (One-to-One), Department (Many-to-One)

Department Entity:

Attributes: Dept_ID (Primary Key), Dept_Head, Dept_Name, Emp_Count
Relationships: Doctor (Many-to-One), Staff (Many-to-One), Nurse (Many-to-One)

WageSlip Entity:

Attributes: Account_No (Primary Key), Salary, Bonus, Emp_ID (Reference: Staff), IBAN (CHECK IBAN LIKE ’TR%’)
Relationship: Staff (One-to-One)




Ternary Relationships

Lab Ternary Relationship:

Involves the entities Patient, Doctor, and Lab Technician.
The table(Relation, Entity) Lab connects these entities through foreign keys: Patient_ID, Doctor_ID, and Lab_Techinican_ID.

Represents a scenario where a patient undergoes a lab supervised by a doctor and performed by a technician.

Invoice Ternary Relationship:

Involves the entities Patient, Insurance, and Invoice.
The table(Relation, Entity) Invoice connects these entities through foreign keys: Patient_ID and Policy_Number.

Represents a scenario where a patient's bill is associated with both the patient and their insurance policy.



Functionality

The system allows for the registration and upkeep of thorough medical histories, as well as patient management. With online booking options and comprehensive appointment information, it facilitates appointment administration. Prescription tracking and medication information are included in medical records management. The creation of invoices is automated by billing and invoicing features, which take insurance information, test fees, and room expenses into account. Prescription dispensing and medication inventory management are handled by the pharmacy component. Employee information, work schedules, and departmental connections are all kept on file by staff management. In order to ensure correct tracking of departmental details and doctor-specific information, the system also manages departments and doctors. User authentication and data security are included in the secure login capabilities for physicians and patients. The technology optimizes resource allocation by managing work schedules and appointments as well.

Workload Division

	As it is crucial to have excellent team communication, we will schedule regular in-person and online meetings. Online meetings will enable team members to communicate efficiently virtually without being constrained by space or time. To enliven the team and delve deeper into subjects, face-to-face sessions are planned. GitHub will be the primary repository and version control system for our project.  Because of the simple communication on project files, we will be able to monitor concurrent work and alterations. Successful project completion will be facilitated by this ongoing feedback loop, which will also improve team communication and allow for early error discovery.



Task Name
Responsible Students
Database Design
Duygu Can Gündoğan, Alp Eren Çakmak, Melisa Yurtekin, Yelda Sıla Mumcu
Front-end Development
Alp Eren Çakmak, Yelda Sıla Mumcu
Back-end Development
Duygu Can Gündoğan, Melisa Yurtekin
Testing and Quality Assurance
Duygu Can Gündoğan, Alp Eren Çakmak, Melisa Yurtekin, Yelda Sıla Mumcu

References

https://online.guven.com.tr

https://www.w3schools.com/mysql/mysql_wildcards.asp

https://www.w3schools.com/mysql/mysql_sql.asp


https://www.geeksforgeeks.org/introduction-of-er-model/

https://www.lucidchart.com/pages/landing/er-diagram-software?utm_source=google&utm_medium=cpc&utm_campaign=_chart_ol_tier2-tier3_desktop_search_nb_exact-phrase_&km_CPC_CampaignId=12085241482&km_CPC_AdGroupID=116506691676&km_CPC_Keyword=er%20diagram&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=491652640063&km_CPC_TargetID=kwd-304149638871&km_CPC_Country=1012763&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=Cj0KCQiArrCvBhCNARIsAOkAGcV0ZU2e5gyXF37MCpddKAVYTmFWITufNJe6vcnbNvdR_0JbjT_z5mUaAk7_EALw_wcB

https://www.oracle.com/database/what-is-a-relational-database/#:~:text=A%20relational%20database%20is%20a,of%20representing%20data%20in%20tables.

https://www.baskent.edu.tr/~tkaracay/etudio/ders/prg/java/ch27/JavaSwing.pdf

https://www.javatpoint.com/java-swing

https://www.jetbrains.com/help/idea/mysql.html





































