# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from model.studente import Studente
from database import DB_connect
from database.DB_connect import get_connection

class corso_DAO:

    @staticmethod
    def getAllCorsi():
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # con l'asterisco leggo tutto
        query = """select * FROM corso"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.*
                   FROM studente s, iscrizione i
                   WHERE s.matricola = i.matricola
                   and i.codins = %s"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCercaStudente(matricola):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.cognome, s.nome
                    FROM studente s
                    where matricola = %s"""

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Studente(
                cognome=row["cognome"],
                nome=row["nome"]
            ))

        cursor.close()
        cnx.close()
        return res

