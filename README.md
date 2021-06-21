# Database2021-Final

為中央大學 2021 資料庫設計課程，實際做出課程與學生的關係，並做到第三正規化。

## About
* Web Framework: Django
* Database: sqlite3

## How to start-up

### Pre-Requirementss

* Python3
* Django
    `pip3 install django`


### Run Program

1. `Enter folder`
2. `python3 manage.py makemigrations`
3. `python3 manage.py migrate`
4. `python3 manage.py runserver`
5. Enter browser and type in "127.0.0.1:8000/admin"
6. Enter account and password (admin / 123456)


## Table

* Student

| Entity         | Field Type |
| -------------- | ---------- |
| id             | Integer    |
| student_name   | Char       |
| student_dept   | Char       |
| student_status | Char       |
| student_class  | Char       |


* Course_Info

| Entity           | Field Type |
| ---------------- | ---------- |
| id               | Integer    |
| semester         | Char       |
| course_name      | Char       |
| course_type      | Char       |
| location         | Char       |
| course_time      | Char       |
| course_credit    | Integer    |
| course_max_count | Integer    |
| course_status    | Char       |
| teacher          | OneToOne   |
| enroll_students  | OneToMany  |

* Enroll

| Entity          | Field Type |
| --------------- | ---------- |
| student         | ForeignKey |
| course_info     | ForeignKey |
| feedback_rank   | Integer    |
| selected_result | Char       |
