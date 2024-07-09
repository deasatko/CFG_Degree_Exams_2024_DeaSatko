# Section One: Multiple Choice Questions

```
Q1: A
Q2: C
Q3: D
Q4: C
Q5: B
Q6: B
Q7: B
Q8: A
Q9: B
Q10: A
```

# Section Two: Query Evaluation

**Error in the query**: In the line number `8`, the null comparison used has a syntax error. The fixed line should look like this: `OR department_name IS NULL)`
**Not just one patient**: if we want to visualise not only the one patient with the highest number of admissions, we need to remove the `LIMIT 1`,


**Suggestions**:

1. Since we specifically looking for the `Cardiology` department, there is no need for a null check.
We could improve the query replacing the whole line with: 
```sql
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Cardiology')
```

2. Since there are `8500` patients, we can optimise the query and speed it up using indexes.

```sql
CREATE INDEX idx_admissions_department_id ON admissions(department_id);
CREATE INDEX idx_departments_department_name ON departments(department_name);
CREATE INDEX idx_admissions_admission_date ON admissions(admission_date);
```

3. Improve readability and depending on the database engine also improve performances using `JOIN`.

```sql
SELECT
    a.patient_id,
    COUNT(*) AS admission_count
FROM
    admissions a
JOIN
    departments d ON a.department_id = d.department_id
WHERE
    d.department_name = 'Cardiology'
    AND a.admission_date >= '2015-01-01'
GROUP BY
    a.patient_id
ORDER BY
    admission_count DESC
```