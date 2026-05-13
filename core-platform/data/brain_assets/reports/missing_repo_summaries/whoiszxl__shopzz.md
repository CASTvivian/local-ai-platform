# Missing Repo Summary Source: whoiszxl/shopzz

- URL: https://github.com/whoiszxl/shopzz
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/whoiszxl__shopzz
- Clone Status: cloned
- Language: Java
- Stars: 438
- Topics: bitcoin, blockchain, eth, flink, flutter, hadoop, springcloud-alibaba, usdt, vue3
- Description: 后端使用 SpringCloud Alibaba 开发，移动端使用 React Native 构建，管理后台使用 Arco Design 进行构建，并在支付上接入数字货币（比特币、以太坊UDST、平台Token）支付，后端采用 Hadoop 与 Flink 等大数据框架构建实时计算与离线计算体系。

## Extracted README / Docs / Examples



# FILE: README.md

## 淘物 一个使用SpringCloud Alibaba开发的微服务 C2B2C 的社区&交易平台
[![MyWebSite](https://img.shields.io/badge/我的站点-whoiszxl-blue.svg)](http://whoiszxl.com)
[![docs](https://img.shields.io/badge/docs-reference-green.svg)](http://shopzz.whoiszxl.com)
[![teach](https://img.shields.io/badge/演示-mall-orange.svg)](https://shopzz.whoiszxl.com)
[![email](https://img.shields.io/badge/email-whoiszxl@gmail.com-red.svg)](whoiszxl@gmail.com)


### 项目介绍
后端使用 SpringCloud Alibaba 开发，移动端使用 React Native 构建，管理后台使用 Arco Design 进行构建，并在支付上接入数字货币（比特币、以太坊UDST、平台Token）支付，后端采用 Hadoop 与 Flink 等大数据框架构建实时计算与离线计算体系。

### 后端项目架构
![arch](./docs/images/taowu-arch.png)


### 项目特点
* 技术全面：提供多种技术栈，移动端、PC 端、后端皆有支持，且每种技术都是当前较新技术。
* 方案通用：封装的 starter，代码规范，DDD 领域驱动设计，RBAC 权限管理，各种封装的组件可以灵活运用到其他项目中。
* 代码复用：管理后台封装 BaseController，一次继承解决基础增删改查。
* 版本管理：通过 Liquibase 管理数据库版本，跟踪、管理和应用数据库变化。
* 数仓支持：提供 Hadoop 技术栈支持，通过 CDH 构建，实现离线数仓与实时数仓。
* 扩展方案：多种分库分表策略，高并发场景。
* 持续集成：实现 DevOps，通过 DroneCI/Jenkins 实现部署的全流程自动化
* 容器编排：通过 Rancher/DockerSwarm 实现多容器的部署、管理与监控。
* 系统监控：通过 ELK 实现日志监控，通过 SkyWalking 实现链路追踪，通过 Prometheus + Grafana 实现系统监控。
其他：待补充


### APP 截图

| ![1](./docs/images/screenshots/Screenshot_1.jpg)                                                          | ![2](./docs/images/screenshots/Screenshot_2.jpg)                                                          | ![3](./docs/images/screenshots/Screenshot_3.jpg)                                                          | ![5](./docs/images/screenshots/Screenshot_4.jpg) |  
| :--: | :--: | :--: | :--: |   


| ![1](./docs/images/screenshots/Screenshot_5.jpg)                                                          | ![2](./docs/images/screenshots/Screenshot_6.jpg)                                                          | ![3](./docs/images/screenshots/Screenshot_7.jpg)                                                          | ![5](./docs/images/screenshots/Screenshot_8.jpg) |  
| :--: | :--: | :--: | :--: |



### 开发环境


### 项目部署



# FILE: docs/docs/index.md

---
layout: home

title: taowu - 一个使用SpringCloud Alibaba开发的微服务 C2B2C 的社区&交易平台
titleTemplate: taowu - 一个使用SpringCloud Alibaba开发的微服务 C2B2C 的社区&交易平台

hero:
  name: taowu
  text: java project
  tagline:  一个使用SpringCloud Alibaba开发的微服务 C2B2C 的社区&交易平台
  image:
    src: /logo.png
    alt: Logo
  actions:
    - theme: brand
      text: 项目文档 💫
      link: /taowu/01-快速开始/01-后端环境Docker搭建
    - theme: alt
      text: GitHub地址 🤖
      link: https://github.com/whoiszxl/taowu

features:
  - icon: 😀
    title: 通用方案
    details: 具备项目常见解决方案，代码规范、RBAC、组件封装等
  - icon: 🤣
    title: 社区&电商项目
    details: 具备常见电商模块，用户、文件、即时通讯、短视频、社交等
  - icon: 🤩
    title: 大数据接入
    details: Hadoop + Flink 等大数据框架构建实时计算与离线计算体系
  - icon: 🤪
    title: 前端支持
    details: React Native构建移动端，Arco Design构建管理后台
  - icon: 🤓
    title: 扩展业务
    details: 直播业务、短视频业务、即时通讯业务实现
  - icon: 😛
    title: 扩展方案
    details: 海量数据分库分表、DevOps、高并发场景、复杂业务实现、区块链
---


# FILE: docs/docs/tags.md

---
title: 我的标签
aside: false
editLink: false
lastUpdated: false
showComment: false
---

<ClientOnly>
	<Tag />
</ClientOnly>

# FILE: docs/docs/archives.md

---
title: 我的归档
aside: false
editLink: false
lastUpdated: false
showComment: false
---

<ClientOnly>
	<Archive />
</ClientOnly>

# FILE: docs/docs/taowu/01-快速开始/02-前端环境构建.md

---
title: 前端环境构建
author: whoiszxl
date: 2023/02/23 12:28
editLink: false
categories:
 - 
tags:
---

# React Native App 构建

:::tip 提示

:::



## 管理后台前端代码构建



# FILE: docs/docs/taowu/01-快速开始/00-基础环境简介.md

---
title: 基础环境简介
author: whoiszxl
date: 2023/02/23 12:28
editLink: false
categories:
 - 
tags:
---

# 基础环境简介


## 端口分布

| 列1 | 列2 | 列3 | 列4 |
|-----|-----|-----|-----|
| member - 9999 | admin - 10001 | comment - 10002 | counter - 10003 |
| file - 10004 | imWeb - 10005 | imServer - 10006 | live - 10007 |
| loans - 10008 | marketing - 10009 | order - 10010 | pay - 10011 |
| product - 10012 | search - 10013 | sensitive - 10014 | sms - 10015 |
| video - 10016 | walletBtc - 10017 | walletEth - 10018 | walletTW - 10019 |
| wms - 10020 | - |  -  |  -  |

# FILE: docs/docs/taowu/01-快速开始/01-后端环境Docker搭建.md

---
title: 后端环境Docker搭建
author: whoiszxl
date: 2023/02/23 12:28
editLink: false
categories:
 - 
tags:
---

# 测试环境手动搭建

## Docker环境搭建

### 1. 移除之前的docker相关包，非初始化环境执行
```sh
sudo yum remove docker \
docker-client \
docker-client-latest \
docker-common \
docker-latest \
docker-latest-logrotate \
docker-logrotate \
docker-engine
```

### 2. 配置阿里云yum源 (可选)
```shell
sudo yum install -y yum-utils

sudo yum-config-manager \
--add-repo \
http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

### 3. 安装Docker
```bash
sudo yum install -y docker-ce docker-ce-cli containerd.io
```

### 4. 启动Docker
```bash
systemctl enable docker --now
```

### 5. 国内配置加速
* 访问[阿里云获取镜像加速配置地址](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)，获取到加速器地址，按照操作文档进行对应操作。

```bash
sudo mkdir -p /etc/docker

# 需要替换registry-mirrors中的加速器地址
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://xxxxx.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker
```

### 6. Docker基础操作
```bash
# 拉取镜像 - 镜像名:版本名（标签）
docker pull nginx:1.20.1

# 查看本地镜像
docker images

# 删除本地镜像
docker rmi image_name || image_id

# 启动容器
docker run -name=my_nginx -d --restart=always -p 81:80 nginx

# 查看正在运行的容器
docker ps

# 查看所有
docker ps -a

# 删除停止的容器，-f强制删除
docker rm  container_id || container_name
docker rm -f container_id || container_name

# 停止容器
docker stop container_id || container_name

# 启动容器
docker start container_id || container_name

# 应用开机自启
docker update container_id || container_name --restart=always

# 进入容器内部
docker exec -it container_id /bin/bash

# 查看日志
docker logs container_id
```


## MySQL环境搭建

机器内存不够，可以只运行一个MySQL容器，在单个MySQL容器下创建多个库来模拟分库场景。

### 1. MySQL安装
:::tip 提示
docker启动MySQL进程时需要间隔十多秒再启动下一个，不然会失败
:::


```bash
# 创建MySQL网段
docker network create --subnet 172.18.0.0/18 taowu-net

# MySQL-001
docker run --name mysql-001 \
--net taowu-net --ip 172.18.0.1 \
-m 400m \
-v /opt/data/docker/mysql-001/config:/etc/mysql/conf.d \
-p 3301:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-e TZ=Asia/Shanghai \
--privileged=true \
-d mysql \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci \
--lower_case_table_names=1

# MySQL-002
docker run --name mysql-002 \
--net taowu-net --ip 172.18.0.2 \
-m 400m \
-v /opt/data/docker/mysql-002/config:/etc/mysql/conf.d \
-p 3302:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-e TZ=Asia/Shanghai \
--privileged=true \
-d mysql \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci \
--lower_case_table_names=1

# MySQL-003
docker run --name mysql-003 \
--net taowu-net --ip 172.18.0.3 \
-m 400m \
-v /opt/data/docker/mysql-003/config:/etc/mysql/conf.d \
-p 3303:3306 \
-e MYSQL_ROOT_PASSWORD=123456 \
-e TZ=Asia/Shanghai \
--privileged=true \
-d mysql \
--character-set-server=utf8mb4 \
--collation-server=utf8mb4_unicode_ci \
--lower_case_table_names=1

```


## ShardingSphere-Proxy环境搭建

### 1. 创建两个配置文件
* 第一个：server.yml，点击[server.yml](https://github.com/apache/shardingsphere/blob/master/examples/shardingsphere-proxy-example/shardingsphere-proxy-boot-mybatis-example/src/main/resources/conf/server.yaml)查看模板。

users中配置可以访问proxy代理服务的用户名和密码，privilege的type中配置用户操作数据库的权限，ALL_PERMITTED为所有权限。
```yaml
authority:
  users:
    - user: root@%
      password: root
    - user: sharding@%
      password: sharding
  privilege:
    type: ALL_PERMITTED
```


* 第二个：config-sharding.yaml，用来配置分库分表的规则。此处模拟order库的分库分表。
```yaml
schemaName: taowu-order

# 创建一批数据源[ds0_order, ds1_order, ds2_order]
dataSources:
 ds0_order:
   url: jdbc:mysql://127.0.0.1:3300/taowu-order-000?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&nullCatalogMeansCurrent=true&allowPublicKeyRetrieval=true   
   username: root
   password: 123456
   connectionTimeoutMilliseconds: 30000
   idleTimeoutMilliseconds: 60000
   maxLifetimeMilliseconds: 1800000
   maxPoolSize: 50
   minPoolSize: 1
 ds1_order:
   url: jdbc:mysql://127.0.0.1:3300/taowu-order-001?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&nullCatalogMeansCurrent=true&allowPublicKeyRetrieval=true   
   username: root
   password: 123456
   connectionTimeoutMilliseconds: 30000
   idleTimeoutMilliseconds: 60000
   maxLifetimeMilliseconds: 1800000
   maxPoolSize: 50
   minPoolSize: 1
 ds2_order:
   url: jdbc:mysql://127.0.0.1:3300/taowu-taowu-002?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai&nullCatalogMeansCurrent=true&allowPublicKeyRetrieval=true   
   username: root
   password: 123456
   connectionTimeoutMilliseconds: 30000
   idleTimeoutMilliseconds: 60000
   maxLifetimeMilliseconds: 1800000
   maxPoolSize: 50
   minPoolSize: 1

# 此处定义sharding分片的规则
rules:
- !SHARDING
 tables:
   oms_order: # 定义关联[oms_order_0, oms_order_1, oms_order_2]三个表的逻辑表名称
     actualDataNodes: ds${0..2}_order.oms_order_${0..2} # 定义一个数据节点，这个数据节点的规则是ds0到ds1，再到ds2,这是一个范围的表达式，后面的oms_order也是一样，表示可以是oms_order_0,oms_order_1,oms_order_2。
     tableStrategy:
       standard: # 配置一个策略
          shardingColumn: id # 表明要按照id字段来进行分片
          shardingAlgorithmName: taowu-inline # 定义taowu-inline规则，下方有定义
     keyGenerateStrategy: # 主键的生成策略，这里使用雪花算法。因为多库多表用自增id的话，会造成id重复。
       column: id
       keyGeneratorName: snowflake
   
 bindingTables: # 绑定表名，把oms_order表名加进去。
   - oms_order
 defaultDatabaseStrategy: # 数据库路由策略
   standard:
     shardingColumn: member_id # 分片列名为member_id
     shardingAlgorithmName: database_inline # 指定了一个database_inline的策略，这个策略在下面定义。

 defaultTableStrategy:
   none:
 
 shardingAlgorithms:
   database_inline: # 数据库的分片策略，让member_id对3进行了一个取模
     type: INLINE
     props:
       algorithm-expression: ds${member_id % 3}_order

   taowu-inline:
     type: INLINE
     props:
       algorithm-expression: oms_order_${id % 3} # 表名路由规则，通过order表的主键id来对3进行取模计算得出来

# 定义雪花算法的一些参数，比如说worker-id
 keyGenerators:
   snowflake:
     type: SNOWFLAKE
     props:
       worker-id: 123
```

### 2. 运行shardingsphere-proxy服务
此处需要导入mysql的驱动包 `mysql.jar`
```bash
docker run --name ss-proxy -d \
-v /opt/data/docker

# FILE: docs/docs/taowu/01-快速开始/03-数字货币钱包环境构建.md

---
title: 数字货币钱包环境构建
author: whoiszxl
date: 2023/02/23 12:28
editLink: false
categories:
 - 
tags:
---

# 数字货币钱包环境构建

## ERC20代币钱包测试环境构建

### 环境搭建

1. 下载chrome浏览器，安装metamask插件，需要科学上网，插件地址：(https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=cn)[https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=cn]

2. 通过metamask创建ETH钱包，生成钱包地址，并向地址中转入适量ETH作为发布token的手续费。测试环境可以采用 sepolia 等环境。


### 获取token合约代码
1. 进入网址：(https://etherscan.io/tokens)[https://etherscan.io/tokens]，有所有的token代币可供选择，如：USDT,BNB

2. 任意选择一个点击进入，如： HuobiToken (HT)，再将url链接中的token修改为address，再点击进入(https://etherscan.io/address/0x6f259637dcd74c767781e37bc6133cd6a68aa161)[https://etherscan.io/address/0x6f259637dcd74c767781e37bc6133cd6a68aa161]

3. 再选择页面中的合约选项，便能查看到Solidity的合约代码

4. 查看合约的最终URL为：(https://etherscan.io/address/0x6f259637dcd74c767781e37bc6133cd6a68aa161#code)[https://etherscan.io/address/0x6f259637dcd74c767781e37bc6133cd6a68aa161#code]

5. 将代码拷贝，再打开网址：(https://remix.ethereum.org)[https://remix.ethereum.org]，在网址中创建一个文件，并将代码粘贴



### 修改合约代码
获取到代码合约HBToken这一段，对币名，发行数等记录进行修改，代码注释如下：

```js
//类名修改 HBToken -> NiceToken
//每种token代币的合约代码都不相同，功能也不同，有些代币是在构造函数中输入参数对其进行初始化的，比如：USDT
contract NiceToken is UnboundedRegularToken {

    //总发行数量 5乘以10的16次方，如果有精度，则需要减去精度的次方数。如精度为8，则总发行数量为 5*10**8
    uint public totalSupply = 5*10**16;
    //精度
    uint8 constant public decimals = 8;
    //代币名称
    string constant public name = "NiceToken";
    //代币符号
    string constant public symbol = "NICE";

    function NiceToken() {
        balances[msg.sender] = totalSupply;
        Transfer(address(0), msg.sender, totalSupply);
    }
}
```

### 发布代币

1. 修改好代码后点击右边栏的第三个`SOLIDITY COMPILER`进行代码编译，需要在`Compiler`选项中选中代码第一行`pragma solidity 0.4.19;`中的版本

2. 然后再点击右边栏第四个`DEPLOY & RUN TRANSACTIONS,Environment`选择`Injected Web3`，弹出`metamask`后确认就OK

3. 在拉下选项中选中`ZXLToken-browser/zxl_coin.sol`,再点击`Deploy`按钮部署，确认下去就完全OK了!


### 验证合约
1. 通过合约地址进入合约界面：`https://sepolia.etherscan.io/token/0x954e2a8476312ae980fed44a5cfaccff41ebf74a`

2. 点击合约选项，再点击立即验证并发布(`Verify and Publish`)

3. 选择代码中相对应的`solidity`版本再继续，将代码拷贝进入代码框中，再进行人机身份验证之后点击`Verify and Publish`,就验证完成辣！
