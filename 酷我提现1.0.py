# 大大鸣版 酷我提现
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 kuwo_mobile  appuid#q#phone
# 代挂群 1025838653
# 多账号
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
# -*- coding: utf-8 -*-
import zlib, base64, marshal, hashlib


def xor_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(data))


def decrypt():
    data = "Hj=vkV;@2@^V5oC!{pOhLMS&*;hv6{4+%(USN^Z_PR>Wz*q4Fosvmb^-RntON912qG|WTFsO4$rJwWmA2Tr*5wXB%c4!)R(I4n*oP@~zA-01oQjKS873YQyas3GF3oMoK1m-K4ZU?%6vhQC}-oO`*c#Z~*Mt=@;c)~qJO<`CxU3X3GouvoS9ma|&!eNwRGCvwmuKfuSq5y=$Nq>dJM09KM&trV(Zx=~PQ<P#=^FcKBu<I+WM^<g~W!Ws$c&03)=Fhz8e+_92@9LT?%@|m!HP0C|$>I2@eo}RrO#SC)lH(CI6D<zm$I|YRnvvO}6VI8BdP#6@(c|1gzUgBLiH=7sKHL&3QuMCYV0bZ(7Klrc7FzY9%IQ`L8$F8^P#D$Y5=IY3leO&)oh+OK)FxrJQ|9NYpVMPu!uMIknVJ&nWdOyhEwXT3nKKBxcn#-+1vCyDc)N-&ETKGxKsW1@ky`^cW^>TdoVj#n5fAlz-J6M2&<+#qmw+pNO;fS5soIf3bp1$`gl6(VUuh0<c1v^}E7MkxZU1^k3HLjC_86y)OZaHkVsRtfbDqVL|CidI0=j@qOWLExG8U7cD1;E;rKMY&EYo5_qc^O`ti{~{B<T#x*y~*)5pZ*hz<jdfwR<VeDCE*rXC<e-%10fG&g|N0|CT<$Oj?p`jk@8xtnxHAS{2+~^+D_qgkpQdR%uBpq2u4CpJFQhRMwZB2zK^pZ@G*uy?2NfNxv<q~_kwqun6Q){3#5^qF*5*&P^%klUvV09W(O$LC7&dj<oKrgKe%MzC$K0R=S@s%l5HVuWp(PaaNQ@!s#a)WF-$brC!0}LC23^cK@!ho;@zsmYu57Gy~ojUZG6`JOGuV`^+!)0RaQ`3U;Cjuya<hdhl<$B$Lf9g?%l%-rq{`}4MUQYg@Rzf_q>u}oMmvrT#nmvhIqIxH*x_a`CiMo@GEOtBCJ0hA%ei<t3Yg>s=I0bt)y4A=M9K5Qy%v>;<A{R)H-`O253MS>~pG!ncXeON>IkSQskloeYDK6fZ{Bw#m67S0ef`GxqgnMf$XY8j6!OSAD`#T`9<>YvnBDQhrfp3?bVZrUvY&ah(D3YjP1PSbVnw;HJg&i{<*>Ws)U50g2F>Nq07{)<4p$}j5j<Zu;iM*xB&w@Dd4UkFj}&t&1tg*Zb342PYF3So&Lwxqf7hY+uF1$PGIw}{4U1!fDNb&`pY1gyq;)EGjkgBiJ{U5^1W+g0>Z$#UoKV(ApV|I1Jda)lt3$5{aUYdp0i5mS?TBzvfNMejfIX?Vs$E!w=)#$8bu02q-Zx>h}47M&;wuDcFCYjEu>YjQD4d4?Y5t!SnZD^efnG;!pj0^iYbYtdQhE~Nm584a5DU_&K~A55;}ZLs(;IUQH$g*2_;o4V-D@6)MM8gP2zI!=iL+z?8`b1GLp7D%bu4RFeGWpuwv-Aw#@ngGEs@*P%FUPX4qBl1S8`rLX49wadJOS@*s6fUO@V!YJ1!s66+o3t;JO&DF_`Ke=ZLfifA}gr_a3ANsF;+xQ5ca?IyLM9A=j#*TjelcC^liNUIS$y(0xDP71IJoRL!A3C^u?zpYQ4{3x<D7{j+mtAhs-b59No^>crHcNk5csbXAK_#!q7I#F8A)o*rh!A^T`LsJn%9WX0>>g$KT;0w3s*Gt`Io{sAgqn&;OX!hBIG$ps46Q{Vv;%j~&cSHN)Xwb~H2#f<VQQjoLz($k&zsDHR2-Oo@Pu}YiS%>dgA#1cDS7GqDf7-HSz#{sQU;Os0gaBXW2>7<p!SzrW#D*L{xvp^DP>vE&+1DJZ%NqM?Gt>Sqqta0XR|W>pV!K{RC2xWmcLR)wHkr7^!X>`<Al<Vp)}@~qp`m-Qy&8LUcb%hDq6|L!yW=jrj7<N9+g=~_?|^6=We4xO?WBjFA4t1fDN_brWUpSd#hGvEdF)Y<Zh+}L<>)6=cS707C5)iext^lKsG2Iwo`aw@s$K&Xw|amPCrR2r=HTCRWY@!0cpI#c&r@U^324+edjY*N?@RqT!^>?w2{0N46ng}EReWRWsj2^>FE~sbRYf_GbCUWasD#u6^9OjWuqd!&{o*+hc$zaU6MHw>mIJ!_(~?3cCVCRG0PSgrNhrX#aE>mGB;%}KG3RvdU{<Tlfgpt_b{P8G-<hy)egeBlLHSuG^Ch_Lvv3oeZi=65bPxT+BGmgS9=O^-)rNI`IGQl|-N1H3m#W;<fme5@U5_DHMdJ~T8=9Ucj`^mRy=~c>*{)uT+ym^MRy&KBjyIyLlK*z0X7r$H9>yLDyp)BcfmyR+sKq+UbNxuv>`O%~{a7P+2kI){6h0j2#2@?}tB@Smflv1r&;dew6srYMWBm|ezBmcTd&{FsfD?=_p!ctJT_ETjX7BBxnTH(Yd_maEbBQS<p!?;=1nF?hy4STTgX80?4tW;E%MpviD39KRR}#>aLl(uSc_uh~?MLPg?TlUxE>SRNf&O6B`mgtIhK$DSb)Qx#td50EE%5Q&)jCHKJ}JIqOpSTv<_at0Oj-eh6UdOcV*&d%uaJ&?N*3HU9Nzy0Gczk9GZ-lvj(WW_m9jjbbz1l>7esDBq0zbj3&D_~5Eu1HKGA~S$aa17a#u&@vT6x)!M|ejul%#u|E6)vz4%vAo<|&CaOs6a3kKL>C2mOIEiWW=-d|dA+B(Bsdlq?<kSRW+9dk;>wF7TGJtgP2gmPZ%EE1z{xDxzNUM8Bkg*$5PeFl;U4BrB%*#Znh7x|K8vbN7I#^l_&z<-?g>8eY3<UmO9Sr2FS7kpZ>$`nRJm#^2en$kOwpeNfeR@Onyu%IKDFF}k6Aa1wxm}w{re<#%vRh&YxQ-!7KpSCKlyP3D4Vp->fU7i(e+&TR=jTUQIy+9YQuzHXj<yw&>uw0)68<~Qbp&u908TW|D3f~r6o!WzAVXbyCKnR0ak2Nz%R~L7`KqY|GZita|=7hpI<+Y701jK8clLj=7g|neV4*fY}U6`B!r9<|9eB?2CEs+MEcIdr>A~f)@=rH|MB|5V?-Y{YB-^-9qiQXIq2s9q}i&PjuG+_cBjY{oCobQlhbUS$<r8>0w-Iy_veCnt`8$IuLwTknQZLsWeW}8e<I8Pn*qM{j9&<sAO91feytQ)8JM>7Ik<sqVTze^9h*=PrH-DaENy7xGenDc1CrX$z%?~QLD(s7Q1w}GaAVPtX28nN?Xm&pJkdjcPPonHJoLR1$Y*w-lu6=$Sy-#^4A<}w*FnpEfh>{Db!b2=i2kIILj9v_#bl-vYX{Uv-;i7gT!4k{hVz1J5>xFX~O?dBgR(Rc-F)Syu=t!ua9Gpk&YY@Rf%b8Ul%Gpa;=bb~Qv7K;YT!s%qI!{!Ntw-Kbu8ogyjhwOS^d*=tps+R-|UJ6iM&#5#!X8};d3`F<Mo|Hp12(Q022mx4Rwb2+H&M-&v{&|IV<P#IfrfD@kba8U4<`&I#igqOCn0cp9eNI^asLt8GbEtpTFEsRGAAeXbAMxE@+(X)%C7}2FGasc%?u;mbpB@yGpa5t>di<1-(*@@bVj%WX9-wMqsx-M?2Cdo-MP!R_Z2^)HC{OqB_8a((jvHdGHBcA$o(l83R%~zlXIu*O(>^WR#k^FCW_5WE^+w7(06SkNw3i;fw(`IYA2vf`th=)xeEe?!DfUaq;r{H<k)IEd;TE8cUpR9RAjl^i3Dx3bDerh4w>F95Jew1uOS~-T7p+u}U`ah%3j|)kT$niex1ar#y@K$x9^g1$?7k$)rjOjsLaB8X?}RO(+d1z)Q6mEAjZJ7FL4qZgFhh@WBX2_MJI~KPaE6|HCMHtwWRNg}%=d&0S>%gk33H2dbFpTm3K?NV;bOh)KPtQ}Pz7T!li)^o-tUNt7owN#ew9{SWX!QI^8pShZZ0&-$zsG}-E7U5pojT%9JuvB6N3}?whHPlN4E~fuHmIk7_#q+nrlSuCi9*ap_@t0nulM6bhvn}4b%rO7#HfuHQTgupfE~#`fozt!A^bR8ln+eIuMtV&L~Qiitc!oqfth&jAIv}5+P2Q8l(F(!K`)X2H;eRQwXKUJzb64;Y}d6eB}I<EIqzR5P%N=CE#-Q{;b`qxU;f-s@Kqrt?VNuzO4Oh$OA-E+6ZOQ7~?|hI=7zrZSs+w{;h!4(7A|^-hoda&oMxjFQcB%fW<r!?TKGMaRc+b+iLt5k-vZu0aD@|63Y&6wLi@4l**cxsbwx98F@h7a0@K5@trG>FW+*~jMyYGA(6I5YF$WoG<dB3kL+6kjG0XB<N36^!G5LYD=H<ZXaJL2(A!cEGol^vRwf&DeD|W-z;A;fxl)>xwa;!n-Zh0&QS0a23tG{&#;D~KtQ1mdc?l57*`SeP^(&$sA~J{@iU?`EfuP>rzNMPE=6KB|3iDp%Bn&%Me=kD&T~e`YrTUdsqN7SEq-bU9Ci_n=N}OkP8q#@lXxpN{@7UYq7XE>(pR}_C%W{7jjvk0Dz-*GGzHj7OoGvG;32+tRN%Vp0i-P`}`2};HL7g`vnwDQqLRvG%l-qKlHMxnGn$+l7?+WBPV~w@vs@NbIixC(z3=Jnns0u5bNQ(o>;XOFYHtn*ZSG!OA;E2gIV5CVeuoE@;C@vz9?{(b=>bg1DjQ8myKR#19eeF(d-HCLE=1cFy*XQ`=(?)E?I4bZ(ScLw7L3p&n$izC1AhH&)qIVmlU_n&s0W&cY2V$B}k0GG=4Q~)&`|;rFkS;n>$Gs#d9!q(RUc5XC`1OFyIirwSsd8X4S5m=SX;R<>V+#uN{weftvQh}7k1TmhV0<(upV%XC+JB5!%k?3i@Jv7`&?y=l09?N?m?kA^a(9;nQiXf(RF6&GIkQ4IPkbh&^{gb;PYd)E<3f?jZ=Lw?OKDYtwcX5B+hKDTuz55wQk|&-<iWAwC`JT;SYjb-Yif<Wz46@IEU*fO*)8sQ+Ynse^OGiM&hgN~T!g~QTi{+;jJ~9g=N>F%u9r+bq$bSuc@I?}lT@+Kt;TR#Y(+x"
    key = "NHwf8OYdiS1Av0iyc85RbEnVYklFQ9wc"
    checksum = "477991c92345008d"
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError("Data integrity check failed")
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)


exec(decrypt())
