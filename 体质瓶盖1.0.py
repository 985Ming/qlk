

# 大大鸣版 体制能量 一天5次 两次算到账
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_tznlmz  抓取 ck WXlogin=oK6LwjplxxxxxxxxxxxxxxxACljzGM  只要=号右边的值就行
# dadaming_tznlmz  自行获取 瓶盖码  有便宜的可以联系大大鸣
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

def custom_decode(data, salt='TX3fvLa8VSyvfnby', magic=1970):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='e&l+Rh3fvYedH>q2mR5OwH?&%F_^b2x;Id1Dr1*DFO+9Mx)5AvSR^O-Pw`&OPMe2ZdJs5t8ZK1B+GVdx3#J8~CFT`Zm?v5mb1KLhgZ}FyT(*;I3W9V7BqSNNLSNichOOqFNiH3<ey02P^?I}9VF9n{`T5Wj72iQB;DU7rX6It$y8_Q7yqs#u<)0L+KkeOt(oiVv3bhiQ|ES}FA;^nKhx7*5tQQF)#RrMhrtin*==SF(`=_vK15DvJXFYwnN3v*VycDwiwF%FK&H4F%wj%&vM_1qWp#h@(`Sowt&E%{e3Qfosi3YGQ2YbyZhXfQC)1H#^<%L$1A+gbE{l}yJx8D)$_s4|Ih5aEG{_ZL*5+Mw5U4`T7psh0b`Wu5MSsvk@@vFQW1kqCE?nJ2Q*Io08Vrk(9^XUfLQ$gw@3J00774KsWv)lt!S5)rL2VPTZ14xC}MefXnhJzmZcG~@db!cHDrtyELfm;fs{Smp5k=0g_V7iT3h4=JNw;tg#%InQ>)<+SyUk#oSM(<C$5{byv9b^qW`!nVX&nS=9uK;Eg{uK~eNAawns2>T!Rf*mV5z!(k8Y3d7R33CHZM)QzB%9pf{sc)O76tRY1(@LkU$L_3dh_15i(icp(E&u)Eu4|#?gG%$g%$b6{pjYC8<V)zLr{8UM)O1Hz5T`2t>}=~^_5x&na0tIex6iTBoJBIBb3442R)veSBKvWKOK<G!(=Gy#~#%J1oBX~UVR74Ph?3T*L)HdH3y9MCe704000DU+6N;gr~2NX>J4)9=G;mI^0z?_+gUQeCHmo{r*wKEqx;7x_yEV_+p&@8p>C%q-Cux>MM-@3r}rXVMBDn)ml5`oIf!D(p~d)T1^vLs2?zry!tP`ir1}FjFyt!dF%SU|_w__d7li=l`AD{B6=J6bvF)sPy7Aa@-(0G1=9}A!1l(YEw0n@*2VFfEkM;AmMMqXUp3ZrO4O=g?6rD)8-ElL7rR2?@C6;){b9sfcsX<zTKtBE+p4@~gcK2>z%;tmoJ>KKGPy>-(G81TS&Xm9$`#kkkINk}ssgJSwGbv5|jA-Itq<=H}y+K(dpC`B1Vx^qB#5L68=o2>#yge)N{j8DF<=2*}S&FG2M1vDNPE;-wUr)rm#Ugc|IbVTBwpXGCTxm4fN19W@6+u;s=E-!+G+@o}jL9b(h?%^CbeF`n^>e>Xm}^F!zxQo+_Tow^hkuBMtc4gFHJvuh%<p0HuU?&6Luu$oju)#Np$B*myS5pIC?%eH3xyVeOElN2+h{;Bx;WDvQI#@%!e3c#j~to#m0Pf|tvwi03gf>D;rKGAyG}Fjh+rSVIhFJuuV~A$Ma}5`&&I7y1@GAq&hCXr1IrAwmS)ZDh7yI-j6*Cud9_ErE+hKxRqrQWVn~UX#G*!mM!|-=L?rMcTba$<H>(Ns3s$S3lRSeVoWewv6}g^BROZ*<P$BZXLK_P{(6Z5QjUHWp94{twU1zsyp~$N&H8)YCbyONYWswCEw9dGeRAqty;{bTTwdpB9gh?1!Vfflit2I9bfZf4yx9we$6ZDZEX;_3Gy9ET6&MC)h6$4k-<BG7<N^|L8D=p}aoR6<P#NrS}&FPs%L#j5X+Ye<e(CTzwn!`5)tZ&FxDd!Kr8!$zwZQv<+bn)L6B6TIXM+_U3gi5!G)ari7iowGJj&_75cOZ6NfCzHM;`j%;4}-{499}#qrL%7vK=I+xSSU5LDn#^-ZP@HHkj5Ig5}RaAT65N~3XX|4ND@|x8LX$F(tdYwZiew+Nv)hLzddi5+<k|_1<bIC5+@l3#=)O80lqLoEbDscc9h(Ed7Hbfa}IY0&hyQ*t>@9o=jX!XV7eJZMk#l@J-~uOzi6>7Vp7Fax`I{E9j@CS-0AzqQEOST`JQS`cmBCDluiD+wUk)T?*`u(v&urded<fxWj5lKBb8mN{}edzQTp+g>arPeBnzi*e@8XFTYRfp=_Sk%1A2SilF)G5ahED<Ea{(MN9`1oRrGUZggzaSjjw$n+(m`uF5|~ScXJSu!N9@)|0LA_c$K3_k!cAe!9tj$^F9HZ+VYdn`-3LA=ZQ3WLavYfE@<;zn6&+z-Le<=bKL2OqcS?h&-;Tk3&uIxC)*OOrBEd#Lb&v6dXx=??Z+TSo1-o(<sfy$=6UyaOp%%eZsyA(v~P<R(M3gEGu^s8C0K1}9;k~cq>lGd^q?cYeBe*zgovz<StM9$fq9=XQ`sH{VvkV9?(w9}%9RDCAMYqV;!Qp8JJ>YRwV_x*J}&K|T~9mt7SBt6Mr`9|lTb8S%_9MMjz^nId<k+G`l!?2>sh{|3+x>fNM$04%-D-x5>Vh+09rA=9}7S959)i@AfTTadl`H{eA-C-)2T?_-o2yHzk5(PPh20<YrcbvuW&_A=Js5VuQ#{cJ2$$(V{kv0^O{?MV}c?R?l%v0aq|!VFZrf{d!M%P_ZyTzeesdV^e=Yk{mlTQKxjECwYqNk^on6b#_}(9&ecMAv;fW%x3%*DX7OpA62GpBzw=q^6uRxuAr<bJNkQBFb;G?g<$J&dHzbkOCz84ZA=3CnSA3a}>}mW&2p3Zdq*6BvyPzMhiDh<EwSC#b6GFi~n9_B{sWgQ+SPf*GJnAS}|3E0TuVe`^5p%l$^6Qi*L_B&~Lkl;gWk>n_h^lxMy`e>0CX}aQHl)`Ab##6L)z4e6phLYdU*E92=8;MdNxtGmI6bSY7Yk4ykehs<Q|D9RKrB0XC^!Ow`1Z}S*}e=eV-&ySET2gdHi<%;&cjqb<f+k(abHJG2`frzF<XHnfw8R0<F8%EWm?mdaF{T_DhyVP+TYjGIO&8&PeZUuQ@Q&SDZq%U!%M}1zFuU<@@8b1R4ik94ck+b<e67wATB)?U<+K`Nr<*e(LbcM>E!=fBigTMJCvZ~V2_`E?lt>9u({>w5vm+_hE;1i<}#oT=sXiQ)Aeb|vtEt@9VeX~r#FgYdBz7JP2cyoU)iLOzcnFa?T@e~rqT_`XtAuLxstQ}1lNK^Hm!D#E&NEgHu!ybWhZKIm%{w4EiG+e!_iAC^f-nE*BP?wb9rnuIW|KwBRm*INsu%TMA$|Z{vvbr_D}!(roHLQB$`d*@V`=$Hw;Pmnsfm0u{}wI8u}k)UT*3Dbkal9#7&-*zd+4eXvxnlEIjA7g2~odj*_^#Np?UK=i!jmNV~kj%ry&Nm!Vf`d3o*@eNUZ8lldy~8QT_r-=~;q>RfmCE$!#qUEj|v%(C#9aEfas8fMam<d%#@AqBTek~fRgO7j&0ib{2_Pl3<%6Dm%~>TudCTv?dlE!2WLZP&3ph~(w<LF?$~>8drsb}esMS?u$|3UmQXSDl>l{JNmlls7`iUqJbod#*;ChEsoVx$L{xdGE!<cQm(Sdl=hfS#;P~7g%NdlF|n*OURWVZDjMxflI<)wKDe<U*J&wwFQZz$mxY)S$nPn#aFZ%Sc6Xm8&ZX*oy7srKQh3=4qpk6goHQ7%WlkpIFB3SLd2@l>X1I`4+f8K8398~E0g@>d*jP9+X8X0y>4)H^kd77MeT$-2&lVUpqJ}{|FAusX@TOSxvg4VA8WRpATb^^L@T^4DqCtqe{qd)uF*F(^}{|J!+`Mrf7WnE?K*Lz6>%$E;gaRdTy^@uw!K`hPPrNCB63b5zTKlfpbF8-1S5hs(RGqKz^e2J;6kpq1&`vlmR{ta9f?TC^CNsps6sT)P};S=ad5ZbnXhq7-lFhT&9~uw>)&deKzkff>xDg^$T4T!_^kpVHrPFGBGxN+m`2*@?RRclb>mhG^lLjQ#xBBs@m-#bv;2}x_8hy@VfR~NaQ~o)gCTAq>dX#Y0+|5Hd&7jqX9hoX&wvjenQSCQo4whrQsJDHDaxBwgWLocE_s2o&xZf4_O(@Z84c?Br^On+;P(0EvcMdtNw$Uj1U4@R2jg8qb}4nk{=!C%UZBga{0~s!%RpW;GT!ENhECUYIYoe8c9~#YU_{t&cr{#Qz`7lQKaxLim)kBf#dJ%#;-jX;12bNa0&)1FDSG|KjlvT>Kje+bQ|ab$-tt9Tp5KQ#H%{xv4Tp{Z!dD8Be3z<AKzNjpJqd+}ONS#aG;nJ8*XzaI;JhcS?f=GU4PH7Lsg*SeUoxgwP0~3I$}SIapg%t*`y)m-2iG+Wvi!Q;qH<{oqd}_LeJiGBVTO0T`737%c|+D6yMsl&Xd;2}?}F(rQj}i0w6*zDH_mZ(T7mCkMBK(w#d0-oNNk;S3G;^}v>}e%?Zy7F<CYZQQg2N;h+SShMb3rdpe0+kX*hF&p3*B9TbmRe@_Pnr|82}<8y|mH1F3K1Ns};)w;OnWl`(A<hHVLXR{nmZzwu6KACf_IlP3G*FkH!EY=A0Q-3RbsW!f$p?an2Aw#uRFEGhuc0r^cpo$=D5UrML_b)|M(GVPI#f)0}n*^eoBO-{S+>uoBV?BPN;Q<hwb<kK4bLP%7W1uSsjxM!RCiqK($StyD~$h8=%IUc?VE%?IuywhvLzAdlG*ny^?Lg%B-i?Sc_H%d2UBUH`5L0p@{Is03cB!14roM4U~h-mD3?$rfgyw*)kq^~PWvA9t+ujU-F3}usVNA3KBqp!K~%`|gZE@!^@hGb|idBDKX4zJg_q)C_g#?(Pq&`S9wlDxCv0$ln6L%WDj*lF`=!OToO&YNv@$@FWq@R_$1_*U}f+>Rh}HzS!$F0Myq`1t2ni(*DoPQs0UJl<{ej!fLfS3Pnw#d~E;>y1n+!HlMP%AT)6P;BP(TU7eL%M(@AZu5HjiSskaXiGRSK8u=!jO>yi2g{DF%R9PX4zt1Apu*nuW!A%w;nwL|uehkgZ$}RN&B+6NBw^R08T>OFO){%C&9O11s%P?%FHv~QpYi)&o|$KnItLR`EtG=X#%sbEnM=ZD(c*`}tr|g7-{x9px7Nw0d+w3)d-IzIOLn(j+Nw!7X4)H<B#jLVcZF9b5y!1}iF!`SGt9->F>z0{hmp&6P(6iRHufcaK)(vU=Ek9gVgh^h#$%rRSae2o(WF`zc+Pmvi@`=@3pXhDSy)b;q?sNPwQn?R_`>T6;dZgJ^TBP04s<o~sgGX6{gk{8>7FBbRPh<d586HpbgD+@%ZB}Q-nAyncERk^>;BJ(agAHW@VMhTUOv1+mq$+0s=)W&Jx|GYH=3H+F(#z7hAO_ft^7U?*~$Tf#yexu;_`M=ZF9&4Y*$QzoN$ot${FEAVS@vSN&9d0;{^`30H2D6Q^HEgM(=o4U7@&|P<^sg&P}1F_rhet%6f{=se!L($tXWHBx`6gXQ_!eW#w;^`>>C%|8O9YMWwhS*+<6_5jrISuDy*Pvk7q5)jVxsutp02yp1xFm`;x(w4LVrD?oLl_HRv1SaU@Ojrx(I-fO+6rI<hc1{W)bU#OWI%uH$-HfbBi#hxW?R$(?gLQogp$y`QTp3rsA9@i&@2{WFfh9bj7&5Eq-J_7x4;O7XJHCEfajQbRB<F~AdP8I4ctS_n8$Yz|`Y>2Lby`XV+LXC7d-X(9Q3FCm+mWOx=Or25}MD>kC`Ayei!=b;tmD&es`#xWjy3=8yvOZ)8ARl}k7lvW=6)l6eB7o35)ZQU>J*nI~)y4ar%<nR~ct@!1yb^OBNqDV!0EW~FgWkj+{z#!b8<M%3cK>Up*>z0D)ljTeYbFnKpCUVYuMjmVcgQTIrvC_Cc2z1Ik!4imxI?+5_E|}`7`3jgEAR=Xm41mOxsdfXB68Y$hu?ZYU|h-_qa?u6kILO>d|Hil+6&~)``}%Dx2|u$YM`q6<WqL;A+ZYK7K7u{6Y-j!b~uWo4|3qD>@{UyQrp^u<8sQumTu(RTLjn$P%C#vvti+*!)bYqOu~GM4Vj8oGwaukqH_1WGK~)IOb;Owg;rL0fr)CCx{G*(F!aQX=c;1I%~~2okIU2q9HjuYR|>A0oVow3M(9Opa;+BDfvyGT3T%QBZgo5&bZ(F*zCb7p+mavIKSCv`^+EBk^+K7Ta~gjZ*iK$TS>@9?Qb)vX4$Jw-?yLvT49M5Ja3Oc2q_=XT!R9*KjqN@po)>vXLlT%nf2jZU^l($vi(e@GZ4k3aQ#s=k`LugcD&zJpEc|Sf1P?L)ZsrThYy+PiIX|UCVRHI}NJOUv<|Z;lXlJT4M|$#C;DCuWs+V99aV}+nl#KIu3~dT~hG7Z9QMt7m4SYbc-qMn9M>(2}OXjaVd4$SJ#y?~L2M)<F=3X*|=c;bmdCu-^fmP>S;6=zIp7W)z#jS@eba!~H?$;+xo6Jw7JDrY9#6xJ_#C4!{TL73ZEwvw#gql{81U<o3@9w76KHDu(TK@MHAr@D4V$EIQ2;;C7d}}elm_b$Hydp{!SZ2K^0>XQ<?_i#o-C4~Hq|UO?WAB)j;&IXlb!0%5!857Ik)9KN6A_HX<otXPBpUq8uc16a)zyAqZ<Qzb7b)4DT+Y<uO+bqRC2nzWH_Ysy47P{3?CZR7$#Od3wH5-EWncb|bJLEMm;JJE8>feQ5ubpbmbFDH3_W7c<~DueK46xMx6GG712nGoaAJxqS3aToH;fC?u%#r_)!@xb#Q-*Aa-;SgjE}9y)-x74vjLy6YF+7_eh0?J<@)Cr0C%+zV!QMFGzi{J?6YNKp(l`<ZCh)W(RGSW(7=(9MmZC)by?-KMjZ6J(c>aKRx7olGus=)im{a_YTG@neuM95LAJKBwY|H2=4zp~QesgBuNvD=S=>iO5Sr)+t5HN_eSpW?m88PJSo85_rEo>~FAbl8FujJ+c@}qcPE)6rAUhUwE(zjeYhRbIlgnR7%rKEE!5+>4`E-Ab2{FeSSL=SyW)Ya-)t9}((VG7+S0<3&{Q<kykpdmsS52P6fFpE_7y3O2^!H2cMU0`v)aWM^G*_0T)UUGQ(XJ+X25#wDfjr@Wr)*xOIrG-@9kXOx_y4w;r>5MoO{p$0e%qz2+Vm>7ysjARk*aKvH{gEyJ{Oxdy61qxWLF@-69@3yS&S)>&}d9E#RYT<Ez!dk2x?BernJ4Rb($c)OxP1hPVJX-Y~rJ>s+4TDy{mUO2Mw`B4Ah9!g&DUrkr~$Y5xXkSDB=@y%Gms`<z2YKx^VLI{G>&`5$yNUgrwG+K7POuOKmuK9nyQiK>hnbIffxK`?d*ZI?I6^rz7Csvo(&FWx!Tc&j3w@IX=8Rd*|Rs7$i$S0P~dC22~m~sdk$46I+L&-}08Od&m#O{EvQo;o#d51U?CzD!cWv+4&&GauKqSn~bNS#idcti~9$M`Fc;rh9R4$-{*z+)4j?09I#WxfU&ziglh>|UKKej82i>v?nK(OV#ERKM)0pjH16<{3lJ-XRgvvUpE$Qj)7RP3MWZr{5+_S_C0#KFcb&QblSABolc31|*wc5?!s63op`Y)o@nBU0)xoe5(*5#3TyVy%o>W@y5rEs^0VT6#{OpN2%A9#a`TGF<BkovrGrg_0;;>`rindK)Zj4pu-PU(1H_y)#yn=$BrdZf|4SrzH8^8Op%e{OFV1_-cG9=#vO1#`e`Sqr7$KAr!6mAAT>p$0f2C8EKHKSLX#87{!!Hs?!b@9VGF<m`PU(a+ZR<smNG<3^HIWIysoUGjCI6~9zosOg|=<&u$ei=5nKEtrP2tyd-P!={zn{ViqlUe1B=GGy*p_d_QR)6qVmsGNy#a}|p4Te^KxxfkTp_;p`e-~x-$Yj`#N|dfElS^iS8Ac>_TP?N+BCmcy61%m7vcA^k7TLU&H@<#2Z#%_NjQ#k1^mg=fQ4vm5hNj72rx$r?tv{5X+^uM!%ke$4;c9?@(f6=`^_E~S7g3FTW}NKb-sAPya?$U7k?{nSu<W9CE`iSe3Ad+IG%?Ijo8pfBPl2LPMQ6}bN^Z#xEvN)@jrckBWA42u#dQdV{8<p&Evd-a5~Rp4291|L>*pX65k1-|F<`?0;M$j_aa1s4IdD~v^NC&?7rONHtqy$U!4k!I3-T(Y=dQW!qCc_@&t;3qhpH(Ye!iVG;fP7|Hh)|Y6Fg{059QqOv<uL|TCpe?V6$yF!k2t*3Y1(99xu=EK12eKI|sK@A;KI#{0!dcSzKVTIl=oIih#)G!Oho|f~?1VKI&qwliD)*S>jc%ozdvS<S(OJD%Zkhe8N?}+`56riaY1xiBR%%n3?U)Guzx^OeH+IcJ&4qLVRnJgc0BEWFlAs!+L)F#OzP5)!TvALge=?(d;oZa)7n|;wzdByR!Y2`sK&iYjA|s@Pom`^l7Yx@`jgG-w*tF(ZZnB!fCA(LB=8I5S#X&Awh>ERXZL%k_Mj(=)m-n%i0@7=aoH*KZXT8BFX#agv4(hW^>1pisDL4S$jub>v7FQorn}1q<=_X0b&ovpH=i*WpDF191ldK>^9f&aF$$WXg6-&_O49GJbelDp!LIJ(7W!7f$EC$vd+^&n95UR3pU9UXz{{HmCph}lQja5k+$@IEawZxQLGEgzkzRr-q8g-M_!QjPN*SfQ~r^Jnf$~6V7`?lW_XdEY`=-Kw3v7UoJm-A#SU-!kR$nlEjR(vH$Rn8b-#1Ga`%jY99*m^@wa!@=66rhf9!hlxt$X|(U@Hj09C0@`3ziN`Asby{9Wi?L~bsab?*pr!*J*`wxiMaDQv+dvh;g&kvC9s$&0%gt@*ux*5a+_Eb;GpX){ooXG`;1OueH*y;uS4(nyws&Vyah{QM+ZJlBkeEo$+fPAGQdt@2|@kYt9TK85;$LOP03O429XSYbeSD7+Vp3Zz27k??hOjc#eQ;f+ykJhas7X)3EAOTIW#7_rpx4GqrsV$9$I+sYjUfHmuQtDFN4q&4t{xSEr-1g!W`li%0%zO+L>|C_efu}r1#uFSnbE@DN{;<3xM7(#j&?>uLz%UEvJpnu7p6Zy?n{iWcQr*A15ZDqL<A$l=Eu+ynJbnT~TKkRSiTf)Y}=Kd41Q4BvDf(Y<Dd?h5Nuw5y60Y)&85`b(sQ4i>d4ke{mO$Bo%lT_thjw97p!ACT99^(OM@T4m#Kc|$Q-Xe@6+)iOYJv$MWe1E=RP@PdEM^Iiw=cwLOCKKMZ%4%ci%Db^B=lUibk#STafERMfb$y7qShezBWz`;ux=PSoVs}v2TC4*k$gtnlv!tOdueg?vo0E*4$cF~RY|rbZk~^qJu8b3rjK^#8C{Xd9fVMe+BRmw&(tQ7IdVYq2wVAZc+K3f~<_eTy@ZZd0;=SEsk<fhhe`;vlDvRn6z*saZZjJeK-oV(Ku}G3Lje5X&m}gkjpmtKy%&r;sU}nT|nzf%|?gj^cwC=OV?;gmCsP<QB9~nRfk>u7|j?sk}mzCICMYOoo8)JYbt@CbA`>*nQeB*<p-XLk)B*9LP11sOe($47iTER?|{Mg{&u|fgXX!IqA*_^}zs=De$wUhBG^-%>VaK3131FUz=e^;~Udwi<3ofmnro;aM;JbnX({OSzHko`j}7ATy{cn!R99%KQB!QURunHF7-`4~d>d<GV=$PE6+K(VY-LH(`q$b|D3M**L&Q*_GK9&ehE@>_8W7HU`8$%dL%Xu3VqX-tdy>z5eq(`UF<w5n0Rd~{258L6ua$#<XYY3bMn<wXcq2Gf3Hv!+#IqhGV@v5cWfZO~{thokNU9wosque%J7Gt`<Qfinp$tk<5SX+@gm;H+?m1i{3)^H1D#y2n7Ki)UK@6(4ca-Dd<d@}4m1pO0jojI>M9ot9iZz|`u3O+}U5Q{K4}j_Mp*IVA!wa;ebdDnQ;wf+05#C6U>bD@sO#(zyJLu-n#Qe+`mvpQP}_YAzGE35G&9tDXPl8vww{)c5FjZ(>Ds8a{(c?d6{D0GL#z6kc)f--D3le_N~GoB|8Sapdkd)mgW9W6Lf_Z&X5EjVu&1jwK}oGZjI+hgerdCf<YLHaEirbR1_Lo&aqnzRyEL&a))4*huZqdv<cSwZU!T12B{XB2uA~uYctYJbU*zj?b$zmL8KL|EUPPG-j+>bzxMCo?D7}T~&b6n_Xr#DjA_Rqj)EN*$1aaY2UTK5b(jxYI3|UV&nDjX}s(tz@_>=1JgkVPqdUeW2&N!c7+=EXv(e6Or~($!hQrs8u&>F>N1YLj@boo<Q!p^eS)(k%hs}m_l5OJaukvC4&1eKm$Ay&qY6Kgky6&ILNxzXYp@=yUHey3xXhub^)|NksTj<gTstK7VZ%$n{roN(Q`s;AmcROgSiiQ}Q{Pgq&~9V^VeXiqm2LRnJJa7JvyjyP4oCFMQrz30XYiDDv^8Tv*lJxiRr_u$o;<sbD7qg-W8B|$cm3SKsPfT^9r+7g+C1_qKcNx!e%Y2JQf0=Hzr{s}|I3DLh8aBquyaEXI;-JfIxL_M4S34jjXMjT;<H#<RX2F9EDB1$e2+u9({2|X=41OqZgC*T)nVSW{7i+NjyJ9n?~dLK)D;0#JSc1_SW-PiddYmzq<q2B{g!$~yD*464pAC+rT0#L`KzgW=B~F+{T5bZd}c@FQj1xDu#fTUMVV0Cuv_(weaMZhFqD5{X_n`<E-92dnXz=-)|r&N?u<~k$Bi=e5@q!0ByiW;<yunnQxOj^ukFsp5!5eM&B0@tGGPKkZ8*smmSOIjxrDm~QXOnk1Gz~`L9s|q;%rEjy_7K-0dq36NP?KXj>J6_Zki#nhK-FJZr6?9>Gxf0<pZle?J*T$nsHaB%Vm;n&nlw?+*k6*QPoSbJYr(tM|XAF7BE*hwNMkbsEF%V{>J$QFk+tT{Cy{Y8f^i+G+3XFI~=4i!z6DFBIDeYgK3y&w1jyG7>8f!MH*~s>M3mBbS`1@aP<+p)=_i@^U%ropDs4e5;|{LY;mQ(6lsp8cGF4;$^TBo<w9HuF6#e;h<ymV<LTz7+R9rX8Py_2b<IskM%ICIg%h33U;sB~r|aO=oqvM??gHT^jh}zxi`;IIKV*be=h}H$7111bMX1TC>_M6n)tQsbB%u8g4k;ccw=@b)-re7rf&CAZQ{TQ>qoK&(R6O$Md|uQ!_<RP4#abY15*@RU(Z}BSMS_;u#8T3uuR+WI<%Zh7)NK;!HTW(G`5m**2uPE+Ow`cmaaV{MX&dyISm)d}4AHs?$9*LNaGnKJ0U<;c)lICa0Dl+z-XD-E?~Rm~Bm6Mu!=P#e6rl%l)Nz#i$GxHHzuXEU3-|LS@;~7bllB_P0LEgc2(9Ca?FrFuCi;lakF-{266JFw=eb9>C1CX3XE7%jo8njR%?aHLw>%8!H-aH~3KOHfr9fm18Lg68`Yc*!6Bx^B1p=H_4SfgOHw65bmLKcsu87^Iro9iRX8;%L5C=2yg#r&2R%Jrx9rR)bLLdK{&oNZt*Sa`ad)o=*R6Nn5<@$nFms~)(Q}SwL)q{`H_32?)U|H~?pQ*y3uYwMH{%IuOw_Q;wM+73zhaLnf?FiPxKh5>sf17Hil6#U${!`vRv7M)B7Xk}Ewm-3omg!xRrtRiIr;}+#74G;3nd#mV-@Osj!{lb*7dsXwDgO', c1='dcdcee39bd412cd0', c2='a34af47b30244144'):
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
