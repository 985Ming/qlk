# 大大鸣版 优培 积分+抽奖
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_yp  抓取 userid  dadaming_pg  自行获取 瓶盖码  
# 多账号 使用#   例如：账号1#账号2
#多瓶盖换行即可
#停留时间10s，黑了就别玩了
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

def custom_decode(data, salt='iumsyEpSnbfRUizE', magic=5108):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data=')kF5+$OTUy*ECs0FqZ|fD?OJ{5xUo_^V)u(Os5j3E$$n)gv%b71e)Wnj!u-y@3E_kvceuL2JZZm*<HLDy=9qfhg_wlJ`HZJC|IUom8tE9ok;|CEAiXri9Qu0oP02YD5B>%6l{?_r^xH1OdcvUGC0*bFicKmLYzA1K^%Ncv+}_tQngH>M^l^lKv+Lnv^9q;u+s*DoBWo@GB6YlH_WqURi*Fk=sR8rOV>3{L@Yhl5ztsTbW*MN8voDc#`7VuOEuo*Mq07j+Gx3W$|_<Qv`b0lBL^w&s$x$*4R+qg*bwZ+$W%uLMqg9{?4w_t_0`HPhgT>koJB6x0u;069i<oqz*nP@AvR!gVNO(}y%g6CClFb}n`y)rQHawp4YjehfLv6xTw`ly>9it(KT}xg913a2DOjLk!rtrh)fH2lHa;=b_)0F$B=DQYda8I*ClfL7RQR_MhPU9xSzpY>^gK<&R9L>^x5?n1*YY8q^7NgU8)GI~2^>BFn}t>=206-ZGG;rKiT5A=&X=pJB)louLBIEt8`UOm!7G`%_3$anTwd6o?66lcNa1ngG)@f`{MBEPUA*(gl2j`!7%e?ET)|nk@(?3h-APA2H0)8Blj2xk^gu)?sZFVyoD+gBTQa=IWGD?SIHt!Jo*?}t<k}I24HJWf`qEBZy)JCVh$vu3ip5%f5zTlYg7$Td4A<XbPt*ehVSPzOI^?Z2O@3M$e3u}yS`|}8M!0Pr)M!jr%V@&}N)i(oSeM;*MdeZ-(74##_%-L!5FC2iLsmRbD|SO~**&!@8dh8uF2X(Kic<q7UrBpB^uT8_0O-F-r?`Sf9T5qQMbRa-h|b_kD=-<;R64PHNI1zb;NY>PYWQh4Tjy05gg)!W8i>FoWdsw0o0ZUo$D}=wbGY#4x(IhZJw*;d6H`|LT$+XjBmSd5ILkz8aEhU)PcPH0yz&;`E0G-9uv#c}gX_u!3;NOaPWA3XVat9(d)UmpnxeuJb-^du;-LT&mX`IFHukoefUf_EgrnhnkPfKg8ncFT_Ij~8kVpWD$-k41e!({#i+g@;9IFNy7}0Cej>0Oxv_A<d2?N-KtB$iP$JCXY&_(uiPpL`O@u7@Gox8jQ3S7L(<7PDPhlCN2#?gumeu9snu{4{ojAGi++^l_AbnlF7XN*{Z&;j2TK@-K-pUjNA>zBs@r)X{7$BBJ#7zmQ|;g`YBwTNWvd(XjZHUAp4hJ=cBjaw_ao$qugw9(4o+bBYF+f{{0$Kr+2XeVW*Y5$QX?*i_xd(o~Xfn||~=<5!N83koxW{OwuWw?TS6sn~5cT;tA3C_QSgo~P}CTQ}^AL+GCbxMjX_eD`+!=jUgeXTb8dPOFT#C#C#q^16xb_ybkQxc-Dt~w@Od{`5s!H!FxhK20l>eoJc?|voW)-<q+Ql>#9_(!I6=jXhv_=zx;5qU&O>fWf+k;bN&?BpJ3$QCzT+~rF)qGjUg$9NYo+F$w-bK{)_r%DSO0CpTQ5ood}I;Q=Ka>0aP(i_K$V9`o(BOt^KN(wxh)dD=hX=M=X2Ib43RE{ELH(ov5)=$lWY9G~B+PQ?$yBLze(zL}B>T@oSP6!yz2D}KlL-O~0WoO~bvokE9BW@45tc8(s@kLA+0|@dk6Qpmf<0cX1n91DGjBy>owVk&>XEZSgL4}Qg#NjZWk2a<k5M~SNX9_aW&A^Yfr1<isqWxsvF+($`NgV!SnlHxy)?qX(^$I6T6)}@jld+IZQG6gFY<j+^XMD2C+e7t{$^kInGq)-kcMcH9c0<Av`ie~(4A;2hvFq2TAb@kx55+x4z6YGKamwhu@ltMK^!X-a_*a*k93j(ojt9i>H+tyQ#E2c;nw_Ixl4KQUfL0BqJ92Lh(%*D#{bahn_EoExZODY*aw;5~yCHkMaFRQzI84s^^_Lds1l<)KF&PIQ2EZr7{R@2DeH#4oEgOjYWj7qqR=)nNd1`-m92+qB)admYh8BN6g36#m!FJg2|N5F!ucIvgfh&BY-<MG7E50DR;>Yy9Yc$b|nHf<3pGMMoW%AW=l(mvHd-AxsXVK@r;9`OsB^eRj)KsFHIu{V3R<_oJ_l2$I+d8Fc8TF6&@Z#Qkc$N8}iNz%=n!rB&9L4elXvtL<E?Od#XL`xYrt@YQY4gEqSJ-M#$1I&2tdrZX0}%JG4Z)ftZ!aZ$OtJ4psqJjA3kmfw8mzSTBIa-JBzgICz<-l}I=Qp&R(pmQdE1diN!a(I0cGyqsV-dytQ_;RfyDZ@W7FjGp+53s_U%GE(9Hl4qC`_B^zvI_v{(NwzLTsFyr6_m*0F$MY`CY+5-dq7SQ1C5y|wXUiz7fmUW~0v4K^r^vjd2mLD$(1h)&u7eNFWj54M`WiQ!IXvgP=3?^xQWq(aoM@prfW4jYF3ev5$<UJ@fRumWLl1Yi`giXzPX34a5G2T#P^U(MEQF^}E&4SvI^joRql75-W&`P6TAe7itL-By2v$kBAA<nF@p3y(9>%619~_YEO09L=&)7e+jNUq<hiB-}TAuf0t-8TR~#2edAH*KxriHR^WoQc^lPF>@<b*#TF(A<-LvfAplom|}r(k_Cf)4{|wUA)w^y$PFyqEOaIN&VU#A6Mmd~LY@WzcknF5&hwnP-naTjej36?)f~~WX5HN0t({S3qsNSqJ9{TH^X4s@w6_1rM{niWNhgN5!bGr$F%{vJ;rsZ_5BIdy+JZ7J_4NdG`%870Koe(f*xqJ#?8w}l2)dDbIE}c~41x`NfXQQs1qVwF{N}L|WEvQ5n|(tG=>pX)#(k`rMUspqtO>_Y*h?RUhj8aW&)X?#%&05{pxb{Wr)%uAM-0vH??&`!N*W5V6A@;em%{`6;$!@WC#R_}i4als$jAQ>yveECaT8}Bn%)G`IPfsjiVx1+6e4-SZ9$;trCACgDfVXNE<!vi<=%iY<eiL>zH`f_pDt*K6}I8WmMa|#9w)G?$Dnc%qr!r1%7EJF#uf$FEIo%v=s;kX&thqZ&l6KI#nfjs2FgX>N**WCQpO&Q;JqIf$%~b_Le7)D3mArccO<LHlJBdl#}WOIvNIq@?Zy5!MuQ5-3~kxMNyl+6u`Mddsb}e&KFr-x$hn3K8M=>@*QYQ|)z&s$#&Oh#6ClLBY6g%<QA^u@TuBTRdAB6|V&T$OzbAiD7v}x~J`SXTVHZE_j%=tF0T(JIgn_yn<HpRXJB}f8OYF4Ks$yd{@?C^Y*~xAse<FOLAs$heK;8HFW);3B)<EK-g4VSCy-GEEpf*flvu#}Yh&!&$nAS?DcxhITqUEFm5Bq-`9(hxn{7Vv~em6bOdL-w28%(QS()y#ee5=d+fTrL(RAjLt2j<`S191WZqVcl_MSz(In}sZmv?w*b;Q&v6S_Uws%c%r%^8YjvxSn(WFQ=LXN~83F+jDRRI|_|oQ+cv|ZopgB_5;>aFipXrN(;-It!Ux2$L||_Fm0&u{)^$G7A%!U^4)_raa07HML~gR;W}Tuoa}iSIwOR<Gf>wjff8R@<WtrBpj2CttEQ%_W@yvBUKX5S=bRx@RGTNUIq^qbviYup0kWq8bftK9s3o`q0^(jp0OE$$!UWn3Uu$iN<Dl@oC?l{Z;NS)II%tb@30Xf?XPiFuWB$n9^~}f@F}yaM4hS+#DGJYP2x9h>-DVMP@XLsiSngq2N)|VSC!bCRaj_RLDm(HNKKL3ko51Aw>=Y)fz?sh?t<}u3nIIm}bxbN(MLmpDyR-0z0KXyu!DIc-QBe?-9t?~vbFm^x{MHmGa_SvZqY_$LQePW$h|F}c{MHP}EQ^yJqh=44M<Hpp;52U74(qDryi(WjB>M8qqZhWl);o$0zH?JEI~T+v+2FJ#Hqz6XQqW(i+HXj?NCEX(yhBFr#EC?I8pfH`0U&4Erq-~B5^PW{!i>&jdb90~&8&S!&jZ-L1QnvpQGOohah=cyv-oh2euG$hDCjuo>NvQaYe}@{2iNVfMS0YDnt!69d7AzIsG}>)xFhTk5jmH?VF-*N2|@e*Lg{s3ogGGgE;5$i2`Q&lm4*)V1LuOAfjbAy!`2ymo%_+q^^VYAhwhw}NkcUW*VQD66$hvrpz7S71bTHlTFrJ>!LaDDG~t@1IHF;!IyD#`tw^>e_2A!jx{-BY`p}p6wOTdH!k7oH|9Q{@bmPLdS6{~b`fei6^s&89<m69m<*T}Nd1%s!3CKJgKOeo6Nc!4inMy$q;;<U82z^x}+_;PXS}ojF#J|7?S7N@BhsoR5ANX}dR+D0L(U@@gB)4Wkvt&EhPw>SR{lR`HmGR~o!oF{V7I(80MOUggUt`#GDi*Y0&v%sg`T#li)ua+~OmbEk>ild;Z3`>)>9QbkIT2;E3c?~6)NTYJ1H77~92L>Aln4e79b`+RhI()Jl)Vw0Pcof}C<+NsF#8M141V&6vs5(65S^&0yYgV2%-^?F#q*g<SOm=3P#1^!=S{JJbQw~CF2+9llfupU_N`s#tn#yzc4i<n(25~x=X`LGZX*ama=13r!6wGp<if8CnB-E`=<@6T>t-BC38f8RZavtw^6WlG9J$k^)}l1cDYt6?*D82gH23^zci}ekYN{xdO~4LnAdLay>_9QnyVbpul%spX9l@S>ROL&`rU@7?fgRpKdcP+KJOYQ!XzR*HI>bA*l~=!}Za%x8(xMkm`feATZ+{=mPzvGHmMTN#LeY~w)&|1|VF8>Q=z{@uq`cN0bk26x-v!3Z5sN<!gv6w)Ph7ira-+~Pp$dh&)CX*qnbD-EW#IMTIny~i<0Gb)HRh;WP}Mtz<_ea+w#PSg9kD-I0eW-H_6{U`HUh|BX}0?{)=|;T#C|U#D{^;`@c^S6oc+BG1?vH6^eq;p769LzDp#b^s@roO2?etA{_<6`s_94KD-o0?y&9;-q#!hVsYdoq!r*pwR^?11-tEqn1pAAjW$?p5eB=+;2b>dT+yaxEY!98wNd~H?QWAdYDSk1o-?xDC^FN^!vM$$VHIPfeJCw~M60L9mhQM|y@+IGpZJvXLNGJ*87n31iqcY$wvo-bDex14!T$cT_GZ7G=k%9I9r;_QKyaS)r8T&>I5fviUkNe`}>gJxWbb&vmF3zxYV<j?p8?^8-1(m{7V$-Lz;1wdx#|yoA9jxeo`+clw=EZBR$U3&8`ze-2fUrMlx7?<fq52@rXBSPK=8Pl1O8XTYs<NCN7ex0FAAWlv=1duvEo)n2^-e-r{u#UWo9x`Vw}5v{)~V(9#uDl?$(YS5pz&@!pMVP1NvSdh9PFSd_nkA8(l><h>EH@fCy|N~J+GRcP*U8QE+t8L>sr|9)q?UP6tB2)yY(tHieJvWPHN01xr(C`yQrr1jqNF*l^D>j-uoL+II`gN;{}{q<S7BCLJ_M?l`#Ny1=CNC!eC}QApT^c$+8^a?@utqb-Ei`-aNTcvT(TpK?KE@GNKI00p?U+xW)GH4vZvEt{_goM42zo$q;YsW7)GwN02mpA)5{`m+i=GI;!hr$b(`cfyyV(4m_<I4y{)WK#W#i2<6O+sP=~}6}~tzGfcWI30FD_r-6L&1l+X)IH?Y28T$x?c0z7?zUCsVgk98^QM%&l41C4xzp_SGLfyJ$61H3MYhLg!&mHKqk$MdX^~d)Uo`e^t57{I9eW}I=9jFR)oW0eHF3mLc$a5YryO40`>`g26IiGggD&mrHv3=Xo#_ta`PvpV<qusrMq?UZ_!{Xw$AjY)Hxb5Zy;&e$lYKC+_*V$$)5Ykt0H*45TaCAgK`)vQ--EymA4WaGry8a3a(dV^7G;d<h94GiL0md-~pW{BN3|ikoL)L_6$1f*NWF;O}n?2HkNxKr|z?lfV`X=*ko92c%{KW#?ww+9u;!4En2Wt{8Wf-_Z>k~#7sTvPyOhc6&IM1<5y%;;d)}oQ6C_wez{Sl7eJ1`2pmwNA@m0W1Taks=BqHD^W-@@84&J25Kq>GUZ=6<*;Xc`2~fWR|s<SGFMkaWiN$aMc;h0lZbPOG_53)}Vq&W3weBs{lP6Chl2d-Qg8@R47iaBYyQ$xn0z8FG`KLztUd+yaay%yxYRFz!Ab**f6#9)Z(C!(unI+t$Q8xk|p1N0)f^@Jr6=I7<kBZv6f2_y29byJ=>ZAYM^ZLj!5;?{v3Lua$Dw!U8vl-tV*RP%Q*`k31Zrauo%a-O-jvaWdzP7d5u;s01;n^r3Hl{L+YfE5S>z$N&}v7QSvkLmIU`ECev&4YY|v)=$5ED6+TPfJ#yi#~|0_Ay~3s@A%hO1he@NNI{h}3Ndo~sc-=rA2Qb*^<7hIe{g{}bTn!DUp@mRU>>_{)G8V^@%=+F>vjllRP*c%vpQp$ay-FM+!QY5CvG<2BkO{0W}$sJ!549>SUmy%TP-`Au1r7{x#JS#1^?49Q;Kh}rb^=J?0-WhwiDOIb!mkx9)q)M8!j)`(IvIGv|M*>94^Hk$2B*cz2y?=9raSc=ag#d2__$u80b1Y=6`~K|M~-av*k~(3hDq$evS~?6;I%$Cmgn2aiafu(o(5gcH{lUNI#D<TNr6Lf|yS24J5}SKD;>7hnT=Mv9<|uLuE<jvi}k0(NbR!5W-c9G}LMU$gIII=cl-YWH({x8ZZQ#BokUR1p7%3wk2YOi}R`)&>?0NIbU8%FudwMfy8sMq|ypB#P7+*g6C4^4uY$<3#=^%^GKlPc=|nIaX(J|V$Z|!+-Ud-d=O)A-kU;#Mo-20(qxkuYbE=T*FLnsNA1EmF8&=MW->t(>G?P_bUzg++-SB;6j*7cmsCL+<V20O*J9#XMk}-3;lfrH!CHE;P<2@X)YxD=6{Wa^j614)+gmOM=_rdP-bscxpgd<J#14=J0=HV!QPNA{5;RSL8e*qW_#h4P?B!W2<aC{QTt7^HJ=A*_jYz>|NK^g)+-FH#G#KMLQ%$*-h*)M6oMrwt>?98<X;nN`Je+9eG>Bo=t2rXSZW1RS&^#gdSV>*htjYUUMv-YMYQ*a}CE89N>M=UzT^&TE-ds>03PHT)>?)wHx**W&Ur9C;ytTOQY$2}2U_MYhKg`|tR4!mPUMwrV88bCy@tiHPJqTzfQMhu&D^+7aMU>p=^2qX5OBJHPS59v|(^xAi1WZ6;RSff`A2T@!Mm%{va7h', c1='fea6d7f5e1dd9fd5', c2='c477bc631cda5311'):
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
