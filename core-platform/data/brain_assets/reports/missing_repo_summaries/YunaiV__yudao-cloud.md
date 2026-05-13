# Missing Repo Summary Source: YunaiV/yudao-cloud

- URL: https://github.com/YunaiV/yudao-cloud
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/YunaiV__yudao-cloud
- Clone Status: cloned
- Language: Java
- Stars: 18921
- Topics: dubbo, elasticsearch, mall, mysql, nacos, redis, rocketmq, seata, sharding-sphere, skywalking, spring-cloud, spring-cloud-alibaba, springboot, springcloud, xxl-job, zookeeper
- Description: ruoyi-vue-pro 全新 Cloud 版本，优化重构所有功能。基于 Spring Cloud Alibaba + MyBatis Plus + Vue & Element 实现的后台管理系统 + 用户小程序，支持 RBAC 动态权限、多租户、数据权限、工作流、三方登录、支付、短信、商城、CRM、ERP、MES、IM、AI 大模型、IoT 物联网等功能。你的 ⭐️ Star ⭐️，是作者生发的动力！

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
 <img src="https://img.shields.io/badge/Spring%20Cloud-2021-blue.svg" alt="Coverage Status">
 <img src="https://img.shields.io/badge/Spring%20Boot-2.7.18-blue.svg" alt="Downloads">
 <img src="https://img.shields.io/badge/Vue-3.2-blue.svg" alt="Downloads">
 <img src="https://img.shields.io/github/license/YunaiV/yudao-cloud" alt="Downloads" />
</p>

**严肃声明：现在、未来都不会有商业版本，所有代码全部开源!！**

**「我喜欢写代码，乐此不疲」**  
**「我喜欢做开源，以此为乐」**

我 🐶 在上海艰苦奋斗，早中晚在 top3 大厂认真搬砖，夜里为开源做贡献。

如果这个项目让你有所收获，记得 Star 关注哦，这对我是非常不错的鼓励与支持。

可参考 [《迁移文档》](https://cloud.iocoder.cn/migrate-module/) ，只需要 5-10 分钟，即可将【完整版】按需迁移到【精简版】

## 🐶 新手必读

* 演示地址【Vue3 + element-plus】：<http://dashboard-vue3.yudao.iocoder.cn>
* 演示地址【Vue3 + vben(ant-design-vue)】：<http://dashboard-vben.yudao.iocoder.cn>
* 演示地址【Vue2 + element-ui】：<http://dashboard.yudao.iocoder.cn>
* 启动文档：<https://cloud.iocoder.cn/quick-start/>
* 视频教程：<https://cloud.iocoder.cn/video/>

## 🐰 版本说明

| 版本                                                                    | JDK 8 + Spring Boot 2.7                                                  | JDK 17/21 + Spring Boot 3.2                                                          |
|-----------------------------------------------------------------------|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| 【完整版】[yudao-cloud](https://gitee.com/zhijiantianya/yudao-cloud)       | [`master`](https://gitee.com/zhijiantianya/yudao-cloud/tree/master/) 分支  | [`master-jdk17`](https://gitee.com/zhijiantianya/yudao-cloud/tree/master-jdk17/) 分支  |
| 【精简版】[yudao-cloud-mini](https://gitee.com/yudaocode/yudao-cloud-mini) | [`master`](https://gitee.com/yudaocode/yudao-cloud-mini/tree/master/) 分支 | [`master-jdk17`](https://gitee.com/yudaocode/yudao-cloud-mini/tree/master-jdk17/) 分支 |

* 【完整版】：包括系统功能、基础设施、会员中心、数据报表、工作流程、商城系统、微信公众号、CRM、ERP、MES、AI 大模型、IoT 物联网 等功能
* 【精简版】：只包括系统功能、基础设施功能，不包括会员中心、数据报表、工作流程、商城系统、微信公众号、CRM、ERP、MES、AI 大模型、IoT 物联网 等功能

可参考 [《迁移文档》](https://cloud.iocoder.cn/migrate-module/) ，只需要 5-10 分钟，即可将【完整版】按需迁移到【精简版】

## 🐯 平台简介

**芋道**，以开发者为中心，打造中国第一流的快速开发平台，全部开源，个人与企业可 100% 免费使用。

> 有任何问题，或者想要的功能，可以在 _Issues_ 中提给艿艿。
>
> 😜 给项目点点 Star 吧，这对我们真的很重要！

![架构图](/.image/common/yudao-cloud-architecture.png)

* Java 后端：`master` 分支为 JDK 8 + Spring Boot 2.7，`master-jdk17` 分支为 JDK 17/21 + Spring Boot 3.2
* 管理后台的电脑端：Vue3 提供 [element-plus](https://gitee.com/yudaocode/yudao-ui-admin-vue3)、[vben(ant-design-vue)](https://gitee.com/yudaocode/yudao-ui-admin-vben) 两个版本，Vue2 提供 [element-ui](https://gitee.com/zhijiantianya/ruoyi-vue-pro/tree/master/yudao-ui-admin) 版本
* 管理后台的移动端：采用 [uni-app](https://github.com/dcloudio/uni-app) 方案，一份代码多终端适配，同时支持 APP、小程序、H5！
* 后端采用 Spring Cloud Alibaba 微服务架构，注册中心 + 配置中心 Nacos，定时任务 XXL-Job，服务保障 Sentinel，服务网关 Gateway，分布式事务 Seata
* 数据库可使用 MySQL、Oracle、PostgreSQL、SQL Server、MariaDB、国产达梦 DM、TiDB 等，基于 MyBatis Plus、Redis + Redisson 操作
* 消息队列可使用 Event、Redis、RabbitMQ、Kafka、RocketMQ 等
* 权限认证使用 Spring Security & Token & Redis，支持多终端、多种用户的认证系统，支持 SSO 单点登录
* 支持加载动态权限菜单，按钮级别权限控制，Redis 缓存提升性能
* 支持 SaaS 多租户，可自定义每个租户的权限，提供透明化的多租户底层封装
* 工作流使用 Flowable，支持动态表单、在线设计流程、会签 / 或签、多种任务分配方式
* 高效率开发，使用代码生成器可以一键生成 Java、Vue 前后端代码、SQL 脚本、接口文档，支持单表、树表、主子表
* 实时通信，采用 Spring WebSocket 实现，内置 Token 身份校验，支持 WebSocket 集群
* 集成微信小程序、微信公众号、企业微信、钉钉等三方登陆，集成支付宝、微信等支付与退款
* 集成阿里云、腾讯云等短信渠道，集成 MinIO、阿里云、腾讯云、七牛云等云存储服务
* 集成报表设计器、大屏设计器，通过拖拽即可生成酷炫的报表与大屏

##  🐳 项目关系

![架构演进](/.image/common/yudao-roadmap.png)

三个项目的功能对比，可见社区共同整理的 [国产开源项目对比](https://www.yuque.com/xiatian-bsgny/lm0ec1/wqf8mn) 表格。

### 后端项目

| 项目                                                              | Star                                                                                                                                                                                                                                                                                             | 简介                          |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| [ruoyi-vue-pro](https://gitee.com/zhijiantianya/ruoyi-vue-pro)  | [![Gitee star](https://gitee.com/zhijiantianya/ruoyi-vue-pro/badge/star.svg?theme=white)](https://gitee.com/zhijiantianya/ruoyi-vue-pro) [![GitHub stars](https://img.shields.io/github/stars/YunaiV/ruoyi-vue-pro.svg?style=social&label=Stars)](https://github.com/YunaiV/ruoyi-vue-pro)       | 基于 Spring Boot 多模块架构        |
| [yudao-cloud](https://gitee.com/zhijiantianya/yudao-cloud)      | [![Gitee star](https://gitee.com/zhijiantianya/yudao-cloud/badge/star.svg?theme=white)](https://gitee.com/zhijiantianya/yudao-cloud) [![GitHub stars](https://img.shields.io/github/stars/YunaiV/yudao-cloud.svg?style=social&label=Stars)](https://github.com/YunaiV/yudao-cloud)               | 基于 Spring Cloud 微服务架构       |
| [Spring-Boot-Labs](https://gitee.com/yudaocode/SpringBoot-Labs) | [![Gitee star](https://gitee.com/yudaocode/SpringBoot-Labs/badge/star.svg?theme=white)](https://gitee.com/zhijiantianya/yudao-cloud) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/SpringBoot-Labs.svg?style=social&label=Stars)](https://github.com/yudaocode/SpringBoot-Labs) | 系统学习 Spring Boot & Cloud 专栏 |

### 前端项目

| 项目                                                                         | Star                                                                                                                                                                                                                                                                                                                     | 简介                                     |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| [yudao-ui-admin-vue3](https://gitee.com/yudaocode/yudao-ui-admin-vue3)     | [![Gitee star](https://gitee.com/yudaocode/yudao-ui-admin-vue3/badge/star.svg?theme=white)](https://gitee.com/yudaocode/yudao-ui-admin-vue3) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/yudao-ui-admin-vue3.svg?style=social&label=Stars)](https://github.com/yudaocode/yudao-ui-admin-vue3)         | 基于 Vue3 + element-plus 实现的管理后台         |
| [yudao-ui-admin-vben](https://gitee.com/yudaocode/yudao-ui-admin-vben)     | [![Gitee star](https://gitee.com/yudaocode/yudao-ui-admin-vben/badge/star.svg?theme=white)](https://gitee.com/yudaocode/yudao-ui-admin-vben) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/yudao-ui-admin-vben.svg?style=social&label=Stars)](https://github.com/yudaocode/yudao-ui-admin-vben)         | 基于 Vue3 + vben(ant-design-vue) 实现的管理后台 |
| [yudao-mall-uniapp](https://gitee.com/yudaocode/yudao-mall-uniapp)         | [![Gitee star](https://gitee.com/yudaocode/yudao-mall-uniapp/badge/star.svg?theme=white)](https://gitee.com/yudaocode/yudao-mall-uniapp) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/yudao-mall-uniapp.svg?style=social&label=Stars)](https://github.com/yudaocode/yudao-mall-uniapp)                 | 基于 uni-app 实现的商城小程序                    |
| [yudao-ui-admin-vue2](https://gitee.com/yudaocode/yudao-ui-admin-vue2)     | [![Gitee star](https://gitee.com/yudaocode/yudao-ui-admin-vue2/badge/star.svg?theme=white)](https://gitee.com/yudaocode/yudao-ui-admin-vue2) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/yudao-ui-admin-vue2.svg?style=social&label=Stars)](https://github.com/yudaocode/yudao-ui-admin-vue2)         | 基于 Vue2 + element-ui 实现的管理后台           |
| [yudao-ui-admin-uniapp](https://gitee.com/yudaocode/yudao-ui-admin-uniapp) | [![Gitee star](https://gitee.com/yudaocode/yudao-ui-admin-uniapp/badge/star.svg?theme=white)](https://gitee.com/yudaocode/yudao-ui-admin-uniapp) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/yudao-ui-admin-uniapp.svg?style=social&label=Stars)](https://github.com/yudaocode/yudao-ui-admin-uniapp) | 基于 Vue2 + element-ui 实现的管理后台           |
| [yudao-ui-go-view](https://gitee.com/yudaocode/yudao-ui-go-view)           | [![Gitee star](https://gitee.com/yudaocode/yudao-ui-go-view/badge/star.svg?theme=white)](https://gitee.com/yudaocode/yudao-ui-go-view) [![GitHub stars](https://img.shields.io/github/stars/yudaocode/yudao-ui-go-view.svg?style=social&label=Stars)](https://github.com/yudaocode/yudao-ui-go-view)                     | 基于 Vue3 + naive-ui 实现的大屏报表             |

## 😎 开源协议

**为什么推荐使用本项目？**

① 本项目采用比 Apache 2.0 更宽松的 [MIT License](https://gitee.com/zhijiantianya/ruoyi-vue-pro/blob/master/LICENSE) 开源协议，个人与企业可 100% 免费使用，不用保留类作者、Copyright 信息。

② 代码全部开源，不会像其他项目一样，只开源部分代码，让你无法了解整个项目的架构设计。[国产开源项目对比](https://www.yuque.com/xiatian-bsgny/lm0ec1/wqf8mn)

![开源项目对比](/.image/common/project-vs.png)

③ 代码整洁、架构整洁，遵循《阿里巴巴 Java 开发手册》规范，代码注释详细，113770 行 Java 代码，42462 行代码注释。

## 🤝 项目外包

我们也是接外包滴，如果你有项目想要外包，可以微信联系【**Aix9975**】。

团队包含专业的项目经理、架构师、前端工程师、后端工程师、测试工程师、运维工程师，可以提供全流程的外包服务。

项目可以是商城、SCRM 系统、OA 系统、物流系统、ERP 系统、CMS 系统、HIS 系统、支付系统、IM 聊天、微信公众号、微信小程序等等。

## 🐼 内置功能

系统内置多种多种业务功能，可以用于快速你的业务系统：

![功能分层](/.image/common/ruoyi-vue-pro-biz.png)

* 通用模块（必选）：系统功能、基础设施
* 通用模块（可选）：工作流程、支付系统、数据报表、会员中心
* 业务系统（按需）：ERP 系统、CRM 系统、MES 系统、商城系统、微信公众号、AI 大模型、IoT 物联网

> 友情提示：本项目基于 RuoYi-Vue 修改，**重构优化**后端的代码，**美化**前端的界面。
>
> * 额外新增的功能，我们使用 🚀 标记。
> * 重新实现的功能，我们使用 ⭐️ 标记。

🙂 所有功能，都通过 **单元测试** 保证高质量。

### 系统功能

|     | 功能    | 描述                              
