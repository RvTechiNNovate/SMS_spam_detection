import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from tkinter import *

df=pd.read_csv('dataset/sms.txt',delimiter='\t')
cv=CountVectorizer(stop_words='english')	
mnb=MultinomialNB()

def mytrain():
	df.columns=['label','msg']
	X=cv.fit_transform(df.msg).todense()
	y=df.iloc[:,0].values
	mnb.fit(X,y)

def mypredict():
	msg=e.get()
	X_test=cv.transform([msg]).todense()
	pred=mnb.predict(X_test)
	if(pred[0]=='spam'):
		outlbl.configure(text=pred[0],fg='red')
	else:
		outlbl.configure(text=pred[0],fg='green')
		
mytrain()

root=Tk()
root.state('zoomed')
root.configure(background='yellow')

title=Label(root,text='Spam Detection',bg='yellow',font=('',40,'bold'))
title.place(x=200,y=10)

lbl=Label(root,text='Enter msg:',fg='blue',bg='yellow',font=('',20,'bold'))
lbl.place(x=200,y=200)

e=Entry(root,font=('',15,'bold'))
e.place(x=350,y=205)

b=Button(root,text='Predict',command=mypredict,font=('',15,'bold'))
b.place(x=400,y=250)

outlbl=Label(root,bg='yellow',font=('',20,'bold'))
outlbl.place(x=350,y=350)


root.mainloop()
