import streamlit as st
from datetime import date
import yfinance as yf
from plotly import graph_objs as go

TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Visulization App')

stocks = ('^GSPC','GOOG', 'AAPL', 'MSFT', 'META', 'NFLX', 'AMD', 'NVDA', 'F', 'INTC')
selected_stock = st.selectbox('Select STOCK for visulization', stocks)

START = st.date_input(
     "Select START date",
     date(2022, 1, 1))
st.write('You select START date as:', START)

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

    
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data of selected STOCK', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
plot_raw_data()

st.subheader('Raw data')
st.write(data.tail())

