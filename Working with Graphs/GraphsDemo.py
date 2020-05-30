#%%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np

class GraphDemo(object):

    def readDataIntoDF(self,filePath):
        # Load the data
        #df = pd.read_csv('WHO-COVID-19-india-data.csv', usecols=['Date_reported', 'Cumulative_cases'])
        data = pd.read_csv(filePath)

        return data


    def plotGraph(self, graphType):
        data_global = px.data.gapminder()
        data_global = self.readDataIntoDF('WHO-COVID-19-global-data.csv')

        data_india = data_global[data_global.Country == 'India']

        # Plot Line Graph
        if graphType =='Line':
            #pio.renderers.default = "browser"
            fig = px.line(data_global, x = 'Country', y = 'Cumulative_cases', title='India Covid-19 Graph')
            fig.show()

        # Plot Simple Scatter Plot
        elif graphType == 'Simple_Scatter':
            #pio.renderers.default = "browser"
            fig = go.Figure(data=go.Scatter(x=data_global['Country'], y=data_global['Cumulative_cases'], mode='markers'))
            fig.show()

        # Custome Bar Chart
        elif graphType =='Custom_Bar_Chart':
            
            fig = px.bar(data_india, x='Date_reported', y='Cumulative_cases',
                         hover_data=['New_cases','New_deaths'], color='Cumulative_cases',
                         labels={'India':'Covid-19'}, height=600,title='India Covid-19 Graph')
            #pio.renderers.default = "browser"
            #fig.show()
            fig.write_html('custom_bar_chart.html', auto_open=True)

        # Grouped Bar Chart
        elif graphType == 'Grouped_Bar_Chart':
            fig = go.Figure(data=[
                go.Bar(name='Cumulative_cases', x=data_india['Date_reported'], y=data_india['Cumulative_cases']),
                go.Bar(name='Cumulative_deaths', x=data_india['Date_reported'], y=data_india['Cumulative_deaths'],)
            ])
            # Change the bar mode
            fig.update_layout(barmode='stack')
            #fig.show()
            fig.write_html('group_bar_chart.html', auto_open=True)

        # Line chart
        elif graphType == 'Line_Charts':
            fig = px.line(data_global, x="Cumulative_cases", y="Cumulative_deaths", color='Country')
            #fig.show()
            fig.write_html('Line_Charts.html', auto_open=True)

        else:
            pass


def main():
    demo = GraphDemo()
    demo.plotGraph('Line_Charts')


if __name__ == "__main__":
    main()

# %%
