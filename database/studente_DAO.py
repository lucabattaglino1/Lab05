
from dataclasses import dataclass

@dataclass
class Studente:
    matricola: str
    cognome: str
    nome: str
    CDS: str

    # comparazione tra le chiavi
    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):
        return hash(self.matricola)

    # qui ritorno una stringa dell'insegnamento
    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola}) - {self.CDS} "


