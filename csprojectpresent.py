 #--------CURRENCY CONVERTOR BY YASHASVEE AND SHREYAS-----




import tkinter as tk            
from PIL import Image,ImageTk
import requests


HEIGHT = 1080                            #canvas
WIDTH = 1440
root = tk.Tk()
root.title('CURRENCY CONVERTOR')
canvas =  tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()

img1=ImageTk.PhotoImage(Image.open('money final.jpg'))  #placing bg image
label1=tk.Label(root,image=img1)
label1.place(relheight=1, relwidth=1)



currencieslist=['USD    	  :US dollar',
'JPY    	  :Japanese yen',
'BGN    	  :Bulgarian lev',
'CZK    	  :Czech koruna',
'DKK    	  :Danish krone',
'GBP    	  :Pound sterling',	
'HUF    	  :Hungarian forint',
'PLN    	  :Polish zloty',
'RON    	  :Romanian leu',
'SEK    	  :Swedish krona',	
'CHF    	  :Swiss franc',
'ISK    	  :Icelandic krona',
'NOK    	  :Norwegian krone',	
'HRK    	  :Croatian kuna',
'RUB    	  :Russian rouble',	
'TRY    	  :Turkish lira',
'AUD    	  :Australian dollar',
'BRL    	  :Brazilian real',
'CAD    	  :Canadian dollar',
'CNY    	  :Chinese yuan renminbi',
'HKD    	  :Hong Kong dollar',
'IDR    	  :Indonesian rupiah',	    
'ILS    	  :Israeli shekel',
'INR    	  :Indian rupee',	
'KRW    	  :South Korean won',	
'MXN    	  :Mexican peso',	
'MYR    	  :Malaysian ringgit',
'NZD    	  :New Zealand dollar',
'PHP    	  :Philippine peso',
'SGD    	  :Singapore dollar',
'THB    	  :Thai baht',
'ZAR    	  :South African rand'	
                                 ]


def next_win():

    top=tk.Toplevel()
    top.geometry('500x2000')
    def for_top():
        for i in currencieslist:
            label=tk.Label(top,font=("Arial Bold",12),text=i)
            label.pack()
    for_top()


url_2='https://api.exchangeratesapi.io/latest'   

def check():
    global base
    global symbols
    base=str(entry_1.get())
    symbols=str(entry_2.get())
    convert(base,symbols)
    

  
def convert(base,symbols):
    global lower_frame

    params_2={'base':base.upper(),'symbols':symbols.upper()}  
    response_2=requests.get(url_2,params=params_2)  
    resp2=response_2.json()
    k=0
    for i in resp2:
        if i=='error':
            label=tk.Label(lower_frame,text='enter proper currency symbol', font=('Arial Bold',25))
            label.pack()
            k=k+1
    if k==0:
        req=resp2['rates']
        for i in req: 
            c=i+'      :   '+str(req[i])
            label_2=tk.Label(lower_frame,font=('Arial Bold',25))
            label_2['text']=c
            label_2.pack()
                
def clear():
    global lower_frame
    lower_frame.destroy()
    lower_frame = tk.Frame(root, bg = '#EBEDEF' , bd=10)
    lower_frame.place(relx=0.45, rely =0.22, relwidth=0.75,relheight=0.6, anchor = "n")


##widgets
frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5, relwidth=0.85,relheight=0.1,anchor='n')

entry_1 =tk.Entry(frame,font=("Arial Bold",30),borderwidth=10)
entry_1.place(relx=0, relwidth=0.20, relheight=1)

entry_2 =tk.Entry(frame,font=('Arial Bold',30),borderwidth=10)
entry_2.place( relx = 0.46, relwidth=0.20,relheight=1)

button_go = tk.Button(frame, text= "GO",command=check)
button_go.place(relx =0.66,relheight=1,relwidth=0.15)

button_clear=tk.Button(frame,text='CLEAR',command=clear)
button_clear.place(relx=0.83,relheight=1,relwidth=0.2)


label= tk.Label(frame, text= "TO")
label.place(relx = 0.2,relheight=1,relwidth=0.08)

button_catalog=tk.Button(frame,text='LIST',command=next_win)
button_catalog.place(relx=0.29,relheight=1,relwidth=0.17)


lower_frame = tk.Frame(root, bd=10)
lower_frame.place(relx=0.45, rely =0.22, relwidth=0.75,relheight=0.6, anchor = "n")


root.mainloop()
