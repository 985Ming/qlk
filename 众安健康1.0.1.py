# 大大鸣版  众安健康小程序 签到满5元提现
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_zajk 抓取 Access-Token
# 多账号 使用#   
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
import sys
import zlib
import base64
import marshal
import hashlib
from itertools import cycle


from itertools import cycle

def custom_decode(data, salt='disM8r2sZrzjRZ19', magic=7644):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='xF6)AZ5sKfs4NvC+f7{b4!z&nciO4)J8+A#eo;18)QOqR3e&KYhhk`tLVsSVh|V#~nW&0vs@{&auID~h50K9{q*^LRn?O89_pvJwT3i<i8&nqGO-aK>QFc9K5yUF|k+tv>KIMR9%!y)j-Iz0CcuSq?tpvTr`89KkW#leVOBlPrX-eQFJf-Xh`z9=el8wryBqDtf>o8%C;)CdBXY7ncnnt3(BoEpJIU?L6_Q*_5|Dz@4t>X(k_Z%S>!<faUV=HksCzVVqnpB=W-Qz4h%{VtF$K%Jd{ntLH7bpvI>LKewA@SUVj{L3#5Uc6_(Ms*T95Y0UKPSDPzbcGH_{&fe>j`|-;<QbOwEd1gkU&F$B-Cu=1Ze*UsY>}OFe3$V=FyA?J;ckdlMG8P(>zozEUNg^V>p%|)BNHNa7B@&1u!i0967#c(+kT;8O}(q9_$kHej#cT9?Af}Eq6$^*>&k(Pc*Egeu_&6;4zZ_c(ecBXY|b?mcDALmA4P2?0t3riXy6?;!W($qupzp<VB+pX{P&*-M)bCw5wGf-$Z^oKQR865;*iE1LcJw1sP1we<DjR1QDIiUQEt89Z764KC(Rs`K%4iA{)&p-F2Ik6)7wXgKUq|EnOuV!}4S4$LzkUQ3|#Fa-j=rg**HL2e$u6wJ0r(&<fR2$m)y$3S^C;8}SP~A?qEyJT#U66%rnYl1TwZH9}K`Cni)h{_jmCm*xFwG=1GgC=m?)PeVdTaD8nKq74riJrI0TsKiLkfz5*C%q`>6RrMFP1~MuU(u?hPtu?VLEV2XxC~>{$9os!UG)!heBj*YCJ~ZaxQjJ|r4=asntng^l)%T8@^GQ^duSh}QEg!lN0f2YN5iJl$vOUx~e6DPGFKnh*5=wcV1f4R~4F>?q1sLK8<U!(01c^fg<g<qlzky-+ZXnGF?3-zE;s!>=ly~bB=6+w;UV6E6=+Ra<+7Cu0t%M@<H(v9kTx2G=^IhcFE^#@cLO-~|T9x+#8n3#fg%&&h(bsI7C9+9y40{R2aCKyPYqZ1l=oIA7H3o>KwK;K3W;jfW#*(pP&fElkg#6K#KOc<~1UwreW20XRUnhnVSke-nXC)$_FZwdTJ))-UPDKcnGQGD&N*KhXr|PAKN5lz&0yrOMQu|n7?ws*dI61sPV$^GF6{gad#@n}l7>UfFy#ze&oHL6pwESaI%om?f?y;_TzJOP7RJZ9~!bRs+YtaSc5$-@5=>)!M<zTq_?FG<Ean$YMY`<~r-k**C4BJGHP*83Sw~-uEWg^z*2=qiS_NOc%&OA55&qJMCkC@Hp5Qgg)EsuzZd6^C}*UNA+d|KD{qnbSB7w&SMh9y{M#iXUHVN0T`<(zli4wg!yVdk;s;e_#&*wnn8E8Bws<vuLif{`8&0z&``N>JykA{3V`Y~2Z(^ns4~mzKT!hbp^5E^OZ-AYz$f_LpDRyx5skoz~=7UJ<*~TJBInO;*az+Bl!5?8S12K)CW(3#mqVusiy<pM^1MqhdJxT;Ib6$AW-%kHLwosN;~3c^H>-;(IUxnyHkObqs&+8edx9Q$4*BiHFp3X#XJ>#uU<d%j>%xBRCJB0xk4{=^Fb{kn2a2uU@gX6kJ5}y7y^Re#C^KyO)XpJn5)|`5|ew?<{&9`V&8hd&t@8wOItfcK?#o(G<7+Qa$PkXsOV@)UqT^yme7GTpIX=j|Q1cb_G@=i|frT7g`-uIWa2^rs)jbC<%M(7t;6=3j4<0Yp2AzoiRG7MVv)q)Vti8R46MZ(Nx`YVSRGkDn2VWAkq<Zdlu;~mI1c#L~!Mmg6cvM5wg6@LHBMo*0Y8hT8q`Lns&Xm;1*$u`RJ&HN4X+J8uDjmV%_u!qVN#coAaugp@RciW8C-uTHI1D$b=K60EcWk{r8)VT#@mYxu2>M)^~EO08hjKYJqA#m&>C64gewUUk>-XVkl#M-vuI=p|xPr>uy6JrUn{`J_C1|1NhVKO5jk>=9^t~&2<z7?~i*6<=sN!Oyl8GJkyce^Hq2+`Jy$6hp8*a=PSGu4#2iBg?=)x+I2{#oaK7rX%U$6TiQo(Lf%JA>O7Z-u3z+@{MI6b!cLVSJi9{J0+^O!;ry~C)1`vVm}q##QT^Bk*QtI&TJ#9>{?hoQw<e7IXKTsZyQYP(H1;#tDD(EsSE5DgVwt!Lh&W5Ojg?`a=Y2)L1=XQ!AaHu7m?IkCI5z5%e${KxAhPQi%-jdAG*R)K{V8ELOK6~o7YZm4$9&;+yY}4~`@Xt%t?<m52E1+BT&QrL^LVru4_t5&IKZ88`4}qiPeWRrW4rCPdR>GswGQ&~q+5_fn0L+E=lGO+Ij-TsdD~obLi&Rx*5;=3-lfxR@+aFe$)pKg(L~T^&mEG9jo8)d&ATWtKY5w(78spjklT8K3{U5BG@Cz>T95+_B>M*Q9)JJIMY~=_T&KcGU}gTIyxLDZ$40Zl&|EGn72oT;vRWsXi-HKUK6fbfLUJzG+68|iy-aXvovC7EZI|dEftB=XDUjXaqjCxQon@8lH?au1&TWRXO{=E*+!CAyk=sJQ2-QGC`S>!l7lcZ=^Nu)PXZWbu81tj@4$6_*`HVFDaSsmpUy=t+9V~+(b>QYE#^YaEPcO_?WIg?Co(tmF_o6k@u8dte0wC*1hlU1=w1P2XRQU(i`sjHXl=B*j+0ClMkr~&xFb5TgM#KiaiANQ@UB)W;Xts>m0@I(o@D^C%4b(?frrjOt5i3`p+{CIYmvXigXnie=8&(#6ZWev>wKiRW=b*ADWL~_MIEZVKWYm(I&txF+2fXH0#R6G+3l%zNkt(R5t|A+GqyxP0-bz)xRIYuy%0a+f;z%Sl_-wS(U6iCXY#DCx)&{#IdJ6~RT=WExxCC6jna;Nhisoa5d~=n#Ip|}cFFCv*X_YpAt3J9sPTx|R5^(<6a=e7gPh!xvQOg9aSxc);6Cm#e9acDD502Pk+sEsgqi%0{(}EMsn=>A7%S<Y~jEBHoS2E=z%zxOAV$QiQZkc^cxNIwubb-yR?2_%@>$!&8RoQ|pkU7@#&25THbM_hMn`?8$h&`){*7|CE%rA-ZPo9Q|-$KFWY^J7R^W4-FX$7Tz3;B1m)M}(1b5_#l<!Zu}1|Zz{LqZUw$*B}~F)m<;U-ozdfYZ(ATWt2L6n=(`P~(5(N82y&S~7E##8dHW9nKTx%q2RKkcCO~X~PZ_DT?;H4sJp}a*kwt3x`oB`xDrjQmAyDf>+uTyw{!Cw8J{Fu3;p%-9?`3%)0qYTmD@BQ<IcTeJ_W2Ng)40sCHkPb$<4z6=6gXhk>f&L%)h1%O4>pg$J=quyPLxA>lA@e<blXl1KIyidh560-zd5qp8!DKo))AOod=|*m~O-*`R<+u@LxWz_hwjQn^jXo<#bpd!}bkZ>wz;oe~OS1HzuQa!nsHgU>Wk;31?gMl59BOH;L7IJ#C?p~wnG$sQEDxmZw-@edkvCjX9;by66B)ZsYg<YXRvZk~n}2+pqa%6fFq7LX%asCT5EHuK=WZfxQ72p^Vwz)0Gmxd%p55S39n(D><m3LvuX22Zl2+gRi+AB>_RqXG;(rN8e@b0q;J?C<z{@Q)Xd7Qy!y-Jy23nVFmA%GqtA<4IS|1R0cob&Ts`yhd(T%XmTgByXvutQnE&caaN@ThSK@lR}}6vG*<4#3J7<T<CF#z6>5fD}4N|z`~hTsLi#sBNY8)P6SplPHT$7PnTkf9w0JOcZq-pHzikxV)9lwF}ET|Uo=<n2QCU}c$s-A<S=7@O#9!Q5*#c!r}QXZPaBq|<A491CScZC4rUDjS}FnXN>A!1Z;J{nTRfB36B0R}tuLP>Mu!8fE?+D)?6I7nht4V74Z5Hm6L2%LfNN%j{&P{d9H_PjSK8Y=xicnHR$sNFoTUG8KX6V@<86oUH2>hK=V|@f-;Ib`u$-1-0=5*}EHMEwSsI=7&8Nw3*%eA5jEH$e5ZJAkv$xyWELLNi@wD7ifZIB9)RNDum?zIdd=aY^X#73;tec*SAfCnAkWiB=U=a@_vmb=t2PgTl?-a8FkcpYbF<TlT3AA~NAY!qtpn>4vu<PK_Foo-AVgy};VZ!<Foum6V3jy>~{yTvYk#V1Xo%8OQhs|l6Y$R0Lnui{_wlXz?D)ca~$Ck<H%-rBrV14oRH-*pu!oiQI^Nf3*;V8mjqO9$QO}GH9q@;*}?C55^LqErdmpz#sJu_Fp+S>Ti==|iF>$6HG%fI*SX%)}yPNREk7F8ddD{dN^<WT#sJKI_euJr6z){6x2lcywPTLh^(v9(3LxqQP+ijo=b{_-NB4;BE-<>07;G9{xEh9a4(okv{ELYF8gQ|g(ILc})thr#H-gy@5XyU6@ga3n419jd9+=?}oT=e7;yQ-&$5#lReEQXMy{x$B$&T_Dp|>)UsAfcbjVPqq1M<trw<?IAHjUOpN8h)yRp`U51)L^86?x@U&u2qzkDdgVJbTm$UbXlQOfe+>lt9kn|hrkY6LZk6UMdSZ#oV3=lxV0<|taOXClfMVSHoTdTe$+i6dmOxoC7w%YELzK}1Hdjd5*kkAgP{vGbrYm1K18|--3d3#N&MG(U$kO|bnR8iS4MQt!x9vAIVKTee`@{oBw^CAw{C7cL`36s8PhI01Z0i&;uuQoTOsi?#Yfl<J6wZ}umq5L};8J<;uapR!2Ws7AS;%0cM|orgMJz{#k%){^fYpTj{bGwOp>nL-uB<kHsFRW$MGj}lQMZcvvNCxA4GhUj(NbAmci4(lpQvL@B&qw?Le<=G-e4Q5c7>o5as#4EaPbt85Wa04jzgeLqF@~jfBKX(>kGrtk^oW+&6+N?aj4&PaEMI3=hN~0$C(?JJve%BC=BW1a=@fn==$8(n_fbhk24_;%LaB+t-PJ4mX=%<^8Nk8GbYd*gno){ZbdJSX(9p}Qb0D<EYa;anW%|=yQ5^F1ZVMuqA@wKt?S3~`?g#D25do(UZg|;4QS~k3h0!eO{|@i_7kK--Sk+p<K5?`bFGku4$nK@u$68vPzZ!hYjsmZi~1SS%_;)@!PPc?Vg_=<UvC|te#`9n2JW6--iXg|rweMmZXr5W{Wv2uzuqQYww{9)k-1Bw4`Ei)y=ggc>J8eau7#Q+R+?L6#b{(&^NaCZlwF3&8qn^2%9CY=Kw>eP&uG;io$obn$XUA}!kNOIsA^1S!w$JwctxMUnar1x$SBzx5tI|Kdjg%})W*~hG8lfp`JE(FbRyvV$V~?nWTkPsg6nz!n5QYk1rpl)8sgdDBE5i;VAFD~xao<T*imX;P2jIx$$i!79-*eqin_@N(nr_NDM^cGPF+F<z9_&~p{$5<JyyuSYieo>j`=^Ly}PX+v{^DcExU}_8?M#c&_=!^nKq*DrOrfCzU!Vlp0zVm(bHl#=YR)z=O>XV3KX07UX+G{bM|M*yT9ss4#(v10$HTXbe%JVHpcwGUTw<@mfS43(}?rhZ_|cTU<oWQzR&q~9ghz>D4F8+DZDx&O5{Bdl-s!pO(||xd&RR6Za3AwLEgC8>J>R3Lb^%=l-N;5DD&{IeU$c68q#r^!;b&Q3art({xU`;C>GexbsnH~4u~cg_fu@^>e-9o6i@50#o~(+NR(5<nSwm8sYcp>Mf`4IBxjg>O7;l5)If0bx8IFJ?G#tQhtO`VVH6FS7uga<9lKNAznf+WaJ^O~Cm$leWOmLknwTg6p}a41eD0(6k*qu(-_MPvQs1xm(38C4(B$lFKsASE``92j4IpJTOR#LUOZ-4KgmIvHVBn~mUL`ETXTd^;r~YU=z&MD6o*}k_3lqMpY*2e+$-ju_7L~#YpJh9s4$d_wG1hM#3jw!!v5vNR0e?81`-%$n3Appc=>kILlu>GV9TgE+sn=n(6FBzN&0s7fov{U19gB0SX>pPKp!l@;N)US+@s_-T0&u)%1Vq)seRnPnM$$L52-REy`h^un8s7+^%OjJ<1X7k^>_^+<)|f}>v1R&$HvRDWT!UaPvYjkOnuh%2AuqNZ9+yE&?VvzfM%eBkkNNpc6}=BDnluVc!=j|}8oa!G6mM$*kK4++W`E^=#UGR@FTk?`O8^{?cEs7iZPQ+ou3AJ!Y$w}99Sc12i2%cFU2{7zusk-FzW%8^k@a)ESBX)(`y<2ackrU!_7K#8-RL59>Tu0$t;rVN{<Vd6#K`6nnSEQSI8mdqQ}<UCCxToD+p~S^%^-r!q8n%@2vix~WRU8lGxTUSUtq%2ACtqQWwGhwm`6b^rMj!42<s9|@#m(rcY0g1#ju>L2ahJ2#?_&>AW&)@2hPt_^|t;;X9;~@&J#iP=+@+wfUu)z0vE4;<~~l7=|jY;_LEU-+GZ9P640hRhsP=p*LOPf&a+&}8y?oT#-z}i4AHU8METw`HzUPeJ@J@3W7fl0E1(AbKmgZw(3}9%S%SMGE7{j959o6+*Pn=gZC7VK<R9XjeS_Jx5TPxNmVG*X%-w7q?EW|M$IrF5#)&_y4#u?ucOXNk(pqI1?`o_ok4$CQDrQT=_9uo|*n>Oy8dIF0PO&^gv@&L1IFUKF!gEnzF8lHCq3Mefbhx>0tjhabZ}`<JK|aRTRMB&^l3Qa)Fu|IF+{3})Ne}S>7>6_aO6gxO#NY2aMe{c0_N&Lv==yv=@QDB_tL$ZnI*GbKI@*4gg}1+CG4g%lwQ>B$#8lt|V(CZEf`n0jWT2w}jkbuat(N4>lX&RPy+`o*EYBc8nkOVbu{kyl&I4eSy!TNJiesOCo<EUtD_0j-GmM`qT<8Sf_mh+;?8{+vw{v}WBBA36j#MnYJ_wpV)!=uifbafz!JNMd7j$kMB~6wMWG0jsh2)1anLIzTP^I%UU4fr{f;$NXAwH{{`qWI!t~4U+ra;0p#bYhRzsXZ3iWSqo?PVsj3LQlQlEy^jQe&fp>TO!QR62lw1Vn{S`C(O;@iCmtj1Z+p`!C0M52f1-@riIkX;ViPuTszw!3Abw{j%9b{E}(W-Vq57NXrsLi5ECmCmyB(r8xwo<S$S4AVThdDGIX3^%Z47AT({gWmP*6_w+Z&(M^%2`|Z<8>fj0Fr+j{A4mtpm8$mneTs6@V(LPC{1RDV_waHX3jdTnNHMleOhcdM;G&fDfC?iDVlf*y<)5=`TFX~V~<@5;pFXjH|nF|MHEHhy;*ckAXI4d+zb4mm{%`c60@#VKvKRrgLKuqUMA>GwB6d5eh>OxBl14{Nr^+q%Gxm5|6e-lk1i>-}cvO$+N`CZP;sZl>>56PV!H7t2Q632-Q(Sc3xlLm#WF}rmHBOUIZ`kXW<gh6CG;|&$UZ_aqya~bP4(HqFDQ%tR$Ai)Um8z4@n2TMIpwcNFW=kaoczwJ#6`rnOUF4$F{7GVpF5L^zPkNXPgvOPRJ7vVI-#GDaGp6!>;E+4&R>#)ew#Xt@!wkUce', c1='170d3f2fb62df580', c2='e1bb81993dd6b101'):
    try:
        # 完整性校验
        if hashlib.sha256(data.encode()).hexdigest()[:16] != c1:
            raise ValueError('Primary integrity check failed')
            
        # 解密过程
        stage1 = base64.b85decode(data)
        if hashlib.blake2b(stage1).hexdigest()[:16] != c2:
            raise ValueError('Secondary integrity check failed')
            
        stage2 = custom_decode(stage1)
        stage3 = zlib.decompress(stage2)
        return marshal.loads(stage3)
    except Exception as e:
        raise RuntimeError(f'Decryption failed: {str(e)}')

# 执行解密后的代码
exec(decrypt())
