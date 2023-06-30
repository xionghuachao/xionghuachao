import random


class TestRerun:
    def test_rerun(self):
        num=random.randint(1,3)
        if num!=1:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")
        print()