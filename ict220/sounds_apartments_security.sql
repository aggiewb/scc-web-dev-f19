/*CREATE USER is the same as CREATE ROLE except that it implies LOGIN */
Create user Manager with password 'password';
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO Manager;
Create role Tenant; 
Grant SELECT on "Lease" to Tenant;
Grant INSERT on "Lease" to Tenant;
Create user jacobtaylor with password 'password';
Grant Tenant to jacobtaylor; 