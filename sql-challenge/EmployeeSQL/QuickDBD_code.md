# SQL Homework - Quick Database Diagram

departments
-
dept_no PK varchar(4)
dept_name varchar(255)

dept_emp
-
emp_no int FK - employees.emp_no
dept_no varchar(4) FK - departments.dept_no


dept_manager
-
dept_no varchar(4) FK - departments.dept_no
emp_no int FK - employees.emp_no



employees
-
emp_no PK int
title_id varchar(10) FK - titles.title_id
birth_date date
first_name varchar(255)
last_name varchar(255)
sex char
hire_date date

salaries
-
emp_no int FK - employees.emp_no
salary int


titles
-
title_id varchar(10) PK
title varchar(255)