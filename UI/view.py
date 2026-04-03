import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.SelezionareCorso = ft.Dropdown(
            label="Selezionare un corso",
            width=500,
            on_change=self._controller.handleSelezioneCorso
        )
        # chiamo il metodo implementato nel controller per riempire il menu a tendina
        self._controller.fillSelezionareCorso()

        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca Iscritti",
                                                        on_click=self._controller.handleCercaIscritti,
                                                        width=150)

        row1 = ft.Row([self.SelezionareCorso, self.btnCercaIscritti])

        self._txt_input_m = ft.TextField(label="matricola", width=150)
        self._txt_input_n = ft.TextField(label="nome", width=150)
        self._txt_input_c = ft.TextField(label="cognome", width=150)

        row2 = ft.Row([self._txt_input_m, self._txt_input_n, self._txt_input_c])

        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                        on_click=self._controller.handleCercaStudente,
                                                        width=150)

        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi",
                                                        on_click=self._controller.handleCercaCorsi,
                                                        width=150)

        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi",
                                                        on_click=self._controller.handleIscrivi,
                                                        width=150)

        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi])

        self._page.add(row1, row2, row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
