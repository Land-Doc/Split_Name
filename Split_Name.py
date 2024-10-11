from pypinyin import lazy_pinyin, Style  # 用于提取中文的拼音的首字母


# 分割姓、名和首字母
def split_name(full_name):
    if len(full_name) == 2:  # 两个汉字的情况
        last_name, first_name = full_name[0], full_name[1]  # 0为姓氏，1为名字
    elif len(full_name) == 3:  # 三个汉字的情况
        last_name, first_name = full_name[0], full_name[1:]  # 1:指后面的字符都为名字
    else:  # 其他情况，不拆解，返回原值
        last_name, first_name = full_name, full_name

    # 提取每个汉字的首字母，并连接成一个大写字符串
    first_letters = ''.join(lazy_pinyin(full_name, style=Style.FIRST_LETTER)).upper()
    if len(first_letters) >= 7:  # 若拼音的首字母长度大于等于7。目的是防止AD中账户的Initials属性过长导致更新账户属性失败（限制为6个字符）
        first_letters = first_letters[:6]  # 则只提取前6个字母作为首字母
    # print(len(first_letters))
    # 提取汉字的拼音全拼
    # pinyin_name = ''.join(lazy_pinyin(full_name))  # lazy_pinyin() 返回一个列表，char 作为参数，返回该汉字的拼音全拼
    return last_name, first_name, first_letters


if __name__ == '__main__':
    full_name = "李四"
    print(split_name(full_name))
