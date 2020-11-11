--List the following details of each employee: employee number, last name, first name, sex, and salary.
select e.emp_no, e.last_name, e.first_name, e.sex, s.salary
from employees as e
left join salaries as s
on e.emp_no = s.emp_no
order by salary desc;

--List first name, last name, and hire date for employees who were hired in 1986.
select emp_no, last_name, first_name, hire_date
from employees
where hire_date between '1986/1/1' and '1986/12/31'
order by emp_no;

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.
select d.dept_no, d.dept_name, e.emp_no, e.last_name, e.first_name
from employees as e
inner join dept_emp as de
on e.emp_no = de.emp_no
inner join dept_manager as dm
on de.emp_no = dm.emp_no
inner join departments as d
on d.dept_no = dm.dept_no
order by emp_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.
select de.emp_no, e.last_name, e.first_name, d.dept_name
from dept_emp as de
inner join departments as d
on d.dept_no = de.dept_no
inner join employees as e
on e.emp_no = de.emp_no
order  by emp_no;

--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."
select * from employees
where first_name = 'Hercules' and last_name like 'B%'
order by last_name;


--List all employees in the Sales department, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name 
from employees as e
inner join dept_emp as de
on de.emp_no = e.emp_no
inner join departments as d
on de.dept_no = d.dept_no
where dept_name = 'Sales'
order by emp_no;

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select e.emp_no, e.last_name, e.first_name, d.dept_name
from employees as e
inner join dept_emp as de
on de.emp_no = e.emp_no
inner join departments as d
on de.dept_no = d.dept_no
where dept_name = 'Sales' or dept_name = 'Development'
order by emp_no;

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, COUNT(last_name) as last_name_count
from employees
group by last_name
order by last_name_count DESC;


