from wx import *
# only in app's startup  module
from wx.lib.pubsub import setuparg1
# in all modules that use pubsub
from wx.lib.pubsub import pub as Publisher

APP_EXIT = 1
FILE_SAVE = 2
FILE_OPEN = 3
SHOW_HELP = 4
SHOW_ABOUT = 5


class MainFrame(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.InitMenus()
        self.InitMainPanel()

        icon = Icon()
        icon.CopyFromBitmap(Bitmap("./img/icon.ico", BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        self.SetSize((800, 500))
        self.SetTitle('ICT1002 Friend Finder GUI')
        self.Center()
        self.Show(True)

    def InitMainPanel(self):
        panel = Panel(self)
        vbox = BoxSizer(VERTICAL)

        panel.SetSizer(vbox)
        panel.SetBackgroundColour('white')

        st = StaticLine(panel, ID_ANY, style=LI_VERTICAL)
        vbox.Add(st, 0, ALL | EXPAND, 10)

        welcome_page = StaticText(panel, id=ID_ANY, label="ICT1002 Friend Finder",
                                  name="WelcomePage")
        welcome_page.SetFont(
            Font(18, FONTFAMILY_MODERN, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL, False, "Open Sans"))
        vbox.Add(welcome_page, proportion=0, flag=ALIGN_CENTER_HORIZONTAL, border=20)

        st = StaticLine(panel, ID_ANY, style=LI_VERTICAL)
        vbox.Add(st, 0, ALL | EXPAND, 10)

        self.options = ['1. List all the profiles.',
                        '2. List all the matched students of one given student B based on country.',
                        '3. List the top 3 best matched students who share the most similar likes or dislikes for one given student B.',
                        '4. List the top 3 best matched students based on books they like.',
                        '5. List the top 3 best matched students based on the overall profile information which may include all the personal information for ranking.',
                        '6. Store all the best matched students into one .csv file on the disk.',
                        '7. Running the open Function.', '8. Clear Screen (Enter 8 to clear screen)',
                        '9. Exit the program.']

        lst = ListBox(panel, size=(100, -1), choices=self.options, style=LB_SINGLE)
        lst.SetFont(
            Font(10, FONTFAMILY_MODERN, FONTSTYLE_NORMAL, FONTWEIGHT_NORMAL, False, "Times New Roman"))

        vbox.Add(lst, 1, EXPAND | ALL, 20)

        # add main widgets
        widgets = self.loadWidgets(panel)
        fgs = FlexGridSizer(rows=len(widgets), cols=2, vgap=10, hgap=15)
        fgs.AddMany([(widget) for widget in widgets])
        vbox.Add(fgs, proportion=1, flag=ALL | EXPAND, border=20)

        # add button box
        button_box = StdDialogButtonSizer()
        ok_button = Button(panel, ID_OK, label='Run')  # create the ok button
        cancel_button = Button(panel, ID_CANCEL)  # create the cancel button
        button_box.AddButton(ok_button)  # add the ok button
        button_box.AddButton(cancel_button)  # add the cancel button
        button_box.Realize()
        vbox.Add(button_box, flag=ALIGN_RIGHT | BOTTOM, border=20)

        # Activate the cancel button to close it
        self.Bind(EVT_LISTBOX, self.onListBox, lst)
        self.Bind(EVT_BUTTON, self.onRun, id=ID_OK)
        self.Bind(EVT_BUTTON, self.OnQuit, id=ID_CANCEL)

        vbox.Fit(self)

    def loadWidgets(self, panel):
        widgets = []

        api_dir_label = StaticText(panel, label='Specify API Directory')
        self.api_file_dir = FilePickerCtrl(panel, id=ID_ANY, path="",
                                           message=FileSelectorPromptStr, wildcard=FileSelectorDefaultWildcardStr,
                                           pos=DefaultPosition, size=(600, -1), style=FLP_DEFAULT_STYLE,
                                           validator=DefaultValidator, name=FilePickerCtrlNameStr)

        widgets.append(api_dir_label)
        widgets.append(self.api_file_dir)

        profiles_dir_label = StaticText(panel, label='Specify Profiles Directory')
        self.profiles_dir_label = DirPickerCtrl(panel, id=ID_ANY, path="",
                                                message=DirSelectorPromptStr, pos=DefaultPosition, size=(600, -1),
                                                style=DIRP_DEFAULT_STYLE, validator=DefaultValidator,
                                                name=DirPickerCtrlNameStr)

        widgets.append(profiles_dir_label)
        widgets.append(self.profiles_dir_label)

        combobox_label = StaticText(panel, label='Selection')
        self.combobox = ComboBox(panel, choices=self.options, size=(600, -1))
        widgets.append(combobox_label)
        widgets.append(self.combobox)

        return widgets

    def OnCheckboxChange(self, event):
        sender = event.GetEventObject()
        isChecked = sender.GetValue()
        if isChecked:
            print 'Checkbox selected'
        else:
            print 'Checkbox unselected'

    def InitMenus(self):
        menubar = MenuBar()

        fileMenu = Menu()
        openMenuItem = MenuItem(fileMenu, FILE_OPEN, '&Open\tCtrl+O')
        saveMenuItem = MenuItem(fileMenu, FILE_SAVE, '&Save\tCtrl+S')
        quitMenuItem = MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        fileMenu.AppendItem(openMenuItem)
        fileMenu.AppendItem(saveMenuItem)
        fileMenu.AppendItem(quitMenuItem)
        menubar.Append(fileMenu, '&File')
        self.Bind(EVT_MENU, self.OnOpen, id=FILE_OPEN)
        self.Bind(EVT_MENU, self.OnSave, id=FILE_SAVE)
        self.Bind(EVT_MENU, self.OnQuit, id=APP_EXIT)

        helpMenu = Menu()
        helpMenuItem = MenuItem(helpMenu, SHOW_HELP, '&Help\tCtrl+H')
        aboutMenuItem = MenuItem(helpMenu, SHOW_ABOUT, '$About App\tCtrl+A')
        helpMenu.AppendItem(aboutMenuItem)
        helpMenu.AppendItem(helpMenuItem)
        menubar.Append(helpMenu, 'Help')
        self.Bind(EVT_MENU, self.ShowHelp, id=SHOW_HELP)
        self.Bind(EVT_MENU, self.ShowAbout, id=SHOW_ABOUT)

        self.SetMenuBar(menubar)

    def ShowHelp(self, e):
        print 'Display help. Maybe open online help via a html.HtmlWindow (or in a browser)'

    def ShowAbout(self, e):
        about_text = 'Put info about the application here, e.g., name, author(s), version, license, etc.'
        dlg = MessageDialog(self, about_text, 'About App', OK)  # OK|ICON_INFORMATION
        result = dlg.ShowModal()
        dlg.Destroy()

    def OnQuit(self, e):
        self.Close()

    def OnSave(self, e):
        saveFileDialog = FileDialog(self, 'Save your file', '', '',
                                    'XYZ files (*.xyz)|*.xyz', FD_SAVE | FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == ID_CANCEL:
            return

    def OnOpen(self, e):
        openFileDialog = FileDialog(self, 'Open a file', '', '',
                                    'XYZ files (*.xyz)|*.xyz', FD_OPEN | FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == ID_CANCEL:
            return
        print 'Open file %s' % openFileDialog.GetPath()

    def onListBox(self, e):
        choice_str = e.GetEventObject().GetStringSelection()
        self.combobox.SetValue(choice_str)

    def onRun(self, e):
        print self.api_file_dir.GetPath()
        print self.profiles_dir_label.GetPath()
        print self.combobox.GetValue()


def main():
    ex = App()
    frame = MainFrame(None)
    frame.Show(True)
    ex.MainLoop()


if __name__ == '__main__':
    main()
