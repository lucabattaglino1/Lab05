from database.corso_DAO import corso_DAO


class Model:
    def __init__(self):
        pass

    def getAllCorsi(self):
        return corso_DAO.getAllCorsi()

    def getStudentiCorso(self,codins):
        return corso_DAO.getStudentiCorso(codins)

    def getCercaStudente(self, matricola):
        return corso_DAO.getCercaStudente(matricola)

    def getStudenteByMatricola(self, matricola):
        return corso_DAO.getStudenteByMatricola(matricola)

    def getCorsiStudente(self, matricola):
        return corso_DAO.getCorsiStudente(matricola)

    def getIscriviStudente(self, codins, matricola):
        return corso_DAO.getIscriviStudente(codins, matricola)

    def getIsIscritto(self, matricola, codins):
        return corso_DAO.getIsIscritto(matricola, codins)