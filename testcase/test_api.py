# -*- coding:utf-8 -*-
"""
@author: JunCheng
@file: test_api.py
@time: 2022/5/27 10:57
@desc: 
"""
import pytest

@pytest.fixture(scope="function")
def execute_database_sql():
    print("数据库查询")
    yield
    print("数据校验")

class TestApi:
    def setup(self):
        print("在每个用例前执行一遍")

    def teardown(self):
        print("关闭")

    def setup_class(self):
        print("")

    def teardown_class(self):
        print("")

    @pytest.mark.run(order=1)
    def test_baidu(self,execute_database_sql):
        print("百度")

    @pytest.mark.run(order=2)
    def test_google(self):
        print("谷歌")

    def test_tengxun(self):
        print("腾讯")

if __name__ == '__main__':
    pytest.main()