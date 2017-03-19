FROM wangpanjun/calabash:scrapy

MAINTAINER xiaowangzi

# 数据库配置
ENV INEWW_DATABASE_NAME ineww
ENV INEWW_DATABASE_USER root
ENV INEWW_DATABASE_PASSWORD root
ENV INEWW_DATABASE_HOST localhost
ENV INEWW_DATABASE_PORT 3306



ADD ./ /app
ADD ./supervisord.conf /etc/supervisor/
ADD ./ispider.conf /etc/supervisor/conf.d/
WORKDIR /app


RUN mkdir /var/log/ispider

EXPOSE 6800