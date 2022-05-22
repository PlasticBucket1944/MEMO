# SETUP

１．どこでも良いので作業用ディレクトリを作成

２．作業用ディレクトリ内で以下のコマンドを実行してソース取得  
git clone https://github.com/PlasticBucket1944/diet_logger

３．diet_logger/config 下にdatabase.yml を作成  
中身はここに置いてある物をコピペ  
※DB接続の為のpassword、host名はdocker-compose.ymlに記載している物になっているので  
　変えた場合はそれに合わせる  

４．Dockerfile、docker-compose.ymlを作成  
中身はここに置いてある物をコピペ  

＊確認＊
現時点でのファイル構成

作業用ディレクトリ  
|-diet_logger  
　|-config  
　　|-datebase.yml  
|-Dockerfile  
|-docker-compose.yml  

５．dockerイメージをビルド(権限によってはsudoしないとダメかも)  
docker-compose build  

６．コンテナ内のyarnを最新にする(権限によってはsudoしないとダメかも)  
docker-compose run --rm web yarn install  

７．コンテナ内にDBを作成 以下のコマンドを実行  
docker-compose run web rails db:create  
docker-compose run web rails db:migrate  

８．コンテナ立ち上げ  
docker-compose up  

上手くいってたら以下で確認できる  
http://localhost:3000/
