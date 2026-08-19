# AstrBot 原神 & 本人圣经插件

基于 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 的多关键词随机语录回复插件。  
支持两组独立触发词、随机回复、共享冷却，并可配置完全匹配时忽略冷却。

## 功能特性

| 功能 | 说明 |
|------|------|
| 多关键词触发 | 原神组与本人组分别支持自定义触发词列表 |
| 随机回复 | 每组均可配置多条语录，触发时随机发送一条 |
| 共享冷却 | 两组共用同一个冷却时间，避免频繁打断 |
| 完全匹配免冷却 | 可单独设置每组完全匹配时忽略冷却的关键词 |
| 群白名单 | 仅白名单内的群聊启用，留空则全群生效 |
| 灵活配置 | 全部通过 JSON 配置，无需修改代码 |

## 安装

1. 将本插件放入 AstrBot 的插件目录。
2. 在 AstrBot 配置文件中启用插件。
3. 根据需要修改插件配置（见下方配置说明）。

## 配置说明

插件配置为 JSON 格式，各字段如下：

| 字段 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| `group_whitelist` | list | 群聊白名单，为空则所有群生效 | `[]` |
| `trigger_keywords` | list | 原神组触发词，消息包含任意词即触发 | `["原神", "启动", "派蒙", "旅行者", "提瓦特"]` |
| `ys_quotes` | list | 原神组回复语录，随机发送一条 | 见示例 |
| `loli_exact_ignore_cooldown` | list | 原神组完全匹配时忽略冷却的关键词 | `["原神"]` |
| `benren_keywords` | list | 本人组触发词，消息包含任意词即触发 | `["本人"]` |
| `benren_quotes` | list | 本人组回复语录，随机发送一条 | 见示例 |
| `benren_exact_ignore_cooldown` | list | 本人组完全匹配时忽略冷却的关键词 | `["本人"]` |
| `cooldown` | int | 共享冷却时间（秒），`0` 为不限制 | `0` |

> **完全匹配规则**：仅当消息内容（去掉首尾空格、不区分大小写）与列表中的某个词完全相同时，该组触发会跳过冷却检查。该词必须在对应的触发词列表中才能生效。

## 使用示例

### 普通触发

- 用户：`今天玩了原神`  
  机器人随机回复一条 `ys_quotes` 中的语录。

- 用户：`本人照片`  
  机器人随机回复一条 `benren_quotes` 中的语录。

### 完全匹配免冷却

配置 `cooldown = 300`（5 分钟冷却），`loli_exact_ignore_cooldown = ["原神"]`：

- 用户发送：`原神` → 立即回复，且重置冷却计时。
- 用户发送：`原神真好玩` → 若在冷却期内则不回复。

同样，`benren_exact_ignore_cooldown` 可配置 `"本人"` 使单独发送“本人”时无视冷却。

## 自定义配置示例

```json
{
  "group_whitelist": [],
  "trigger_keywords": ["原神", "启动"],
  "ys_quotes": [
    "原神启动！",
    "异世相遇，尽享美味！"
  ],
  "loli_exact_ignore_cooldown": ["原神"],
  "benren_keywords": ["本人", "照片"],
  "benren_quotes": [
    "WC，宝宝，原来你长这样……"
  ],
  "benren_exact_ignore_cooldown": ["本人"],
  "cooldown": 60
}
```

## 作者

- ましろSaber
- Foolllll
- AlertKArma

## 支持

- [AstrBot 帮助文档](https://astrbot.app)
- 遇到问题请在仓库提交 [Issue](https://github.com/Foolllll-J/astrbot_plugin_genshinimpact/issues)
