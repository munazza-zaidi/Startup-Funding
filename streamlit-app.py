import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Startup Funding')

df=pd.read_csv("startup_cleaned.csv")
#st.dataframe(df)
st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox("Select Any option", ['overall Analysis', 'Startup', 'Investor'])

def investors_details(investor):
    recent_investment=df[df['investors'].str.contains(investor)][['date', 'startup_name', 'industry', 'city', 'investment_type', 'amount_usd' ]]
    st.dataframe(recent_investment)


def biggest_investment(investor):
    st.subheader("Biggest Investment")
    max_investment= df[df['investors'].str.contains(investor)].groupby('startup_name')['amount_usd'].sum().sort_values(ascending=False)
    max_investment = max_investment.reset_index()
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(max_investment)
    with col2:
        fig, ax = plt.subplots()

        ax.bar(
            max_investment["startup_name"],
            max_investment["amount_usd"]
        )

        ax.set_title("Biggest Investment")
        ax.set_ylabel("Amount USD")

        st.pyplot(fig)

def invested_industries(investor):
    industries_of_investment=df[df['investors'].str.contains(investor)].groupby('industry')['amount_usd'].sum()
    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots()

        ax1.pie(industries_of_investment, labels=industries_of_investment.index, autopct='%0.01f%%')
        st.pyplot(fig1)

def yoy_investment(investor):

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year

    year_investment = (
        df[df['investors'].str.contains(investor, na=False)]
        .groupby('year')['amount_usd']
        .sum()
        .reset_index()
    )

    fig, ax = plt.subplots()
    ax.plot(year_investment['year'], year_investment['amount_usd'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Investment Amount')
    ax.set_title('Year-wise Investment')

    st.pyplot(fig)

if option == 'overall Analysis':
    st.title("Overall analysis")
    pass
elif option == 'Startup':
    st.sidebar.selectbox("Select the Startups", (df['startup_name'].unique().tolist()))
    st.sidebar.button("Find startup Details")
    st.title("Startup analysis")
else:
    selected_investor= st.sidebar.selectbox("Select the Startups", (sorted(set(df['investors'].str.split(',').sum()))))
    indetail_btn= st.sidebar.button("Find investors Details")
    st.title("investors analysis")
    if indetail_btn:
        st.header(selected_investor)
        investors_details(selected_investor)
        biggest_investment(selected_investor)
        invested_industries(selected_investor)
        yoy_investment(selected_investor)

