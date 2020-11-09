# SQL Homework - Quick Database Diagram

departments
-
dept_no PK varchar
dept_name varchar

dept_emp
-
emp_no PK int FK - dept_manager.emp_no
dept_no PK varchar FK >- departments.dept_no


dept_manager
-
dept_no varchar FK >- departments.dept_no
emp_no PK int FK - employees.emp_no



employees
-
emp_no PK int FK -< dept_emp.emp_no
emp_title int
birth_date date
first_name varchar
last_name varchar
sex varchar
hire_date date

salaries
-
emp_no PK integer FK - employees.emp_no
salary integer


titles
-
title_id int PK FK >- employees.emp_title
title varchar