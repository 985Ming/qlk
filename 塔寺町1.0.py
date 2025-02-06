# 大大鸣版 塔寺町
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 yymtsc 抓取 token&phone
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
# -*- coding: utf-8 -*-
import zlib, base64, marshal, hashlib


def xor_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(data))


def decrypt():
    data = "L6oQ(AwhqGcBHUA!NE?1LEXLN!N=;!$V%geEg<gD;Y||?2>{&UeIwq*@w}&@gid5dlm|v82{&>PC}Buv1zaXdLmUZ&Bl<Tgln1CMNcEmqnTIak1_4N}Mxp7^g8T`K`!)=}Z^1INx@ncu{ojs2q->FfW(<SD63F>g{eKBWDFI?30tbvvi<ie0m><Jg@!0kT0L#hs`<f?xS}JX!AXI#PSmxByRS*<#ZR6_Ckz7<@!f>8gze@+eTdE}&=EG*L6LYGd+0av~cN)jEFv%J#KOf}Y#WQ%!%;$VaA}_~O$s3kUkwuFl5|dgmexhRpCYA#bZYe+H6i+ho5Tm780YOy)AA6)CqZ7c#XFI1Sp>2!~r=<t^mag(g0us4QrTx@Jh9wSH2?Q<8aYc%KY!lkvPrSHdhmG1(Qoyr$AtTwUJ}8hIyxfKNfTZu$nkqn$mfN_Q`!#Z)+2)vI2(g&8Slmo;wS%<&B*j6)y$h%bHV`nr;p!9}uso8w`)Mxg%YIX4sK7`SvwXYHp$Vq$%dPZLM!|W3o&`7w{o|XasDLf$f)r^+*{LUcQ80WOGgSWNMM>)99Sj)3j_;$6t3ThmiHOTsqY%;;E~&PurSQX`Sh?Cva(ttiEM2P#E$CVCKGglo+OC3$cDIzzgPWnO4rto#!)NN_YE~v&c=7e{1mYMB2|CpDRg3iBy0$XCwxL3dv=o|`2WeP<P_`GAQVrckg;6aJnyWOlWt`IS;63*dFl|69|EWe4CuIV>HelX#lN1>zl(A5ZI*wI(s}36Y-Es^LXGI%N^d(Meol^P2-T19tD@low9+h>H+MJkI2p`{iXpe7a%(L)rnrm_Iz-CnH8L(MhK-<6`2?XOH9=-mb08S}t$1!NBME+Qn!+w0J;I?cA2K>w1zS+Lv_+SPCoy?0?yz3?__L;nd{Il8c)n*gw*h3^@04OGGKmvckk)qTgQDR#dEAJ)OWn?`boRUGC`LF8%_0NI`cxp1_oj^a2il!!J=8CF#6++f$QAq%1XITM}tl5iu!qlw6%t7nku`lWL{SM-VP(-pvBgDL~jLO=0>Fu$2Q_lKliA{0l^*YZhGQ}p$Ejv#gS9cqJA%KA)AAmX6Fsm3~t(?PAi$%1Y3Lp2>K$Z=@I_|;;PhCM$1Q2RzJ2Mg0;hKies51Ph!~49m8t0ep>Y-i8H?ktQgM(Aunf+f&eaZeIYvlf$FpPGCDoUU1gIu1T##GTfu|xF~8LZ6=r_pAsj-q7KV6UBTST8WOlAvX}EBvT7z2IZQk#cAC4UKy)z&h2@AkL|8KX_f7*#~8_5Qz(!1N4`Jgm&IZ$=EoWM|hu4B?q$RfcoX|u9?rzAqZ9pyPM|p2?wgrGLsXIT{~5Ty_A<S4S?k&^pOEMl`<P9Am`5Y5}OkZIF1opPiPREiJ~irY3(MfnkdbeZ~{P-1Pz1E-Fgvu@2W%0AMbskhFx*61suhxCkOr;=GFU(WfM4=8Z1oWqB{8^|Fo7hg1;%8bQgZ0|I|;I$jhbDJ7ur06u)yHwU>6<Vk*>AN3KgjiH--Q!9do9+qj&y<h!#0f9H-2$QKeB$Bnord&4|Eg)eT<92wT;k#}xAJ<{7~&`@jdL*X%nX9yxxRt)CF2U1|0MJ>vqp2}%o+|xT8TI9(HqdQ)vDFAFv5}H;9QC5p{V6ayXby_FeFTl-4eQ~lwGlgem|4DMA&OW3zJ5RTO@ZK}u*OyOD)DN>Prcq(7!;3}OORw9Mh1_g};<w|Tp15@KDcc4P<IdEdDaKY-w6W>a2ukHp$bpD6I0&Mc{ruzQogoOWQCUXlnOfFS1v;r8(@T8I>y^j4nHI3Bx$F^LDRC+%pH~yJc~u~n(#E=R?5z}6%<Hqnsjhg_;up0=AX_k(|9?2#3Gd^|gIbKICWew!{ZE^^^m(D9x0O3xx07SdYQJ{vw!-J%=Jh)o+ACXvx>Iz%WJaBc%&gK^G#20nXYzMVbk?)<1%Re0nThAPkWlh=k(ynQV$|vsuQ)WJz>4g3T$Vc?uf}w%3{qSf^Lq3Pr5;%zVAzu5s6_!pb830+iV&~#$p>MXa}YD&T=68+8%X?T=%gk}<Yp%^5Zqx2_WqBzIxF60WvP7d6>J!=wi5b@Xaab{H0%U5bGn4JaSZqq;Z7~d+mpwe=Yhuum*aaaTk(}r&;Xq|{CM(({H37aHoj9kFP+leP(l3XM~pIlQe%;>rSH?AwIdsT9AJ0-Q{7Kq5x#awYLFaWlpU>$68hrfxjE)b-1!h^na1HFko1l@1ql%gnIwe<EcuPp+`rw7aKZe68B0o*CaJhB0hP&i_5*W*<uD0cwz@10Qvn9ZCWUPPg|?wSujKL`ItS7Cny1im`SPZ3jHtiuF^#JXlbj}iF3Ub7ewI<??El>y#dSC*wnKrnfbEv5<frHKT1)K3FB_;`vIgZrI_S+e&Lgxr<XY+x_LGzuCjaD^s1o<2T3vM(H2g?o=_hpAU;Y!weI5Q9SwK<fV|u$8KaCT8i|tGJ=|6l1LExkO!e#zuk^G|t_h<T8)x?f4G&&tt15RNG&f_D09s<awX$VVAdYHEOa&IZyr-$>UwA3|d=>brvd>WO%#h6n^mHq3>IQD6M%8s`fnV+)U=8SNoZYiR&8x7$3`fD<=RMI+zm|No9{?Y*jXjaTYV|^Q_Jz-7pgsapgsi$NV8{+r$fWV3BE3$cNSZm(jCVi`@OXJG)Ov+knW55QCpx73L8_j%?y*QUKYx=D(IAWsu$cp;h4dG=@k(gGU(~I=Mqx09mm$I>r3a6ZNl<k>w+Tp5u;!YHGeTG&BUn5+0S&9n3=D~ugs?=u_<h}kp+V{}|?H-z#l7iN!?>s|e?5pmrL0(?c@^D&xWA9#_USh9DZE-`N*jfTtRE|RA_kDGlf-yWon^i;;I2d9edC}QELngMyLk+%EYoa5(PSWfXKJo?l6X>iGGy_Z=t4nuFsDP&QdY=rjNF^wI<DqQ>4o5<}86E!FC){5Lg9^>GV&r=8xfM21H?Ve8?{f2JI?qh`U2k?U9rmn6Y7^3Hhqay>zK+|3l7u1)>9@MaLY;QWbv2)4q-IG|Zc3D5)ElfWr_(@ih`S|Brq^F<hM=2_QlonC&*_0q+@ZNn>-pI#QA?0!=BihZ5@(naqeBBSC%_br2^-5Kt4{N`MhIQ`<T*sMjzshC(@5bhy6Z&gHO@PL@MY8yMsec2HqfXRy}rQ(Eyd$3!Q-3D4!c;wIu7-8S6LR%F;bd9VJY*td)$A+iufdv_Dq+9uO^Rb@xeakmL_HcRRaWOv;tW0O>_&(%*fDzgx-Xb)xYq@@s3R~QKcO$OPd`z5^R5rV$GN+fxq{^-WEYh4g)xQ@18;qhtR6=v9g=$w$Ie6o$kj(OVT#qZ-ZP5Gq+TQx&dvVB>O51S4#_H?Ij#>{pj>CLrTGUN)4BWK#j&)Ke1A+>Qw~Ve&?5RA1}vZB7+o>;C4!qk^F*dSj|5;D_%Zdbj(0a91K`e?=NimHb~`<?e`?ns=Ks0>{39N*23TNXpYrwi;F2f_;|lGLqt^ck}G0ulbQG"
    key = "9NeBJ1dVczeTdTbON8P3SWflyTUdJbFO"
    checksum = "4f396188cbec277d"

    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError("Data integrity check failed")

    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)


exec(decrypt())
