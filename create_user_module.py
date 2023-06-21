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


conn = lite.connect('bookmark.db')
cur = conn.cursor()
###########################################################################
# Class createFrame
###########################################################################


class createFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel4 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText5 = wx.StaticText(
            self.m_panel4, wx.ID_ANY, u"使用者名稱", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        self.m_staticText5.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_staticText5, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.user_name_textCtrl = wx.TextCtrl(
            self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer1.Add(self.user_name_textCtrl, 0, wx.ALL, 5)

        self.m_staticText6 = wx.StaticText(
            self.m_panel4, wx.ID_ANY, u"密碼", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        self.m_staticText6.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_staticText6, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.password_textCtrl = wx.TextCtrl(
            self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer1.Add(self.password_textCtrl, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(
            self.m_panel4, wx.ID_ANY, u"密碼提示", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        self.m_staticText7.SetFont(wx.Font(
            16, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.m_staticText7, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.clue_textCtrl = wx.TextCtrl(
            self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gSizer1.Add(self.clue_textCtrl, 0, wx.ALL, 5)

        gSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.create_user_bt = wx.Button(
            self.m_panel4, wx.ID_ANY, u"創建使用者", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.create_user_bt.SetFont(wx.Font(
            14, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        gSizer1.Add(self.create_user_bt, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel4.SetSizer(gSizer1)
        self.m_panel4.Layout()
        gSizer1.Fit(self.m_panel4)
        bSizer3.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.create_user_bt.Bind(wx.EVT_BUTTON, self.create_user_bt_event)

    def __del__(self):
        conn.commit()

    # Virtual event handlers, override them in your derived class
    def create_user_bt_event(self, event):
        cur.execute(
            f"select user from userdata where user = '{self.user_name_textCtrl.GetValue()}'")
        row = cur.fetchall()
        if not row:
            cur.execute(
                f"Insert into userdata values('{self.user_name_textCtrl.GetValue()}', '{self.password_textCtrl.GetValue()}', '{self.clue_textCtrl.GetValue()}')")
            MyDialog2(self).ShowModal()
            # 我想要在按下確認後將creat frame一起關閉，要如何操作app，才不會讓bookmark的frame跟著一起不見
            # 想法1:手動按關閉視窗(很麻煩，但可以重複輸入)
            # 想法2:改成dialog(不確定dialog可不可以當父類別)

        else:
            print('user already exist')
            MyDialog1(self).ShowModal()


###########################################################################
# Class MyDialog1
###########################################################################


class MyDialog1 (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel7 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(
            self.m_panel7, wx.ID_ANY, u"已有此使用者", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        self.m_staticText14.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer10.Add(self.m_staticText14, 0,
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.confirm_bt = wx.Button(
            self.m_panel7, wx.ID_ANY, u"確認", wx.DefaultPosition, wx.DefaultSize, 0)
        self.confirm_bt.SetFont(wx.Font(
            10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體"))

        bSizer10.Add(self.confirm_bt, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        bSizer8.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer8)
        self.Layout()
        bSizer8.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.confirm_bt.Bind(wx.EVT_BUTTON, self.confirm_bt_event)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def confirm_bt_event(self, event):
        self.Destroy()


###########################################################################
# Class MyDialog2
###########################################################################

class MyDialog2 (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.Size(193, 118), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel7 = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText14 = wx.StaticText(
            self.m_panel7, wx.ID_ANY, u"創建成功!", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)

        self.m_staticText14.SetFont(wx.Font(
            18, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "標楷體"))

        bSizer10.Add(self.m_staticText14, 0,
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.confirm_bt = wx.Button(
            self.m_panel7, wx.ID_ANY, u"確認", wx.DefaultPosition, wx.DefaultSize, 0)
        self.confirm_bt.SetFont(wx.Font(
            10, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "新細明體"))

        bSizer10.Add(self.confirm_bt, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_panel7.SetSizer(bSizer10)
        self.m_panel7.Layout()
        bSizer10.Fit(self.m_panel7)
        bSizer8.Add(self.m_panel7, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer8)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.confirm_bt.Bind(wx.EVT_BUTTON, self.confirm_bt_event)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def confirm_bt_event(self, event):
        self.Destroy()
