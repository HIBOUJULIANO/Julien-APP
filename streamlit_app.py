import random 
import time
import streamlit as st
import pandas as pd


# Remplace par l'URL de ton fichier CSV
url = "https://www.julien-hoarau.com/Aribnb.csv"

# Lire le fichier CSV depuis l'URL
df = pd.read_csv(url)

# Afficher les premières lignes du fichier
#st.dataframe(df)

resultat = df['Name']
st.write(resultat)
st.write(resultat)



st.markdown(
    """ 
   test My name is Julien Hoarau and I create little funny
   games with Python in order to test librairies








    """
)

st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHg2dmpjODdneHV5cW5hYm14MWUyeG83dDcycm91YXNhbzd2a3NnNSZlcD12MV9zdGlja2Vyc19zZWFyY2gmY3Q9cw/TFmEOTKS49wkn4Qeos/giphy.gif", caption="Einstein image"
         ,width=100)  
  
st.markdown(
    """ 
   test My name is Julien Hoarau and I create little funny
   games with Python in order to test librairies
    """
)

st.title("Casino of the emojis")
st.markdown(
    """ 
   Hello, welcome to the Casino of the emojis.
   In this virtual casino you can win virtual emojis if you have 
   4 similar emojis. This game was created with Random and Time Libraries.
    """
)

defilementA=0
defilementB=0
defilementC=0
defilementD=0

A = 0
B = 0
C = 0
D = 0
#print(A,B,C)

a=0
b=0
c=0
d=0

combia = []

tirage = 0


e=1
t=0
bontirage=random.randint(0,3)
f=0


#print("bontirage",bontirage)



if st.button("Play"):
    
    
   
        i=0
        while i < 5 : 
            i=i+1
            time.sleep(0.8)
            defilementA=random.choice(["❤️","😊","😘","😍"])
            defilementB=random.choice(["❤️","😊","😘","😍"])
            defilementC=random.choice(["❤️","😊","😘","😍"])
            defilementD=random.choice(["❤️","😊","😘","😍"])
            st.write(defilementA,defilementB,defilementC,defilementD)

        while a < 4 : 
            a=a+1
            time.sleep(0.2)
            A=random.choice(["❤️","😊","😘","😍"])
            #st.write(A)

    
        while b < 4 : 
            b=b+1
            time.sleep(0.2)
            B=random.choice(["❤️","😊","😘","😍"])
            #st.write(B)
    
        while c < 4 : 
            c=c+1
            time.sleep(0.2)
            C=random.choice(["❤️","😊","😘","😍"])
            #st.write(C)
    
        while d < 4 :
            d=d+1
            time.sleep(0.2)
            D=random.choice(["❤️","😊","😘","😍"])
            #st.write(D)

        st.write("Your emojis :" + A,B,C,D)
        if A==B==C==D :
         st.title("You win an emoji !"+random.choice(["🏎️","🛩️","⛴️","🏠"]))
        else : 
         st.title("You loose but you win an emoji" +random.choice(["🤡","🚛","⛈️","🎃"]))

fichier = open("Test_streamlit.txt", "r")
st.write(fichier.read())
fichier.close()
time.sleep(1)
fichier = open("Test_streamlit.txt", "w")
st.write("...........                    🍎")
fichier.close()
