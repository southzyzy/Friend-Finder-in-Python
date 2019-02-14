import wx

APP_EXIT = 1
FILE_SAVE = 2
FILE_OPEN = 3
SHOW_HELP = 4
SHOW_ABOUT = 5


class MainFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.InitUI()

    def InitUI(self):
        self.InitMenus()
        self.InitMainPanel()

        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap("./img/icon.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)

        self.SetSize((800, 500))
        self.SetTitle('ICT1002 Friend Finder GUI')
        self.Center()
        self.Show(True)

    def InitMainPanel(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        panel.SetSizer(vbox)
        panel.SetBackgroundColour('white')

        st = wx.StaticLine(panel, wx.ID_ANY, style=wx.LI_VERTICAL)
        vbox.Add(st, 0, wx.ALL | wx.EXPAND, 10)

        welcome_page = wx.StaticText(panel, id=wx.ID_ANY, label="ICT1002 Friend Finder",
                                     name="WelcomePage")
        welcome_page.SetFont(
            wx.Font(18, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Open Sans"))
        vbox.Add(welcome_page, proportion=0, flag=wx.ALIGN_CENTER_HORIZONTAL, border=20)

        st = wx.StaticLine(panel, wx.ID_ANY, style=wx.LI_VERTICAL)
        vbox.Add(st, 0, wx.ALL | wx.EXPAND, 10)

        self.options = ['1. List all the profiles.',
                        '2. List all the matched students of one given student B based on country.',
                        '3. List the top 3 best matched students who share the most similar likes or dislikes for one given student B.',
                        '4. List the top 3 best matched students based on books they like.',
                        '5. List the top 3 best matched students based on the overall profile information which may include all the personal information for ranking.',
                        '6. Store all the best matched students into one .csv file on the disk.',
                        '7. Running the open Function.', '8. Clear Screen (Enter 8 to clear screen)',
                        '9. Exit the program.']

        lst = wx.ListBox(panel, size=(100, -1), choices=self.options, style=wx.LB_SINGLE)
        lst.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman"))

        vbox.Add(lst, 1, wx.EXPAND | wx.ALL, 20)

        self.Bind(wx.EVT_LISTBOX, self.onListBox, lst)

        # add main widgets
        widgets = self.loadWidgets(panel)
        fgs = wx.FlexGridSizer(rows=len(widgets), cols=2, vgap=10, hgap=15)
        fgs.AddMany([(widget) for widget in widgets])
        vbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=20)

        # add button box
        button_box = wx.StdDialogButtonSizer()
        ok_button = wx.Button(panel, wx.ID_OK, label='Run')  # create the ok button
        cancel_button = wx.Button(panel, wx.ID_CANCEL)  # create the cancel button
        button_box.AddButton(ok_button)  # add the ok button
        button_box.AddButton(cancel_button)  # add the cancel button
        button_box.Realize()
        vbox.Add(button_box, flag=wx.ALIGN_RIGHT | wx.BOTTOM, border=20)

        # Activate the cancel button to close it
        self.Bind(wx.EVT_BUTTON, self.OnQuit, id=wx.ID_CANCEL)

        vbox.Fit(self)

    def loadWidgets(self, panel):
        widgets = []

        text_control_label = wx.StaticText(panel, label='Open File')
        textControl = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        widgets.append(text_control_label)
        widgets.append(textControl)

        combobox_label = wx.StaticText(panel, label='Selection')
        self.combobox = wx.ComboBox(panel, choices=self.options, size=(600, -1))
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
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        openMenuItem = wx.MenuItem(fileMenu, FILE_OPEN, '&Open\tCtrl+O')
        saveMenuItem = wx.MenuItem(fileMenu, FILE_SAVE, '&Save\tCtrl+S')
        quitMenuItem = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        fileMenu.AppendItem(openMenuItem)
        fileMenu.AppendItem(saveMenuItem)
        fileMenu.AppendItem(quitMenuItem)
        menubar.Append(fileMenu, '&File')
        self.Bind(wx.EVT_MENU, self.OnOpen, id=FILE_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave, id=FILE_SAVE)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        helpMenu = wx.Menu()
        helpMenuItem = wx.MenuItem(helpMenu, SHOW_HELP, '&Help\tCtrl+H')
        aboutMenuItem = wx.MenuItem(helpMenu, SHOW_ABOUT, '$About App\tCtrl+A')
        helpMenu.AppendItem(aboutMenuItem)
        helpMenu.AppendItem(helpMenuItem)
        menubar.Append(helpMenu, 'Help')
        self.Bind(wx.EVT_MENU, self.ShowHelp, id=SHOW_HELP)
        self.Bind(wx.EVT_MENU, self.ShowAbout, id=SHOW_ABOUT)

        self.SetMenuBar(menubar)

    def ShowHelp(self, e):
        print 'Display help. Maybe open online help via a wx.html.HtmlWindow (or in a browser)'

    def ShowAbout(self, e):
        about_text = 'Put info about the application here, e.g., name, author(s), version, license, etc.'
        dlg = wx.MessageDialog(self, about_text, 'About App', wx.OK)  # wx.OK|wx.ICON_INFORMATION
        result = dlg.ShowModal()
        dlg.Destroy()

    def OnQuit(self, e):
        self.Close()

    def OnSave(self, e):
        saveFileDialog = wx.FileDialog(self, 'Save your file', '', '',
                                       'XYZ files (*.xyz)|*.xyz', wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return

    def OnOpen(self, e):
        openFileDialog = wx.FileDialog(self, 'Open a file', '', '',
                                       'XYZ files (*.xyz)|*.xyz', wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        print 'Open file %s' % openFileDialog.GetPath()

    def onListBox(self, e):
        choice_str = e.GetEventObject().GetStringSelection()
        self.combobox.SetValue(choice_str)


def main():
    ex = wx.App()
    frame = MainFrame(None)
    frame.Show(True)
    ex.MainLoop()


if __name__ == '__main__':
    main()
