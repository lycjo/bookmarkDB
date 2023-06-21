import wx
import wx.xrc
from wx.html2 import WebView
import sqlite3 as lite
import webbrowser

import create_user_module
import clue_module

# 設定chorme.exe的路徑好讀取並用chrome開啟
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
conn = lite.connect('bookmark.db')
cur = conn.cursor()

###########################################################################
# Class MyFrame
###########################################################################


class MyFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            718, 418), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook2 = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.user_panel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText12 = wx.StaticText(
            self.user_panel, wx.ID_ANY, u"使 用 者 登 錄", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)

        self.m_staticText12.SetFont(wx.Font(
            36, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))
        self.m_staticText12.SetBackgroundColour(wx.Colour(228, 254, 236))

        bSizer5.Add(self.m_staticText12, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        gSizer61 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText13 = wx.StaticText(
            self.user_panel, wx.ID_ANY, u"帳號:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)

        self.m_staticText13.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))
        self.m_staticText13.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        gSizer61.Add(self.m_staticText13, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.user_textCtrl = wx.TextCtrl(
            self.user_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        gSizer61.Add(self.user_textCtrl, 0, wx.ALL, 5)

        gSizer61.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer61.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText14 = wx.StaticText(
            self.user_panel, wx.ID_ANY, u"密碼:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        self.m_staticText14.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer61.Add(self.m_staticText14, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.password_textCtrl = wx.TextCtrl(
            self.user_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        gSizer61.Add(self.password_textCtrl, 0, wx.ALL, 5)

        gSizer61.Add((0, 0), 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.login_bt = wx.Button(
            self.user_panel, wx.ID_ANY, u"登錄", wx.DefaultPosition, wx.Size(150, 30), 0)
        self.login_bt.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer61.Add(self.login_bt, 0, wx.ALL | wx.ALIGN_RIGHT |
                     wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer4.Add(gSizer61, 1, wx.EXPAND, 5)

        gSizer11 = wx.GridSizer(0, 2, 0, 0)

        gSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer11.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText29 = wx.StaticText(
            self.user_panel, wx.ID_ANY, u"忘記密碼?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText29.Wrap(-1)

        self.m_staticText29.SetFont(wx.Font(
            14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer11.Add(self.m_staticText29, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText30 = wx.StaticText(
            self.user_panel, wx.ID_ANY, u"沒有帳號?", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)

        self.m_staticText30.SetFont(wx.Font(
            14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer11.Add(self.m_staticText30, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.forget_paaword_bt = wx.Button(
            self.user_panel, wx.ID_ANY, u"密碼提示", wx.DefaultPosition, wx.DefaultSize, 0)
        self.forget_paaword_bt.SetFont(wx.Font(
            12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer11.Add(self.forget_paaword_bt, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.create_user_bt = wx.Button(
            self.user_panel, wx.ID_ANY, u"創建帳號", wx.DefaultPosition, wx.DefaultSize, 0)
        self.create_user_bt.SetFont(wx.Font(
            12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer11.Add(self.create_user_bt, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer4.Add(gSizer11, 1, wx.EXPAND, 5)

        self.user_panel.SetSizer(bSizer4)
        self.user_panel.Layout()
        bSizer4.Fit(self.user_panel)
        self.m_notebook2.AddPage(self.user_panel, u"使用者介面", True)

######################################################################
# add_mark_pannel
######################################################################

        self.add_mark_panel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.add_mark_panel.Enable(False)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText1 = wx.StaticText(
            self.add_mark_panel, wx.ID_ANY, u"書籤名稱:", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_staticText1, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.mark_name_textCtrl = wx.TextCtrl(
            self.add_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(320, 25), 0)
        gSizer1.Add(self.mark_name_textCtrl, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(
            self.add_mark_panel, wx.ID_ANY, u"書籤類別:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_staticText2, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.mark_type_textCtrl = wx.TextCtrl(
            self.add_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(320, 25), 0)
        gSizer1.Add(self.mark_type_textCtrl, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(
            self.add_mark_panel, wx.ID_ANY, u"網址:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_staticText3, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.URL_textCtrl = wx.TextCtrl(
            self.add_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(320, 25), 0)
        gSizer1.Add(self.URL_textCtrl, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button1 = wx.Button(
            self.add_mark_panel, wx.ID_ANY, u"儲存書籤", wx.Point(-1, -1), wx.Size(150, 40), 0)
        self.m_button1.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.add_mark_panel.SetSizer(gSizer1)
        self.add_mark_panel.Layout()
        gSizer1.Fit(self.add_mark_panel)
        self.m_notebook2.AddPage(self.add_mark_panel, u"新增書籤", False)

######################################################################
# open_mark_pannel
######################################################################

        self.open_mark_panel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.open_mark_panel.Enable(False)
        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText4 = wx.StaticText(
            self.open_mark_panel, wx.ID_ANY, u"選擇類別", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        self.m_staticText4.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer6.Add(self.m_staticText4, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        type_choose_comboBoxChoices = []
        self.type_choose_comboBox = wx.ComboBox(
            self.open_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, 50), type_choose_comboBoxChoices, 0)
        gSizer6.Add(self.type_choose_comboBox, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(
            self.open_mark_panel, wx.ID_ANY, u"選擇書籤", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        self.m_staticText6.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer6.Add(self.m_staticText6, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        mark_choose_comboBoxChoices = []
        self.mark_choose_comboBox = wx.ComboBox(
            self.open_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, 50), mark_choose_comboBoxChoices, 0)
        gSizer6.Add(self.mark_choose_comboBox, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(
            self.open_mark_panel, wx.ID_ANY, u"開啟方式", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        self.m_staticText7.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer6.Add(self.m_staticText7, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        open_choose_comboBoxChoices = [
            u"on GUI", u"on browser", wx.EmptyString]
        self.open_choose_comboBox = wx.ComboBox(
            self.open_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, 50), open_choose_comboBoxChoices, 0)
        self.open_choose_comboBox.SetSelection(2)
        gSizer6.Add(self.open_choose_comboBox, 0, wx.ALL, 5)

        gSizer6.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button2 = wx.Button(
            self.open_mark_panel, wx.ID_ANY, u"開啟", wx.DefaultPosition, wx.Size(150, 40), 0)
        self.m_button2.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer6.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.open_mark_panel.SetSizer(gSizer6)
        self.open_mark_panel.Layout()
        gSizer6.Fit(self.open_mark_panel)
        self.m_notebook2.AddPage(self.open_mark_panel, u"開啟書籤", False)

######################################################################
# delete_mark_pannel
######################################################################

        self.delete_mark_panel = wx.Panel(
            self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.delete_mark_panel.Enable(False)
        gSizer9 = wx.GridSizer(0, 2, 0, 0)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText21 = wx.StaticText(
            self.delete_mark_panel, wx.ID_ANY, u"刪除類別", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText21.Wrap(-1)

        self.m_staticText21.SetFont(wx.Font(
            28, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))
        self.m_staticText21.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.m_staticText21.SetBackgroundColour(wx.Colour(109, 252, 252))

        bSizer12.Add(self.m_staticText21, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer12.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer10 = wx.GridSizer(0, 2, 0, 0)

        gSizer10.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer10.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText22 = wx.StaticText(
            self.delete_mark_panel, wx.ID_ANY, u"選擇類別", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText22.Wrap(-1)

        self.m_staticText22.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer10.Add(self.m_staticText22, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        delete_type_comboBoxChoices = []
        self.delete_type_comboBox = wx.ComboBox(
            self.delete_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, 20), delete_type_comboBoxChoices, 0)
        gSizer10.Add(self.delete_type_comboBox, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 9)

        bSizer12.Add(gSizer10, 1, wx.EXPAND, 5)

        bSizer12.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer12.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button5 = wx.Button(
            self.delete_mark_panel, wx.ID_ANY, u"delete", wx.DefaultPosition, wx.Size(150, 40), 0)
        bSizer12.Add(self.m_button5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer12.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer9.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer121 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText211 = wx.StaticText(
            self.delete_mark_panel, wx.ID_ANY, u"刪除書籤", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText211.Wrap(-1)

        self.m_staticText211.SetFont(wx.Font(
            28, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))
        self.m_staticText211.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTIONTEXT))
        self.m_staticText211.SetBackgroundColour(wx.Colour(109, 252, 252))

        bSizer121.Add(self.m_staticText211, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer121.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer101 = wx.GridSizer(0, 2, 0, 0)

        gSizer101.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer101.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText221 = wx.StaticText(
            self.delete_mark_panel, wx.ID_ANY, u"選擇類別", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText221.Wrap(-1)

        self.m_staticText221.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer101.Add(self.m_staticText221, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        delete_type2_comboBoxChoices = []
        self.delete_type2_comboBox = wx.ComboBox(
            self.delete_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, 20), delete_type2_comboBoxChoices, 0)
        gSizer101.Add(self.delete_type2_comboBox, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer101.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer101.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText28 = wx.StaticText(
            self.delete_mark_panel, wx.ID_ANY, u"選擇書籤", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)

        self.m_staticText28.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer101.Add(self.m_staticText28, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        delete_mark_comboBoxChoices = []
        self.delete_mark_comboBox = wx.ComboBox(
            self.delete_mark_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, 20), delete_mark_comboBoxChoices, 0)
        gSizer101.Add(self.delete_mark_comboBox, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        gSizer101.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer101.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer121.Add(gSizer101, 1, wx.EXPAND, 5)

        bSizer121.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button51 = wx.Button(
            self.delete_mark_panel, wx.ID_ANY, u"delete", wx.DefaultPosition, wx.Size(150, 40), 0)
        bSizer121.Add(self.m_button51, 0, wx.ALL |
                      wx.ALIGN_CENTER_HORIZONTAL, 9)

        bSizer121.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer121.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer9.Add(bSizer121, 1, wx.EXPAND, 5)

        self.delete_mark_panel.SetSizer(gSizer9)
        self.delete_mark_panel.Layout()
        gSizer9.Fit(self.delete_mark_panel)
        self.m_notebook2.AddPage(self.delete_mark_panel, u"刪除書籤", False)

        bSizer3.Add(self.m_notebook2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()
        # 設定第一頁作為開啟GUI時的預設
        self.m_notebook2.SetSelection(0)
        self.Centre(wx.BOTH)

        # Connect Events
        self.login_bt.Bind(wx.EVT_BUTTON, self.login_bt_event)
        self.forget_paaword_bt.Bind(wx.EVT_BUTTON, self.password_clue_bt_event)
        self.create_user_bt.Bind(wx.EVT_BUTTON, self.create_user_bt_event)
        # 按鈕事件
        self.m_button1.Bind(wx.EVT_BUTTON, self.save_bt)
        # 下拉事件(跟formbuilder裡的不一樣)
        self.type_choose_comboBox.Bind(
            wx.EVT_COMBOBOX_DROPDOWN, self.choose_type_event)
        # 下拉事件(跟formbuilder裡的不一樣)
        self.mark_choose_comboBox.Bind(
            wx.EVT_COMBOBOX_DROPDOWN, self.choose_mark_event)
        # 按鈕事件
        self.m_button2.Bind(wx.EVT_BUTTON, self.open_bt)
        # 下拉事件(跟formbuilder裡的不一樣)
        self.delete_type_comboBox.Bind(wx.EVT_COMBOBOX_DROPDOWN,
                                       self.choose_delete_type_event)
        # 按鈕事件
        self.m_button5.Bind(wx.EVT_BUTTON, self.delete_type_bt)
        # 下拉事件(跟formbuilder裡的不一樣)
        self.delete_type2_comboBox.Bind(wx.EVT_COMBOBOX_DROPDOWN,
                                        self.choose_delete_type2_event)
        # 下拉事件(跟formbuilder裡的不一樣)
        self.delete_mark_comboBox.Bind(wx.EVT_COMBOBOX_DROPDOWN,
                                       self.choose_delete_mark_event)
        # 按鈕事件
        self.m_button51.Bind(wx.EVT_BUTTON, self.delete_mark_bt)

    # Virtual event handlers, override them in your derived class
    def login_bt_event(self, event):
        user = self.user_textCtrl.GetValue()
        password = self.password_textCtrl.GetValue()
        cur.execute(f"select password from userdata where user = '{user}'")
        rows = cur.fetchone()
        if not rows:
            # 跳新視窗，顯示無此使用者提示
            NoUserDialog(self).ShowModal()
        else:
            if password == rows[0]:
                # 跳新視窗，顯示成功登錄，將其他分頁enable
                LoginDialog(self).ShowModal()
                self.add_mark_panel.Enable(True)
                self.open_mark_panel.Enable(True)
                self.delete_mark_panel.Enable(True)
            else:
                # 跳新視窗，顯示密碼錯誤
                WrongPasswordDialog(self).ShowModal()

    def password_clue_bt_event(self, event):
        # 跳新視窗，輸入使用者名稱，按鈕顯示密碼提示
        clue_frm = clue_module.ClueFrame(None)
        clue_frm.Show()

    def create_user_bt_event(self, event):
        # 跳新視窗，輸入使用者名稱、密碼、線索，按鈕創新使用者，名稱重複顯示已有此使用者
        create_frm = create_user_module.createFrame(None)
        create_frm.Show()

    def save_bt(self, event):
        type_arr = []
        cur.execute(
            f"select type from marktype where user = '{self.user_textCtrl.GetValue()}'")
        rows = cur.fetchall()
        for i in range(len(rows)):
            type_arr.append(rows[i][0])
    # 判斷書籤類別是否已存在 & 新增書籤
        if self.mark_type_textCtrl.GetValue() not in type_arr:
            cur.execute(
                f"Insert into marktype values('{self.user_textCtrl.GetValue()}', '{self.mark_type_textCtrl.GetValue()}')")
            cur.execute(
                f"Insert into bookmark values('{self.user_textCtrl.GetValue()}', '{self.mark_type_textCtrl.GetValue()}', '{self.mark_name_textCtrl.GetValue()}', '{self.URL_textCtrl.GetValue()}')")
        else:
            mark_arr = []
            cur.execute(
                f"select name from bookmark where type = '{self.mark_type_textCtrl.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")
            rows = cur.fetchall()
            for i in range(len(rows)):
                mark_arr.append(rows[i][0])
            if self.mark_name_textCtrl.GetValue() not in mark_arr:
                cur.execute(
                    f"Insert into bookmark values('{self.user_textCtrl.GetValue()}', '{self.mark_type_textCtrl.GetValue()}', '{self.mark_name_textCtrl.GetValue()}', '{self.URL_textCtrl.GetValue()}')")
            else:
                MarkExistDialog(self).ShowModal()

    # 選擇開啟的類別
    def choose_type_event(self, event):
        cur.execute(
            f"select type from marktype where user = '{self.user_textCtrl.GetValue()}'")
        rows = cur.fetchall()
        type_arr = []
        for i in range(len(rows)):
            type_arr.append(rows[i][0])
        self.type_choose_comboBox.Clear()
        self.type_choose_comboBox.Append(type_arr)

    # 根據選擇的類別選擇書籤
    def choose_mark_event(self, event):
        cur.execute(
            f"select name from bookmark where type = '{self.type_choose_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")
        mark_arr = []
        rows = cur.fetchall()
        for i in range(len(rows)):
            mark_arr.append(rows[i][0])
        self.mark_choose_comboBox.Clear()
        self.mark_choose_comboBox.Append(mark_arr)

    # 開啟書籤
    def open_bt(self, event):
        if self.open_choose_comboBox.GetValue() == 'on GUI':
            url = ''
            cur.execute(
                f"select URL from bookmark where name = '{self.mark_choose_comboBox.GetValue()}' and type = '{self.type_choose_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")
            rows = cur.fetchone()
            url = rows[0]
            MyHtmlFrame(self, url).Show()
        # 選擇瀏覽器後，根據書籤的網址通過設定的chrome開啟
        if self.open_choose_comboBox.GetValue() == 'on browser':
            url = ''
            cur.execute(
                f"select URL from bookmark where name = '{self.mark_choose_comboBox.GetValue()}' and type = '{self.type_choose_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")
            rows = cur.fetchone()
            url = rows[0]
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new(url)

    # 選擇要刪除的整個類別
    def choose_delete_type_event(self, event):
        cur.execute(
            f"select type from marktype where user = '{self.user_textCtrl.GetValue()}'")
        rows = cur.fetchall()
        type_arr = []
        for i in range(len(rows)):
            type_arr.append(rows[i][0])
        self.delete_type_comboBox.Clear()
        self.delete_type_comboBox.Append(type_arr)

    # 刪除類別
    def delete_type_bt(self, event):
        cur.execute(
            f"delete from marktype where type = '{self.delete_type_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")
        cur.execute(
            f"delete from bookmark where type = '{self.delete_type_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")

    # 選擇要刪除的特定類別
    def choose_delete_type2_event(self, event):
        cur.execute(
            f"select type from marktype where user = '{self.user_textCtrl.GetValue()}'")
        rows = cur.fetchall()
        type_arr = []
        for i in range(len(rows)):
            type_arr.append(rows[i][0])
        self.delete_type2_comboBox.Clear()
        self.delete_type2_comboBox.Append(type_arr)

    # 選擇要刪除的類別裡的書籤
    def choose_delete_mark_event(self, event):
        cur.execute(
            f"select name from bookmark where type = '{self.delete_type2_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")
        mark_arr = []
        rows = cur.fetchall()
        for i in range(len(rows)):
            mark_arr.append(rows[i][0])
        self.delete_mark_comboBox.Clear()
        self.delete_mark_comboBox.Append(mark_arr)

    # 刪除書籤
    def delete_mark_bt(self, event):
        cur.execute(
            f"delete from bookmark where type = '{self.delete_type2_comboBox.GetValue()}' and name = '{self.delete_mark_comboBox.GetValue()}' and user = '{self.user_textCtrl.GetValue()}'")

    def __del__(self):
        conn.commit()
        conn.close()

###########################################################################
# Class NoUserDialog
###########################################################################


class NoUserDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(200, 100), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel8 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText32 = wx.StaticText(
            self.m_panel8, wx.ID_ANY, u"無此使用者", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        self.m_staticText32.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer13.Add(self.m_staticText32, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel8.SetSizer(bSizer13)
        self.m_panel8.Layout()
        bSizer13.Fit(self.m_panel8)
        bSizer12.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class WrongPasswordDialog
###########################################################################

class WrongPasswordDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(200, 100), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel8 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText32 = wx.StaticText(
            self.m_panel8, wx.ID_ANY, u"密碼錯誤", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        self.m_staticText32.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer13.Add(self.m_staticText32, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel8.SetSizer(bSizer13)
        self.m_panel8.Layout()
        bSizer13.Fit(self.m_panel8)
        bSizer12.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class LoginDialog
###########################################################################

class LoginDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(200, 100), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel8 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText32 = wx.StaticText(
            self.m_panel8, wx.ID_ANY, u"登錄成功", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        self.m_staticText32.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer13.Add(self.m_staticText32, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel8.SetSizer(bSizer13)
        self.m_panel8.Layout()
        bSizer13.Fit(self.m_panel8)
        bSizer12.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class MarkExistDialog
###########################################################################

class MarkExistDialog (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(200, 100), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel8 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText32 = wx.StaticText(
            self.m_panel8, wx.ID_ANY, u"書籤已存在", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText32.Wrap(-1)

        self.m_staticText32.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer13.Add(self.m_staticText32, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel8.SetSizer(bSizer13)
        self.m_panel8.Layout()
        bSizer13.Fit(self.m_panel8)
        bSizer12.Add(self.m_panel8, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer12)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class ShowHtmlFrame
###########################################################################

class MyHtmlFrame(wx.Frame):

    def __init__(self, parent, url):

        wx.Frame.__init__(self, parent, -1, size=(1024, 768))
        web_view = WebView.New(self)
        web_view.LoadURL(url)


if __name__ == '__main__':
    app = wx.App()
    frm = MyFrame(None)
    frm.Show()
    app.MainLoop()
