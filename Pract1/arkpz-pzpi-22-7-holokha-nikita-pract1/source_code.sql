-- 1
SELECT employee.id, employee.name, department.name AS dept_name
FROM employee
JOIN department ON employee.dept_id = department.id
WHERE department.location = 'Kyiv';

-- 2
SELECT
    employee.id,
    employee.name,
    department.name AS dept_name
FROM
    employee
JOIN
    department
    ON employee.dept_id = department.id
WHERE
    department.location = 'Kyiv';

-- 3
SELECT
    e.id,
    e.name,
    d.name AS dept_name
FROM
    employee AS e
JOIN
    department AS d
    ON e.dept_id = d.id
WHERE
    d.location = 'Kyiv';

-- 4
SELECT
    e.id,
    e.name,
    d.name AS dept_name
FROM
    employee AS e
JOIN
    department AS d
    ON e.dept_id = d.id
WHERE
    d.location = 'Kyiv'
    AND (
        e.position = 'Manager'
        OR e.salary > 3000
    );

-- 5
/*
  Запит: виводимо список менеджерів або тих,
  хто має зарплату вище 3000
  і працює у відділі, розташованому в Києві
*/
SELECT
    e.id,
    e.name,
    d.name AS dept_name
FROM
    employee AS e
JOIN
    department AS d
    ON e.dept_id = d.id
WHERE
    d.location = 'Kyiv'         -- Фільтр за містом
    AND (
        e.position = 'Manager'  -- Менеджери
        OR e.salary > 3000      -- або з високою зарплатою
    );

-- 6
-- Не рекомендовано
SELECT *
FROM employee;

-- Рекомендовано
SELECT
    id,
    name,
    position,
    salary
FROM employee;

-- 7
SELECT
    e.id,
    e.name,
    d.name AS dept_name
FROM
    employee AS e
JOIN
    department AS d
    ON e.dept_id = d.id
WHERE
    (e.position = 'Manager' AND e.salary > 3000)
    OR (d.location = 'Kyiv' AND e.status = 'Active');

-- 8
SELECT
    e.id,
    e.name,
    d.name AS dept_name,
    p.project_name
FROM
    employee AS e
JOIN
    department AS d ON e.dept_id = d.id
LEFT JOIN
    projects AS p ON e.id = p.employee_id
WHERE
    d.location = 'Kyiv';

-- 9
SELECT
    s.emp_id,
    s.salary
FROM
    hr_schema.employee_salary AS s
WHERE
    s.salary > 3000;

