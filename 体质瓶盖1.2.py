# 大大鸣版 体制能量 一天5次 两次算到账
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_tznlmz  抓取 ck WXlogin=oK6LwjplxxxxxxxxxxxxxxxACljzGM  只要=号右边的值就行
# dadaming_tznlmz  自行获取 瓶盖码  有便宜的可以联系大大鸣
##坐标dadaming_zb  维度#经度
# 多账号 使用#   例如：账号1#账号2
#多瓶盖换行即可
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
import sys
import zlib
import base64
import marshal
import hashlib
from itertools import cycle


from itertools import cycle

def custom_decode(data, salt='DFaNisGjqR2OqP8I', magic=3991):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='Q@4#@U-pT4e#p38_k@U(7I?%lH(PNvQg5LwXsMa_wmtddi<b|#IUkQ4a+rYOUh2@Re>&Wlah@K5GJFLwg}T3z)KG`>x@HuM{-j<TtR;n$v|NL~ELij_oskQ*(o1ezHdpx;%i_cFq}t4U%GBs0=TgOhL}spD2Ue+{jr-i7PtbAl^e1v9afYPFQpy9`#l_U70=q#+#u+Vo%J!$RSK!&lgUCmV##W2p$OP@$i!srJ&)&mzCRxqICeC-+{PG(Byx_%l+GbHd+QQQ_=hq2D=hQevwzIdb)?TqB1PI#3=WD;%HJiF)*JuyKeZ(Aq2hzA8hGmyu&_DOrXW8856V#$!2Hn=%(pzrS`oTW3SLpb*7pMLj&cvs2_XJPkcWRRL`c`daVmk*_PYJ@f2HMQz_29+A)xU2<Ua8e!>Efn+M;61}E6Y!$e1zP`+kCs)<<7Q;x@Zwp2ZqeS*H|Z@uJ(>v&c9QRH`%P5Z|0W0CK?2JAXsahd;h-s{Ja<?1Jd5exEpBUMeB{gP8b!%L{w3t)D%Y0U~G2uD8sd-O`^J)$;$%7`ux}2k;a<!`lijo#0-`rdj!A8>deJ;0|q<a@72Z(-y>ac1K7INPv(Wt%IBBlCIF)_uPDe01$ri)Rol%#;QFaJ_k_n{b$>p-R^;Te*H+!(p=yU6>3)#AQ03Mq4am=T(15rmpJ^^wk4!e<3edismn1mF<IJvt)yd(sKM2Hl$LG*R2jo87yc9ObfBwJ7X9mHgOy<OQ*|6u~=jm7d1?4Q)lkUtg*S|Z~hq<ERtMI_$vwgtIf&<K7esR0dzYwge^}t72R?f}3SxDW@Jg3OW_a1<MI;iKQ`~?>u=eTrb2FW%HSz4)I#~)g?2g8_Nl-^A~%^Y*Xe**KB_vond0Np{~tTe>nVTE1w*vlBC+{?vE+NMv*d_%zY-N;+n=H+Ie&AX3CU+LLEMsmO*LWM_K?V|R2kOf+kq6Pmp#6tSf)*2#tRCq$@tKDz?9BW!yFesQT^-v`3rr(2R3D3*~6!Pgkq~7WJx=%2^nOtcBG3ruM%QZxkyVhO8I12ajVY6vW^txx#TEDRls<#v@JgGV+I)8B;MWG-RW0)f(w>_^)<W0b(RKD+7#aL$ZaX9<Hw0o_{pJRqT)z@;HYqONSnldW^GbA%SsDO<a4B;$si{8?6_InEOLmi3JCn^``mq1H`QX9`;si(rL9x5ca_kOd7-plg^bFATgOjLIiqQg28wOGmNJRRf;nwt4=ZWQQo3lgw!p}8<zKQbB|>c52}#{;bubdw<*>9u4%6u4_M*?0bzTYEaylvw8zFYXt2DllytmBM2_<Em>g=96#O8&z;_)(*&yjw1O<)<1$|+6oWBl{}wAb9PHWb4srAO_>D%bT=6NM!6(#Pu<(ny49Mvc_pjpJSzGZN2ud6+u&g7U8r-rL`0Z;avJdC!98)5C|smEEyn6kTr$NE3;p$ci6n@PV#p<f?Q&X1Yc_fb@8OFFML<7`;iIM>Pe&_xrTpO`1S}4WsfdOL;hpsBDP&iV?jK)dK_7fdHxP`E<eMfzlRMUI{@2hf@k@{DTM9~WD8p-8FGW5ZkE2U#R8e2K9xnfol#?(}T1swZy5717g2CQMNMms}5k-z!O=(o~B%(peI_tiHoppgYWZ72jle_OeFvx{M1QS>ck7bMRX&Ak+#Z`qUi$c#MRky&U5Ftpw>i-ZYpWE{<8k9Ub|A-4s+}EsI)x;_$E!HbrPo7&()5FB3LkHXrL^V^Q4+2aR%&L;D6OzVmQ<9?`7KyJ(i6*Bf>?);NkPap~=xn`@c&kf%d*P*`849F2GVl2sO6mU{@`T0|ou$S*Mqw|}iZf0D(#>D^5;J@hY$L;9|Ju84B1Jf3*lk^k8#Grj#o5Jv60Q?BYrmy$E(EvMb496TqxXadx+#>;bG5L)JZI*oA=@ky)@@jB>-xw@jYQ1D*3V69TO07_-j5O#YFiP7dR~En@yDVfePM;OEBY=?a1nk%A?}b40h)L{fkeII)E?H4zvyL^MVDZiFMw=@;>-KHVw}9wB*BT-d=2Q?B-2~GZ4h$YOUS6VfSaa65t09mBhz0yp7L<eRiD~k`q8bo48c}bhi5Ht@jS*?u7<Zi$Z@zyPU_<yP}aRy%PU?^bg7{7I6J%NQb<DgUR<vld$RTUjtl{daXamp;ca9-QIreHC}y(9`ja<_iMO>_7rKwU<-i?_LR*DKgLdG@V88t5aA=H6cYp|1ayD@}Tgy4<6S`%XvzIA*Zqm~x!Z;m?5HU5E<cJl@xqz)Gd%i<Tb1*VSk(2>QQ#OjL)89>Z1*Aa<=Y9o4Yu+xj(;e11-9R6@(L3>(Q>0Z|0Xq19Bc(j>*k-JVLAmEHxJ;#~bg@)Jw~x}3Ccfg4Y|j!9tjG#GSv3vQNc9PsSy7_l>QQc-TQbk{O{5i+(ZS0ob}d_dZxwg?Z3U>8iKZdl&}PLfGxx@4ayvl}iS#r+6f`;>9)oU*bs$4kSn8A9Tv85G4ILw}BZk{FKF^qraFAn~@`w-Ed4{n=4omVWAvvM251y{Pw|9fZKp-~Lhf-+}hbB$h=2=>~i721uPzRGXxrfA^BaU8)_pji%$Oe&68-Qa1<Tpuu-h{L+V1B3PizHhGk*ZRX%WN#qk!Y0+g>^JoRb>Y5BhvTgfKt8@dCvyWH7q}Q6C3~gcxkptHoNquYBk5gqck{HNBH3}B7G3<R-g~hW>eP(Ng;O-kKwq<;kRuM+fOHIvvcAHD~xNab$L=}WK_fUp>`0nv~*vF^B(k4a84!vpfO7xMbRhc?5ndpuG%~ap1X7VAurfvg_S_?AcrLj)}~(a0tgxsbCJG2obf0A=)>#*Azn?@7C+LRmoVx|Sp@|d8C$3C*hb#CO9Yo!3DD809eF=$zI}T!xe1w4-Jw&g#l|qrZvh`L^V~DCrsQTDUM2MM`0tBazL;4RLUgD^8##-w<P23_@E;(TzAWn*axx0zlU8~K8YCp?frQcJjQE)no0F#T3v^{hrOo69)xLH>`*{IV&UTOOBr*YwNjKuM?w*D-KMqOUg#uh3fg%FKx}J}cUH7Vgg0vApoyu&Wc=*LPz6pq^IuDPrOm$0(pT|3EsHICLj+nG7qz-<GZP152ugSaxatvifs^<sA{+_K$o0sV_<pUnv9u=Z5Tklv;HfK1;m!Kiwlno1^iANk1y#5CL{Rxbw)#Mh6qQ*FaRlwcMfo(Ap^iI{+^nV}&eJ!?G4E2nlvt*o>*+BXkvermpUET>Q7ZFT&^kGauM*rc=4H!CK)y)EH*J(BrF|W&J8i*sZ7J`Lw^_Nh<&@NQ0G)HlA)T(_|Z`(f}rNoAfSHCU|TIPO6yd7CQ9t%{Ei89>Ee1?|OKt8#YfIG2Szx(WfXO%40TUuxA7obvkEm#WX-Lx~07K8I+DSR;Qs!R?=7W!)W)*^F)ibe7pViOxRE?xvlQC4auThy4vNi#uR`E&_^FGqX!=QN67U~l{{R+u5y)h(1GJEgrQ0Sp4537)l*VOL2+PeFWhX4O;wl8`&^xf&W9+rHO;l8%$grGo5Y7$<K*FWIYoI(Np4mZQZn!|u8rX~ygUVG^L_#jtOzPw*R-Kmw#;?z8KjgFQ!d+ZKdf;!-$rC~Mpoa_K{vgNy;PFtr$<7C)*~ZqLIbMhAIgj=Av*j?vO+7U1cINiZ!6IrvUo`{h^-AWlTbj=F!++mlj1UP!pfXe}#3+sbzibNEbdz|<=<oif+!Dj)a<>&gA`U1+SzxO)5rGc-;v<;p>RbFw;u5+>iiRg3b3KLPv?gHbM=b49}K<9YFNMZn^sEjci9riwdkC4{RM>X}OYM1)C!KIm(O(JRrnVT>x2uAG&eX+FI>vJled)fkBX3BzqWnn8ssa9SdL0#PWxM_S$)R7EKf%CeB4MI|NBP4l5PbY>3NHf~(}kCZmkw`=3)Rgr?{<6rs~Zbd#g7O$N!Pw^;@V+>ARjm1E}nb4EaK@~Uyn<9Yg>k%k}w00Ly&A7U+Z`&{M*!(u8_WEsA5Rc!!B1cj?*V;2oUnjVty$z8+eg+l;2$Vz0w5c%ui|^RR){aFM;IS;HK6p)*rz2yo3WFMU)AF_il;Hgi7_eGW@q$wE4M7x_IM7mK8?dt_!dav5wsK!a2AY?6hMszm9AVDFdeK9FhN~{UMq+gCOAe&mE=-0MN_Ww!a*1qCGNb$&HCjIaiN@CIE0+Rzo3|S`ILS1H6Lv1w%PM$Ey}G8aI^~J*I;PL3O!N8PbHu>S>M)j@L}%B1VU*;3bqGjOlp?RRb+Fwlt)Tcy6A!8q3Rheg_rlp7Ht*2l9Gw&SaKT&bTL({&tA>Y1>!l9LBKJE4GfJ|<UmcO^#`5D=N_(b_<7IB~8E;XnDsWp**~M(@N1Z8ZB*%*|z~>p7Qkz50+tOLU%J@X8aY;5*tT%A7A(_gQmjkJSrx6sP6J9-GWDNxSTSTxia`Y>dUgshSfSRhId&?9!J@=>@@danMvy<O5OF_u9JIw5`))HJakv%iuq{e~yI#F_KN<8~co4QOxuWvqj+jzq2lLWza8@WV&IxqWI8|vzwq5Bjld%#Kv9R7EF;7;X3O88j1Wu?JD(^w#wnOUGMu{nx+^f@4mR+GT;0wUBeqZrfw`=MBMzDci9v3-)wLX;<if<O?YWKi5c)-dMcJeEZGnwYvEmdgM8d`>!&6>32RJYI|5w9NWKfJl-A-%cKa%*!B_+Lg||rv@%t(hdd;>SWcQCYFv|bilM&@4ui!j<krVmA{R}2-(r_m6CsnV@UQfb3X+GUOtV?#atWErOvA#9Dfbc`G<*9bm6D3TdJJ@=j^c;6n`sC@cs9<&5lq_47uqK>SKUXj8;=M_lwps^@bP@(9QpqkU@>ZVcBgZ<2K*s8+^V;xgi^?ubE9f)!W+sT&jTAwynL$sedZcLifs#c5f1bbJY}vI;JR(0cH&*HcoQMer0NfPOqkj@XreD<>UPDdC~f|D~|D59OT<!C`B%%nJMPEGlQ+inV7MUe?}PgtLvDxljXMwVL244UlK09P%4O~4EyH4^~A?(U`k#Rq`tbCQl~PhjSZV7S_t=G%I|IU?y_hj9~*65sv6RrB~$wZLj9ksN*wJJ!8@A;8^H2b=MwkL2i@!|ucgAsfK2-s>K<XNQoSX`r>g;e!X9FKJ>N0vgP&EKq|)V+RmkZZ6{!niPeI9=ieYBD`_f0{A><}ia(P#y-j@JuQ5k|xc<CY@HY;##ADpD4-U{7mF<U7TkHUDD_xuU3B#2~{wEJ&=Wj}%W4IzgRWR<BlJAy?{H4e{YL(h+zAcTe!h$dm8Kc&uZoy1%Dlr!b1K~1rf3*AyfLK(wQp}T^+uYXI;7unNAU*3E9ItT|AKV#mBg7BKfE5cMEgB&24viPFL0!1vl-%G8mqT8nD(vQ>2mR=i2@8xy7;GC(^_BJF_n*C0;q)p&}+4rxmAZ*7oGu2flx5UlPedL9&i_k6v*=kJGa-nhH_zg9NeCy+vi$tb(cewstyAM3~Zg$}a6K`cGqxnam4K=MV|8R9KE4P|`CdRdl6)VMXXNNDT<|4R5MV(K4Bc3AVJ@llBk=x*^8)b-wmnf<A#9qsCciYTa<l%pavU%csM*CxW+@gN?=_@xB=2XRKtVMFQuVT|lcb=O(Wv^~1ko1<y(ih$+t4q(*30O2V$4pC3p{}#&|6T+qs`@=<I&<$>VE@g*0HZ%Gp}#R4iBLcN!`3;l$=au$n}GA14vs8#4Yuz<3#<+1t#?1&<B>a&DbCqQX$~O0Z7Ls;IFG{FqD>A7ufW`Mj6W6ZACn7NS3TOHwgtvWgDov*ioS#qwf*y<WU4>75)XAWNSE6NKPez9rc?Ml+ItUrJpUh;d`Mq#3!%%Z8rry?hKUNn_4H`lxIAFnxLJT3Yc3JGddmZkOO9lV=6VK0KWlEx;fHJ?1wS4qSeq1sq{jTd2WDdtmakiApW0IIZH@&})WxA}3q(PyhSuN!zZOCLj&z{r7BHc1xfvq2a&3N<!`Nl*c*k`J-Atek>5g*LOdUfQ#hJ|n_@@sYp|sYyyWy!?#kYY&L0J8kJZzMf_OH$Fd(bB@nSLk$^V1#L969T$DKkkucFKX$fiqZjEqN#Wtv}R*&9|z~)x8OL=KT=G<L?Px6JcZ;Ld7A7gVht(Jkqx6FRVZcxW~URMNS%u5e}hx`tgbo0Rd2&$304@{^dNm)pgZP55^X<dr)W_(0g}aGoLS(330h9n|2MnjNs|j|JwK@o=6*KA3inQDJlMk`j6$2@QSPQPpdS>QzazJJz$C%`nM|@V558vv{=ffFP6J#WnQ}u(Kbt1{>z_9-1Pps%)kt~(9jA7uN<J;%UhpeM-uAsFn0`3K_o^siO>B-7AX#lTM7U)Tbl-Q`~ewP7vQZh+Q@e}F@6t$%hd98BM7b|k{m*-Inz2%)F+!Y7tE`!T;O9_RJ((ZcJL2twn!hlIUr_8l%^ait{P7V*6P)TY;y%zBx06RZrXYeQAf2&Q714F+Bu!E!Nlm-cL~e@QxTmYd>E#<#uAn`LBO`dLV{U1Ym<Dx2~P4xg`aIrQ<>ztIHpvoR#JrHB^P_r74VwnthKt@fJB{Ws0C|;%2$=;dWIFF#Ij|s_`J3g;y{ENv*Y5AtZYe1WD--7{(!!&uyuTz(x-`mLh7zk^w#{j{bSVdQ|o)5P&E#ulg^Sve(~#Rsg73v<-=Kf!mX?cc5@l(uY*I1lz-#ULi=JP<%*#Z^T~%sx`#lXxV+e>E_S3K<)bBX(Ne1dOqFBZ9PN)tMa+_(YI{;EsX!&xL!WDWFJeOBT*3hxOKf{A*ztvW10FNG7ahAunJ4M!+gfY7-i6(z{7LA2v6g)vIu>|N{M|PkF|??@u0Sn;`h9DulOCNUq&X^+A5O)GFmMW5Jg%Vr3oAY!za@433pA@+zom^gA|W#VwC70pqEf**tf1M!%ti(or=D^>CvBk*6g8n)f-<s$D`=4}#qasMwVt;Y$U{LNm67V{%-N=hHWG5Y)$3z)(ecAMyKlzI8db)Nav83Twmp*0*i?#Zs{)B53r$)!N%p+CmueTxOdU}QXOJuGt)_OykRJmG#>3Lu?5S(Pm3UGi#X)Jyz7~XJ#DAwW>a<UCz+OJ)TyeCx{!K&n<~F?qQE;-t(oA<a6kt28@2PoldB-QqdJ?#hG<m%`#rF*qB)MwQ+f_Rle~`IN$t_A5rv2hcjWRSFmMUVl#naHVy3vUV95vq{Y>AArYP%LiS`6(>4E(&{g>8!MFXo?yd&DM|q#)T032^PPwC*h2t{QWMn30dZ=vdnANU>lbjB%>fMdaJZVS1w}mRPk7`7!);c4gb_n<K=}w!f!o#og%=lXj`;HFd7Ycf^US=vJv7dQ2+<Vwb9qTTdbH_>*%~@mXU0e!%g|v^T0%i>H?I;_~MF#!fKor^C;+=5<&8K%E&$&+&W347Mm;$+oua81V1i1q^^skXJxY<EHxw2z^<K^7ch5*WHWDnX%K4l{mX3%kGjFhzlT<cfMwh+|NZeUcl&mrY?dZ_V0~k2CsptV7g>ClFWPC<)NjNBYmh;Us7nokMH;_#XQx5fbDwN1T>EQNpA=ju-9G~LeNn>OUE6dWLYU;kBa^Q&R>9)kJOF(VY%vnQ7oSD@8|XN_y%PH=tr9wWrJAeCdqqydKOPuB|`W3zmgjs#BBjT5j_;u_KquG?pFssTdrXM3ha+dIq?k}c-$lD?=;7>W4~n!;tp9r?kr1^6{?4?(xh)=knyqD1moR1!+fy)Jdqr+@!Mm|84ZsAZcg@x0?Ww~4zq+%X5_7WN9vtIYr)J|o$QjGp+oOq&>D4vnReO@(Wggtstfo8gA4|AuV77**p)F%mTKngx_oN{@#D+oz2Mdp>`t_e4j(E$oLMrIN?tj^Om)w0vg`btQ#~(r+@mH>I~61v>XSqazmq>*c-I)H_G_%(h>ZnHx09Iqw>w2#%p%`7Z8En5YH6e`p(4TPouwze%muo5hjht${i;2#0^{#p?O!!gy8rpRtnZSAYBtROp_rAL;gxy3C>Fq^oVIAJrll|>g!U}_coQPjJzlS7UXe-~N2EGJu~Y|qYu=F<65$#~0oLyuME?-PS|kgDTVK2vI5r_TR@Q^VLTSA)s}$M?(OFyr^6kTE+g8>E7G^=9>rD$9IKj6h3nN4|Viz%aT#&)eOnp<M+rRANJY-;3Ze-octOOAr&{>OTDZ*&Mu(KM0=}ea#KZk-uXPW{}cSZkVk15C3LP{W3j%nig1sqj2y}G?zFnFO<gKmS+wHZ{~`DXLnZc+caGJr~Ub`u9<fayUOoo|=QZ8xINC67CauCAhBYR&8FetU;c`1TZ0S#@qeKmedmm4g(Cb4&l~Yhg(FPaSX7GaGOYw~GDw%a2Mi{Tzv0OlKSV_w3cLsq?G6LcRUh{Gn$4BdJ!617m|T)&(mO#$1?0oRhF8p#J+oMNcV90#A5lH{(L`+JQmpJ{r%>%}qAD;)%34&kn)kIV)o$QL`A8aEgSFYXx$Sw%Q#h#D4zti@gTA^`j~bosXvGlQ44?2qYO0c&CnENfjkZnqWlEifi9re9F1L<WnK{Hd?bF--T;5hV*}b+Q2Of#-S!Apw)o#oj8t-HQg=rYrq7qEY@@z>zRL@dYk>w90oJmD*&%$pyPkjF4$y#*V_d5b?0$OL&6G~CKnK6cp)uj3$jT!*B*PGAG-1rU72OAFi3r^EusN#?x{dzIwtu|_qbL(+s>FE3vX_8W4E?<Us<8E677}>W-on#WpoiPy2$TN7o*I&Gesvf^ji>|9L56s@as(Hza)YZX8KFylP45ns_xYR=%2b5zqCb}C{xHC$~{mQd~)Sr#I?c|`&wZXmK}^VAC1(lCptpQ<qM&*Qa%1xX>Q)hKN6_QiK#9}xnlZHDip$&_V(O{4@H@ijSrJoy?`L=%Cf|%0nGTqm^HPQW$%alIj=$)_>?2g<5)>-%VCC-qprjQSQ;AEvdx9IKzegAU}kb35gE{(4N@DfWK<w(w;T0B>aCo}ZB;@XNmc}t_!A@?4_f(+UbqHXun1EN6)fVr6g|NDz0LB$b0m7npG6<m3+I=!^~?Lq6Q&oOV3QZa53lGo57z*X(2X(^!j5P{xJjLJ1=oYE8m_)I?JjM9a}geHShO!-m}(!xr2_FD7aQv7CAU{f!XkS6uDu?<fZty|(@%TWk1cDrVtj*cy}|7PZ=1R!-+8ooy02$=ZulB1PF&Azx?M8BVg%L>3|7!nj6otm>JpiAi!G?nRisD^3+-1ol|dSf-63Ow;VUeEgi=(vBZ@n~e?8fF@2znZh)zv^AY@Ee)x&9=pv|N8xbOp*HvZ7_(t)4lm)KDBwO7y7jc$;#kI*&Op4qBeZu><GA8PuVx4LUA@CVk-NRTE>#ojRA)HsSc$d`H=xa>DrYh7z#d=w`*(TPkNZr>ol5KMY)iL3<jw=~(%Ig;lM@gc+#p)8eJECb!0n5Vmf4Tympi&&1D$n7fnGZrZ)dJ^<M*S*!kylawTFD!Dtg;ppHNhfxq=6vBE8{j1AupV-*D^q#EG-%^X9`h^uxQ5`HU~mclR82tm&TYJ?BqO4AFEMacB&<JR#7>MwbeI|MSyDK2pl@_trSg)J;KDgrahz9h6qWC&-f2|k?78%u3HGjSyJ}w39kDt^_{v3>u*^1D<!oEG{_?dD4Z2ZV>`i%|Fi#0YRq@3aM6vR1B`AgAT9QhTX1B+3EfWK48;6GwD5IxEX*{QrMJKvet)ils-ZE(h3eaV>mDwyeCEMYtUx0xz0whRG<=?r_SVGdH+b5F}ZNs(ZyPdc{7mTH$i@pR5VkX~6`GYGqwG8=yh#}LAL0h-oa~tF?5ILb~Ni_Tb{dfmf=^J)jnFaz8^Y)({+-eM#>EZ@8Jy%9N$I+6>Xtv|HxIH=ebIFtMw#X1YUMFyE)?oM{K^O|WH>AKE^J4YD+=&iYem~(;ggzcv6NmMW(`5UkT4@wnP&+0{KZ~b`vR=1(g69rD0SjP8V^7sg<JWc3F-w!X0Jj%>WCBo`Afl4Npa@NmPp<l!+LNSK<#9{Ew6CNlIM2Zj?G6LY_C8lF2y8Z6lO4zchIOkUZW)5{ZS)amIMtrshr$R@B62Q#h0|G_Wxw85QAW|e#RDFqkh3f?U!>T}xLu+7)&hbU$z}ghj@G^PIoOsi#yXH%+g1>4khKyzl4F@W#~wtwWuo76NWY{whyK>5^*qB%ulv)A7b>Y}Q;eQh19pl!g08Q6ISj4~k#+o%b;T*S{=6Tq|5?JkW%IwhYEy`v49<9dhY@`rH=5~|F|&!;5W~P-FAIIppgJQrFkI`x&J<;S!lxWqH~{;!9&f^NWw+H+p~4sAZ!7vI<6301q4f3}$sib-2CT`WfvSMug0FPv@F}c#r&ypS&ppHv+3-_=`-ydG_V9QrHKHGpJN%_4Oj<X2BVH_+4?&sgp=5KUym@)JqYfoy8xZgTr%~lv81`0=yD1hB+l`~?9UtNt2G63RtzWH=?ic#&sEr0nYagF}<%)8Y?NdH_e>^$M!WktPhg96lC(em^g7hR%G{%;iN}3orv8y_y&8$Hb@~qib6FnLBdNywC^KIORQ9YGHO0b5FxEpV#?<!lml+h{yz<@~3U7U^RndHe_aEWqwZt1aNZy|JDCK5RPWoWvNW0oY?K0ntvVl+ikaDuxkoPiO}wHlJF5?}oZDITQFvFx*#GkrqNoVJv(x}(O9u~VqC?#~!`%X@NowE;GP2*pqiB4i{_hCY|Ghn_iFHmduU_MqmJT~QaqeK>b%IhY&UmdtYg<W(w?F-i_B@XO~4)1GX!e9~(4KB5h==F!o_3D?+)kG_1?Ut%dD(wu8=*&1C^{*SZ@N0MQSwW5YDc<vvypC}i8CZ~avOtQ`aT0cT`y@9XhB;lL>LT-a&=mQ_JF|7Athqsj|GGD-KWm*qH6x+4HNnOxUC^_I3hTQVxkYFO1ng^$7fa0pFh7fKL#tH3%PZBci{H1NKB$8Yprm41C>8ReZzXsNBoyiDDC)kvSX`C<ofxT@%rNpmd{g8AUiAK1@c>TE7f1k9n=A(|2&`~b@yl+_aJ;Vk7)~Tz_x>;4W-HkU4ie9<Q1%QncPIfOuo0~VpghYznw(q{JhR{>)Ux``F<L$3h|ILJl;_P|Tn*qAEcGaofhdrg&!C-Iob`i~P<;a9MM!HAS(0r<+{RtJ#7j1;yhdF}S6I)8=_ymR4hskW+$-=px${N5-Pf1+z{C2y>%}%?2TH3E9s|eRf$WT`00p+6S`dahj9qpN{M?uD<|8A|viojQ)jtQ06=i_|6=i$p$#c0otABNEg$KFg;hS&+)f}HA1uhkuWW#^g|2C?2>5Y+J$5^35a`K;J(k8d8{y!01j`UgGx1WdVcm#CiD`daGH-zDAh)3^xV^%f1;$gGki`tEfA_#lYob4EoU*W|aXeEGFM2N}n!kJ#>>Wt<}ugvs>%&P1+d1r*5C2-c09<abZrqkx2C_*LD%#L(V)c|64c>C)!GLuAg{-nUZ#2jL0@(O`a-7i`YeUfJ-<^Zn6)hvRky2IgxYS<>2``v&{;&p0^2_pVK{*-qLF?dcyt0B*3Y%NCeV7aF(R*|n{Qr}oIt0K&3g)vm83`u4l<CB?||-}V}?', c1='35bb2f498507c338', c2='f303d0791eb65612'):
    try:

        if hashlib.sha256(data.encode()).hexdigest()[:16] != c1:
            raise ValueError('Primary integrity check failed')
            

        stage1 = base64.b85decode(data)
        if hashlib.blake2b(stage1).hexdigest()[:16] != c2:
            raise ValueError('Secondary integrity check failed')
            
        stage2 = custom_decode(stage1)
        stage3 = zlib.decompress(stage2)
        return marshal.loads(stage3)
    except Exception as e:
        raise RuntimeError(f'Decryption failed: {str(e)}')

exec(decrypt())
