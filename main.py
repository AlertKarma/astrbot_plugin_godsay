import random
import time
from typing import List, Dict, Optional
from astrbot import logger
from astrbot.api.star import Context, Star, register
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.event.filter import event_message_type, EventMessageType

@register("astrbot_plugin_genshinimpact", "ましろSaber&Foolllll", "一个原神启动插件", "1.6", "https://github.com/Foolllll-J/astrbot_plugin_genshinimpact")
class GenshinImpactPlugin(Star):
    def __init__(self, context: Context, config: Optional[Dict] = None):
        super().__init__(context)
        self.config = config if config else {}
        self.group_whitelist: List[int] = self.config.get("group_whitelist", [])
        self.group_whitelist = [int(gid) for gid in self.group_whitelist]

        # 原神组配置
        self.ys_quotes: List[str] = self.config.get("ys_quotes", [])
        self.trigger_keywords: List[str] = [
            str(kw).lower()
            for kw in self.config.get("trigger_keywords", ["原神"])
            if str(kw).strip()
        ]
        if not self.trigger_keywords:
            self.trigger_keywords = ["原神"]

        # 本人组配置
        self.benren_keywords: List[str] = [
            str(kw).lower()
            for kw in self.config.get("benren_keywords", ["本人"])
            if str(kw).strip()
        ]
        if not self.benren_keywords:
            self.benren_keywords = ["本人"]

        self.benren_quotes: List[str] = self.config.get("benren_quotes", [])
        if not self.benren_quotes:
            old_reply = self.config.get("benren_reply", "")
            if old_reply:
                self.benren_quotes = [old_reply]

        # 共享冷却
        self.cooldown: int = self.config.get("cooldown", 0)

        # 完全匹配时无视冷却的关键词列表（新字段）
        self.loli_exact_ignore_cooldown: List[str] = [
            str(kw).lower()
            for kw in self.config.get("loli_exact_ignore_cooldown", [])
            if str(kw).strip()
        ]
        self.benren_exact_ignore_cooldown: List[str] = [
            str(kw).lower()
            for kw in self.config.get("benren_exact_ignore_cooldown", [])
            if str(kw).strip()
        ]

        # 兼容旧配置：如果新字段为空且旧布尔值为 true，则回退
        old_ignore = self.config.get("ignore_cooldown_on_exact_match", False)
        if not self.loli_exact_ignore_cooldown and old_ignore:
            self.loli_exact_ignore_cooldown = ["原神"]
        # 旧逻辑中本人没有完全匹配无视冷却，因此不自动添加

        self.last_trigger_time: Dict[str, float] = {}

    @event_message_type(EventMessageType.ALL)
    async def on_message(self, event: AstrMessageEvent) -> MessageEventResult:
        group_id_str = event.get_group_id()
        if group_id_str:
            group_id = int(group_id_str)
            if self.group_whitelist and group_id not in self.group_whitelist:
                return

        msg_obj = event.message_obj
        text = msg_obj.message_str or ""

        if event.is_at_or_wake_command:
            return

        stripped_text = text.strip()
        text_lower = text.lower()
        session_id = msg_obj.session_id
        current_time = time.time()

        # 判断触发组别
        is_benren = any(kw in text_lower for kw in self.benren_keywords)
        is_loli = any(kw in text_lower for kw in self.trigger_keywords)

        # 如果没有触发任何组，直接返回
        if not is_benren and not is_loli:
            return

        # 确定是否属于完全匹配且允许无视冷却
        stripped_lower = stripped_text.lower()
        skip_cooldown = False
        if is_benren and stripped_lower in self.benren_exact_ignore_cooldown:
            skip_cooldown = True
        elif is_loli and stripped_lower in self.loli_exact_ignore_cooldown:
            skip_cooldown = True

        # 如果不是允许无视冷却的情况，检查共享冷却
        if not skip_cooldown and self.cooldown > 0 and session_id in self.last_trigger_time:
            elapsed = current_time - self.last_trigger_time[session_id]
            if elapsed < self.cooldown:
                logger.debug(f"触发被冷却限制，剩余冷却时间：{self.cooldown - elapsed:.1f}秒")
                return

        # 优先处理本人组（如果同时触发两组）
        if is_benren:
            if not self.benren_quotes:
                logger.warning("本人文案列表为空，插件将不会回复")
                return
            self.last_trigger_time[session_id] = current_time
            selected_text = random.choice(self.benren_quotes)
            yield event.plain_result(selected_text)
            return

        if is_loli:
            if not self.ys_quotes:
                logger.warning("原神语录列表为空，插件将不会回复")
                return
            self.last_trigger_time[session_id] = current_time
            selected_text = random.choice(self.ys_quotes)
            yield event.plain_result(selected_text)
            return