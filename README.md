# Unraveling Brazillian E-Commerce Dataset #
![Olist](https://valorcapitalgroup.com/wp-content/uploads/2020/06/case_study_4_olist_1.jpg)
Recently, a company named 'Olist' located in Brazil set out to improve the  average Brazilian experience of selling and buying online.
The company platform provided an opportunity for merchants to connect their  products to main marketplaces.
In 2018, Olist publicly released their Brazilian ecommerce dataset containing information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil.[Here is a link to the dataset.](https://www.kaggle.com/olistbr/brazilian-ecommerce)


# Dataset Description #
![Data Schema](https://cdn-images-1.medium.com/max/800/0*ui5tAFczBhBGGwUL.png)
The entire e-commerce dataset consists of 9 individual datasets with features such as orders, products, sellers and customer information and the geolocation zip codes.

# Problem Statement #
Olist has a very low percentage of returning customers and a decline in sales was recorded at one point ,so with the aim of improving the company outputs, we
* Carried out customer churn analysis.
* Investigated the decline in sales.
* Provided solutions and recommended ways of improving sales, customer experience and service.

# Our Approach #
We carried out customer churn analysis where we discovered that 96% of buyers were one-time customers so we further explored the reviews of customers and delivery performance  to trace the cause and recommend solutions. We also observed that a decline in sales was recorded in 2018 so we carried out order and sales analysis to tackle this, a predictive model(FBprophet) was also built to predict future sales. We were able to work on models(Logistic regression and Bidirectional LSTM model) that would classify the sentiments of customers properly and help the company in making better decisions.The models were deployed on a web app for easy access.

[Link to the medium article.](https://medium.com/p/e78463d77340/edit)

[Link to the project summary and the Portuguese sentiment analyzers.](https://share.streamlit.io/abuton/g04-brazillian-commerce/sentiment-analysis/main.py)
