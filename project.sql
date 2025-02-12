
CREATE DATABASE IF NOT EXISTS Job_System;
USE Job_System;

CREATE TABLE IF NOT EXISTS Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    role ENUM('job_seeker', 'recruiter') NOT NULL
);


CREATE TABLE IF NOT EXISTS Companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    location VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS Jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    company_id INT,
    recruiter_id INT,
    location VARCHAR(255),
    salary DECIMAL(10,2),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id),
    FOREIGN KEY (recruiter_id) REFERENCES Users(user_id)
);


CREATE TABLE IF NOT EXISTS Job_Applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    job_id INT,
    status ENUM('Applied', 'Under Review', 'Hired') DEFAULT 'Applied',
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (job_id) REFERENCES Jobs(job_id)
);


INSERT IGNORE INTO Users (name, email, role) VALUES
('Nikilesha Nivas', 'nick@gmail.com', 'job_seeker'),
('Ashwin', 'ashwin@gmail.com', 'recruiter');


INSERT IGNORE INTO Companies (name, location) VALUES
('TechCorp', 'Chennai'),
('FinServe', 'Bangalore');


INSERT IGNORE INTO Jobs (title, company_id, recruiter_id, location, salary) VALUES
('Software Engineer', 1, 2, 'Chennai', 100000),
('Data Analyst', 2, 2, 'Bangalore', 80000);


INSERT IGNORE INTO Job_Applications (user_id, job_id) VALUES
(1, 1),  -- Nikilesha applies for Software Engineer
(1, 2);  -- Nikilesha applies for Data Analyst


SELECT * FROM Users;

SELECT * FROM Jobs;


SELECT * FROM Job_Applications;


SELECT J.job_id, J.title, C.name AS company, J.location, J.salary
FROM Jobs J
JOIN Companies C ON J.company_id = C.company_id;


SELECT JA.application_id, J.title, C.name AS company, JA.status
FROM Job_Applications JA
JOIN Jobs J ON JA.job_id = J.job_id
JOIN Companies C ON J.company_id = C.company_id
WHERE JA.user_id = 1;  


SELECT J.title, COUNT(JA.application_id) AS num_applications
FROM Job_Applications JA
JOIN Jobs J ON JA.job_id = J.job_id
GROUP BY J.title
ORDER BY num_applications DESC;
