#大大鸣版 金杜丹签到 
#有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 yymjdd  打开微信小程序抓access_token填到变量里
#多账号 使用#   例如：账号1#账号2
#
#
#   --------------------------------祈求区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#   --------------------------------代码区--------------------------------
import zlib,base64,marshal
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))