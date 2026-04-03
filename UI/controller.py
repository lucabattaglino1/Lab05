import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

        # lista corsi salvata (serve per recuperare oggetto completo)
        self._corsi = []

        # valore selezionato
        self._SelezionareCorsoValue = None

    def fillSelezionareCorso(self):
        # prendo i corsi dal model
        self._corsi = self._model.getAllCorsi()

        # svuoto eventuali opzioni precedenti
        self._view.SelezionareCorso.options.clear()

        # riempio dropdown
        for c in self._corsi:
            self._view.SelezionareCorso.options.append(
                ft.dropdown.Option(
                    key=c.codins,
                    text=f"{c.nome} ({c.codins})"
                )
            )

        # aggiorno la UI
        self._view.update_page()

    def handleSelezioneCorso(self, e):
        codins = e.control.value

        # cerco il corso selezionato
        for c in self._corsi:
            if c.codins == codins:
                self._SelezionareCorsoValue = c
                break

        print(self._SelezionareCorsoValue)

    def handleCercaIscritti(self,e):
        self._view.txt_result.controls.clear()
        if self._SelezionareCorsoValue is None:
            self._view.txt_result.controls.append(ft.Text("Perfavore selezionare un corso"))
            self._view.update_page()
            return

        # se arrivo qui posso recuperare gli studenti
        studenti = self._model.getStudentiCorso(self._SelezionareCorsoValue.codins)

        if not len(studenti):
            self._view.txt_result.controls.append(
                ft.Text("Nessuno studente iscritto al corso}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito gli studenti iscritti sl corso {self._SelezionareCorsoValue}"))

        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))

        self._view.update_page()

    def handleCercaStudente(self, e):
        # pulisco output
        self._view.txt_result.controls.clear()

        matricola = self._view._txt_input_m.value

        # controllo input vuoto
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return

        # recupero dati dal model
        studenti = self._model.getCercaStudente(matricola)

        # se non trovato
        if not studenti:
            self._view.create_alert("Matricola non trovata!")
            return

        # prendo lo studente (è uno solo)
        studente = studenti[0]

        # riempio automaticamente i campi
        self._view._txt_input_n.value = studente.nome
        self._view._txt_input_c.value = studente.cognome

        # opzionale: stampa info sotto
        self._view.txt_result.controls.append(
            ft.Text(f"Trovato: {studente}")
        )

        self._view.update_page()

    def handleCercaCorsi(self,e):
        pass

    def handleIscrivi(self,e):
        pass