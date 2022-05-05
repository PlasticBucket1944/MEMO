######################################################
###### diet_loggerのwebサーバー側定義
###### docker-composeから呼び出しされます
######################################################

## ベースイメージを指定
FROM ruby:2.6.6
# 必要なパッケージをインストール nodejsはバージョンを指定
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update -qq \
  && apt-get install -y nodejs yarn npm && npm install n -g && n 12.13.0
WORKDIR /app
# 同ディレクトリのdiet_loggerをフォルダごとコンテナ内の/appにコピー
COPY ./diet_logger /app
RUN bundle config --local set path 'vendor/bundle' \
  && bundle install
