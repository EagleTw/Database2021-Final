# Database2021-Final

* Student

| Column         | Field Type |
| -------------- | ---------- |
| id             | Integer    |
| student_name   | Char       |
| student_dept   | Char       |
| student_status | Char       |
| student_class  | Char       |
|                |            |


* Course_Info 

| Column           | Column 2  |
| ---------------- | --------- |
| id               | Integer   |
| semester         | Char      |
| course_name      | Char      |
| course_type      | Char      |
| location         | Char      |
| course_time      | Char      |
| course_credit    | Integer   |
| course_max_count | Integer   |
| course_status    | Char      |
| teacher          | OneToOne  |
| enroll_students  | OneToMany |
|                  |           |

