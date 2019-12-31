import os,sys
from public.models.myunit import *
from public.models.screenshot import *
from public.models.log import Log
from public.page_obj.test1Page import test1
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting

try:
    f = open(setting.TEST_DATA_YAML + '/' + 'test1_data.yaml',encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error("文件不存在：{0}".format(file))

@ddt.ddt
class Demo_UI(MyTest):
    """学信网登录测试"""
    def user_login_verify(self,phone,password):
        """
        用户登录
        :param phone: 手机号
        :param password: 密码
        :return:
        """
        test1(self.driver).user_login(phone,password)

    def exit_login_check(self):
        """
        退出登录
        :return:
        """
        test1(self.driver).login_exit()

    @ddt.data(*testData)
    def test_login(self,datayaml):
        """
        登录测试
        :param datayaml: 加载login_data登录测试数据
        :return:
        """
        log = Log()
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(datayaml['id'],datayaml['detail']))
        # 调用登录方法
        self.user_login_verify(datayaml['data']['phone'],datayaml['data']['password'])
        po = test1(self.driver)
        if datayaml['screenshot'] == 'phone_pawd_success':
            log.info("检查点-> {0}".format(po.user_login_success_hint()))
            self.assertEqual(po.user_login_success_hint(),
                             datayaml['check'][0],
                             "成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))

            log.info("成功登录，返回实际结果是->: {0}".format(po.user_login_success_hint()))
            screenshot.insert_img(self.driver,
                                  datayaml['screenshot'] + '.jpg')

            log.info("-----> 开始执行退出流程操作")
            self.exit_login_check()
            po_exit = test1(self.driver)

            log.info("检查点-> 找到{0}元素,表示退出成功！".format(po_exit.exit_login_success_hint()))
            self.assertEqual(po_exit.exit_login_success_hint(),
                             '登录',"退出登录，返回实际结果是->: {0}".format(po_exit.exit_login_success_hint()))

            log.info("退出登录，返回实际结果是->: {0}".format(po_exit.exit_login_success_hint()))
        elif datayaml['screenshot'] == 'pawd_error':
            log.info("检查点-> {0}".format(po.phone_pawd_error1_hint()))
            self.assertEqual(po.phone_pawd_error1_hint(),
                             datayaml['check'][0] ,
                             "异常登录，返回实际结果是->: {0}".format(po.phone_pawd_error1_hint()))

            log.info("异常登录，返回实际结果是->: {0}".format(po.phone_pawd_error1_hint()))
            insert_img(self.driver,
                                  datayaml['screenshot'] + '.jpg')
        else:
            log.info("检查点-> {0}".format(po.phone_pawd_empty_hint()))
            self.assertEqual(po.phone_pawd_empty_hint(),
                             datayaml['check'][0],
                             "异常登录，返回实际结果是->: {0}".format(po.phone_pawd_empty_hint()))
            log.info("异常登录，返回实际结果是->: {0}".format(po.phone_pawd_empty_hint()))
            po.phone_pawd_empty_hint_accept()
            insert_img(self.driver,
                                  datayaml['screenshot'] + '.jpg')

if __name__=='__main__':
    unittest.main()