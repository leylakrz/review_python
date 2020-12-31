import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="iris",
    user="postgres",
    password="1997713"
)


def insert(values):
    cursor = conn.cursor()
    select_query = "insert into iris_table(sepal_length, sepal_width, petal_length, petal_width, variety)" \
                   " values({},{},{},{},\'{}\')".format(*values)
    cursor.execute(select_query)
    # role_records = cursor.fetchall()
    # print(role_records)
    conn.commit()
    select_all()


def select_all():
    cursor = conn.cursor()
    select_query = "select * from iris_table"
    cursor.execute(select_query)
    role_records = cursor.fetchall()
    print(role_records)

