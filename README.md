# 🎮 AstrBot 群聊圣经

> 基于 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的群聊随机语录回复插件  
> 本项目基于 [Foolllll-J/astrbot_plugin_genshinimpact](https://github.com/Foolllll-J/astrbot_plugin_genshinimpact) 二次开发，在原项目基础上增加更多自定义功能，让群聊充满欢乐与惊喜 ✨

![License](https://img.shields.io/badge/license-AGPL--3.0-green?style=flat-square)
![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![AstrBot](https://img.shields.io/badge/framework-AstrBot-ff6b6b?style=flat-square)

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🔍 **多关键词触发** | 支持多个关键词绑定不同圣经内容 |
| 📖 **自定义圣经** | 可自由添加、修改检测关键词和圣经文本 |
| 🎲 **随机回复机制** | 同一关键词可随机抽取多个回复内容 |
| ⏱️ **共享冷却机制** | 多组圣经共享冷却时间，避免刷屏 |
| ⚡ **完全匹配免冷却** | 指定关键词单独发送时可跳过冷却 |
| 🛡️ **群聊白名单** | 支持指定群聊启用插件 |

---

## 🚀 快速上手

### 安装方式

AstrBot 插件市场搜索：

```
群聊圣经
```

安装即可。

也可以手动安装：

```bash
git clone https://github.com/AlertKarma/astrbot_plugin_godsay
```

将插件放入 AstrBot 插件目录后重启 AstrBot。

---

## ⚙️ 配置说明

支持通过配置文件自定义：

- 触发关键词
- 对应圣经内容
- 回复概率
- 冷却时间
- 启用群聊

示例：

```json
{
    "keyword": [
        "原神",
        "启动"
    ],
    "reply": [
        "你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏..."
    ]
}
```

更多配置说明请查看项目文档。

---

## 💬 效果展示

### 🌟 圣经①

**用户：**

```
今天玩了原神
```

**机器人：**

> 你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「提瓦特」的幻想世界，在这里，被神选中的人将被授予「神之眼」，导引元素之力。你将扮演一位名为「旅行者」的神秘角色，在自由的旅行中邂逅性格各异、能力独特的同伴们……

---

### 😎 圣经②

**用户：**

```
本人
```

**机器人：**

> WC，宝宝，原来你长这样……

---

## 👥 作者与贡献者

- [ましろSaber](https://github.com/MashiroSaber03)
  - 项目链接：
    https://github.com/MashiroSaber03/genshinimpact

- [Foolllll-J](https://github.com/Foolllll-J)
  - 项目链接：
    https://github.com/Foolllll-J/astrbot_plugin_genshinimpact

- AlertKArma

---

## ❤️ 支持

- [AstrBot 官方文档](https://astrbot.app)

如果遇到问题：

- 请提交 Issue：
  https://github.com/AlertKarma/astrbot_plugin_godsay/issues

如果觉得项目有帮助：

<div align="center">

⭐ 欢迎 Star 支持项目持续更新 ⭐

</div>
