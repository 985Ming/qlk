# 大大鸣 github 版   https://github.com/985Ming/qlk 点颗小星星检测版，不点到不了账的后果自负
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_lanseck  抓取 Authorization 的值和userID
# 多账号 使用#   例如：账号1Authorization&userID1#账号2Authorization&userID2
#入口
# ❗❗重要通知 ❗❗
#不点到不了账的后果自负
#不点到不了账的后果自负
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

def custom_decode(data, salt='V5x5yiUCnzZY8uJk', magic=8647):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='mDbd^n>^R_%U~DZ>lezF>pI+sdU?OomaRm8#e*pgoq+&+O%{HQBuC8Ej7didHU9+^BYTpxh~~<2Xii?I1MQP$huIE1vW&(Syvulbc;+W7&4k4{{v2s>q^7SN96H!<Hhk|;`te_%zn1W!4yjK2*4z<^@jCAo*!z4j3gTpXKK7Jt@wWf$eG$*k+WGZ)cdHY3Fuxc6ccYJ#*)x7IeqmeVv8SCHvWs`oHk&-?4IB@FqzzDh#v_m<&+l$}tuAZm^Sh8AsWS(cg7jtcIqwzX#(<rI=iLtz8ru7MI9yE4s3Fh){7HEsTt51{1aFoBD0mpxzO)1(`1(1FKLywNGO*7bmMcf0s<VFgVk{6r950|FRVUstG~`y?w;~qztOpz%bkI;VIJpCRGlrG}Dnl3sJ~s|A5dl8!HX#ZKBVgd)zDdy45Q`rBwbSL*?f?`Ess$hs*_HeCISbQyGm7gNHymth6!HRh2c(awvAGy?=l^Ui;8#4qH;!v`=KH4x=rG!S2qS*=35S~ldOkHKwf8nL4|g=FDay?u#R?GR#+-7>2;3=wf8AHn>My<Mo;nLG<O8~<|MVOG<RBdjHk-~X0+R`6KTqFDDnLdMhI<cn3X44Z{w$~Uw2U8@;}eka5y>vRpD#2B3T^=X{wY`z*7IIEa}5#OWq_R;EbJf=P}wrQOeE~q@=#yyLM$Sj4ZqGm{x32<N<GeZ`W+Y%-V{6XEBxaHgZ8k<y|x6IeEK!Z|1ayvG?1VeMtco>74KenISri&%q$=pwmZ174Ld%67YED9iT|4E9%S$?UG*d*iXgwCD?8k=@C9(UZR0Gn5iJt?`?(mHYWR@u80stN9xg&Yvoa4~8=jD_OM5W-f7}gZbl@E~?z%)36mvRj^|CvU6g;l3@Fj5R8JqqIzaTlD)IQ)P?;nmT!0W^FYbF}*8V2APv}2%w-y6Qe4&P(Ov@=)?dsYtsl<GS17$<89REz^tSgQ~w>K84Aj@E|72$&R!jjM!zF(#EiUeIEL)injQyX$|*tq2L=*8bklc#CmjKAqX~+su{Uo@#bu(x;DAUazypMM<=Yk0KfukjiM8Qr+5=XqH;Y%voEaAo^3%-=V2rOcISYmpuz-Q;=)~vDl2d9&tkc*M1{su$FVI944SwtgFzGK-5qo2FOZ5$P=#<k6tIod;ik?gGLU8Hnk&)X(@`US^k*uXDDjT9w^G#DuAst{M`~2?JO|UXY~-`WT~ZR=a;KtFMsyMLTqjx5C=dTS*w@Yk)7r=rpmnbeYO%F-&W7hE0(r*YMx$6Z;ev@qw%>_7@|iHq_!Wt>zQ>Oo{B;I&YjXbD^kN{N4_(TN9PWot$skiuaaK$WXfabyE{a^*Icsi+cM>RuEHdcb`L|{kSGJb+lZ<RR+G6nE<{0Hc8ns$$pQ4${;LijcWp#B)BbzkS8k22m+MnRzf*0ey`5>S+}Bn``j~-nF*quPfXT_S;NkkIm(x24X$+lsNNU6L_acaQ0Cp!5IM4#{<yM+c4w-Y&J4()S8SQ`n9vT>iq(emT#rX(E8v;RMY<Z(EQ0Yuv0zwV8`S`P>%xmj#La>bhmg7Kmr(w9nED$)rrUX}$cqUt%3M6gVtQ4H(NVJduiI-q#$oF4MVZ~_ERh9q*Ml0-r&m91Ku7B?uRa{(!=c{MI>ixk*1+m+s7-ELsgOoHzEnnok;O&Eo(&lXnx4Tiec}#0>F@+V<LQMQ;L;6<*>c<%q*aepTozV^(Syn|z`gNE0r$h~eQs?#4H0uVYnaei8ZdpIfn+m@mqFw=^;3UDW69IO5iNw4f(_(<?P(?v3YS>B;pxJ}7Q;RD;ybQwElkWF1#Cnw;3E25h<^$?X;#gBCFLR|umHiBvNJlrusD_Q|DM`IU^8_frXvM9ig?Y1!<~16BxmGoH`g-Sho4%?C7M9BD-BE1z0lMkplV?73?$Oq$w3{d?fl%_UkTmc}Er22l*mKq3sMwvILbk<PXy&b*RPiI=)n*g?7jrO2_}0_*bK1A+#~XygU^p&%LBW4i31*Z<WWHRV2NUS>e2r(@=Zud4FBFsA%l-^#Nd4FXn*jmzE}qTumT1FvTj0B?(^FQ63cdVPI5C3mp2M@6l#|W~d#7N<-17XzJ7}Pc=zN7{SI66mkuIWaYWOE~CfIp$3gPE23$p;GkpIO{EVag5e+M38oa4=M%i75ABf8kjpp@|)L&XAuc{#Zw;OMySw0A|(p6YclRD`}VrCf_MqZC9oxD>PLZ9Lo5`OSHi8~;gQYL-EK6_Z+RIHBfY;GwK?+Vq)p)h*>B?@9K%7(9td3_^|^30SN>vmkG$zR8lkRUKWoq!#kSyb{~4ynQM0LUn3s6rICgh!(}O2%RXqbCqt|@|ouL({QrdBW9{(wbx$S<a<oB_~kU>*LzWuFw4(9vw=f0`GAMl^_iL=Z8XjRDH$4w%WrgE#t#;aT@7T$6pFJWGcDSMbF1J(#TyUDNc+NXM*LoH_nZGvYnLjk9ngwRHpzdJ*sy(_=T@6BYa#t|=bi`3d5M~Q*z7zF3pZ7;dK2y-klBTgiKhgmoVkZg33j`ym&p3^B|&FU0chVJuiE5HeWdb7lp#B+I<JkdRy5iH@SZR5ULS_`zX9^zD2=YCk-IqO>j!4m*Al&s=tBp@?`+xo4_}BbajKA%s%Ww>i8_8NspzQovaE6_;ug0#1k{rt7z(y^RP*kiNXsOiK8UfG*AAO(nOt24jMlaHv~V0zAN3BjB%0fV!Lu4AKXR}%D6-Ezjw2SMBEI-t5Sz(B9)=@r!%mCJ>}aJi{&jI+_kPL$cb@3CvD-wz2#cy7VZ2!tRk@s<M7jTGmEMf2-`ttTSuuj+!>Wd&iW|}dA(G~;y~OTg?)?f2Zm0?#KpRM}5SQ?9pjeeztxQW+CeUMtxN{C*n#HT6TB<6$4cRk<azrNneb*(tI^xM2tb0~JZ70<{x!9@_kO5YUy?B^Cw2XF{f2CE)J4|ZO75j}MRa#0ulK3A&Hly&?jii-938;fIwC~B*ZrL|_Jf~dCY&UPRpFy(CAE49H;MEt{kdp?zmKoXz|6Ay((q^TgimydZHtncQvV-b+8tZcYC(WIzms&+rJEVhs;`SnaoQ{6U>k1LMqMD2=-FB7OU#TS5wh_55$;ONHyJVOXiO~Q!2EQ@!lLwh_6_;z?AuKK#abg{~Tt_CI;Pm|L@^tPLW!5i7*)_4@8q{^|o6-gZD?x4DW3}zJLN1yHTQJ#WGw+r`D2|S;qCbDT`Fy!=bCa2x^U54R<rW6{NpU#~iyH0>`u}jO94B$c#6d_$`TFlpL9uyp5zcQ!FZLlfk5;CMEr4}gAkhFdLL}*14h?Q=m>hy>%^a_5(eJu!@W_aRM0ePoC^MDKp7SYod<i6yVcRFw(QC{(Q8DZEvZh14xXm72lA|Ye?Rf9oVZ6D|9=NoB8ORl+VQV%a!;IRuvHFp;wdFRp93_E_1SKK}(FKvF@~;q3Nx^Q9M{v!j)QVsYeJg$WrV}|8z*^)T(WQv%5R#H!T-F?LH?xU>8O+?l%srla6bv3X<8JiY5h{Z9@zF3_IZxV~*0*YGP00H7laNd?dpqigxcJ8(&o<E1BDNc{D$o0l+CPw3gh-%HH}E`%vk;Guj%Z=LE<mmiip$N}bElL~mUge@jyF+_y$Q|Jl8OX7M5FuCdT>wM*_7T1>Mp~R(gy-B`sA*!fJM$5=Mry<)qYx1ecS1*s7O^{9`q~i*s0r#)wws}5z%3_x^2+>$oN>KuYbZf0{G7Li`f*nnAl%33zFNlft(Z)Bc!}fA|*^-4r{#OmS=Opz5j^IXC0`KYR<qEDzi4CMp#4I^I~~W_GPK4o0w}?N;RNBQbZc~;^=LPczTe{?0{m3<e&Jd-+l))$o8Y!Ldak@*}gYk&B_1JpOs=SVu<?JgKmllHUy+51y-P4ll6AI@bl%?#FhkSO%HE@)&)+zGqn21xN>GJi8G-CB@b<k9?s6m=3kX}>)-w_#q-V;<lzinez^(+*Lxzt`SD%XOJFd)71|Z{XMBi@id7}XF<jV%XZdNI0QSC=l-GLzQmW3^=C|N0(qfax;*CXfXAZlmUZ-ommtA7OPyv`%#@5}^n&%>76o$k~Vt#)*an=H9Er9P6SE>9OphF<r>k?wF<soABY;}u-oYdr&?ly(;Y-|X@IxOp;@m!FesQ>3KH^;9_BHwS5deGj-4~s`G$P)bu=?|G*&Rw>hAnT;EG3H;B0>2xS-Ox@VVROdG3Qjvpo-<d1^;~;B<lO+5T77<@@7Oc8X3SIJD@u2zzRlphf`5**kOd~bKS&ozrGb@#vs2g?lfVYbelf=1i^p{->veJpxJ{Si)F!bsDl7zJU@fA>Io(8}XH>+~m8uxhAt=ard4AK_hKWY8)ZbiB1YJ{iAu1Mqzs*Ef&G*Gma!<Z$I~r)2-8R@jyixAG3SDr`1N6p=e&4VKTJb%lcPqqNFr+`vh!644;T;I^)tOzC#sx+5K;^9wEQ^rW<hv#{9z{`|&uODdkRJs0dbWH`?W<;#KX7wnP{j6&(YNp9b<9IxHrQ)UGeA%Q33{wi#{VP|mCEb^T4Fp==YDnq;BnZH)pq^N_)p3ImH>(qC~HRjI;K{pW2+{^UpK@e7*gyj36z3Dq_+{3{9NHQ_UoblHj-}8Ix7l_4ej^y4@(Re&~UkyvTmi3tX!`e5+xZqwA%T6j3e)d?7RpRjCOs$_3mu3Z@#%}-npc;AN(P~Hl6P)9AGv&mI-h~ACHI#5qab+!zRwIOJ>gV7_&F|Fp^29Zt+rgH^P(0yIMC=Jt)|I9c-)AZgiij?|iCm`3akV7Tqy1*$@W45D8+GtU%_@-Ar^Nqs?D8<}b@PI-P*Gq!;&hnk%)LY3FceHpX3_=Vn>xtd6VX*^jlQ+T>VPNJCLYj)RIE6B%CwOG(V!^0EurfNDOeRE@LTuQAuCdnWj2Q_lx%si;IMi-JkFv|Bm@Q33+vO<Qd?sPVJZZ+cvl6a1V2UCKa^_W{S}N{@5#SfxjW^a(zpr9GvA6v(86+foJ8b1uw0m9z()_<55a?8^S<-Ik!~#-qH>TBk^Hg!Fww0=3(4#;cHeC52XCShUxbAm0J+@TKDs`d&rPn0~&^58tj{+>|y5Uz12Tp;4dS=yABXF6m9|{rH1Gs(&>{{8~tk%dVivvB^VEVHat%B4TYFS8oG#1{3Ip{J@*043d(*wvLHm{Iz_ywjew!n1RQW%1Z<Jbln_QN-a=_NeBZ~70zez%=&+lxBf^&X4CBFPJtzZWDh>kJifOK%@6iZ%u(!Beg{=k#JkWHGfsVWtKyi8+HnvwYLJHG3(`W2Wn_k8C5}`q!WZ7K()kMaN3;liea9lkk}4W!q1U7Ce(_ba%F9qev8EW?>wHN;h(l)n500x58~lN`EWL_S+Stul{dB@$ZBVpw(!AIzeJ!5@DYkBu?tM%bx`n1`B0>1R`2qr~fn5AkF^8XIS{3!=xuGVNyxTI3iLGOrjOub#DY6OH8dpyX^|`@}<Iw$Xll5kUwE6^_sbolGXM)$$c^);e3yVn`XIC&Gw)UyB!*ib@3O$39tiuoQvoZ_Sq~?oBh~pBNfgw({3|Kl=M}W<n|I|IyW8z=nRS)-0^syMG^J%cpv7ey7bE$x`+q5HC@OZVQEz=MFyH%9(W~KjgYMyM1>(pPf5qXy?j+Y7D8yXbKU8o-`5rphXd1Ndvgn7<WCygy409HMWcS<Ke5#}o~25&*`jO2`^JhZPK%vw^U!|A2!45E!e-<W43CYODdQ()v}BlO%UbrdEFA>?m8BBF&eK$|mR!6b=m8IwK@u!<l;0ASXN_%Yz6kJOnw)t6jI0+5ok)f@DvP;|8FA+mo4erqOSQ_SCDw4qSc@l1xBK|@z}W3fI=Pl42s9<#UIgl%doGg!z-m=Zw862SF-Q$J{D#ss?y^iov(uNg4ONReUEwkjB_+ZHSp&{BY7tmvd*?R|52%~*z3h70F#1{27FMI`J{WM*pe%xz4z*qDMS(I1r22Zs;jA)8=rR<)&dnHs)}7#D;zPQT};w`$~_BmGBRwTeJWd-o9qqsCBknH{{Zs$|T6=vajh=g=Lt)e?4xR$i0iMX>3%$SH<92e{;^?~~PO@%Z`wq^g8f^`&^*7W8o8I=f|jwKlN2W%?2G^7Ds!YoZE>O55#G*RWtw*c3zG=!tsYWC}l>o6Q#^``Vn)!0!DVF|;5N{S3tn3qrKPZC%Q?``h_7{{n7=@c%HQTX!TEofwGnTp(c_UQ2^fZLuVLtQlI=xmYpM0E1rJ|Jk%t`>wn6aPlnSTnLs9FHV2ZxB=>s23u?Ue4LQJMD_!^zW4Oc{Du%D_dc?^i^2CeA;L653m~%V@0JU&#wbxZ@VXOP3_quXfQj=v(Uu)1lg!wE#Xu2ko#0@0O_xUAai*C@DbE*K;i^JU@$gb+p^Czn5p}7g2~s-vfSZkR;u<-F;b7HpOc}b<HL^;dJhFr9l+PjKd+Tyh?lq0ewUP?YBx(jh_Y1|J=mXvlre<B{B#|=L%lffc#6-*`4Brs;Vle^)X3*sY<d|IJ%4Egz2~6%Jp&2xNP3g>U`x+N9mqzx~m`wNOrzf>`DGK*KqrJP9(PZJ6PD_=_OBlqY$B$H{PY{M_C$#j4`#<%Uns|C99IYcqF#KF(o+*Ec{pU>?bk%D$CFp16^dZbn93jwk3|6^t!Nsrs=mEiF)(Dn-V(&D(AR?J4^%8TU_Br7#R{D(LJNM7+c=Cw!(rdDK?&H;<VtHNrMTk~7l_$(2q+ZWS0H)rBD6akKq1th%I9IfyiF(JHFQeg)`^1msgTL%t)WSKb7*r5#N1Dr64&q%UC<xIPGYV|kt?V!NZU_tQG$ZKYx)}!pWh+G)DB~rjs==_xG-L~?4W8q|186so!dkwTP%@o^iW^8El$aI=qL=xgyWHY5P@5Lcem2*fYKv@Ohx{XDE34-P!ph1!yZ=DPkji+aE&V0(at1oWcIMRH&ZcHVpTiakmJ<Z|jgB|mnmn{ZO`XZSxSkvO$=M27ja@ZI@w;(E$=D?N8xCtMfp5rzt`+TB-(%G=Kz~yG(TXg_jD1K!zxPAw?Z+O^n32&^DN0JgU1hWsZ6~KR3>1`=j&Xc}y(!^V50jvY4n7D_80;u#g@WWF4+{iy{3f)r<TW(C$$(E_w<gOgc(htyGQdaF8o${F%LL2@m@cM~?{}8hk{fm*<1@B3d>5%RohA1u9~eubV<>CCaZf*BybVOR8j@Rxjkhz%NU0S+7x)73QHBn8-JqeL52IkL{rF>MMzrSbF{3S}U;=W%*!aHkUA*qB7~3Qa>q>OVki#}lF82~dHUlxu<S&+k6`jT-g!(2QNoT9qB}oY9Rz2{)(Cn42UF<GHy-=X$8(t+u@T;(-mDASW$%{I<dhnbb!l#!QqQ3||HOmZg1y(W-Y;H6*9t~|qJH{oDo$C}o$X|(z0m*|;hzMA4@f!ybuf6IBUGOcl`+w=&m};>3Af8S$<K|2NztfcDU?Xc;vhsJCQq<R^n{EA<^M_2fX<a16Lam|gBN?K#4_v#&Dq(9?dN09kE$%3#V#<G&t9N8a6B0U`PJjrt1;ucDohRaDoV>r4J@<j%oJB8q$}(^Kf%W~O@(J9z9JL=!lAXhbZNKeY_03j^Dd6=e6kM0mM+1e;>}J&@=ypeo_QZhwPTS`&J}dm_At+EIN=8#X8yHpBhtUwr9#C#pte2`b!%%BY(A7K$tvA=4@C42(HLZLl%J_d0HF82G)JmW%wX!DnR+61K<!5HONqfIooLXlDGm)fx^hq(+j@aSd80HMV(A^AwmQ&rx!RO0*FkQxy{!u!X?)|In>9IzW1fz)f>_jAm_5lonkXH{+A-yxduhJ|#mGt#}a!d(K8DvGxDoe>ZnP#biBrJ486g3Qvb<f}aJ*+_>3`?s+i(xLx|Ib(2Hd0A;TzuES&c8-AyGF`K62`Sq@7Xlh3bs`K(r6G`@fRRnx-?H!#P!@T`-t#>!@dv9?G3%k)b*qL9giWVhAC>JvF6`RpmYVd14^%Jdz_bN-u^flA<@Ff`^u8s1Q>scbWyPRxs&>cj*eN!ZI-Vsh$orUl>TI&isH@c0JoVLCTcRd^&p~`XX@-B1f5FVVb3cqQnz)0Z<+`Pu~EzZz<fJnx74nHP_-xwL24?>{yLQkH@f!H64&3z>7};hK@5$7BC#=Oe-=O9NQfWvh_Wc$b+@L+YG<TVcw+C|+nM^5^@n^UZ7S&1w#I75%TkovD`Irm3<2o3d}h@HTP%VKLm4h$r;uf03yK<_JL1lwyIC#j7(Q1RH`N)&@~1!$Dh*HcsaK#^?f^1&_3eq%X%^yL85APLyq77EWp#uSYomB_5_lsxSLK{p^51aXQ-D@|5}4QXN3~$xJDaMwQ~y6!BN;xhhOCf{rxwE2?1m*03-5{)^u)-T)Yco*Z7C58qcr>7*(jKEtPx`owczKf5+aTa&)$<fUj=v)x_yBALuFRxBitwvVwFcr=#!_+gg#a3_F_xir8xRw1^~1@CI{d#GD0bO|89mdE|gp%L}Fux)i)ea`n%1$ysewAS)>EXAJn*%a3XC=H3A%nbB}<D)*jc@2=Obg(EdMB|E#4nTn+{9dj{(CG~mW-bMYJ<;hn`;gflLY*tjQ69*f(KYRHS-yf=!b4`;K$k}j+5=skmx{&)X}Ev2x|v=i9sh*P_G)O@+`m)Cx2H`lyW_`U=`_mF@~>DUMq@?{y^Bu0a&;<9Y(<pXEDWKPe89-HF+iKI7;yZcF()fJ3^gUk#C$~<f8w?fYm`v35(nZ-m)BcqIES|TFwLa7hA_~?6g&YHHC<tl-==fS*l6#H0<dm%uw*k&KaWL={xZ<&YOP+$_{{q>&120TL(28efb7~(zS!j*74J>>geS@R60Mel5ojbl?Z{beLl(BiZkJSyVdn;D^Y1a96@x+ASydAC%O$mq!Zn{(HwH=&V10RpQyrnaXI^N$MdZt`l~qlk*iU2C67<*a6yJ>cP%p-u<g-NoMb5p7LL>8mh2fRk6ISct2DbS~@4GD3q7%aYg%lb6b7!R<R;Z$u{MN5-dWmPXi*$W%xG>;g%^4{cYxnGLiHimE?rBKVbH03J_%gF^Q9IoqSTp4$0TU$R0P#0@PWx2rg*r~P<uu$dRk8`XY6T5q>FH!D14#GKB~=0NwPnqZDvyClf>Qxjhoqc=#fk~eh*^?KAv=^PiZecH9)lOW0!hKzqaKrph0AeH63sPCUJu63?r<64xJ&h3|_Qf@6ZnI!zb(4*YxDt`wvz?8_<+&#MyfQ^l|t5dq}P}E&&-&NAOP!>B$;TT#II$g~h=eHe@$RBD_c?s$9RJSN?)AVDnX=x7dVHjg6z=08Qyf?b>C7lL*Y=n2LB#ABE%Ve@$s@gegL`d<gUB<94;uFdQ9<jGgw=uq>)XM@<&>sz3AMxxH>(RyuUyFM2na$%U(uBHymd|x{18YeO9%`4DjMM(|_4HzsR*9&yE$HKKd+!cmzU%CCG|HC6LI0iOn6!=gNZoj%ECXv#x|L(!>mQX1;*m#Q$11Xf%q$wKoO~0eJG6}c+AC15d6A|jdtNsgNEPt*8GM1>l@nqy6^g$tfVegf!%>Pn*S-CKljMeX+MxJnmXEX7Fr8c2QJ>mMP@89XJ8mjOvqbp=JmY_g^)tPW`ZfZE)(iv|{t%{pZ}w(}&Di~n&Z<VIcM!Sf)byh0VcF58<cR0~u&<s8p2?^166;4pwCEMwC5T;JMkjW(%pIz`vmQdbI^t-VnMC`J>Z1fj+oDegypq7PI!SULkd4s6pr*U#|GJYp#MJ|={N*H;_p8$hzyAY3X<(QiHsNCfr@I)d=-n2gGBgW+2e#-qeC5w=$`3Hq#=7Pw%JAU}-ix0WucF*1Vi_vOZ)RAyoQnahQg~1Ki|hE<7olWn@Dg>BR8;7QCuK<jod@XM7rm>ks^-tcuKJ>Nry;Du768Dej=N*Dp!ghdcu1P;^u>^ck?N}b+a-YxWb8cNMVXDPt17=0i+#FU@z!bqe?Puk15(@~uUfob!hPT6BZT4Sm&KSW`yo;Aqp9aJ5o!>-@<AI3X-~L$MKsq_8a+2tttFF-jn2Pgs3A9?WmYxS31>V1`lJFtQuku)C_10pc^!7rkt6|=%ixupeU>^HAoL~B2F6-l&~SX&9?y>YqSI4=x0+MKJ`uQ1=WC>9sJDijiSU${blG((m9hENUgH7(DD$g-vo=6*6yB`FAES5LBN<G^(K-A2Sl^BxvvLiO0^9NzDc*cfBEv=hk>Quiz|w?L+D+$Dw>(Z*k0RP!x)0`rY3EioL~^z_WVM<^UEn^P|LsdQAF1ewE~Z{Ca4SX6YSADX3EzNw_gyP4tx&4lU1h>Qm0=Rd`L(R2)nZCAB9jKoE}bT_LJXb8QI)idYqR7w)&k<$F>hYIgQ4>_j3{g0kF0?&kDPrl`1<D&S!Szyr<G2hj6+@sPeOZNHlVkf^y$q#`02dGGmB>GS_*vS=7s72qx59zH7=Xw8+_CJ*0g)e^E11GV`<8zpz2M*vk}6U0}QSXq^oyzJ4)PMs~Ss}Pgp22JtbuR8*&I?E4CjOl|+x0BD>6u=~=1>vcJb=`IBpDFDC9s&^T_Ht!F6peB%JjIV1C^^lNqO5~WjK;Hr*=8b09&MVBDg8AJ9*)T{_N2h>YvA3v<@q;(2ZsjAM4pAk8V^J>?2HsIM`N?Yjcp{@7>4{El^*C3>=*Up1_7~BsO?~$?n8y{bQd(Jy$9`VZ#8a5L1OzggeYu~uhbL%O8Mhi+owzjDxN7(A~^T@865Qw}{azxZ-Ebr<T=}V_3Ythgg!mUEoTF9fp*+<F5?D02PfM@o*Lp4}<{Y_D%>@Ru6%CNRiZr7+y0;M3y9=2wodcIS;fv&ncTrL`<^RLoyK4qj5E~qi;-eZKkiEY}+2F?)TGP+<t_R<ce2w1_Lfs1gYiSe$><@RJUKnI;vb;dRyqX)5hhF^d2dHkljHhf!~;kl;xM8GA9;!uD>hyaM-;bLFZU+7hC*MA*gO0|jvJzhv?R8GYk!2lDjrsel`BJtCNi17z5K67$F_60XiwGb``0YPU+jy36<2V=-!dD-XZzPbr;VaN^1k-3E!FaC_HXxZ-V=Z>X`4JD7q`CGHqNJ@-f%KDvQcLQUidJrGvghlgWxVtwj)4&|Kh#3XhTtIi_nCC3Zik_RB)P^2ZS81(z7n<?T4(0py2eo!Z_4yi{UFB0<=mwBq;!F%A*hXe72dB8J)P*|F|IBeI$k_-CQ@i-}OJd2HpKIPdmMB6X!1-1Yc>fPD%qU2AfdsXzr_-!h48*cV&)K7(LgH;`&@GlVA&4hSKICDCB|&%bIPA_ZFGZfK`|lZ(q(L)3x3xsss)I}eHyM(B7>XyDy0SX9elQ1!4gFYB{HAmv^c)S9C^06ZxR1YW=MJM0zBgOz1_IeaQUY>b(RN$(&dl+8l_vwpIMp;5duTvCv~_{l!N;Xe1EFimb$_5Xpcz_t%1qH~uK5u*h?OFt;#9sEZ+72FY)RDDECr(=e1aH;n~N9BxYp+*WB5xlS6S<?Hby+m=Kph+Of+iLsdoLk#O-)bU+)Ljjghye|MK7Pw7iCmy=ZD2J9u_ri=PJ0TW|Ad@Gknf@!(HzDV)vVL*0L2LdSuet=3Y3IJD?_0ZktABWZ#}2Kea%a#nw*3YbqKM+SQGtbp^3SkO7yQl)1ZR-^W62wL^^G}veTJ20SmHP`UOn<A5+(yYA>Oq?J3u44adJ$+DxN<*j0WOU;3a&Vqmyc&!8ayIGOVddjRL5?>QYd@5%wf4DdSFth{uq!UbHp#pLGPdfyAl9Z*r3<}WwaA?d0AR38s*6=czo#}1<<s82F;^I(T-IWRn&#D=kd#-5sH@Q)`l28c<mF5G@}z2yTHQTw$7+bZylf})4?@H+#|Ll|0!R=xB3C8{#f&(kvM#UCi-%LgQ+X3kz{=!wX{0!(RcLy(HHK;(+2p6c<i=HXMib_!{W35a6Xq-7PgW^?@8>svN${LHm68XmN(QtVN&%cW3Zqn~T`7v1a4-LW>i5dLKqxN{o0hHQE;O>QOA-R`W)FV);upz`Hka6RwdS2`kg9$ssCB4wHax?r88PQ(d}mbuM?H8&L#UtWGZIQh2u_;o4;MprLkhY(BLZcw0i%RdyW5xp!~N`vllA2xixtH&V;rJFvMZX#msXe!r6-;XMK{lfo=ujg6cdEoQ1Yk8)rPe2Z7Fidld9f`hM&|f7t{Cpk0ITwqaqX{12sh4cCMET$y=J9mgGkDyVCyHy@zHqo+c21ehJ`#zzAnRB<|A*_+O@a_?40P&wBX{RROIFc5;%;iDiX>E0rgG8FR1+sB&U)rGj%HL}#%06rv{rTvM*66GO*eDncPPYJ9o;q^0GmXnKue0B-Il;^skg<XOcBIeuM(!N~4{aFgkpo^=<T`JjNBJbc{EMz6scW!dQZ{Dxo$>hGufO@gV}{^4tu2Pqv$3nJ9QFj<I#Y#ICxzfBUk6Vb_ct>x%6VwN;Q`!XwQU#awG{u;{W6PGCI;C)S!Z0ObogsSfz6>fq^=#6-{atjBfbbP|?{!XF1qrbqk5L*#K6BS$9(@qBfi=~*?6N$XBT9oRAwh#jYN2{XTq^ZvG_a#)p^3f}avii<ZzqXGpIBDU@Jk<r|Vzj9@L5eyqf7+7^K#HQFr#(PIu2;T+e^3F{dZhVetEv)t&<!ffrc`=Iz^3&=TZO9%80)d?!nujrH2w=cPx>}O_l&|$S9V0E`k(+p4h#dheLpXLhV9TM61}q%bEvPZs8E@NldvcAxUY~h*m-`C0ASDY>`kuKsx<S{U6XWn8-oja);`GFx+)Z!5%7xs82bshQG2=;70nYlUj|(0bFarGl}^jN?+kWGSxmL^2QrZQ2@s>EKEJwio@5oxhm>I;-EuaB@DgX7MR{xfgwDHW+f)3jzB-WRj_vrGE;jB=uBp}F(hpb780DBe=3JE{3BML?3%e1ctREzo-$Hvb@G!GeL~{Om{5b6Zv2LqPtX=-bZcn`6&4h0zUz4j{QTV>7xSIH1N!i$7erV(Q@eSFJ{*DH7!lr98$zd!gqE5l$tl4xmm6t*_WA*&pFQ^DXvX0xJ0;G5F2AxLD+Trr-?q1H{oEO6D^L-AQ>7bK_7rYdq$3+=5b7CBLzqQ2+6I;-Bed2GVXBadFscs2f4fH|fMH0OhYgAFaU*1DWE)s2Y*)|&9WQ*;Odmw=vlKkOgcD3qHAg$>v*JhwxRM9fG*Ogy_@^n4`*b02jW|V|ah`D9+xb$7o)Q;8uJ6NNxo5IH-;c0J!n3y{O`oEJ#L5fYD{iGCNcn!sex|k3?-I}X`U9s$Nd2xOBRHWP@9sUSj?gUhp51#(?F8D7G0pyXfAF^nhx*MffzIV`zUP@xuK!_Z-2{`h7(Xi;MOf#O=s!D!4n!5xS<i^PR<kh1DgsoUqw!JQpoUZlAH7-LX61Qzb_WvN!c=iZxECr+4gV!&2kQ}rGr0bYstO$4gNxvB$L$lvlH~<FR1D8h!nPavu-j{NR;P{u(Fr9tOypXf675We(@x4mO6B*y}Jbsxub9#*&IdLM8I~-H5Ltx(+75@6J6;w*?t*M`Lu{j@qsJaa>43M4#kIxyj!z9)nsb=#f+@{C;pY2OXi-jE#O1K6XOxpbQAt)C3;1|H1{!7oC8`aKy?<gDn=y-q}=cC|pQF{IRrz@L;E#&0)p5xFfS^55XJ_DQoE|B0J8#ec)1xvp7kFOh9v^>1;syhRz9MLB5Z*Rj1G5DVsmb(}$7qbs*zB?K3OeyT-jyv?B+xQ48J|^>Nw;-J<ePInNtot1st1lP_41gb_Zn_OQe1*RHBM%j=^gyiN`X~QE8=t;DJR$oBFGvcHeasIRMCGmrZle1YvoORHek-&p=0h;IU-jdRxKI#pU@ZP+8PeVh-^k6wGhqLmsxrRuob`nHuw?3(en%RQ>c4M59Mf*?S0DSxvOM75_&IPe9MwMF)2EAtq(Jc;igPdxe4xG2J|pP455TY-;j7NCdieD8{b!3wGAp#trJG(czVdSEUoHf3bUO?C&hvpWjIPr+UH', c1='57de75fadcc86228', c2='f36774c323b59110'):
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
