# Add whatever it is needed to interface with the DB Table corso
from model.corso import Corso
from model.studente import Studente
from database import DB_connect
from database.DB_connect import get_connection

class corso_DAO:

    # per popolare il dropdown corsi
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

        query = """SELECT *
                   FROM studente
                   WHERE matricola = %s"""
        # risultato --> [Studente("123", "Rossi", "Mario", "INFO")]

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    # controllo esistenza studente
    @staticmethod
    def getStudenteByMatricola(matricola):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT *
                   FROM studente 
                   where matricola = %s"""

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res


    # corsi dello studente
    @staticmethod
    def getCorsiStudente(matricola):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # "prendi tutti i corsi a cui lo studente è iscritto"
        query = """SELECT c.*
                   FROM corso c, iscrizione i
                   where c.codins = i.codins
                    and i.matricola = %s"""

        cursor.execute(query, (matricola,))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res


    # PUNTO 5 --> obiettivo: iscrivere uno studente al corso cioè scrivere
    # una riga nel database cosi: iscrizione(matricola, codins)

    @staticmethod
    def getIscriviStudente(codins, matricola):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        #questa query aggiunge una nuova riga nella tabella iscrizione
        query = """INSERT INTO iscrizione (matricola, codins)
               VALUES (%s, %s)"""

        cursor.execute(query, (matricola, codins)) #esecuzione (manda la query al database)
        cnx.commit()  # IMPORTANTISSIMO (la query viene salvata nel database)

        cursor.close()
        cnx.close()

    # aggiungo questo controllo extra per evitare i duplicati
    @staticmethod
    def getIsIscritto(matricola, codins):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # query evita duplicati, rischio di inserire una riga già presente
        query = """SELECT *
                   FROM iscrizione
                   WHERE matricola = %s AND codins = %s"""

        cursor.execute(query, (matricola, codins))

        res = cursor.fetchall()

        cursor.close()
        cnx.close()
        # il return mi darà True se è già iscritto e False se posso iscrivere
        return len(res) > 0