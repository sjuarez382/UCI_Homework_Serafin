# SQL Homework - Quick Database Diagram

departments
-
dept_no PK varchar
dept_name varchar

dept_emp
-
emp_no PK int FK - dept_manager.emp_no
dept_no PK varchar FK >- departments.dept_no
from_date date
to_date date

dept_manager
-
emp_no PK int FK - employees.emp_no
dept_no varchar FK >- departments.dept_no
from_date date
to_date date

employees
-
emp_no PK int FK -< dept_emp.emp_no
birth_date date
first_name varchar
last_name varchar
gender varchar
hire_date date

salaries
-
emp_no PK integer FK - employees.emp_no
salary integer
from_date date
to_date date

titles
-
emp_no int PK FK >- employees.emp_no
title varchar
from_date date PK
to_date date

