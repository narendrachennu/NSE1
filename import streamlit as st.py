import streamlit as st
def plot_line_chart(data):
    # Create a line chart for 'Open', 'High', 'Low', 'Close'
    fig, ax = plt.subplots()
    ax.plot(data['Date'], data['Open'], label='Open', color='blue')
    ax.plot(data['Date'], data['High'], label='High', color='green')
    ax.plot(data['Date'], data['Low'], label='Low', color='red')
    ax.plot(data['Date'], data['Close'], label='Close', color='black')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.set_title('Stock Prices')
    ax.legend()
    st.pyplot(fig)
    
def plot_candlestick_chart(data):
    # Create a candlestick chart using Plotly
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.update_layout(title='Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig)
    
def main():
    st.title("NSE Stock Data Visualization")

    # Upload CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Load data
        data = load_data(uploaded_file)

        # Ensure 'Date' column is in datetime format
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Show data preview
        st.write("Data Preview:", data.head())

        # Plot Line Chart
        st.subheader("Line Chart of Stock Prices")
        plot_line_chart(data)

        # Plot Candlestick Chart
        st.subheader("Candlestick Chart")
        plot_candlestick_chart(data)

if __name__ == "__main__":
    main()