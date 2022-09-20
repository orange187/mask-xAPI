import util.globalv as gl
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
gl.__init__()

###############正式环境##########################
gl.set_value('url', '')


###############测试环境##########################
gl.set_value('ApiIp', 'http://3.84.114.207/v1/')



# 设置cookie
gl.set_value('Authorization', 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0d2l0dGVyX2lkIjoiMTQ4NjIyMTc1NjQ3MDAwMTY2N'
                              'CIsInR3aXR0ZXJfdXNlcm5hbWUiOiJMYXlsYTg1MzU5MzY1IiwidHdpdHRlcl9uYW1lIjoiTGF5bGEiLCJhY2NvdW'
                              '50X2lkIjoiZTFlZTZhMDYtNTA5Yy00ODQ5LTkxYzUtMGRkNmRmOWRlNWZmIiwiaWF0IjoxNjYzMDUzMjc5fQ.03WPz'
                              'eUWWjj9vPtnyjZVxIXamG0hJHUiK2D7AsXPxvU')
# 设置account_id
gl.set_value('account_id', '8cefa6fd-aafa-43de-aae0-341732daa89b')
# 设置twitterHandle
gl.set_value('twitterHandle', 'Layla85359365')
# 设置twitterId
gl.set_value('twitterId', '1486221756470001664')
# 设置address钱包地址
gl.set_value('address', '0x790116d0685eb197b886dacad9c247f785987a4a')


# 设置环境lab
gl.set_value('lab', 'jl')  # 测试
# 设置邮箱
gl.set_value('emailpassword', 'BFTHQIXSOTBGGMWM')
gl.set_value('email_host', 'smtp.163.com')
gl.set_value('send_user', 'chen18739220686@163.com')

