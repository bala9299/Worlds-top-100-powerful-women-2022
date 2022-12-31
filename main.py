import streamlit as st
import pandas as pd 

header = st.container()
dataset = st.container()
search = st.container()
st.markdown("""<style>
               .main {
                background-color: #F5F5F5
                }
                </style>
                """,
                unsafe_allow_html = True)

with header:
    st.title("Top 100 most powerful womens of the WORLD")
    st.markdown("This data was determined by four main metrics: **money**, **media**, **influence** and **domains**.")
    st.text("You can find here only the top 100 womens Country, Age and Category.")
 
with dataset:
    df = pd.read_csv("data//womens.csv")
    if st.checkbox("Show me the top five womens of the world."):
        st.write(df.head())

with search:
    S = st.radio("**INDEX**",['Rank.','Country.','Age.','Category.'])

    if S == 'Rank.':
        st.subheader("Rank")
        R = st.selectbox("**Select here**",df.RANK,0)
        r = df.loc[df.RANK==R]["NAME"].iloc[0]
        st.markdown(f'This women holds rank **{R}** in the world : **{r}**.')

    if S == 'Country.':
        st.subheader("Country.")
        c= pd.DataFrame(df['LOCATION'].value_counts())
        st.bar_chart(c,use_container_width=True)  
        C = st.selectbox("**Choose country**",df['LOCATION'].unique(),0) 
        rank =  df[df["LOCATION"]==C]
        st.table(rank)

    if S == "Age.":
        st.subheader("Age")      
        age = st.select_slider("**Choose age**",options=df["AGE"].unique())
        a = df[df["AGE"] == age]
        st.table(a) 
        aa = st.radio("**Maximum and Minmum**",['maximum age','minimum age'])
        if aa == 'maximum age':
            age = df["AGE"].max()
            max=df['NAME'].loc[df.AGE == age ].iloc[0]
            st.write(f"Name : **{max}**. and Age : **{age}**")
        if aa == 'minimum age':
            age = df["AGE"].min()
            min=df['NAME'].loc[df.AGE == age ].iloc[0]
            st.write(f"Name : **{min}**. and Age : **{age}**")

    if S == "Category.":
        st.subheader("Category")
        cat = pd.DataFrame(df['CATEGORY'].value_counts())
        st.bar_chart(cat,use_container_width=True)
        CC = st.selectbox("**Choose category**",df["CATEGORY"].unique(),0)
        cc = df[df["CATEGORY"]== CC]
        st.table(cc)
    
    
        
         

        
        
        
        
        
        
        
         
