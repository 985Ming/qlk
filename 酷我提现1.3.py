# 大大鸣版 酷我提现
# 有问题带着github上的小星星请联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 kuwo_mobile  appuid#q#phone 真正手机号
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
import zlib,base64,marshal,hashlib

def xor_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(data))

def decrypt():
    data = 'KbiP9V<amq*`4D3nT#p3W?X?rlp!~KqZFp=@%Zc`&)y}8($(R!sl}w|V@T%QomjS7Wd7Tbn;%GAXX^zSi&JfF;Za86f_Kj^hov2d&fFMYIK-@i4*wiehC<KD$7%l|LmG#d(l8%$K%#N5i)^g~uaUp!rD5a9Mx@Pq?zjSxw08Jx$2Ad+%!L9y#6L%v4SGPf!d+VyyJcYcrd{mjgc}~eO8gt$qf!js4SEJ0@{bjXXk2-m4;n`4H|{O0SThBXUn%DT0lHy%b4p1x#gg_c@D)$(s0DHVJq6BKAh$~q`Je7l0xyoagJ722NGb6OOw5&?N+s*=5kOqZ4HT*oZsT0-K{<HmcY?-2RXl*qiJT=yRk0OHMfWVQKBdR$?_J1V91uim$DHC(*pp<}dlrEq#m1S$Q<$J`f!&!^Kkd>1?$3DY1#h?be#A&|Y}CpWQk88BTgFUy%YK}pAToT4zEH(Gp?5Dyn&eNON4hyHiKtIuvl#_%Cn4ecZ<G9Px&bSemn@@#=6fJT_ff32!-zwyjQmJnA+1n=B>1wb9B{Mf&T1$CERTb|qd|@QUTSLS(xvL7><>whzL(afX$UeTh0-^ii+RhohL6FJzp@xAgO;!$8fdCiO;V2KZgqEArXy-Ub?wYrjm_)%Ka`%M7!Qs7B7pm?+z0qyc6{`<HI#CT6?+3sek2S)cRxrn>y)z34-3&cmk73`uDm1wvopGi<~lyI0H>e0)=pc%xv2s%MP`EqIu)G!Kqp-lJnrg?Rft=d?jypHyP_wiEW9<W(uS+;)=8i-B*%W1&)JV)Gcq`<v#4tc2onO<+F4%l$SrL84oITII7O$HiQr9upxR<H=Wt3r;msKPB>oBJ@ULwrY_NcMt0ADS9uHl8Q<6+V>)00^q}kNFPrb_{c+jCt57b(k60V+VLS^=u(2GrlJFBxgg+T*h*<#09<_U5tJM^nT!lF-S)79n`3scXDK2qhPvb9k0%*Rq)$wVr<0gDWblre-c2nr?TwE%zZX`}EB1@Tc`ZjN&hOcl0m`kQ;!by$$<XYCQ15ZecLpxvIlV@ZFe1j#gVKtOXgGni?Xz{ilMUjCG=_1g5|=d4$XkMnoPt8-kLz*1?}FbhS2`mU~16Su!Q<0B>m0af?ufvH-BgKeL!b0-e(<!K@>9yY{s{$LL}fi#F8FI*frEK-F7B*d7<o%Mm(mZhnQEqJMsoa@l-iJQdoJwhVmn~W8xU&1Y7iuWd<`I-I3uH9D2{HH~eNDFamkWqkk-tuERNnCB<R?5WyzzNWuHL;+)p-`KB&F)1eM@LlWGJ+KCB}<JEi25~v>-Y-PxAO7Irv;Ehy1cx*#kM|)pMM~lb^qXx%UOf9Y46(kA?>2Q!$kD;du71M7XhF(h+LCx%iO|cz;yF+TeNX2aFVH(Gb}Db*9q3EUmR%@7GozD$FRMZBw#9`n@p3cwP?!D`q46T2l=E1%oKrn@!9L^!P}2kwftsPpqV)(M8%4=WL;v`KWu%r&Zl5jYa(m~RVIMve`24|rU`&UO*ONlMJ+Jd%@zagPEw_r<<kgNbEIuTXMVer-1(5k#hTPWZ+y7=hJxkIflN#B_JS%EY5mAPbgO(NyuWUvC?2BK{Vuusyy}6iotZ;eewqGeGK%?!f!&yc%3FwC=<<upm7EL`PhGfjS4JE^0c>#KK0gO-7+`r)DrVIGdV+7t^wLuG&}~L|fLKJP#0eAL>jILdm46f>gZSVIaroBW_taS*1lE<m!3P4wXEW_Qj8mt*{`hfj;K|MKShye=f-pb3PzVew#VF??*Wc<7K*u&w_*XE3k5itj_c!?ZaMGm46W)olJLkyij$;lEHBarS_^p1g2yA4lHfWtAHX&KL6a#9If2eOKfmiJsl5+taFJQyj;Kjb46iYon0v>%T?hYy!x0Km}n#8VK-``i1cjo-T8=;}CYh5`;0ggjKW%rK*g|=QQwA~tb!$HnBhntJ!q3Uplahp2(P(IQTNWPIkCjFlvB~WVk`gStbN(I}Y!hI4R05S+b!ahu%Y!_<9?a^K+@;zzKWJS4$A;O2wbxaU4A=3SH1HdYPw20E*M?CD1SenG31>P|>JCovjd13yNm#_;beTL+rvjZJF8EKIk4`rc*T{A=ia>1?pa8Hv%E2rM0d6*Aa7~0JF465AT*4^41Jmw7+@TWX}GqrUn1eh$ACda};wTB9L=QNCy?7vTs=cH>{UFUHEJ+r>lM}ufqdyqG(CBHlr*lfaq-w%yW=|KTE#dmDaRa1M6Kf>6QikvQuCzsg<1t&Ajua;Xw041mSMuC2CyZZ*Ix3|97rw;Cngg&bbjV)9=uG5R2wZsbj%BtVWs^&806o2&k!oUzrF!VPK>J99F5ta>jShEg~Dn>Yg)k<uU_*qZyl&er%n54^0?PE!VQ;nkKY*RG=_?OFU8Z+#vn_1=&7Y_>0n>79^;|FBO2<6$3+=1f&xcSzT$J$#sXDk?6O0f7h(cX}35~C-+lhg3VauRUESsY1T-P_201LqH)h6V9um&#O{wJjp^5j=1nR7prO$(*c))zMG$=R8wk-(>A2sF&sI)f}Kc^qdBi;<c>rpzaFS?JZH@>aSTJABq1)6DV6pj(5>XC1_=TCE5Gdo@bhn59jTc`&FbJE&+k<anKh9ow&+Ryi){dW(7m2@tPQ*+N0unPIxgn(R{@5i~CxZY}29G5|n7)i6j;>QCw-c$uSz3mUWY{T0&CnomY4U#K~*?LlkxEr2hi}bnTsOhBQu46R=4W97J=KON$Z8`4!QgW~STN=RK7PJz6t)ZlaoQ&!sYT3qq=g^yWe3IfvsbMxy=p>p0!w_alnO_{<2YSF%(`x-zc!AmRgi@&bF@M5~k<bU{0If^=6|s1iXNYikuOED-7Vxmu<yE?|5Q9Pi$+q%b;F#W<j7SJO)_QQ>2Xh0Pu;-o>gnG0RXtGxzlvFA*0SdPF6OB9+D2{u0TSy}n#V$pv05i*84|WIi!U(#u2*4!WcR`?Q~72rF03CPr%#Ft8^d7z0t+4M+G~(ddX@{j!J~uxa~~BX~H!XV!nfnLbb!pO%u3n0F;f^2OXe3+ZQO*sRCVip9P=9Zl+-Bb?yj$2I+!I1Z7*wz1<zSsEy^?5D*GT+~r0w)X1AWErk59~byls*ln)0tkuB-QT(-^jQyda%|v|Z=Z^2a4)Iw@%R9uC2KHVK`|BsK9J4#DODV8X&fG^h8A}8sbMzCX4D2;D6q&46@t=UwD?DVZ#HPl5T;ya0s<D1Ic!RCY^#?i_$^3p2okgUBTSRX!_?hulnFkhBhEmF#r4#7lc-AV-KsT#elzLT4zw1Ne;wQXgr9^hf?GzzdaB#O_=e&&*)b81d}lxyPP<9Eu{aidV9sJ(#=A*!e}*4|^UsqB43odaZ1BFNsoPJ@ysa~*Bh=({3(dTY0+wxAg?H|LpY?H7&FUocH~c^lVv2{B+(KmM%uaKZXcn!}RB?ep-96EZ6OjK_zFR=2HCYVZy_l3|kIn8cN4d5C$zb$^z+v=>8=$wsf%TEtYAZ@*VIW2A`$J?w*EnW4V-$2jUJ3`|Nl0DIxZ-Lt0s>dLtSofsH8z?WMELe>Q##wzN*#34Qy?cHDlpQ@NOxhK7s2m>fQUaQ99U9=`|8eIQfJSnMteP=8do9^Or&`nY-I)-L~~OvS+dlhIB3IiG2hy<kKPBaT3qV9_;-67mbd<yEVeoF&%T0-JmbJeScA4Mae~<Hdhi@mtylHF0DY6B`TQ4GwE<G7P4rn6<VO=&-=!KHrpZtw9i2eQr}o|;Ai)B$+09A$JDn+_FpGsooc9>g#~S(H$I5eG4;2Ro`J&+S<WVPZTOL6LTgbczjZ;>0<Z8P0Ww;!zYn6HKxK$o_#IB0O(!km>AjFuMwTxeo5Zm8HVHUk@h?CJNA^qbs9Do{ywuHfrIpk5r_Mf7$Y?=*6_*B#Qp*A@HQp_)b!kSBdwfLqLI6MtLG7?B@EU=PA&iQfClKMH1L9CQCJ!Get7(xkCaDnD^<1h<>bhZ#wj9M<e-P0Qj&;PUMmpK#$2*0Yu=Q$^ZyB*{boB(WIu!hZh*tx@KGIqvh03myL`Oj1T9bYlTwW!)b%zpx7J*hiWH1yPAZgWUxYE;M(ML(nvT3IKptno+!IT8&}jOY|BM|Ak-k-cj~b=sl(N(-QrQB5omYQ#t;iMV%I$i-e+mZZ6L&Z*8Q89V*xXsNfNs=D28I~gCDtC|Xfn^^@-p<rVw93`BFZq4RKD;Iq5Jh4P?=zpJL^L0K1Fl+G+Dkj?tkO9rmbF^<H`@)y{;-Dv;Zki!qz3Dw+m<V9Yv_pOO$tNpt<ON1-S*K?kZg)-(FWZ<ec*$($JL$ds@fpG*Qqfp5&2hC-nGpcIG`JdItfc7BsfCTW3H^xINFDG?M?@=&E(o9cjXIwS0TFxeLxNr!VI}t^`Sn_v_k`r4ucCduLqgDUB!yB0UFUCM>Y_|LeP?U@#Zoumd#KX0)%4vTftS;Ve|4H~+z@$#vDX(=N@3DS)NGZpHh|LstiL1A&949C+1BI>acn!3$E4Mm`i<auJz12bOC2*3N<a}R*9&G?279M_ERb;fR^+~Qa<^W$4;ssfwPp7h_g%1KBpX&IQ;bfumXJx)r|N<*j=KhZ+0}eXUn9fYy+PnkA5)o*u>A}8`HHR$otcf;4%QWQ<?6ox7B$_Pm=d+oS|OI)>ptRC_gPjT70epe=5(Lva=}B}2?vMP&V2;AI5>VtdF_GzEIbCZDz290B?X;S<;J}1dBLzAnhuK1(|`-F+;|;savGZ2&APu^AskI~@Xh>tox;sYHIif|DQJW55(JvDLm{?c6T5rsP#zHmoaAh~%bXHob28Sbqf1|BW}}sUXn0qcfr^N~T2+34S$(70^bUM7V<&0tZa&tRf%A$GvG(t~XFbMen&)l^@NNDmRC}mALGJJcfrfFfj9{+Ee!0Cbd#ok`-pBL?1Ky#`P0jSgt+U22QGNz7MtUGQr=CrNyhMe3Se8zmy1_7Q%TI%oQo0`Ce)M@?1)H)(^eafJYoF#t>J;UA!g(}UnwPA~nt3K=E_MFe!NItiNbTOW8ON5-c{VJ1c=ZoDZplhghjQaWI2$+`=xt4*d3$Oy63?}hTxAG@b{`qcuUR2*Q?(sk!YK^}X<_QyItZ&Y>d1iQA2$_Lvf=L)N?<h#pAsTpObRC4y9Rg{+`mot80TSlWCVCoqGX*53u{zl{vTI#QF&jl3F7&%BwEnUn-vS(uo0z<aux&y7Jdf@CWUI|9TG{J<?FjbwK>>?GymRNaFKi-q18%A3e)FM=(6BFLG<X{oG$&$6Plp@u3#jdJO3<git|?p?pgKBl52KYIwog=zo%}`;8qFB`XDBd!E%z?1%iM-TRF-;O3?vL$fO{R#AUrb0f$)<>Hf~a3nTC0jq`(gZG2sN?{826#=fB~U1CI={XjvSm1yTw*yXggrDL{M>$1n#B<@@3puNcAGNLVTeZQ2?nla7~B~jC4AWE52$q=0m>Qq_J(v-}{a4Fco38w2LXb!~V`ct>&9Pc+bOP4wtFrRSQF%(x3^vReCqt176A#6e~3~GRBy>2n7jUm58(m&bAQO8Qt<;DzDby86Ott(3=7>|;?0dc6`iY`fgyhNO7--mN}el8)Vzl7CxxF6DznbG+H78o^-S*HHa?|wqPrR47NH<WeI89m4uKfMJeaCLS?T2$xN#gN5>;F*bUcK@Ut3C=8S(sm@gUC|^PJ|G+Q<~JlvMX`5jss(y4lYAHLS8wYUSR8Iz=eSkXtc-HmBZ3^=PEdc_kR9$t-!kYqXv2AS+fMFAn)e&bbHwWLZ;|rIdI0%sI_7pi7~$T^6_IDvu9on%OMbjl6Obk--Uiq%?gpB&w)r`?$~_0r%j|q!%6oqXI3cnb4HjH`K!UoYt~`e6?Pj*o0E2eBZNZKzJCS=8U%X0LQw#b'
    key = 'GC5n8T0yCsyYOqKJp0RwUeFXZZD7Amto'
    checksum = '0f773825636746bc'
    
    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError('Data integrity check failed')
        
    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)

exec(decrypt())
