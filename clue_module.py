# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sqlite3 as lite


conn = lite.connect('D:/大學/大三上/網路與資料庫程式設計/期中專案/bookmark/bookmark.db')
cur = conn.cursor()

###########################################################################
# Class MyFrame2
###########################################################################


class ClueFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer25 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel14 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer27 = wx.BoxSizer(wx.VERTICAL)

        gSizer14 = wx.GridSizer(0, 2, 0, 0)

        gSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        gSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_staticText38 = wx.StaticText(
            self.m_panel14, wx.ID_ANY, u"輸入使用者名稱", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText38.Wrap(-1)

        self.m_staticText38.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer14.Add(self.m_staticText38, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.clue_user_textCtrl = wx.TextCtrl(
            self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 25), 0)
        gSizer14.Add(self.clue_user_textCtrl, 0, wx.ALL, 5)

        gSizer14.Add((0, 0), 1, wx.EXPAND, 5)

        self.clue_button = wx.Button(
            self.m_panel14, wx.ID_ANY, u"提示", wx.DefaultPosition, wx.DefaultSize, 0)
        self.clue_button.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer14.Add(self.clue_button, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer27.Add(gSizer14, 1, wx.EXPAND, 5)

        self.m_panel14.SetSizer(bSizer27)
        self.m_panel14.Layout()
        bSizer27.Fit(self.m_panel14)
        bSizer25.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer25)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.clue_button.Bind(wx.EVT_BUTTON, self.clue_button_event)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def clue_button_event(self, event):
        cur.execute(
            f"select clue from userdata where user = '{self.clue_user_textCtrl.GetValue()}'")
        row = cur.fetchone()
        if not row:
            MyDialog71(self).ShowModal()
        else:
            MyDialog7(self, row[0]).ShowModal()


###########################################################################
# Class MyDialog7
###########################################################################

class MyDialog7 (wx.Dialog):

    def __init__(self, parent, clue):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(300, 130), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer30 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel15 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText39 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"密碼提示:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)

        self.m_staticText39.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer31.Add(self.m_staticText39, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.clue_staticText = wx.StaticText(
            self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.clue_staticText.Wrap(-1)
        self.clue_staticText.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))
        self.clue_staticText.SetLabel(clue)

        bSizer31.Add(self.clue_staticText, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel15.SetSizer(bSizer31)
        self.m_panel15.Layout()
        bSizer31.Fit(self.m_panel15)
        bSizer30.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer30)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


class MyDialog71 (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(300, 100), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer30 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel15 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer31 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText39 = wx.StaticText(
            self.m_panel15, wx.ID_ANY, u"無此使用者", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText39.Wrap(-1)

        self.m_staticText39.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer31.Add(self.m_staticText39, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel15.SetSizer(bSizer31)
        self.m_panel15.Layout()
        bSizer31.Fit(self.m_panel15)
        bSizer30.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer30)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
