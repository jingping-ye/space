# 第四章 编写可维护的 webpack 构建配置

## 构建插件包设计

### 构建配置管理的可选方案

1. 通过多个配置文件管理不同环境的构建，webpack --config 参数进行控制
2. 将构建配置设计成一个库,比如hjs-webpack,Neutrino、webpack-blocks
3. 抽成一个工具进行管理，拨入create-react-app, kyt, nwb
4. 将所有配置放在一个文件，通过--env参数控制分支选择

### 构建配置拆分

- 基础配置:webpack.base.js
- 开发环境:webpack.dev.js
- 生产环境:webpack.prod.js
- ssr环境:webpack.ssr.js

### 抽离成一个npm包同一管理

- 规范:Git commit日志、README、ESLint规范、Semver规范
- 质量：冒烟测试、单元测试、测试覆盖率和CI

### 通过webpack-merge组合配置

## 功能模块设计和目录结构

## 使用eslint规范构建脚本

## 冒烟测试介绍和实际运用

> 冒烟测试，在提交测试之前开发人员自己测试代码是否可用，可用之后再提交给专业测试。

## 单元测试和测试覆盖率

## 持续集成和Travis CI

> 持续集成：看测试用例是否正常跑过，只有跑过，才可以合并到主干。

持续集成的作用

优点：

- 快速发现错误
- 防止分支大幅偏离主干

核心措施是，代码集成到主干之前，必须通过自动化测试。只要有一个测试用例失败，就不能集成。

github CI

- Travis CI
- Circle CI
- Jenkins

## 发布构建包到`npm`社区

## Git Commit规范和changelog生成

### 本地开发阶段增加precommit钩子



## 语义化版本(Semantic Versioning)规范格式

软件版本通常由三位组成，形如:X.Y.Z 16.0.1

版本是严格递增的,16.2.0-->16.3.0-->16.4.0

在发布重要版本时，可以先发布alpha,rc等先行版本 16.4.0-alpha.3134344

### 遵守semver规范的优势。（依赖地狱）

- 优势:避免出现循环依赖

- 依赖冲突减少

X: 主版本:当你做了不兼容API修改。重大特性

Y: 次版本号：向下兼容的功能性新增

Z: 修订号：当你做了向下兼容的问题修正

alpha:内部测试版，一般不向外发布，会有很多bug

beta:测试版本，会一直发布很多新功能

rc:发布候选版，rc不会发布新功能，重点是除错。