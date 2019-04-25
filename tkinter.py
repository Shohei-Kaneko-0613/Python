#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title(u"プログラム脳適正検査")
root.geometry("600x300")

def DeleteEntryValue(event):
#ここで，valueにEntryの中身が入る
 milk = EditBox1.get()
 egg = EditBox2.get()

 if milk == str(6) and egg == str(0):
  messagebox.showinfo('適性', '適性あり')
 else:
  messagebox.showinfo('適性', '適性なし')
  

#ラベル
Static1 = tkinter.Label(text=u'■問題')
Static1.place(x=10,y=10)

Static2 = tkinter.Label(text=u'ある日、あなたは妻から次のようなお願い事をされます。')
Static2.place(x=20,y=30)
Static3 = tkinter.Label(text=u'妻：「スーパーに行って牛乳を１つ買ってきてちょうだい。そして、もし卵があったら６つお願い」')
Static3.place(x=20,y=50)

Static4 = tkinter.Label(text=u'■質問')
Static4.place(x=10,y=90)

Static5 = tkinter.Label(text=u'そのお願いを受けてあなたは牛乳と卵をいくつ買って帰りますか？')
Static5.place(x=20,y=110)

Static6 = tkinter.Label(text=u'牛乳の数を入れてください。')
Static6.place(x=50,y=180)

Static7 = tkinter.Label(text=u'卵の数を入れてください。')
Static7.place(x=250,y=180)

#エントリー
EditBox1 = tkinter.Entry(width=20)
EditBox1.insert(tkinter.END,"")
EditBox1.place(x=50,y=200)

EditBox2 = tkinter.Entry(width=20)
EditBox2.insert(tkinter.END,"")
EditBox2.place(x=250,y=200)

#ボタン
Button = tkinter.Button(text=u'確定', width=10)
Button.bind("<Button-1>",DeleteEntryValue) 
Button.place(x=450,y=200)

root.mainloop()
