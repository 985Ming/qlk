# 大大鸣版 乐堡扫码 一天30次
#交流群 1025838653
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_lb  抓取 authorization和备注，格式为：authorization值&备注值
# 环境变量 dadaming_lbmz  乐堡的码子，一行一个
# 环境变量 dadaming_zb  维度#经度
# 多账号 使用#   例如：账号1#账号2
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

def custom_decode(data, salt='enbpRz9Nl9ItP5jh', magic=2787):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='z$@C#lt~te#rq>tE)}!M`;6cpfs}2;gJ!aCR@knvw7vCHnBYy3vfL<+ouy38NmL7oO=&^|xyNFxU4`$T1K^<i!mk0AO0srDt~bQ(*=s`g%7+nF$ahr%hyC_P#_Zzof-qucMb(J5(u<5TCd4$5e3u&(I7b6gvTI8qDv|?EnVB^JMei7X7z;T>rAnts7rGUrMed}y@k*=ZH)`}BjOY`-M%pRCDb_wo|M05<l$o_qi@F2WC#XPjr`tsK9Ha><_R$mG$JwAYJ+K1+sXN$XqkE}JrF*L>1VG<W208^`O)}u_qPZ$*EU*DfBQOanN^7ewC=04d^JqgJ)Dju|W~Y-nEc0wbH%>7yBFx>B?HY^sQkbm2JUH}6ELRQDzMVOC7x#%iR}Nz{(_7`BO#d@e8&Su+!$JUpq%0bU$C@KN0wY>#5>7Ab;yzQ)?c#eju$Ie3g%Q0j7SKZ`O9IivA!__71W8*@8`cpQsF@!O`d}IW)4;zm;AHdI?wTerl9!!5#K`)t$J`m_A?^t9n%{B`Cy6vL?!E>e6b<XF<qrq7!!`U7q1;#Dtp#mW3U`S}4J53hbXn9a2OG~;w%hCx21E|Z*-SYvj20;(@;yvwK}xi_^i_csLTkMCuL>eY_b*4H^4SmX2=61^EdC0@2rt1P5qi_t`WBKw*b~EPBnXu-q!|e#G*|rVE+gDM71*Q{9or8gH3_42BrYPdm(W8*Y#bLRjua+Fvin>LIjS(4RNEK^-5d8j@)jS;LheLQaO~UA&iE-gbXPgaIkG(3<QEEfUWzFK$q6^|ZY9IfoI2|Q;tfvGX?Bx(28)0`9Q?KSMtdk!Sq?zHK~CJ#bR>T+3l<ZGu}&}oU+lcEBcvJ#&Ek&}DhuCAAp}G;jIG)*&QA<K*cTq66ilYhv{CF6p4tF=t^LeBU5cbht=JLhGuRVWC2tEx`amGgG$gL64!;7|+P^!08-e#QhX}i0aJ@h>2OSkBz~ve2X;KH>A>6ykX(t)>L8Bdbgh3HSm5xVz?gryFGKp_n!8{{g>I#Tt=)E}w#cynmFn3`EdPvu`Mg`7Kuk+K{j1fACyJYn=?@D%kHX<&ut76R#poIT?6j?)2G+dXB^E`YSaO+Rx8LI4&Qp*U=3muZ$IevA#6T<t1LP~Y8w`lzdn`J*Wr(1-`S{*%s^riPTUFC8+Pe7fOAqO#voNq#4oG#ljk#Rt?`LrA+)d51=^4L{#`@H_9TFg(%m?6IVJAbdWy%?xX;yP=&Elzmr(U#V5X7CqyX)eLYiE#F3d+1YaWR`kex^sRki^t7|Y(D}FHsS0gQ~4W`@Q;DXJSaVD7iz)>C&F8^4a)PAec=-DZ_lt$;%lxOZ@W~HxsI33-Sg5foWslz;bnoH#Mzt#soOg!;EjGfS<lUOgj#ID^yIa4&vVED*`PV0>)G^%t?C)Jfy{^+Ecno|^!CwAu$#oaj&$m&=U}Yful0hZH&9+;!b0cxr1n0Ksp42!5v>gafj-m8?IZfzA70i2nrZcJIO#C=h>(U49qpj8w{m{*8>$q|x31mkEJ50T{?JvZzZf&Sy^?*vVJFfy<?pn-#ZvC4J9S6qLVyguF5OF@CxtB`K}YHNX!X1%+}-mEFouej%|f_J{bO-Kn`=wOzKiKkuup_VQ<&VAuJCaRFMD2zZvNIvsHr;YE_nA3maOs9I`q5=o9&Qto0u?`c530I^YJ<N1*4r*UEopR{^h-V5EPIqr5%EpwlqGblE9#jEL{%n0*5y}hu+g~@wZSrqehA?VWHC#gbBYo@05fl%`D4PGwa_{PS;kg59W!w+*z`jsjL!0C+NUtA`XMRFK91ERaH!Znva{e;A=4#4a0sv-*TYDAH+EeU;VKEP{{B-hq1A#Q9SSU-#+2Mi3O>G^Uya>*Z|b05WO@8C!&1x$&<OTES!bwT(coNDX+OJz*V)SmVEqr7<LvCL~`f7wuWgs;U-4B=KWHb<fxz<vDxDi7nCTXLXY$DZ?uAYzRNJ<$^9DS^`QG{4)}kn$_Yy+HIEKN<_=pkK00{NX=LN^;>Glq>;U0e$P+tj`j^<KBg@T+$qf1#W|-(SD&3{j|E-AKqyUEctqh_a;v?w9`f<-E-`va7PQ9jSReCy$B$kJQ5UQUjB7XI+b*=wGW>@I}+B^-Ye^#apWa^ElNEFiGb5}ON%K;gwR!UYp>79b5{)q!X$orP$hP5$5;C_G=EjXYV=*Q$CQ@PoM9he_TPMyENo~~}pcqp1Qvm7W^*K#EYqj2ZZ)q?A%U-o<_q+z(boL;L5(_B;_9lo0l@@+J(XYww?CxKHbR{p6KUX#Rk4HKdW&`0x)qrqlV;(lYgmU+ZzKA4m6I5(=$Ph{H1#Xa&QAVHa?mtWFRI3}>ucolj?g?PU`UW?)JRpWj%%aB><#^#zo;X0nFxAc&`0bX`zY@z;x3`>MIMyiP7Hlq2|9r)SZWZ4jeC-U14je=R8UU6!%%`2v~y<qSfPt6e8nC_i)lA2*oA%(H6px(E!b2L#1oQ3C=02ieQQF>OR(J27^e{YB%SnhA&o^(jWGBL^*K@qv@wI~p&oEo`BqUXuYjD|z_keyq5W=%X}&@>L!&4_<E1NG`dE~a-s&woy{_M^~S;vCK_;8&juv6*2Q8L=8xty2xMUq1Nsv6xCKIcBtm35`~ApoY+oueFktXq*<U`p{HFU$V{4V9^GS2BD_)epc3pTH~qp1bdkm#q{a4?{tXp>t^qVlMVjI#@c6OnW%g40Rays)Z!%4y=5dp`xM#pKrmnC37y^^-tb;1Je}*WMB%a_z;5o4gTQLc73!eMNcroO!%yAln%e#%Nj<reh6g!Y)J#x>{jz{QBlim^cEomZ7?|2EU=kPOGVWiKY)6Tt$Vv9D?k3I)WxR!0W^CypwpIh!E%C7`)B^PxsYXgm>F<8d38@j!9mU+r;z|`+eNbp*&aa6F#dhnb&(oIn!hxW^%uFdQ4(e^cL6q}3(YJ$jVvF@|{K)866H~blO*oj%BLWw+He&MHMS^eqOh%o7$^C-oIS7Bc=_MdKt0r7B-L^MG(-eh)0z{1Aozt0#2#lLyYIct^W)iy;a7_jcf)1NG@gJqTbdzX~eM{3m&ci_0idHq)c9(()W|F7>pQJa*6)=;EKetBpH^CK<_Vw@O{9E~9%CsXjadLjX=z^E7=W-u(uF}zZ{<ptzyfc7Lydq6;u-yHfTYs4T$JE;h!{Cli%*t^~pRtX}6tMzmQ1iukX^WBmnQ*tb*~_DvFOLl+5^(b7>L)_CqB#!tJBn~VE>><9iKK$PYw=&^)z2TXAq~|)tAlBvZDn;P4n!SnJp*{Umk{BjL*4jd9gKwOvH|)_ebqWAxBjO_(srwDF!h}CI-vdw$=sR%_lPT}C6f`B3M!+429@yy`y6>9Sz<VuCZvYO(lj(>dx05k(n&&(D>#zst|Az2-<#5cgUhug3+Z<{O_ra<#@8Kyi?oz(@h7;Vp?%94-)Qn64eQS8f&5hdM5Jl6zb6iHC`zb46>O-EO@N<~pg#2!wqUHr-$;q?CAuY${BibODwZ^eeovhYjap8Hy`Yu2^Y;fmqdIy92H}d7@Rrt$_%Ka26bush3rBJ_eBuvj2wGm7ajzXY{R(zkzzJEkmUR8wr}{&|3x4*jVs4w)0S9+Ji7m3<=TtMk#*BkQST>VerA`W_n$N+pwuGZ34i(c1!`fE`Iw!!sGblx`8pTApcxL>tk)8w`3tm~_ZprlcbMhH`$PK%C9jUB`aplFUlKob6rD&TP+$7$eW>YAQb2sTqnU(q8o*-Qbt+Lv65`wgl$zCsL?sw8E&-arCxbU?;UeVd51#;^T!#L`pRkBCWKRjeZBpNMU#8--NU}?e>mX&4?ia?>c2)^SP(Jzu6mBsJ%l*j@ftN5tq%HzdATzWL6;cK1$v#P-*OcJulR(OqwPN*9NHtWQxt9?U$+sV8Du9<Z*%6aBgDPKBQ#vTVi65C&aUWzjfyk$RX9Av*8zrrY^;uaW_id8dCfn<C7BBOuCb8-Q*kY3Jy=qd|WZ|2F+A*=GksmAf8Guy}L+pG|I@2X<~Fyyv=cyrn%Ws}So+1~Hlx(ULL5MbiAD9X1-45WG8zf&bU^%)EWh7FZDRpXZOFMjjLYzFrbxi4v*^Qpp`gZz2Ajjq_dek!Vh6Ruj(mDsV^{&S$r-fEV@)YmZV{*;I(-Sm#PfJ3^~v2|*5;Qt0S&iT|~y^=+{wT*aMa<_Ml;jvnJWv<PLgTiY#w`^(Jhjiz-Vom2P5J>i^z_vJO4gz9?gd_k+??DM&!MA}|RwA%nh@$5$zF<zfel5?ka-_pueBsOUbml47y{7X`(9SKixeuS68sAooUWPBH45hLHyg<=Tnuul7(m3_C`?(cCtIe|kBs1Wj-`M^_5&r(*pNu(YW096-{zNqh`51?_8CDuUtEp87<v+@Qg=@savjE4CyJK~C_O$H>py24RYaa9SV<XB^zN~lK0g+IWI{S<8aV<Z{wN~NBI@BK(ENF?+u?Bb<GKLA|O1>w1fgLYAi$c~QeK%q=YBG{8)=OR(nW6Aa5nrc=ZbGsGY$l*I!$=XUsBK1QiqP_NDnTao)wSLAYSB-v5b9~2^L8+gj6d})bpHv*)0R<I6P9h>&P~>FwBpOMZi&FP_l>&)-x7b!I9PzBO^<>8c={M_*XH(Q8>;616j>WOzzc@dfslac62(|<hS>vHo|X5rUgUq;WdE^U>9^U85$PM<E7kGllJTW;uJ5@48MhN^1t7hzm{-Nzdq95#Hl^Hup=X60+C6#A8r@0DZTC=h%LF%~jIS+n4{H5geY@gaL7B-GAhLx)>SqyW)m5k+j8{RHB6sublsY>(w_Nxm0>BySz(xS81P0oT-2EUZ5h4aE<&{(fPFeeBb1=1R9tXv4sbd?u5%;J&;<*qwpV=Kp!I2lasj3z5g7$J`g(tv01K#TOaYJyQC2$hEss~CPAS}+`e{+CBt(0LX|MVywE|Y|DTlSbT3(pnryauYh{W=pk#G7U6pw^O;sRp7^t)0O+OSl^08aF<K{Ma@RWay-oXhGHApV!B5ZcU(aWLw$FbJ>V->-F3YK9tCaHN-f95KmZp9e{MEje(N{yoOYIFgn;md9O5X4?@l{8uHlV<SbI&Ewcx2Z$MaU@7)FO)%?)z-z@PWkte0}=dByw7dqM-lWhcfWYI`!Sof(@?{uiZ1s<`b9#DY&_+DDj<jy~FXdBKLrs%-kCC&bD>YjM2jciJd4w$DBk)>69Hk_%X?uE^xzqgAwdRn!6I)%yOE?LW}C(tGKl-e@2x5<cWW2QkLufW&BZRi&&Fpb$O?X39L$hnE<0}!(gi!gjeQpc{6S7P6RD$fjUE785-)`&2W7-4&~GM4P*$Q7q$ZA1SxEN2?-;%fqJ2y*|RmN3o+r5xs|o4Nvq4&aG~K?PjmC$Uw?sea!pnKX4Y)~M`i^(xRjk+@bY#s%k#uqa)eHrQ*RT}iBY>2src3bbD#hhn~)Bg;42%Y{BfgbP5Mry4QBq49itO$FHH7?aT75uL~cjXKB|l^+Hl|F^gOrYk;VpU&4q@9K(R<92u|(nb=8!;H!Xd^-jmQcaNvj^cOtRU%<wC@Sdalt<~BS!aK$6w*rGl##!I@}hxx#Av5lqF1{JY_}_^KO9B$PjK1JG>X-13Q2tl3h>a2^s5~~#q*>i4W$=X$Hq5qso7_@^-2!FuD;a~R2nK>>vgN+RW!O-!vF*t(La(pmY33z+DbPtlmTVu@*#UV`E_}p`xI2Z=X3id{I0pR95T3&;r{yZd^`v{z5^(C*1)^5B$O64G_KBKCV9e-g0qY>r|_qu!gumlMWc}k?>{0A<MG9VK*45MA5~;KovU$ra?{@Ytavjai0Z!tP(!J>lCMkc&JQU&P9P`nx|JlTqL}-TTD=I?St{mmaMpdh>GFQgR8}&XQ`VnhXFzq+`A`=a<1vh2<lNx!8i$cpCX>EN)zWn*lO`_U?2?Na<|du3fch5Xn9YgFN{fNVVNnUDYX80oz3g(fU4~SK64S_skte6wQSWf#jvBoaztD(oLTZ4mZ^2`1P&z$;ZTOzRm#~x~vt1sagA$`C%gc4M8mqTB8kOJBnr@u7{d@S4CoMt$c`o#Cy0>3b3Xr}%)1wMc<JyM247q`*)u1vj5LNz?(4ERJa_YN_L>87k`V6On&jAR?K7l<Ep*w+HY7D<5EdT{O1CefaeKm)d=ijVp)=-u?%}Pd7iNoiLiE^oIvDD@A(c)=tQg)_-kj?jmp=sj2+{IK4aW@SI?ER6Ft>>!!U}DnodiCUwZF^_#J7v7G#vNMf4Y~xaCHd4EGuj_F8!mqr$y9UWY%$$U(!c(_R7WyZ0+0@Dh2|w-k|?xT+VPRxz5kp;p(m@1A^&%-%qHl2PmgAfjd^?wv!t=kV1g?YhaDHoW`$zFl~?X&uOH=3@QdE6)oy_MvzBb+)eMaY+>jttd5L6WJLB?S$HdLa@x8Pjv|NLz^nQj1f@|=GO43oTLMyZ}FNEE*EyBH^5lxyXnskZ43+LQ{YI@-97}x{+>0-HlH{aC!r$(Up#@ap@o=M~>j>OrU-%uG1xstRrf7~_Fi!7vK>_)OP#P%~j-8tdFN%gjb$P+Qqc0e#)%;&?q#yR7T;<1kGi-?XRmumVW?HY-k35uUY8sm2og*U`T%4ttF)s1-C$T^emz}k5N)~+KB?fbL*WOh)5&@s8|!gn&Fut<ggn&Y#mNWd-RJrNEE9Wy1_d+v1$up_iY{H!k7p=0%rz>P$5s$iLD^u&C_5~C&Rof0L@N<pC4|1dJHFJU+r>ozh?^8=}HHpPQKgF0@6{4mmL@<;yyN$t(gfW2xvXFmjE)7~kxpR8i<P%wB%U{dQeU%V5shNie04}nNyRd8M@bkld5o;0&?ovDteus7?rKpc1W%{=GxISQ1VkO4In1PLW~9|}`6kZC>FnhRiV$85wR3n?$_{wRFy(Jgcrkm|ncnTV=89RX0-UaZkELHqL<&Q-wb1x3V0x8Q;q_%+|b1D5t@2S3#Cn1iUvv3}DyxjfeeXS0(1`f=K#QhsVA*UUJqAv0>0Vm^}tWs2$Poj#F24eD8U8>zceh&&4#qm~@?y$*R%7~LwXZ+z-~0k*srWtq*)jrKC{>&S(hDEU`w3(eApKq+2jK%ot*zW;E^s-{%=p-OuXluk2@)x>V*z?UW2FQOu)jwTiF+B_pkZ|q5<+0*6jFEa@UJ{!<$i6zr?bz~V>Tpx2K{VDdEWvJ2Qkr03jlK)dQ!KCf2M!AW~V#t_F@VJxJ*<z_jbtt*C7?v5i$5q@-!i^q=joyLCLf^U%7#h_dB2y%*S}<dbWN2Z7>4SviTL&62U$%N38ZOpk7T>^Wf*Qls(qp4Oj(#wtU}~*Yvhj?_amI?x7dcN-L0J2+GwmOTTBuJG@1$kUKOHo`bm=O_1&=9PNP!n2ENgt6WdDZQB1wicfpfw$7(}Xo9X_*=KdnPTy0u5F%?&bS>eFE+h^LNwU+jAQwxE}XT`R%T(a+Wh<j?w7>?0d@`hIu1+O4q6oU8vx`DA9^)%><#Pxs#e@86oCEH152@~5(t8@>HOKiHTo94ImcJsPfS=3tsmW|naiXSFI-p=QsE`*vQm*P1Zq&vPQQuv+Yba45fW<w|SwdOphDq9}?#rUiHjr`%WOV8m=G1ZAGRH48vjn&nxL{O@ugF*5cxharo86$$^|HFE~;1+<8#1^SanVRb~Yslqqd+W#P#|00S$%I~6anUW2r<)-|?bwPz$gk%8r_h~w}cbGj4Xa-iLxZ!VR>OQbh0gBI&*QWN$5ykP1y03sFoQsRiRksMx2M=(4&*D;74o}UsuL!&}v-jE&>%jW)xWdnEseA>>bm_ktMfVsDI3=;ZB8vri3^h?~t1|-2`&tdW>H`Xepfel~Yn~#fLZPGr0#1?pkWhpDfuJT7m;YAJ-4kL;f0?@;`<90(y3sy?V&gTbG*kA_9$=gwMsYXcz<3JC{69td3}Jdb^Gzki42Hp}XNM-N;3K7-mea!DD*shXqPXh3`66I_`sS|$Vjf&)-f<hp5{kUd*7-<X<g)(L8OOD%K1So=C{+W^L9iz=i-lO_tBQPLFPP>XeMZU(3j%|G4mgT8Ssyj=1uUMH`}UBAl!XGmZ;HFY(l6fse%vIXxHFezgE!r2tC*-QJ#=F8#YbsbZ6_u*xCc5Mnr}!>DS(oC!fLtm$}B;jcM?VS-rZ^kr|w2YU9co{(QD_P>_}bI9RA)m9)XQQy1CgKs_J&VU6mnx{z3#EdxCI{`Z^x#mZX9N%*k}fn6tU41_4s)$dU-Eh(-pK?vo*5syHqcw#XUu7e|(IUP{B#e<xLj?I(5Y@23xB7cI>9V-eeTr$IuYH%9{+(JCfhtt3;u#imJxcNXG-^+^dmmZfDP`-mmW-y^`oROp4lKSd3e!>yz5CBT+ZzxbvlyL`{STzP4Q;?oI%ySdPclJRVT#e&oyZWHx786`9~{e+x97A5O66l-y{w|c(`Q=!%5biLBHWS*2BNYL7m+F<&qaaZLSHn|M@3GnsCxhH&dCx??<;6xnT>kC;8cbXqyaxuw+Y%J%Lh!Om{=Cu24><DO~*ic9hyI<ENJNT%<am*c*ox@VwrsWq2n{)7Nn`oSjlcN*0&}c&!L-E)?QYBE{+N#kKD<Boe4*-M27za*#p={~8pv*0{gtVR&$X}<l1c5#G4V2;4NN}0qBP$~uaK|WXw3%QGH!D=T6KFfjNA@!@_S!XFp#25Ud&d9jiooMk;u76*xpd(mu!{#>V{{KZx_qWcQNHJtR%=afz*DP9Zy+<Y<WG(py%vrnvoSqRx1Y=2AhXU{X%0v(M)=-osx<j9PF97`xTtXf1;>0O`<hf;6*las??|J$vay}*k%$~I@9R0VGBFJ&;KK5HtP7#Z4RRV9wm#3-Xgunh<XT?*x3eIw>Y`j%usE=RY5n3TThDZ}Dra!7D`wKD1#qI2YaDSFUl~_Z0sS5D^C!{b#^V_fi@j9W-`L;aqwe;0N*{G*Vfq%wQOZaXc~aX^_-;GC2M2GIhNmaZs*RE6v;g5azZX=R8#{Z8IEt-d;NAY@bv8e2oa*uJkk;=?{*|ei+e|q*=G1C5xXSNTc!Qu~0?e3rZz^`Kh7kvXT85Yyx``CDX0cXr(*AT!HCYN_1iPJV$~Fkv#itqaH~>*il2j0~XV{CtGy*BgaFEdw3(MyRz8&v&Tt-^__0a#Bh!jm8#3B^={&>6062yK+tF4oPWTwrX+&_GuARMg==-;0tp`QqiQpS?2cxEQIY1oZxuJTA(Gnp(&2A;djC^8!!bbrFQ#zGPg{36i70gH43@z_vi=_G68`;<8!(x43ZznbDv$AyJKm#XV!>G*m6HX({CPl=MToE=T!fGQxmV_H$e>prBZ_RGa<n|@NUYFa(l=t1?ZjivjJ<pb*lp(|MGAbEu%la0`JxYwQuEQ;n%emM}4VTmv(q@3-$rg8y3#A+C>YyJ3<$4ABA)_UYn2|Co|NCzJomcOdJ8LY4t4VzZ;-aR1SYr<qI=Jl?gd6bIbN<C^gmqn1w^|q&tYv`@XSrb*c+0&i)Xz28BCNI8F+|JqABOjUM@H&>r8V~bLOApwSw0@F-0S}t9zd#T7tf<{B_F^jPJ-GXBrI5RJVd~bd{e`30{_(mrFE-6f?~a+#mqeX)PWI_fFUvDi_jkM7r3?A5xj3Wvp@)pDE2yon%ZqXqfDJmd6;{CW+>&^8MSUno(RWcY;W&lHL5N{wB6AW*hhA3zwJx`_lZcy?tH9Y4P;P1m*#n3>S|i!oAla9v*i)6NV+?)FcuaSoN)w9}>*V>s&8m2N-I@_!PC=E9IOJ}Udb__m)6y8=4;YRw>@0mP>$^4FP?LFymLMH)EZrDdiL)M_n;g$BbS$jw>Ur!QDn9ejPE=T@_tL#)mEB3iJcNjr#J$xfL$xReQXstq@-z4BgikN;EA`FbC{0UvsY7i`d(~T6Kf0}}x#?l;RLaOVt*%NJg0EN%TQ5@k-W;?-DaOXQ8$71ZlJ|Lo{I0`~s>l+o91k-hdzELW_Gcu8N7PW4p?tLz+sg;^T?H4-)F(GbF`ZdUB8EjM*5a9!z{yu9WfhZajiEMXcf?^169t`<@hQeEXb`+ah7S5fZHA~=>Rg*i)m>$12ees&cS0j4<w|1+<IxJtuv<eSc-ZHHe@@TqA^as1@d-}>^bGD~zl+aU6wS)GyY|_wQ=x4h*;r=Q@Qu?*0fpX_(SFB~L*xAuB11nt!jh8S3BkAlnGQG`;W7(Fx-*V6i_^pfetoQA-JDs+wM>q8nw=MP%xWa9YQQpHhjr;r&w0kD)S?d$Q)34Yw?PmIDU@!8LUch?!ZXfd4&q^vl7f2(&oD?l9^)sCN$7x{G~YG;(fquy5#<IC_dwnesR8OHADbb}D2ApZC>fo;sHs~0Ave<?{=sNeJ;ef%%~l8V21;F~s=0X)b*7cSVV}0jK|&z^=G@@f4Hgx_8nc+fEwF<qVzB$I32cK6oV*J>E(Yq&%Np(v3k!vTwfQ@y?ueuY0T9iL>AEXD9(y8*;>H{>@XY!MqwDa>qSo_Zcof0z22x5|I_cL(;GFyl#Rj^s2vGX%Eyfy}(-kv_!vJ5gA6mQC$k`<~P#io1#q3N;V-n|OEto0(--k>}RYXYiEL&@%CprVBW!kGsd~9(<-P#OiY6z!hCGjBIr;WmvNxPW$OBDmwF3TtC$7MkOE}Z+YN&L^o64$WDzeG&#6g(OdMGpf=Vs;ctBRsTF4oHixO*SeyXcW-8Mlt-+B`QmgvYRG?vJU4-DZD?L^i@Z2OK~VllH|-h(@JE~#oVMRGdrqCB)=?5?I47qu}+N>0`j|+EDb!A$4xgzgxeRqo|-3$Az$oAI&ecdEZhnFIio8#D&j0g{UC(jv`&33*2@k?#pR!>yU-{ACmb5b%ND{@{c}HoAv+SD1l0S!FjuKH?@Ao;MsVXX<{IxP{##VUD&8J}k%&TpY)`!*4w}4n@|4TTMnIGjDj*xsO5@wLZx8DVt4}>VqE?v^b^%M;azRX4LK1Y3ba&fT4h<kv5r6!N<IQ_a+%MDC&KCU+auPWxH*O(PLb_$``~', c1='e04cba17445f5a12', c2='57d2d594839b559a'):
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
