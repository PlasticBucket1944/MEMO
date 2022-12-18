# 概要
spring bootをdockerで起動するためのテンプレ  
ビルドすればhello worldが表示される  
# セットアップ
１．名前はなんでも良いので作業用フォルダを作成  
２．作業用フォルダにDockerfile、docker-compose.yml、serverフォルダをコピペ  
　　テンプレ以外のソースを使う場合server内をクリーンしその中に配置する  
３．docker立ち上げ
```
docker-compose up -d
```
４．docker内に入る
```
docker-compose exec app bash
```
５．docker内でビルド実行
```
sh gradlew build
```
６．docker内でサーバー立ち上げ
```
java -jar build/libs/api-0.0.1-SNAPSHOT.jar
```
７．以下からアクセスする  
http://localhost:8080/  

ソースを変更したら５からやり直す


# メモ
spring bootテンプレを作る所  
https://start.spring.io/

参考  
https://zenn.dev/junki555/articles/a19f27d1045805