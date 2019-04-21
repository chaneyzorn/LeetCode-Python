#!/usr/bin/env python3.6


class Talk:
    def __init__(self, desc, title, cost):
        """
        表示一个议题的类
        :param desc: 原描述文本
        :param title: 议题标题
        :param cost: 议题需要的时间，单位：min
        """
        self.desc = desc
        self.title = title
        self.cost = cost

    @classmethod
    def parse(cls, desc):
        """从文本解析内容，构造类实例"""
        index = str(desc).rindex(" ")
        title = desc[:index]
        cost = desc[index + 1:].replace("min", "").replace("lightning", "5")
        return cls(desc, title, int(cost))


class Session:
    def __init__(self, cost, track):
        """
        表示一段会议的类
        :param cost: 当前已有议题需要的总时间，单位：min
        :param track: 已经安排的议题 [Talk, Talk, ...]
        """
        self.cost = cost
        self.track = track

    @classmethod
    def extend_from_other(cls, session, talk):
        """在已有的日程安排上，安排新的日程"""
        cost = session.cost + talk.cost
        # 保持独立的集合，避免跟踪会议安排的过程中意外的修改
        track = list(session.track)
        track.append(talk)  # 将议题加入到当前的安排
        return cls(cost, track)


def knapsack(talks, limit):
    """用 0-1 背包问题的一维动态规划解法，寻找最大填充方式的会议安排"""

    # dp[i] 表示：当时间约束为 i 时的最大填充方案
    # 目标是寻找当时间约束为 limit 时的最大填充方案，即 dp[limit]

    dp = [Session(0, []) for _ in range(limit + 1)]

    # 针对每一个议题，我们都有两种决策：
    # 1. 选取这个议题到当前日程，占用时间为: 这个议题的时间 + 剩余时间里可以安排的最大填充时间
    #     dp[i].cost = talk.cost + dp[i-talk.cost].cost
    # 2. 不选取这个议题，占用时间不变
    # 最大填充方式是，选取两个决策中占用时间较多的那一个
    #     dp[i].cost = max(dp[i].cost, talk.cost + dp[i-talk.cost].cost)

    for talk in talks:
        # 下面使用倒序的原因是：
        # dp[i] 是根据已有议题的安排来决定当前议题的，即依赖于上一轮迭代中的 dp[i-talk.cost]
        # dp[i-talk.cost] 原有决策不应该包含本轮议题，否则会造成对同一议题的多次选定
        # 所以在一次迭代中，dp[i-talk.cost] 安排在 dp[i] 之后处理
        for i in range(limit, -1, -1):
            # 1. 如果没有足够的时间安排本议题，或者安排了本议题导致了更多的空闲，那么我们不选取这个议题
            if talk.cost > i or dp[i].cost > (talk.cost + dp[i - talk.cost].cost):
                continue

            # 2. 选取本议题，更新占用时间，跟踪议程安排
            dp[i] = Session.extend_from_other(dp[i - talk.cost], talk)
    return dp[limit]


def solution(talks):
    """
    根据输入的议题，安排日程
    :return [(morning_session, afternoon_session), (morning_session, afternoon_session) ...]
    """
    result = []
    morning_limit = 180
    afternoon_limit = 240

    archived = set()

    # 反复安排早上和下午的日程，直到全部的议题都得到安排
    while talks:
        # 安排早上的日程
        morning_session = knapsack(talks, morning_limit)
        archived |= set(morning_session.track)
        talks = [talk for talk in talks if not (talk in archived or talk.cost > afternoon_limit)]

        # 安排下午的日程
        afternoon_session = knapsack(talks, afternoon_limit)
        archived |= set(afternoon_session.track)
        talks = [talk for talk in talks if talk not in archived]

        result.append((morning_session, afternoon_session))

    return result


def report(result):
    """输出日程安排信息"""
    track_count = 0
    for morning, afternoon in result:
        track_count += 1
        print(f"Track {track_count}:")

        am_sum = 0
        for talk in morning.track:
            hour = 9 + am_sum // 60
            minute = am_sum % 60
            print(f"{hour:02d}:{minute:02d}AM {talk.desc}")
            am_sum += talk.cost

        print("12:00PM Lunch")

        pm_sum = 0
        for talk in afternoon.track:
            hour = 1 + pm_sum // 60
            minute = pm_sum % 60
            print(f"{hour:02d}:{minute:02d}PM {talk.desc}")
            pm_sum += talk.cost

        print("05:00PM Networking Event\n")


def quick_test():
    """测试"""
    case_1 = [60, 45, 30, 45, 45, 5, 60, 45, 30, 30, 45, 60, 60, 45, 30, 30, 60, 30, 30]
    case_2 = [181, 72, 33, 48, 99, 12, 5, 51, 44, 1, 24, 25, 32, 46, 30, 60, 45, 60, 60]
    case_3 = [181, 72, 33, 48, 99, 12, 5, 51, 44, 1, 244, 245, 32, 46, 30, 60, 45, 60, 60]

    for case in [case_1, case_2, case_3]:
        talks = [Talk.parse(f"talk{i} {c}min") for i, c in enumerate(case)]
        result = solution(talks)
        # 输出报告
        report(result)


def load_talks_from_file(file_path):
    """从文件中读取议题信息"""
    talks = []
    from pathlib import Path
    with open(Path(file_path).resolve(), "rt") as f:
        for line in f:
            talks.append(Talk.parse(line.strip()))
    return talks


def main(file_path):
    from sys import argv
    input_file = argv[1:] and argv[1] or file_path
    # 读取议题信息
    talks = load_talks_from_file(input_file)

    result = solution(talks)
    # 输出报告
    report(result)


if __name__ == '__main__':
    # quick_test()
    main("./test_input.txt")
