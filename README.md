# 我自己使用的ai 应用

### 1.安装mariadb

```bash
apt install mariadb-server
```

> 包的名称是:`mariadb-server`

#### 3.2 创建数据库

* 进入docker 容器

```bash
mysql -h 172.17.0.3 -uroot -p123456 
```

![image-20230425110625498](/Users/qiukaiwei/PycharmProjects/my_application/assets/image-20230425110625498.png)

* 创建数据库

  ``` bash
  create database my_application;
  show databases;
  ```

  ![image-20230425111138735](/Users/qiukaiwei/PycharmProjects/my_application/assets/image-20230425111138735.png)

#### 3.3 将数据库`my_application` 权限赋予用户`my_application@localhost`

```bash
GRANT ALL PRIVILEGES ON my_application.* TO 'my_application'@'';
FLUSH PRIVILEGES;
```





```bash
CREATE USER 'my_application'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'my_application'@'localhost';

```









# 不能建立容器,我搞不定,直接诉诸机器安装

### 1. 建立docker 容器

```bash
docker run --name redis -p 32768:6379 -d redis redis-server --requirepass redispw
docker run -d --name mariadb -e MARIADB_USER=my_application -e MARIADB_PASSWORD=123456 -e MARIADB_ROOT_PASSWORD=123456  mariadb:latest

```

> `redis-server`---启动容器内部的redis服务
>
> `--requirepass redispw`---设置密码为`redispw`
>
> Mariadb 我创建了一个用户叫`my_application`,用户的登录密码是123456,并且`root`密码也是是123456