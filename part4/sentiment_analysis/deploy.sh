aws ecr get-login-password --region eu-west-1 --profile matej-test | docker login --username AWS --password-stdin 199182205087.dkr.ecr.eu-west-1.amazonaws.com
cd web
docker build -t predict_sentiment .
docker tag predict_sentiment:latest 199182205087.dkr.ecr.eu-west-1.amazonaws.com/predict_sentiment:latest
docker push 199182205087.dkr.ecr.eu-west-1.amazonaws.com/predict_sentiment:latest