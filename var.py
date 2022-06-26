# 祖安语录
"""
type: list[str]
purpose: 祖安语录的列表
"""
herbalist = [
    '[CQ:image,file=file:///C:/FromHanTools/liaotian/img/jb.jpg]',
    '你刚出生就被你父母抛弃不得不去乞讨结果乞讨到了一盆屎然后尼玛你爹被杀你又被人贩子带去解剖这就是你的傻逼一生',
    '你就是歌姬吧',
    '你妈死了',
    '爪巴',
    '傻逼一个',
    '114514',
    '1919810',
    '1145141919810',
    '1919810114514',
    '1145141919810HOM',
    '和你聊天真开心,送你一朵玫瑰花',
    '先辈送福,新年快乐',
    'nmd再戳我一下试试！',
    '滚',
    '哎wcnmlgbd鬼！',
    'fuck you',
    '哎我cnmd谁tmd叫你m的让你sb戳我的？！！！',
    'gun，傻逼',
    '你礼貌吗？',
    '脑残',
    '操你妈',
    '艹',
    '我日你先人',
    '我他娘的谢谢你啊',
    '我********************',
    '你是sadbee，是不是',
    '你是来吃屎的吧',
    '一路走好，SB',
    '你是啥玩意',
    '你妈补天',
    'TMD',
    'CAO',
    '大雨治水',
    '你没妈',
    '你没妈',
    '马牛逼刚吃屎，你个马怂逼',
    'SB',
    '你死的好惨啊',
    '孝出强大',
    '宁真是个大孝子啊',
    '你好骚啊',
    '骚年，你爷爷在这',
    '试试就逝世',
    '全场目光向我看齐，我宣布一件事：你是傻逼',
    'your juice sadbee hehehehehe',  # 中文：你 果汁伤心的蜜蜂，他他他他他他他他他 | 音译：你 就是 撒币 嘿嘿嘿嘿嘿嘿
    '傻逼一号SB的你准备趋势',
    '我操你妈',
    '我不是人，但你绝对是狗',
    '人家走到女生面前是夸好帅，而你走过去，会被骂变态',
    '你好甩啊',  # 甩在南京话里指250
    '去你妈',
    '学校是我家，文明去你妈',
    '学校是我家，文明靠大家',
    '250',
    '我屮艸芔茻你妈的',
    'G他N的,一大逼抖子呼死你'
]

# 复读列表
"""
type: list[str]
purpose: 复读词语的列表
"""
repeat = [
    'e',
    '额',
    '呃',
    '。',
    'w',
    'www',
    '114514',
    '1145141919810',
    '[CQ:face,id=298]',
    '[CQ:face,id=178]',
    '[CQ:face,id=277]',
    '？',
    '?',
    '草',
    'c',
    'ccc',
    'tcl'
]

# 涩图API
"""
type: list[list[Any]]
purpose: 涩图API列表
"""
api_list = [
    # [API链接(str), JSON的键(str|None), 列表的下表(int|None), 返回数据是否为二进制流(bool), 是否不使用框架的下载功能(bool)]
    #                       ①                 ②
    # 如果①和②都有值则是[②][①]
    # 如果①没有值②有值则无法进行
    # 如果①有值②没有值则是[①]】
    # [] # ?x -> ?.??s 《《《 ?x 我给这个API的评分，?.??s则代表了这个API的响应速度
    #      └ 满分为5x
    ['https://acg.toubiec.cn/random.php?ret=json', 'imgurl', 0, False, False],  # 5x -> 0.96s
    ['https://api.sunweihu.com/api/sjbz/api.php?lx=dongman', None, None, True, False],  # 5x -> 0.91s
    ['https://api.yimian.xyz/img?type=moe', None, None, True, False],  # 1x -> 60s+
    ['https://api.ixiaowai.cn/api/api.php', None, None, True, False],
    ['https://www.acy.moe/api/r18', None, None, True, False]  # 试试就逝世
]

# 突发恶疾
"""
type: list[str]
purpose: 突发恶疾模板列表
"""
lis = [  # 模板
    # 取自 @IS-4/114514 的消息
    '{name}？{name}……{name}！{name}你带我走吧{name}😭你带我走吧😭{name}你带我走吧等等……{name}……{name}？{name}嘿嘿嘿……🤤🤤我的'
    '{name}🤤{name}嘿嘿嘿……我的{name}🤤🤤，{name}……嘿嘿嘿……我的{name}🤤等等……{name}？{name}！不对，我不曾拥有{name}……{name}你'
    '带我走吧{name}😭你带我走吧{name}😭你带我走吧😭等等……{name}？{name}……🤤🤤嘿嘿嘿嘿我的{name}🤤{name}是我的，你们不许看😭我鲨了你！',

    # 取自 Bilibili@闹闹 的动态（643333801201631252）
    '我好喜欢{name}呀🥰🥰🥰{name}来PUA我吧🤤呜呜呜😭😭😭不是{name}的错，是我自愿的😭😭😭',

    # 取自 Bilibili@闹闹 的动态（643333801201631252）下用户 UID298283272 的评论
    '我好喜欢{name}呀🥰🥰🥰{name}来rua我吧🤤呜呜呜😭😭😭不是{name}的错，是我自愿的😭😭😭',

    # 取自 @IS-4/114514 的消息
    '{name}……我的{name}……🤤',

    # 取自 @IS-4/114514 的消息
    '嘿嘿……{name}🤤',

    # 取自 某个群 的投稿
    '嘿嘿我的{name}，我的西幻风格魔法学徒{name}，这小短袜这手套这炫彩大尾巴我现在就想把他摁在草丛里薅光他的毛嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿'
    '嘿嘿嘿嘿嘿🥵🥵🥵🥵🥵🥵🥵🥵🥵',

    '请您枪毙我吧🤤请您枪毙我吧请您枪毙我吧🤤…请您亲手毙了我吧🤤嘿嘿我的{name}嘿嘿我的{name}你带我去杀侯淑林吧{name}请您亲手肃反'
    '我吧🤤{name}，等等，这是我的{name}你不许看这是我的{name}你不许看这是我的{name}你不许看这是我的{name}你不许看这是我的'
    '{name}你不许看这是我的{name}你不许看这是我的{name}你不许看等等我从来没拥有过{name}我的{name}🤤{name}我的{name}🤤{name}'
    '我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}',

    '嘿嘿嘿🤤真想把{name}的勋章和军服全脱了🤤把{name}绑在一边让{name}一边哭一边被我雷普🤤再把{name}的6b47头盔和6b45-1m防弹'
    '衣扔到一边🤤然后在{name}面前把{name}最讨厌的聚合物弹夹塞进{name}们下面和{name}最爱的ak-12里面🤤 ',

    '好像要♡好像要{name}的大几把啊♡',

    '{name}{random.choice(["哥哥", "姐姐"])}，给我吃你的几把吧♡'
]

"""
这个你不用知道他在匹配什么呢……
"""
re_die = "([CQ:at,qq=748029973])* *我*.*想(死|自杀|s) *(…|？|。|！)*"
