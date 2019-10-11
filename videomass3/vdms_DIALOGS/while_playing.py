# -*- coding: UTF-8 -*-

#########################################################
# Name: while_playing.py
# Porpose: Show dialog box with shortcuts keyboard for FFplay
# Compatibility: Python3, wxPython4
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2018/2019 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev: Sept.02.2019
#########################################################

# This file is part of Videomass.

#    Videomass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Videomass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Videomass.  If not, see <http://www.gnu.org/licenses/>.

#########################################################

import wx

keys = (_("q, ESC\nf\np, SPC\nm\n9, 0\n/, *\na\nv\nt\nc\n"
          "w\ns\n\nleft/right\ndown/up\npage down/page up\n\n"
          "right mouse click\nleft mouse double-click"
          ))
explan = (_("Quiet.\nTogle full screen.\nPause.\nTogle mute.\n"
            "Decrease and increase volume respectively.\n"
            "Decrease and increase volume respectively.\n"
            "Cycle audio channel in the current program.\n"
            "Cycle video channel.\n"
            "Cycle subtitle channel in the current program.\n"
            "Cycle program.\nCycle video filters or show modes.\n"
            "Step to the next frame. Pause if the stream is not \n"#
            "already paused, step to the next video frame, and pause.\n"#
            "Seek backward/forward 10 seconds.\n"
            "Seek backward/forward 1 minute.\n"
            "Seek to the previous/next chapter. Or if there are no \n"#
            "chapters Seek backward/forward 10 minutes.\n"#
            "Seek to percentage in file corresponding to fraction of width.\n"
            "Toggle full screen."))

#------------------------------------------------------------------#    
class While_Playing(wx.Dialog):
    """
    Display a dialog box resizable with shortcuts keyboard
    useful when you use playback function with FFplay
   
    """
    def __init__(self, OS):
        wx.Dialog.__init__(self, None, style=wx.DEFAULT_DIALOG_STYLE)
        
        panel = wx.Panel(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        
        
        
        label1 = wx.StaticText(panel, wx.ID_ANY, keys)
        label2 = wx.StaticText(panel, wx.ID_ANY, explan)
        self.button_close = wx.Button(self, wx.ID_CLOSE, "")
        
        #----------------------Properties----------------------#
        self.SetTitle(_("Videomass: Shortcuts while playing"))
        label1.SetForegroundColour(wx.Colour('#008000'))
        label2.SetForegroundColour(wx.Colour('#959595'))
        panel.SetBackgroundColour(wx.Colour('#121212'))
        
        #if OS == 'Darwin':
            #label1.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.BOLD))
            #label2.SetFont(wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL))

        #else:
            #label1.SetFont(wx.Font(8, wx.SWISS, wx.ITALIC, wx.BOLD))
            #label2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL))
        
        #---------------------- Layout ----------------------#
        s1 = wx.BoxSizer(wx.VERTICAL)
        gr_s1 = wx.FlexGridSizer(1, 2, 0, 0)
        gr_s1.Add(label1, 0, wx.ALL, 5)
        gr_s1.Add(label2, 0, wx.ALL, 5)
        btngrid = wx.FlexGridSizer(1,1,0,0)
        btngrid.Add(self.button_close, 0, wx.ALL, 5)
        panel.SetSizer(gr_s1)#
        #s1.Add(panel, 1, wx.ALL | wx.EXPAND, 5)
        s1.Add(panel, 1, )
        s1.Add(btngrid, flag=wx.ALL|wx.ALIGN_RIGHT|wx.RIGHT, border=5)
        
        #self.SetSizer(s1)
        #s1.Fit(self)
        #self.Layout()
        self.SetSizerAndFit(s1)
        
        # binding
        self.Bind(wx.EVT_BUTTON, self.on_close, self.button_close)
        self.Bind(wx.EVT_CLOSE, self.on_close) # controlla la chiusura (x)
        
    #--------------------------------------------------------------# 
    def on_close(self, event):
        '''
        destroy dialog by button and the X
        '''
        self.Destroy()
        #event.Skip()