import sqlite3 #biblioteka do pracy na sqlite


conn = sqlite3.connect('organizer.db') #tworzymy polaczenie z baza danych z pliku

c = conn.cursor() # trzeba wywolac aby moc uzywac pozniej execute

#tworzy tabele (przy kolejnych wywolaniach bedzie zwracac blad jezeli tabela juz istnieje)
try:
    c.execute("""CREATE TABLE mpn (
                current_date text,
                total_qty integer,
                new integer,
                done integer
    )""")
except sqlite3.OperationalError:
    print("table already exist")

# c.execute("INSERT INTO mpn VALUES ('2019-06-26', 124, 0, 0)") #dodaje do tabeli rekord
# conn.commit() #dobrze jest to wywolac po kazdym query

#aby dodac do tabeli rekordy korzystajac ze zmiennych:
# data1 = '2019-06-27'
# total1 = 127
# new1 = 6
# done1 = 3
#
# c.execute("INSERT INTO mpn VALUES (:current_date, :total_qty, :new, :done)",
#           {'current_date':data1, 'total_qty':total1, 'new':new1, 'done':done1}) #dodaje do tabeli rekord gdzie dane umieszczamy w slowniku
# conn.commit() #dobrze jest to wywolac po kazdym query

c.execute("SELECT * FROM mpn") #query do bazy danych
# c.execute("SELECT * FROM mpn WHERE current_date='2019-06-26'") #query do bazy danych
# c.execute("SELECT * FROM mpn WHERE new=0") #query do bazy danych


# print(c.fetchone()) #zwraca jeden rekord na raz (mozna iterowac)
# print(c.fetchmany(5)) #zwraca dana ilosc rekordow jako liste
print(c.fetchall()) #zwraca wszystkie rekordy za zapytania

conn.commit() #odsyla do wykonania wszystkie zmianny

conn.close() #zamyka polaczenie z baza danych