#!/usr/bin/env python3.6

"""
1.  实现统计一篇英文文章内每个单词的出现频率，并返回出现频率最高的前10个单词及其出现次数
"""


def find_most_10_words(essay):
    """统计文章中出现次数最多的10个单词"""

    # 用于记录每一个单词出现的次数
    word_dict = {}

    # 遍历文章，对单词进行统计
    for word in words_iter(essay):
        word_dict[word] = word_dict.get(word, 0) + 1

    # 按计数进行排序
    words = list(word_dict.items())
    words.sort(key=lambda item: item[1], reverse=True)

    # 返回前 10 个出现次数最多的单词
    return words[:10]


def words_iter(essay, allow_num=True):
    """一个迭代器，依次返回文章中的单词"""
    curr_word = []
    for c in essay:
        # 包含字母范围
        # 'a' < c < 'z' || 'A' < c < 'Z'
        # 允许单词里包含数字(可选)
        # '0' < c < '9'
        is_a_char = c.isalnum() if allow_num else c.isalpha()
        if is_a_char:
            curr_word.append(c)
        else:
            if curr_word:  # 当不为空时
                # 更高效的字符串拼接
                yield "".join(curr_word)
                curr_word.clear()


def solution():
    essay = """
    Tornado is a Python web framework and asynchronous networking library, 
    originally developed at FriendFeed. By using non-blocking network I/O, 
    Tornado can scale to tens of thousands of open connections, 
    making it ideal for long polling, WebSockets, 
    and other applications that require a long-lived connection to each user.

    Word1 Word1 Word1 Word1 Word1 Word1
    Word2 Word2 Word2 Word2
    Word3 Word3 Word3
    """
    print(find_most_10_words(essay))


if __name__ == '__main__':
    solution()

"""
排序可以参考快排（python 标准库堆排序算法参见 标准库 heapq.nlargest）

def quick_sort(items):
    def _sort(items, l, r):
        if l < r:
            q = partition(items, l, r)
            _sort(items, l, q - 1)
            _sort(items, q + 1, r)

    def partition(items, start, end):
        pivot = items[end]
        i = start - 1

        for j in range(start, end):
            if items[j] < pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[end] = items[end], items[i + 1]
        return i + 1

    if not items:
        return items

    _sort(items, 0, len(items) - 1)


if __name__ == '__main__':
    input = [3, 0, 5, 6, 4, 9, 1, 7, 8, 2]
    quick_sort(input)
    print(input)
"""
