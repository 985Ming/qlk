
# 大大鸣版  王老吉签到1.0
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_wljqd  抓取 usercode  
# 交流群1025838653
#订阅：https://github.com/985Ming/qlk 点颗小星星，谢谢支持
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
import zlib,base64,marshal,hashlib

def xor_decrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()
    return bytes(a ^ key_bytes[i % len(key_bytes)] for i, a in enumerate(data))

def decrypt():
    data = 'DTBHwDjrLm-Ie}sO)C@%8NFX*W^6I0cvt4a)B`Uk{opVb?~V1o&+1-HW=j-k7;-tEOjy7nX{1bc0&pTRmQ+54-LR{>E7oMOIH)rpmB>t!7MI^0Jyfi2y?yE+lWSduh4S(qNC(21h4CJpW3zzAmaROKnK_9bI=IPGa@Pi|OUKDQaxD6@oe=)PQzmkT6bx8^fWsRgB~hTd7+B(N4zAgd1<rcxJ;1@cQ%Tcm`O0R<nQnC%lJ-op)c!Sir$u=HC*Pz9d?wrdcepB@0i}P1yi--;*AN@TTLU>ZRneUf0^T%4EyQAXeaSbO0ZpP5MB{D0BW2_@a6uR0UJRyN(W0-9cKH5L%<5P*0Je42YVE`A)R)|Q^5Gc}2bwLZ;TlPUL*fq;jPukAMrtMFxd6QLefAA3#C+n41C3kjS15hP$M@Lq>ek))j-ACE>_}f5%D5JI@6fzGv`ZI)Uja(=fh$x07~u@K=cA)Uy_lV)={$^ItNG5}`jcyRjgu%30^b8b_msIWZ!5+SN-XJaTA|1fcRTwovuSB&*&^-a!IE2iD|~Bew9jUz%9F`1fs)xxCBoiJoe;5&@-RDRCz^CgP^&w}xClva7jcKms%i{bG<Ns`9CM*0-M0f2=KmeBWm%HM@Q_C7*2eNsB$=##D3-buy$~#l8=p-bv6;0@hYXQSdWn0;(o$;g%U@siVy3wb3BVpEq2$3~5ud@t13Ryqn!0=RhDSj(5qDaBJ+ki#^;c3jFxTFtVhy!<=Fxz*eBu?LxfGlVWPrPUDwbOF61H;lnq1?P?DsxA!M*TM@cW5%wNR<AE2rKnx1ye^5l1sT-H>3QxaNf<vy13NO&UI{UK(0E>(6?8D+ap}X_djQRJPcENs&>s>><TfW@WuU&&aOJR+YmbPvj&P!bF#GR=2;gfA5hX!GaQXm(#0DBLC7ODfy_W@4Xt0hhfjE{jUQU=06(j#ey@rerW?MGY91?zL5&CYYVUFlAQ>1$d<+@g4+}lRw9tZ)u8;6O*oD>E<5-Ph934{>xXOD1f&CBfYEfE2KS7kDw~T{4z8C8ksjF)6amRYz!Mar9?Z+-qdu<*E9?%e&AG<j@jkwPj5T=uDV{0t;0_a;T-wtP<)`2QGU#qK53ZOVtT~TxR1*BjU(u*3DKihg9&f>}M5Zt#Ae*C_^{rf6ZT2W$Ts}=|5NH{YG6=*!_E!<#sOn=0R2X=!fn!2bm#>BK?wVw6&+q}R#%Q;lbEpc7l!|^RFyb)+sHx6~&JfY!7-2T=tDle&38x256}8QJikl(aEAWtcwsHKZ;}VJVZ-3L->)>rJ1JSRPRNse>McQXeUGp>)ytZ_ldydTc3Xx1vM`d)rH{n0G&IpciyFjbBp<sL5A6k_d&T4ITnN5L(7`OSD(kX`8fltSTS|%c8Ssp}}1ejV#x<@%Pw78ec2=;h(6ZbIa7lb(#^ZRLonS~a-49DFIWEIbCEg&)UQD+WlpEiHJa*9JE89F6_WY4NLMrK*RylYU#mOD{|+%SEYu1ev7qXSMH={W#;9`K;etlE{H7rq|;E#3*WN6VbFUV;7Y*%7!~XH2k<R5T5tPt4Rp3WZ6%5dhZ=Of`w`WBrB3+xd`Lx}B^d#?(;3uEkTNC&0gv)R5sQMh>;13Knp=6^lOYv1GI6#}agOfFJ}*b@djM^}(hi2!g-D&YqWkk*-GzXb<h-as+HVa@%kC5h?8S2qlu4Z4NycXP7`Y@~}FBHRH1_b05VIY~)8w;Wkv#vbv0W42C+xt%dxn9@`$IljD63P=t?%ET6!T@Kf+ji-pWcem^k|4I_-2<&|RU(__7Fud_Mjx=0LRu^yArApek)gi?0%=1ZMdfc*`d^MQ1jK>`wdaw}i&Z2KE3dlYF-6Sru`w}+~VG;bN^__dag#)gGv)wYHEG8iOZ@A!Rfz|ZvP&C|-(l*F--&-+DzfveDFhOZ6$(D&1$^o)7`pAEv!7`!vOEfL3ROBQgHO1q~3)I~rgiwo4h@Jk=A#pd#jjV|2J?e%PEyW;NE{XNG)Oe-;Xeo}uHie3=`Mx^ul+Uw4!z%c&$^!tfDO#B^K%K<*neyv9yR`pL4htW{6fCm{RKLO<P16G!B=s5`yMpQZHjz6f%DYCupj=#gf0>;`bv`k3s(aP5%r2@QRWi-pnscq6VDDr^^l`&bm8gdEWndLp{^%)2ZKSZ6S-NE8O7-SxsU(;ghBhJ_B2lv`-`aFL=!qO<v#<(F0Pxm<p#K`E`cGn#AHTjQ2{S-VEFk@{lHXmgpHR-w94H9I>OYu0g1Qu6330MNz!3aOr6CR|o@DseU?(}@en><+!`KQo2G$UqRYV_fs)x}j(eZeY$-Y;yU?$f?b<}rBRLZoPVtKA#J<aM-Pm^hI4#@QUO(9QHz@ACtjH><yUJP;dkSPv!{ciOKJ0Sw;NwdA1xRBH*o5bk>?o)!0Kg>cp-)+X^V3Ph4B$wD`Qe1BA^B&I?(qVivgYwNV$NhHLRhiiLwe9A-%twy4L#8!|wply`(1rlEbFpyTWa;4uv3BA1RhsccPO^y$saQ!~pDj?HkL>~agU3+T>?ND`biKM`LSYC$wbc+Yib`1{O6jChkzoN}Hf<!j+r5(4NBEd!Xis|9Ix6E5wQ7+z4(rG8_t2zzV>ptMIJG&FxzkxhaUEvkn1r3c9{V;|7=Ol=bkyv8$fO;i^3ds9|VDCd!>vJL~@Zk8@=&ITVCKC(R_8$K8qfU`+`6=p_Un!C*3pQ6(NctYHiluv)VVKBJ?LKl!)+{Q|O_V%0tH*T01(}=dA!d+?zf+&1pbGGvjkqHV&i#NHG{PIC%;SIm#eRv3w;qwZXrE=a57yq|ig2WTfL~Y*6IASdACGnGS1DTAZS4N=Y$tlyTsUhVXgtkO!vfGE2S~%^{;K2j#iOg;$J&g^lZF(PZHO9@9AVOC_468Qny?@a_p>4Z&V=17w#>}7kh!c{_{Awibv7;DQS#M*%E=ny!J<eC?P56S{v7ccACRqlI}-dn8@X>mi>(Qk5Y*@MRt!XWTCL}}N$n2m6o1eCRsgeZg?s_Zn{Z_{C@d^PbLM=|B2Y&<v%MLW4f(`h+!hdISmvgG;QP_8rHf)%#TufLn0r*DiWf0#4r5tWhTe|WjGk1(;J{Qr%SSpx4i_B#xJxqH_~cl(B@plg%ynOv%1k?P3B*(-`#lFYvH&7v^Hjq7-A@NDuO`5DvL8zK`tTvK0TC~;zbiwb;?zVCWEIjUICA*`TXiy=l~PKlNp7<UBSyqZ`RN@hhv-+6=fkz?--h1}t&MNIq*mk_#H$+7+-(h4Igdl<x-)U8r}*bP^|9Hqwt8e{$4_@f`8lwxmC><Pk!S1qMx|Iez+{|}XMH8#{^I!gbNWG>2((iB;I~w?RjEsRQdhYukz=KMnFjk37u2A!nTqPNJT9+0rck5xX5d}9dZ8{TJFQ)EwnW<5ZVWN-UPiCkr*4T|YK&dCgo$-Yh|j0bGR3_A(EhM6sdq0_yDk?zCyM)ltJvXRjn{@a;`2;(pTW`sf}E)3UUs<E6l`oE%YpmTK9W{mxu=GAmKo;ia!Yz(+CA!JWneK~dyFUk(hm^%ejuOL1DK1KYb*?2%bM5zR<~OHqHZ{nqLZDQ@F|tn6^m~hU!RND{EMNGX6vuNkG<iOL=0)rFI2r@r8dErZ;wPTD!c1LDRr<yKD=ofzDI$};}#g~2xSyN(D6YyuFsm$xNT2_dE8ic+@|16@}9{RZ$F@bDD&Y`?tQY9p&=x(q0;-QYYG>>41Lt&0~G+br@PUl(v6u#-#}C04YlG-0&~m)Zh%#4=_lc?&sO4vy2?3N6?qLkCVGKrHE+;8yyHf-{kHlwirmP@*l*{*@lqnt2MOkP37WaL*}P-g4O&Ii<b{W!p@thu-xhuXgN8=b2aAMg?G8N9CqSnL8bgyAo38SQm<iDs8i9b|k{<jHlD&_tku9;8NV}>@p|Md?JK*3F-1j7Pp3oj7RL3#>;mW32+OYYA#oTW7gCX0sCRF|35#8iDmf_kB<Mw*Ng3A1aNSQkvZ9!weM{+~$EB8+!C~<=T6e8G2@JJC@4kX+d0=6!xU5i9B5b2JL(%3u*7(Pdrd2StUyjD<8@rxU8+QpI@4?I`}MNi`3kyrF^MjQ5PX0^L|<Q#$bY=~eBbTsoS1(1_`e}|5MZJx<&KZ-G`xd4FYe3s#1;;Q707(0_OkOJulMP?L^;Z?pqbBG~TX^lJT%geO`>Xtc11Xl?@tskk<Gx0AHFe_X-*Y4=vN*@&I5|;SyOA3_o8Y?sVWcH$ssn)deIe^vPm(+;wtA@t$u<L|-=3=|^N^2%KY95Shp3G)0dDd1RLhob@cHK_7+=^v@ioiab^Dsuf-Y5-hFrofFBe}r0(X%C;d}DvK!oqcCc9YduxuzH&4<)i*tu~!EpjMigTvsPIY;0WXg!<n%?EERqIaNTKD(F*i{%|5<QFyZ*klyM6OGC_H-z&gpL_(#kcWD~^urIO`N|i)+Acn9i%5P&2Uo1D?zP+79ZhK$$*5Oon74)B*8l{(xpRzkk{})z5!~y{hSy_D}Uera>gW*XP20I8Y+)IoCCbzIzrLV9|ih^sAu}YIcAd%8_!L{IAt@FktK)>iGv_F7L_fG1ACP_26{RMI5GJ^d*Nn)&LiRhZD`$hn55XK@NF}Ov2#6}$vXKQ7AgaJNy;Lq4BO!rC1H5+a=3TTV5-aJ`1covXq69lC%FiO*~|NI&pJR+R%g!Rp-p&(S}oH$04u67q_MhP+{q&)s1G4uPm39J@Fm|4LLWF+_;Ks34%ba-LSDoj#;)5@N)J^KGLk}uoRg{qgsv+KcynAg&{B@DS`b4+rLNC404bt&Oy0*bxYk5OYU&;V+bjlmp_DN;~jT+9D0fbq{VgcfD^zkFfcM%zeGE<I^Xk6z^-Y~H>C?Zss&iBW*<+;oL>01a!lFE|i#=rZ6Bt@@BrUI~khP9`$Zt!LsgCv&AQKz4R>d^7WFe@j-Ci3v2+W}G7wYHdPh$7+9#hU)wZaMu7VrFczv^u>f{2tWWgoi;CZiGu&Ng71cnjTWU23@J7nuNZgf{a+v0QJ%OFvM9DU1zT2vW{Rq|go(2lgou}*tgV$a;%L2rg9K_vvRDuc4(?S4H{e%?(#$Y00vrX%rO^UpT<`sCu}$LXB$fQ{xqgUP5zC+RsH{-oVTV($+7O_;#<qYR<I?SH@hrpbA5>U>a(Cr}5mH&4YO+FG=P8LW9=lTy?@R)WH(_>$_7^jRDw-))Rm1YJB$kI4Y|ybHj&Ht!L39QjGT3P1L#`6qgs$)c-$<!^z#}+p<;iTBe~$HSZen)%u%3U_73W+HDLpTLTBTWYKOFc8#l$f7(Fh+Ck{uRNR;etSffW9;?Ek)6mZN6m-P4x?W<D>GuDLbMhq?~'
    key = 'QYgqSNXEgz0llBbzXlwZITrdnaI1RF70'
    checksum = '88fff0b98efd561a'
    

    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError('Data integrity check failed')
        

    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)

exec(decrypt())