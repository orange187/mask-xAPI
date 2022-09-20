#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import util.globalv as gl
import config.config
import util.logger as ul

class SendEmail:
    global send_user
    global email_host
    global password
    email_host = gl.get_value('email_host')
    send_user = gl.get_value('send_user')
    password = gl.get_value('emailpassword')


    def send_mail(self,user_list,sub,content):
        user = "mengyue" + "<" + send_user + ">"

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        # 邮件正文内容
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 构造附件（附件为HTML格式的网页）
        filename = './report/index.html'
        time = datetime.date.today()
        # time = datetime.datetime.now() #报告名精确到时分秒
        att = MIMEText(open(filename, 'rb').read(), 'html', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="%s_MASK-X.html"'% time
        message.attach(att)

        server = smtplib.SMTP_SSL("smtp.163.com")
        server.connect("smtp.163.com",'465')# 启用SSL发信, 端口一般是465

        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        ul.log.logger.info('send email successful')
        server.close()

    def send_main(self) -> object:
        # user_list = ['xxx@qq.com','xxx@qq.com']
        time = datetime.date.today()
        user_list = ['chen@mask.io'] #,'shane.wang@mask.io', 'alex@mask.io','junzhang@mask.io'
        sub = "MASK-X接口自动化测试报告"
        content = "%sX口自动化测试结果:见附件" % time
        self.send_mail(user_list,sub,content)


# a = SendEmail()
# a.send_main()
