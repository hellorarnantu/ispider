FROM wangpanjun/calabash:scrapy

MAINTAINER xiaowangzi

# 数据库配置
ENV CALABASH_DATABASE_NAME ineww
ENV CALABASH_DATABASE_USER root
ENV CALABASH_DATABASE_PASSWORD root
ENV CALABASH_DATABASE_HOST localhost
ENV CALABASH_DATABASE_PORT 3306



ADD ./ /app
ADD ./supervisord.conf /etc/supervisor/
ADD ./ispider.conf /etc/supervisor/conf.d/
WORKDIR /app


RUN mkdir /var/log/ispider

EXPOSE 6800