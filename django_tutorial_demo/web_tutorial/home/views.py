from django.db import connection
from django.shortcuts import render
import pyodbc

def student_info(request):
    server = 'NHANCSER\SQLEXPRESS'
    driver = 'SQL Server'
    database = 'WEB_TUTO'
    conn = pyodbc.connect(f'Driver={driver}; Server={server}; Database={database}; Trusted_Connection=yes;')
    cursor = conn.cursor()
    STUDENT_INFO = cursor.execute("SELECT * FROM STUDENT_INFO")
    STUDENT_INFO = cursor.fetchall()
    return render(request, 'index/student_info.html', {'STUDENT_INFO':STUDENT_INFO})

def index_page(request):
    return render(request, 'index/index.html')

def login(request):
    return '<h1>This is login page</h1>'