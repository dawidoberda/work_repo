import sqlite3

#TODO: sprawdzic czy bedzie dzialac jak tworzenie polaczenie do bazy bedzie tutaj
conn = sqlite3.connect('organizer.db')
c = conn.cursor()


def create_mpn_table():
    try:
        c.execute("""CREATE TABLE mpn (
                    current_date text,
                    total_qty integer,
                    new integer,
                    done integer
        )""")
    except sqlite3.OperationalError:
        print("table already exist")


def fill_mpn_tabel():
    with conn:
        c.execute("INSERT INTO mpn VALUES ('2019-06-26', 52, 0, 0)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-27', 66, 14, 21)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-28', 50, 5, 32)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-29', 26, 8, 4)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-30', 34, 12, 0)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-01', 40, 6, 8)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-02', 53, 21, 34)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-03', 22, 3, 7)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-04', 17, 2, 0)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-05', 31, 14, 11)")


def fill_hs_tabel():
    with conn:
        c.execute("INSERT INTO mpn VALUES ('2019-06-26', 52, 0, 0)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-27', 66, 14, 21)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-28', 50, 5, 32)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-29', 26, 8, 4)")
        c.execute("INSERT INTO mpn VALUES ('2019-06-30', 34, 12, 0)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-01', 40, 6, 8)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-02', 53, 21, 34)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-03', 22, 3, 7)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-04', 17, 2, 0)")
        c.execute("INSERT INTO mpn VALUES ('2019-07-05', 31, 14, 11)")

def return_all_from_mpn():
    #TODO: zrobic funkcje do przegladania calej tablicy mpn
    pass


# def insert_mpn(date,qty,new_qty,done_qty):
#     with conn: #mozna uzyc contex menagera i nie trzeba robic commit
#         c.execute("INSERT INTO mpn VALUES (:current_date, :total_qty, :new, :done)",
#                   {'current_date':date, 'total_qty':qty, 'new':new_qty, 'done':done_qty})


conn.commit() #odsyla do wykonania wszystkie zmianny

conn.close() #zamyka polaczenie z baza danych