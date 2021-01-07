# UCloud Uclub 社区自动签到

![Uclub Auto Signin](https://github.com/Ryanjiena/Auto_uclub_signin/workflows/Uclub%20Auto%20Signin/badge.svg)

<details>
   <summary>目录</summary>

- [UCloud Uclub 社区自动签到](#ucloud-uclub-社区自动签到)
  - [特点](#特点)
    - [已实现](#已实现)
    - [TODO](#todo)
  - [使用方法](#使用方法)
    - [参数配置](#参数配置)
    - [运行签到](#运行签到)
      - [Action 定时任务](#action-定时任务)
      - [签到信息推送](#签到信息推送)
  - [常见问题](#常见问题)
    - [关于定时任务不执行](#关于定时任务不执行)
    - [TGBot 推送相关参数获取](#tgbot-推送相关参数获取)
    - [Fork 之后如何同步原作者的更新内容](#fork-之后如何同步原作者的更新内容)
      - [方式一： 保留自己内容](#方式一-保留自己内容)
      - [方式二： 源作者内容直接覆盖自己内容](#方式二-源作者内容直接覆盖自己内容)
  - [感谢](#感谢)
  - [License](#license)

</details>

## 特点

### 已实现

- 支持使用配置文件读取账户信息
- 支持一日二次签到（9 点，21 点）
- 支持多用户（暂只支持手机号密码登录方式）
- 支持推送签到信息到 QQ、微信和 Telegram（需配置 TelegramBot、Server 酱和 Qmsg 酱）
- 自动同步上游代码

### TODO

- [ ] 分析签到信息和推送结果
- [ ] 支持登录验证码
- [ ] 账号脱敏处理
- [ ] 多线程签到

## 使用方法

### 参数配置

Fork 该仓库，进入仓库后点击 `Settings`，右侧栏点击 `Secrets`，点击 `New secret`。按需添加以下值：

| Secret Name          | Secret Value                       | 参数说明                                                                               | 是否可选               |
| -------------------- | ---------------------------------- | -------------------------------------------------------------------------------------- | ---------------------- |
| `USERS`              | `18888888888----abc123456;`        | 用户组，格式为 `手机号----密码`，多个站点或用户使用 `;` 分隔                           | 必填，至少存在一组     |
| `PUSH_KEY`           | `SCxxxxxxxxxxxxx`                  | 微信推送 ，填写自己申请[Server 酱](http://sc.ftqq.com/?c=code)的`SC KEY`               | 可选                   |
| `QMSG_KEY`           | `e6fxxxxxxxxxxxx`                  | QQ 推送 ，填写自己申请[Qmsg 酱](https://qmsg.zendee.cn/me.html#/)的 `QMSG_KEY`         | 可选                   |
| `TELEGRAMBOT_TOKEN`  | `123456:ABC-DEF1234xxx-xxx123ew11` | TGBot 推送，填写自己向[@BotFather](https://t.me/BotFather) 申请的 `Bot Token`          | 可选，和下面的一起使用 |
| `TELEGRAMBOT_CHATID` | `11xxxxxx03`                       | TGBot 推送，填写[@getuseridbot](https://t.me/getuseridbot)私聊获取到的纯数字 `CHAT_ID` | 可选，和上面一起使用   |

> TGBot 推送相关参数获取步骤可以点击 [TGBot 推送相关参数获取](#TGBot 推送相关参数获取) 查看。

### 运行签到

定时任务将于每天早上 `9:00` 分和晚上 `21:00` 执行，如果需要修改请编辑 `.github/workflows/action.yaml` 中 `on.schedule.cron` 的值（注意，该时间时区为国际标准时区，国内时间需要 -8 Hours）。

> Fork 后的项目 Github Actions 默认处于关闭状态，需要手动开启 Actions，执行一次工作流。后续定时任务(cron)才会自动执行。具体操作信息看：[关于定时任务不执行](#关于定时任务不执行)。

#### Action 定时任务

```bash
2020-12-30 09:00:06
## 正在签到第 1 个用户:
账号:密码:
登陆成功!
今天已签到,请明天再来!
签到完成!
检测到 TGBot 配置信息，正在尝试 TGBot 推送
检测到 Qmsg 配置信息，正在尝试 Qmsg 酱推送
检测到 Server 配置信息，正在尝试 Server 酱推送
```

#### 签到信息推送

| TelegramBot 推送                                                                                                      | Qmsg 酱推送                                                                                             | Server 酱推送 |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------- |
| ![TelegramBot Message](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/TelegramBot_Message.png) | ![Qmsg Message](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/Qmsg_Message.png) | 待上传        |

## 常见问题

### 关于定时任务不执行

因为 Github 默认 Fork 后的项目 Github Actions 处于关闭状态，定时任务执行需要手动开启 Actions，执行一次工作流。解决方法有三种：

- 修改项目相关文件，比如这个 `README.md`，新增一个空格也算，然后提交。

- 进入 Actions，手动执行一次工作流。

  ![Github Action Run Workflow](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/github_actions_run_workflow.png)

- 进入 **Fork 后的项目**，点击右上角的 <kbd>star</kbd> 按钮。

  ![Github Star](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/github_star.png)

### TGBot 推送相关参数获取

> 需要`TELEGRAMBOT_TOKEN`和`TELEGRAMBOT_CHATID`一起使用，前者用于调用 bot，后者用于指定推送目标。

| `TELEGRAMBOT_CHATID`获取                                                                                                    | `TELEGRAMBOT_TOKEN`获取                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ![GET_TELEGRAMBOT_CHATID](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/GET_TELEGRAMBOT_CHATID.png) | ![GET_TELEGRAMBOT_TOKEN](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/GET_TELEGRAMBOT_TOKEN.png) |

### Fork 之后如何同步原作者的更新内容

用户可选手动 PR 同步或者使用插件 Pull App 自动同步原作者的更新内容。手动 PR 同步可以参考 [手动 PR 同步教程](https://www.cnblogs.com/hzhhhbb/p/11488861.html)。自动同步需要安装 [![](https://prod.download/pull-18h-svg) Pull app](https://github.com/apps/pull) 插件。使用插件 Pull App 自动同步步骤如下。

1. 安装 [![](https://prod.download/pull-18h-svg) Pull app](https://github.com/apps/pull) 插件。

2. 安装过程中会让你选择要选择那一种方式;

   - `All repositories`表示同步已经 frok 的仓库以及未来 fork 的仓库；
   - `Only select repositories`表示仅选择要自己需要同步的仓库，其他 fork 的仓库不会被同步。

   根据自己需求选择，实在不知道怎么选择，就选 `All repositories`。

   点击 `install`，完成安装。

   ![Install Pull App](https://cdn.jsdelivr.net/gh/Ryanjiena/Auto_uclub_signin@master/assets/install_pull_app.png)

   Pull App 可以指定是否保留自己已经修改的内容，分为下面两种方式，如果你不知道他们的区别，就请选择方式二；如果你知道他们的区别，并且懂得如何解决 git 冲突，可根据需求自由选择任一方式。

#### 方式一： 保留自己内容

> 该方式会在上游代码更新后，判断上游更新内容和自己分支代码是否存在冲突，如果有冲突则需要自己手动合并解决（也就是不会直接强制直接覆盖）。如果上游代码更新涉及 `workflow` 里的文件内容改动，这时也需要自己手动合并解决。

步骤如下：

1. 确认已安装 [![pull](https://prod.download/pull-18h-svg) Pull app](https://github.com/apps/pull) 插件。

2. 编辑 pull.yml (在 `.github` 目录下) 文件，将第 5 行内容修改为 `mergeMethod: merge`，然后保存提交。 （默认就是 `merge`，如果未修改过，可以不用再次提交）

完成后，上游代码更新后 pull 插件就会自动发起 PR 更新自己分支代码！只是如果存在冲突，需要自己手动去合并解决冲突。

当然也可以立即手动触发同步：`https://pull.git.ci/process/${owner}/${repo}`

#### 方式二： 源作者内容直接覆盖自己内容

> 该方式会将源作者的内容直接强制覆盖到自己的仓库中，也就是不会保留自己已经修改过的内容。

步骤如下：

1. 确认已安装 [![pull](https://prod.download/pull-18h-svg) Pull app](https://github.com/apps/pull) 插件。

2. 编辑 pull.yml (在 `.github` 目录下)文件，将第 5 行内容修改为 `mergeMethod: hardreset`，然后保存提交。

完成后，上游代码更新后 pull 插件会自动发起 PR 更新**覆盖**自己仓库的代码！

当然也可以立即手动触发同步：`https://pull.git.ci/process/${owner}/${repo}`

## 感谢

- [CokeMine](https://github.com/CokeMine)/[Auto_uclub_signin](https://github.com/CokeMine/Auto_uclub_signin)

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](https://github.com/Ryanjiena/Auto_uclub_signin/blob/main/LICENSE) license.
