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

1. `git clone https://github.com/Masa1u/Database2021-Final`
2. `cd Database2021-Final`
3. `python3 manage.py makemigrations`
4. `python3 manage.py migrate`
5. `python3 manage.py runserver`
6. Enter browser and type in "127.0.0.1:8000/admin"
7. Enter account and password (admin / 123456)

你就可以透過寫好的頁面看到所有資料庫欄位設計的樣子，包括正規化。

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
