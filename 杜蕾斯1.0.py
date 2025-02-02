# 大大鸣版 杜蕾斯
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 yymdls  抓取 token
# 多账号 使用#   例如：账号1#账号2
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
# -*- coding: utf-8 -*-
import zlib, base64, marshal, hashlib


def xor_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(data))


def decrypt():
    data = "7rc*bFEW0g3n%EMAOoYaB-e#kc49Fp)}ly6qX#Qn8paEm!saXAW6}!#xL_7_cT?PU6Tu@<Wb12vxf@zb=s=9u>AArcp4_4Roz(S%AO8Qu0cz$!xQGF3;rrJB&|4c+TBj?2@1c^2vZT7bBHW+YGn4(t%@As&mB{#MWyi7n2Y!GXFY(og%bz=e_BIcX#u_+O)AXk~l9nAj3ua59Ugl7L!M<N5j=5N$rJ`$VpKPa(VkrSYIK9&2Z|j-_O_-H#=Z*5<QI=#VDtzHLTO$Q>`|z_s=5TIt;b+>jU1R_0_glKjHdy=KThl0_O*2Rot;*u7E@-g<oGc6ae(V!_9<|Kogcg|i&3=Q5&tf}oE?s`>CCdz)NPJsZ1}8Pl415YoyDidwL#AqMa&)`iIDkWqmcms(CpkW6j-cZA)vwY05~ZArbio4>3XT=on3#n0ff=NQ40*<1lk}dY8A$b#o#co7?p%}UHl>UO-F)u>095}eUzJBY>aC1}%|`_DgE)&u!Oua%T^44ROqkfPaINEY3k0K$rjGn~yyh?sqq4fsDfyXWLS(lQIulyw+U}Ct3Ncax_TS<3KgYVahKY|L(746u7`Y@4`_);6{qM|<j!JnCB@mmmhp{}3q;!%5sgscDcAJ36vxU;eHEk}e8Q|D(sPt8zgk=5c64=z?T-;8nSb}KLid_mnmOU(*@trY_r_*CD(n(d8(DwAFW-<}`x3;YMls$@PmF_q_$O_ijPiq+%a4e94XHU^`!I!5?j*xtFgpz8_wU~1t=}pq?9Aa9jY-o%sxD(8tBdjy<1uNOsIo^rzj#I{}{i1C<3JxaX9)vU_q&z1;u1|UgSqtoOH8?t6DE%r|UHVhh&8cQEltfR@HFcq1IUJ=WPZXO}K-&F+bV4}bdWLiwf1)1XQ0R2p^h@gN!EnuH*N|I6HgjwH{syFuieEE6$Fv>J70Vo!d4{~{$1>e$`u`6o^Lb1n?h2#KWI}=FS&ZB5(35@Z)PPL>#)j<sBWPlB9`a!>=HMOVoaJMgJFDxk=AKwM3uxkhHXuJ-3ZU%=4QTyTcJ(tz#fIU?%WX0saAq*7NV&h#ka}*+OH=)=@y|5~@@u7DroiM>=xyqpb!&bxR*gXEh@flL)m4ccSn`;DesK!{BMP!=b8{BNX6w$M_jT5CF^(i{r}>2N@Tv#vw%12(1OjAkg<rUdOeyI;TUe9p_PNB>!c~YS@D)PtMd0N|T$>iK#-G(szOS*rcgK)y%)B)?w({qyOA@uwutcvnGImOW_p&wX9amJ(uq*;y5O@?4qji;X%81^B@|Y>%n?9-ivSqIUZMVR?%9FB9=hi7m51ia2>Zm?TGxFIc7|9uw_ehB3HDLJxIFDd`MSIZ|AEp0Ek+jVd<>RRh$hG&|?z5vV65+$XxRSSkRb6Gv3~jqCn4FTC_z~!wv=e3Wjq-WLpJ(|_25D#c&yp&-hAAkW_uHko3TNc*4WExh_h5+@W3#lr3lyy`i-hGnlml17H6o%)QWo~VT_GE|K7JmwUogFvu*8x;-TuVJZDm0P!?kL?$ezYiYFG7vOmsj2^_6Z5Iend0qy=R@{11x!MqF&UMGBE2+N4o{e?T;}08ylfR6evPW+{k78+N5^eIOck&c*SE9wXh5v!|D9kK1@<RSIu#9?PUIt`D{q!x^=Xz^>j#c>`PoL*4|4{V^;bpY89U3%Hu{Lv(o4We#nl$f>aBN{t7-Y3HEbJqhBe^DEvyqoe?}AM|U^pj3~cL)$>a9~6mD*}I(}h@9Y|KU=6~_eh#svxZ1CC>m#NwT;A<vx4!*<Gnp#fx4rcUYY*RJO>F6)Lo-mCHi0p-j8d=+5%^PplVA)>C5Y(+4mqGbk6FPj?Nt64%)!kJ*)9`=Hn;^RH|Ffe+)DiW*=)Qhl*(QIL?_plRzne^oI!<MEt<{;(HdkisxE**@Uc#b**tIEyhh?&Tvn+FFv<7|HCrK5>t1C_Cyp#0dDTHHRXdGTh0imA=&l`DYa#uNRmVlZT#(UcWhv03RtX|73B+e+kvoQoi2oQuz*07$O>nSa^RA3sbMi~sP-#Ek`P4x+lYmJ(Esppev!JxCBw#K=qO#x3F*gq*OBU=<msLh=jvWC?@=8r-k$v^H_d&=5=F@ETLU8g_kz-t@Wf*i*K(K=6>=H%<_H0bo7l4k0{|-9IJbLsO+m`QwHi&v^9bdgk)+-8(et=aZa;5?v9H+`c*;8mBCAI+8b2?RQ%+MHjk+e)RfA=&b$G{eNy;GV?)E3fa{#elj!|ZQ0Rbt)!q3Fe+Rb&oZ#guaa|U*YDZH)2R?Hk$uA8@J*$A|~E3ahW`s0}R5A<x4_9Do-l(L`9qMpo|hRCk~;fFTwp?IUb;^fx()l8()`0>AVRE?_EM;7X{bJkew;`n7f+UqTOxsl@N#IbB2gJ1;T`Th#+zRU)#t4r-JT?`FJE{ujejm(QLB>F#-v6g|Xt|L&##@1|ww+*Ul^xm!Ajl0FDBjs$))Q~=oh7xAOf63k|&B<z6Yb~Y{1og6mf6Hb}K%mA@6i4EI)G&zV(*HnmYO0Ir0+DQ60&}(1CekC*z&D>gS-Q_s!z<aEF!yw#ob%l9R7Dhh7(0%%{<)jiK`}*H)EnU55gAef&uYn9cD*Q3Z{X)wc~<Vi<s^(5ciqNPN-ov+#R37XCA&~PB#fRGFCB$|^o9Bp<KM1ekJLD*l^(XD!!-&8j}3{r6=R&d8=Z~ZNM2GejGc9F`+o3pFzde_u=LPMov-~Yor-W8g=|!C4D&x3aa$2G92gY@)6NrT1Vo=Rj|Oo<QA!MO@|f~Z<I*y<hvgdsP8$3Bq%i~N7QwK|o2ySyOoCPQ%Yk6#G2fad<0Lrx-imrc1ut+j7p}Bi0X%9s`Ug7LIxJLJXO+)g9xyl(`deb2a6{V{ZG=7AOU~Wp`Ue8oIxAGTXEkT=@WkwoeBp_~0mvtZ?28GN>+2lZ&oT2!KF;ZbX&=Q~j&L|YbQH~p=U5D}Z3iAMPU^;P_o9z<kcf)A7}Z@xuLX@JO2J&&%gNo#F%R#wvOm!IbTo9X<N;#pZJ?VaRwgZ4AFBbi(iC@Rr=n$dc5AO9QS2+w-WRa(1Ggi2`JUW2F7I}2aOR(*nNRV^#I;Wx;-3)v&Ej97azq#}TXvp|Xff@&Zf?u)=3FA7v4V8r<%o;P(1U57qCnv_?@bUO)e9ZlsdRRbDu0k07_J+7wthQk4N}Fdc>#u;^7m5|j;8u)vr^$fN>xG>r#tk6ocA{<;&beI1SU9Zp7`(sMg^)s3Tb4)!!W-adxdT%*2+r;gGIcK&dwizOl&T22<#D$DjZjj$d)V@$2!F%&LG4z%PJMd#W{x~^Q=VAz#J_bU88H#e4}xfLXP(oEp*G>_=vLx)W~0>eKH~2UCtyx@4Dy6{sz`6SuNjQ+(Zi<mkLzkGC9Q!Qo?Us!gMq$4DI*D$lNp@f|pN+15Lp"
    key = "ofBtDbeXrhObiKaRSgd5MLS9DbtYx23W"
    checksum = "007fd6406a7cfb34"

    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError("Data integrity check failed")

    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)


exec(decrypt())
