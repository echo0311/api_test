# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global password
    send_user = "echo20110@163.com"
    password = "lxq900311"
    email_host = "smtp.163.com"

    def send_mail(self, user_list, sub, content):
        user = "20110" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        # 通过率
        pass_rate = "%.2f%%" % (pass_num / count_num * 100)
        # 失败率
        fail_rate = "%.2f%%" % (fail_num / count_num * 100)
        user_list = ['504186732@qq.com']
        sub = "接口自动化测试报告"
        content = "此次共运行接口个位为%s个，通过个数为%s个，失败个数为%s个，通过率为%s，失败率为%s" % (
        count_num, pass_num, fail_num, pass_rate, fail_rate)
        self.send_mail(user_list,sub,content)


if __name__ == '__main__':
    sen = SendEmail()

    sen.send_main([1,2,3,4], [1,2,3,4,5])
