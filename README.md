# stock-predictor-mlops
Developing a RESTful API with FastAPI, Building a basic time series model to predict stock prices, then Deploying a FastAPI to AWS EC2


run the following in another shell on your local machine:

curl \
--header "Content-Type: application/json" \
--request POST \
--data '{"ticker":"MSFT", "days":7}' \
http://54.202.67.219:8000/predict



http://54.202.67.219:8000/docs
