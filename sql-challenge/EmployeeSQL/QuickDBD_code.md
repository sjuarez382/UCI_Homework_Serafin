# SQL Homework - Quick Database Diagram

departments
-
dept_no PK varchar
dept_name varchar

dept_emp
-
emp_no int
dept_no varchar


dept_manager
-
dept_no varchar FK >- departments.dept_no
emp_no int FK - employees.emp_no



employees
-
emp_no PK int FK -< dept_emp.emp_no
title_id varchar
birth_date date
first_name varchar
last_name varchar
sex varchar
hire_date date

salaries
-
emp_no integer FK - employees.emp_no
salary integer


titles
-
title_id varchar PK FK >- employees.title_id
title varchar
