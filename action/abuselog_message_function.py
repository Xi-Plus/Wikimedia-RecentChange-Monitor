def result(res):
    logo = {
        'warn': '⚠️',
        'disallow': '⛔️',
        'tag': '🔖',
        'blockautopromote': '撤銷自動確認',
        '': '無',
        'disallow,tag': '⛔️,🔖',
    }
    if res in logo:
        return logo[res]
    return ''


def afLogo(filter_id='', filter=''):
    try:
        filter_id = int(filter_id)
    except ValueError as e:
        filter_id = ''

    logo = {
        4: '👦➖➖➖ ',  # 新用户大量删除条目内容
        5: '👦➖🔖 ',  # 新用户移除ref脚注
        6: '🆖 ',  # 点击工具条产生之测试性编辑
        14: '🤵➖🗑🚩 ',  # 自动确认用户移除删除模板
        16: '👦➖🗑🚩 ',  # 新用户或页面创建者移除删除模板
        20: '😀😄😁 ',  # 包含其他符号和象形文字
        26: '👖 ',  # 创建极短条目
        27: '👦✏️👥 ',  # 编辑其他用户的用户页
        31: '👦🗳 ',  # 新用户投票
        32: '🆕🈚️🔎 ',  # 没有wikify的新条目
        36: '🈚️🔎 ',  # 新增内容没有wikify
        37: '➖👖🚩 ',  # 移除關注度/小小作品模板
        46: '➖💎🚩 ',  # 条目特色/優良状态被删除
        51: '台↔️臺 ',  # 手动转换異體字
        53: '👨‍💻🔗 ',  # 添加博客链接
        54: '🚩❌ ',  # 模板参数错误
        65: '🚧🖼️ ',  # 加入无效图片
        68: '🈚️🖐 ',  # 没有首段的条目
        98: '👦➖💱 ',  # 新用户移除NoteTA
        102: '➡️ ',  # 从用户页/用户对话页/草稿页移动到条目空间
        105: '👦✏️🗣 ',  # 立即编辑自己收到欢迎后的用户对话页
        107: '👦🖼️ ',  # 新用户在条目中添加图像
        117: '🅰️🅰️🅰️ ',  # Repeating characters - enwiki#135
        118: '👦➖➖ ',  # 清空章節
        122: '⚙️⛔️ ',  # 机器人过度作业
        126: '🔠 ',  # 使用私有区编码
        137: '🅰️🅱️🅾️ ',  # 无意义字符
        154: '❕⚙️🔗 ',  # 非机器人增加跨语言链接
        156: '👨‍💻🔗 ',  # 百度贴吧不可靠来源
        180: '🚫👀🔠 ',  # 含有不可见字符
        181: '⚙️⛔️ ',  # Antigng-bot频率控制 3
        190: '🇨🇳🇹🇼🚩 ',  # 监测对于大陆/台湾国籍模板的变动
        191: '👎🇨🇳🇹🇼 ',  # 违反两岸用语方针
        197: '🗑️🚩 ',  # 添加刪除模板
        198: '👦🆕👥 ',  # 新用户于他人的用户空间创建页面
        202: '❌❌❌ ',  # 加入那个F开头的单词
        203: '👎🔗 ',  # 添加不合規範之跨語言連結
        205: '➖👎🔗🚩 ',  # 移除Link style模板
        217: '台↔️臺 ',  # 手动转换異體字
        '新用户加入明显宣传性内容': '📢 ',
        '阻止加入破坏者常用词汇': '🔞 ',
        '添加不可信来源': '👨‍💻🔗 ',
        '地域或团体观点（安全）': '👥👀 ',
        '违反两岸用语方针': '👎🇨🇳🇹🇼 ',
    }
    if filter_id in logo:
        return logo[filter_id]
    if filter_id == '' and filter in logo:
        return logo[filter]
    return ''