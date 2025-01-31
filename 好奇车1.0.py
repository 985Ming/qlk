# 大大鸣版 好奇车
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 yymghqc  打开微信小程序抓accountId填到变量里
# 多账号 使用#   例如：账号1#账号2
#
# Expecting value: line 1 column 1 (char 0) 报错请求频繁 过段时间重试即可
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
import zlib, base64, marshal

exec(
    marshal.loads(
        zlib.decompress(
            base64.b64decode(
                b"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"
            )
        )
    )
)
