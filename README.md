# ETL
README.md
Certainly! Here's an example README file for the ETL project for Stock Market Analysis using APIs with PostgreSQL:

ETL Project: Stock market Analysis 

This project aims to demonstrate an Extract, Transform, Load (ETL) Operation using APIs to extract the relevant data from external sources and transform it using Python, and load it into Supabase, a online cloud based database based on PostgresSQL. The project specifically utilizes the Appha Vantage API and Rapid API as the data sources. The data uploaded into cloud storage is further analysed and visualysed for analysis. Grafanna a cloud based visualisation software is used visualyse the statistical graph for stock market analysis.

Flow Diagram

![image](https://github.com/1999tanveer/ETL/assets/22239682/9c2ae5bf-3071-48f9-8386-9341e6ab96ac)



Prerequisites Before running the ETL process, ensure that you have the following prerequisites installed:

Python 3.x PostgreSQL database Required Python libraries:  requests, datetime, supabase

Update the DATABASE variable with your database connection details and other API credentials in the code.

THe Rapid API is used to check if yesterday was a working day or not. If yesterday was a holiday it means there was no stock market transactions happened hence the script doesnt run and logs the date as holiday in local logs.

The Alpha Vantage API is used to extract the last 100 stock price details of the mentioned stock. "IBM" is configured for analysis.

The python code can be scheduled to run daily based on specific time from windows task scheduler. Or can be triggered manually.

The logs and outputs are logged in "StockAnalysis_log.log".

The python script performs transformations and calculates Moving average statistical values for the stock prices. Feel free to change the values SMA and LMA to modidy the no of days for moving average. Which is further loaded into the online db.

Once the ETL process is complete, you can access the transformed data in the online Supabase database.

<img width="896" alt="image" src="https://github.com/1999tanveer/ETL/assets/22239682/741e09bc-dbd6-4a33-bf39-92bba04d3fa7">

The time series analysis of the data can be done via the Grafana Platform. The grafana platform needs to be connected with the database connection details.

<img width="960" alt="image" src="https://github.com/1999tanveer/ETL/assets/22239682/e08dc64a-bd19-4b9c-aed2-8de084d84580">


Customization Feel free to customize and enhance the project according to your specific requirements:

Explore additional APIs or data sources and modify the extraction process accordingly. Extend the data transformation step in the etl.py script using Pandas to apply more complex data manipulations or calculations. Modify the PostgreSQL database schema or create additional tables to accommodate the transformed data as needed.

License This project is licensed under the MIT License.

Acknowledgments Rapid API, Alpha Vantage API, Supabase and Grafana for providing access to data, platform and softwares. 
