# 大大鸣版 康师傅扫码抽奖 一天15次 另外每天赠送拼桌抽奖活动相当于多了一次免费抽奖。
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_ksftoken  填入code 自己小程序里 wx.login获取code
# dadaming_ksfcode  自行获取 瓶盖码
# 多账号 使用#   例如：账号1#账号2
# 多瓶盖换行即可
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
import sys
import zlib
import base64
import marshal
import hashlib
from itertools import cycle


from itertools import cycle

def custom_decode(data, salt='HsopkVsFZOL27aNt', magic=4464):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='FuinIHj>VcKb^Zl8aIr*o2L?0UF=Lo)@;Y-&;{Z(Tq`F803-(o0jUP`>--!j3R-Cb02qbjW7Fz<yZWB!;m;=bLrM29JDv_gB)Sm;^`zhJ=_Z5rDN*yK=u+S_jT~*KzWPuGR2vsPLOiQeDUzJoNG9M#aqiiXrXIIDt|nX8q(T){0S<=oaX6#h72F|N%yeI0hVvWxR-IM4Gsz0eaKoXmsCFC6mTawKvn*KMy^r0NJAArDE^htZdf)yX8Zff;cl`TKvv7X9H{6x7Sh=l=*|}Fa61=*~HL@A}7%kbDIRH1Cy{oeYw%lsZ86$#q$+I)R=CGrqG*nmFj(lRLj6L!}X3l@bb%MN`+4DQ1oxaDGs=-Opq}(dqm_$FOB_CfYpQw$IKSJ(MD#gc9$+x|solQAaHPo69ij`{Rv%9KoMhMs;RNk}?HEELb2S^KnBu_lvb$i&Bo~;qC#-*WX8IcuJ7GDb6!9U!bBR;P;Zfp>7tEAE0GS!d;2)LkiX3t*G*PnzF0>$0ouXv&Q&ZyysmmAC+uzE?9qx?8cW2%eTMKWE>X1to^pzix-rprl-cU#%i#7zRfS+e`SC4s#+m>&LLLb#x_i9&lJr3j*<-6Gnpx2>X5$*Z59_V2gWu{us+UiHFqIrwis5RNy~)sq%KjAF)&yt6;2WyPFwJKFV%(tDZ{h&#hviOztBG}gd(3qZmyrZ~4gHjo3^p|*Zs&r{Mgzs`D`qA<CqXJDz{!-;Zqrm#EUrl=j>N21(+S;5q;eNI4e#=`-{tMX+3nb@CY33DR>HC+`W#e~(<mabuR2UzP6cDISYLlSPT#lK2dyS&pOCRw}S5MkcMx^>h}32wT3GH^@Wt*F_3alP1iAw6ORWyrC5x6IPPp7n$>$-dHJUT8&=Hw>HqjJ+zw`Msd6_CIa%*J7xy@&iE?$L#l!#80;`hhVVR(1YR`6nmR@rW~rxK{{Y<Ixd?SA9^2&6;7YR!_MWJA)n--(}Og?vuz`3IH}d3hP%<q1Z+cv!f%3HYr9VYmO;N2_ssQZlRhCvjc^%$fw<V8cHtkwIhk#n0??~L&?I6pE(~wagtbedj%~Vv3Oq|T?DVeulh?^oyPWkD6P9j{9M!MS?eF*^VS!4$$VQwcnb+Sr_SgLQ5)iDwao<DY)rg@h!0VjmW{zemW~|C<&m2+3NhO+H=0ISpaeRL(=PHY@q0Q!bg|^H5aNkk#?D<gw0)R76Nsq<iobU+7`dc?!0|}r_>$VMxCsZ_e_i$*7EA;e=171QBZt6&)^}5ft(xZVkW`BN`93B-b1IocA!Hf=WX}R0NC%j*D%;6qa!Wy39(xN%;|5?n&*zqzF0_CUB08WMpt_W*h>fJK`6OS7TA)UI$z!CE2(eQ{3wzP?iaW)Gx@v`M^o?L!#^(WTQFl*tK{QjQ*66VBH?8{PElz>%o#QClR-S`xR9d<VkR#XnabGAE7LMj>$IRxw(feqC@lZjVG0H~Tf*2aehx{gw%74gIC>_s?DgJ~0V&S1&32RsywRkrHgb6!kuqeTPG*jGF9av1nwW@W{67t1*{_G2n)kln9%rLALs!$?bLEodN)S(h1l=8>tAk=N!2jh~D6yQp0<%Nca8e+_il0ap_E7*{5ZI^X?UU+h_9ES5+(r~z;1OXHsDf_5_vxBG4(<%h}yC86ckfYp&bLY)3zOF+_C<~^8*X#Wn3tFv!Om)vH(T$a}ViRtFIyjp&woT3?6J&{Z<#qN6k686>|ErYRzm@OT8JYCl8dB6K5?<j0$LG7UM+<9lWG0P$44m*NqxVKI}jp<(-xa~)I{Tc&SK<$Yo;)EZKIAk91%;swuB-*w99ep$XeF25+7$8s1V0d!@Rpa02$NWIi?zc)ZD^BRWbCI(wn*6MY|CK418hZ{Q#o33XgP$j0Ln^b(N#8m62a(r_`LnA8cUlE`KmzX(r;QLwz5Z*9f4_gTt7#k+$bXZg`IJub_^y>)Sa)6^%(RCk5}6p2xGVgA9jYXWkWnO)2GX7C1be(G42auYVimtTc|Q+I>WN9+!VDE6@2JpZPYfzI)o<BqFzBQTBKPEWvN}j$X2|3%MydbmxoL)lTP@?M+fIWz4UswjkSG*Dm=|9D`dOQaS@TjDe6~&nHz_kL06qu@$@GIyy@G<qKj$tZtbo9!)`>yy5~Y&0(Oy3t6vj%g)=pOQVyE=Wiojw0_!`nN!$Xz7ygNffCL0N$$Y;WIGmHI54y(c&UuLEV|2p=>0gYncv=k@5N)(g0EkyFMy3&zGXf8k&g0jd@mZSHc-_@`$XQ9XzYmlQK8jOu@lu|Le;mwBrr|g-G_=YX7TairvA%aH-KqO5Kz4cL%GxtV3qjD%-wG<t3C@KvX9%BqTDzQgYeyK;RL>s6CL}&Eqq$_Ok!Z8xTh4J>$Re|g0SqQ5RRVpIOIV@JmbgZO#B?Nb`sD`%dbRpJ@@r2a4e)vHpZ^8OJ<w2a_dU7PqO1FOXF%Uw9X-#L>(=WNV$|8%9_yc+4<Fj2q(7++F{w#_Wz-nF*Ic2mTK?QSmOIM>A5`s?xzS|mkIa?sV(nzeNBn#8Tx+D7h%ZN&+X_g0;G<`k9GYVuBF`~;{$^w>f{mQR5*Ax^%lq6n=NfEab9&ryTWimFAjcYs*EmlxbWwL7LfhY%*P}JIOG!_+CaIq-ptf&sB*E`<+mab~GAP`WQl`Dfw{X&2uYsz7@I=MUY;^Fl}RKAV3iu<5SujUx^G4%(3mRA)TH+(7m<=B3}bnEftUNZwGMB1^(g>+6mWSBrro}}z8)9F`_FlPB#&I+qO_bh8H5i#hfkuxRn7+AO$3@42~|4R<nwv^x+;K^=V^6dh!%{qGS3W+7`JB*2PhizhMQo2nSUIc5a=j473cwHeEsLZuD1}_;+GfjA^n4q`d@-_l8fpIi@Y*?1qjX%EZK|KN};ETa;J_*!cOBH0qjrm7>i^QPWZ|VlnhAE7a+mGSElwUR**dP$_Eo<i)L1DGVf)9MeF?8juZJ{s%&JuO3&m)rMo3o7AZXt*AiKu&HhH+outnpNT?g&SjRKwMI1_G8ABY8+nxA*VhHoN}JPGi-8TW?onEdEi^o^Y#BlnBmUbPIrfSwpB0I*9$JA=nFoZy=%^z%NK0@qvm+CBP}XAND~mVwWUakK_hlcnw{V88dM!XGgY;@_N|Rc+R7vo80$;^n7ooKDa8v`xhLWeR}QMosnEaIa=u(-B6x7f8CI6KO(C~WyM!lqZQN<-bJsPAWOAi`=1VWLm&I#KhJ~`+&C0lxf*_WPjroO*Yb1bvJ8Zp#z9i5o#s)zS<m6Z@c<piSYCH+lL1Uv8?>zh6|5-DkWW>YSIQ1?1_i}~sPLIMyM*TgyghcCvwe(&ig;R7c(J0<BqM0jqt-`EJoOmT3`d9l=G9SDo((dQ_Xa#EVZ40^lb8QvDKZAvE)!)Zc%>pbUSLc2w~r&hK^bpgM_EQaYA;fUZU4r9gZ(q|N?I(dtHWpEV*_XSkl<)k4u2KqJCwm-yR+6{+Y1QbG%NlxtfnCbE9-&+<7s?xNA}ou#LHDyE}W_B!>~uv+7TH{P6@J3G{%OF3jZ)fiiB9}I(N_9o-QWS%@V304?;5wvvZ=_)JXX#wS0$#H?=zbHzbQ~4@DjN3ar>wf~<4e^7~zSU^kY24=XiL8|LgYze&61y({tHY#uf=!F?><SFcI^ebu>|Cp$cFF>~>Y_{kNUB{NVnt)izw5_>S|fm={S1%y?58y~sY)|JOg%xp3kOwbY+&KFl$$set^u={&r7#WlRVIY@p<=0W%Qy2Gw+OV=sEh=T7Ptzm97Kj-KVfv;r=kqz}?8XK=xB6@!JVdH+&3_J<g8dYpDkLaUPi^*{|1_99lw_((Atas}a~%29j0^j4Mp57;R4N13+xm=HZ@$)fDi_R_QTKs8aHe9@LQ*&}bh~UlnR`7y2PIceu#SZCApNOMIY=-y<k>;2w`k4=JYX9ilr7fZy;Dzqb5#i*0saJV%s=#mAnBJa>gaG(LYzribPx#D{T2%9OExe)Lx77;f-ijj8c|4<`ODa?s}LA2l?)vRgw6MxZGKr%u~63H%6E1{l%SBZU6($=hR#TDcRF}5S)jzg?S7g5i~nn8P9EzQ(vvVd0w37j%*Ym9Pee+m)G6GC*chPr6mbsHn5pdSuDb!-gyn!YL019~^uFKxIo4C139?w`^+7<L2x1*lJ0g)T*hqg<D&WEfKb!R%D4DtzkD-gX2&QYcyQaCFK42^XyzOK1hZ3t%@9F?l2Y3&1?KgP3U{oVeXlIcvXoxNkt~+Bq<_9=gz9>v#DG_S4^y8Z@@llI1*Z>Vkb?JvKT2lg&#^qI@rAgcFZ<LIGymDCyztS)aQ?a_@ddSGY=wDr59Gw-j$RzSNeRMg;{eP2O0Fl+HoJ@V3LVc+5(fo5oOO_W2%y?ETtCzj+n6u`V-%W&iulb0aHmXz2n;v3@T1{h{4yQ$vZ<*0;EAwhun&%E<FDqtem@GM6QO5YdW8-8s3_(2@SKUo;%cHk0O_psk4dDib2Pl3w$*UQyxJaWDzZ+sQmXwe%o#o;yzsU>tkf5GibW3F@W}`A{l0=}I2fJ}k-$=nCKo_2A3vT>`j|h4<A8vC+TPnMh<vGK$DPbo7aGogoGyl#1HAkL9Zogb-DXzmy;o6S9^doL|vWzqW!y_Ga2DFbV=;@@9Kr1Y#?C_zM%jx3wTePLdQRw4+szXl=uuA?kh$R1u+W>Nzi>uB0+#Rzmxh?cGcrGh(!1(IGBJO*Y8vO;uJq<$;%6TJY+sU9r=zx`v1m*O{`2?13Q<Gg&W0Vx&$~<EJ_XxLEal;=GhA{GZx2so28eT1PB_q(!AkTSFEwk6w`%BA6-nLT8g1$vNvcqqdl|9ZdQB|CXWKI-b33_mArJ$k~4GlwUcn3Jm)&6XsR7sjD6uvyfA9iDUc_12b>xVkb?NoIq!Gul11(TAoKmF7(U(xV-8#&4)fT;`hxU#`y;6VsnVn`8r7l2@9xjN2^!%J_V36*?{SUhe&OVeh(6^as$pQua|KCW-ID&14~m@Axo7<K)oRZl!zAaz+BxnE0ukyxtsxIn|Gj}>FwgAtG+Yp|tg{0J@W3B;LIcx7%MGDPk*w7R7=mQF39aa{z}MZx-w_K`8_pQ&RW9N~(18k$KjU)&ue5%BOeh63*T9|60Ki{QX`{myg6=BulP@rp{hMzm?6(`?vJXg!(%{(ArQ1Y>Tv7S-TcUQv5enUSghUT=$_%iVQg9Q+608_*dMslB+~XUDR#4aR1!Xavum8ttSyreDKZgI0RSHKS1LH-UTWpA7w9LC8#B2l%DctS)7fRA49jHhK-hi9JfiE(UX<!C{r3N0#weXY@m?E%<Hk<7U62UKXvs=S7Te?QuD*9J(S-d;h>+U98lRL&&;7iiHA9Yc9Dw5O8F3fYNi5z*r^bG2^Vgi*;^A<2(Z7{i$qs-o4hNL~=GW<X`FgNpTnKm^V_MRM~Fr_I?A<WkV_tU`s?#!Zx@T^4~XTXQV7V<uV?dqz`I>;f(Q##$9I`aRu<D)xRsWb2nFC>RfLnSMo~hO~C|}YACQII9YBf4484M4n;MMCoQ-W2$dITImv=Xvl<F{X+2#8bz_InxOBVeh#ZZ=tlIq2!Nq%y(N|oYYTC;TIAd-xRC;yd(suSF^wG`-FH|mp1NYsy!E6^a4%5uaEBTe=LEXWZ3q2J>&K^tvo8Qcqb%Zt>@H5%lzJ`RpQ~s}P&{+PA|L?S_z4{Uk_*yrQ*!NuTD<PNQWXRe_QF<Nt&i32(Bl1N5PemQM4&i!&NYa(r7>$`%@*!)<$S?;byqYmmZ7ln<_gT&fxlGLx$#6w+^hPDTh1~_UJKW&=WMGl2*EB^8@vR1no>`HmcZSAp6T{EF;;~ongZSVXrwzx8_3y{X(Q)+)A~tlDZc!QEH)TR5B?_1xnK7s;E0$5HBLDj2sUVZ;0v*{75~1Z|ngDP)(HC0nRj82V?F$HiO`_ms&F{gSMe8YaLHj5BxC%C`bThep3STs%(CZeh8hQ$z8znuLPwxWCVW{<N*d`#3YYB46NwcnCb?zf0LpxHGy$cW{NptMOe3wcHN)z-N7#?d~AUJKhW~rJBT%8BHC_IHG2Ih<jSP_*OQ+Jfw4@(|w{C<ck=<N;0=#&~{@aRL)(_|U|TMJolgjwe*ra&wq*PlUzy=)pT5HF!0FU1|$K8+eH-}3Vi@cfxH(|8fg)#mm={4i9R$W(>)^*{o>z8IktTT*B?!U0Z@?LUqRCb<{g2FF}RG{?Jk87Im-9v-7yvu$*9*f554RW^6lziIkkcY*1MGCWd7bQ71q)(x_n0GM_+0BB5g+bWU_g|J?^)D{JSW}VG!SAjZ!s}$%xFJ|ra)uO^iF^j#RgPtK^!*t!IRtS4kMvpc$s&<;fh=k3^F7MuXf&a$Z=+T&#Ec|{=xP;Z~G8@YF&@y%o)!}*YUXj5mN6Ki%{cm>xr9@I$`Sm(1XWUvnsQsxQ@yv|y#$y8Agjj;Q`+1;~K_aQhes+(9yNJBG+}?sWMEqr&9LO5}s-~;)DW}|!!*CqMKIN$=kCe_$5KJiijbLCW9e`8O1(~x+@8}8^+}}&TlNp%Vz@8e-pWa3Ap~dwfwMGS}-IFJTR??S11&SA(33xS!mbVwRWnIV=lg=`ksos;3znc37joD-f@hIy#^(V?KSg5DX&cw_TkP(jN3X$J<0_r7iDL%OjVhjUIq=O;`!~eK9=DYh6IO1t27>o&d^t3oy=0SiQSPU5fc%KVB?Jiob!rcSQClu!ZJNwYGxv0`=13)t}3+&7AKRFaifys!sdK_ueR}0s5^nQ3HP`GIj9v=|av)c>|LGk=oj(A8XUaD^Q24Q(h)ktYa8yrQB0<%eNxXnjf?>cm52H_Mbf{gefb_=XBF(!1&2+UGNs?v_i%$FSSc<|Y5wjU@yKEWF%AVzKWf1ah^<X*A)05gg`meZQJp{`K0xvI~Ci(fp{j^5WI_ngJPSiMa<M=1ZQpxhj?eYJ48gc|D8NohkUeS0a3391&wLq*o~eg>ddjjS1E!Sx5L<aAHT1M`WdLPVE;?7SAC7v$f9%~@FGN#5y5so*h@)i3%efUSr4rieyA?iERx#Jc92P3D)2yHA&pZ9MIA>L)m)TOpkGaXWA)o8FGIEN!x`7iA8XbceB&fk|;uS1LWiE41<mZ#b({9JxtpvOJl>$eVY8FY7}1$HVXbg?6|3_^%&Mc^*lZO=Xm-J0_-?vipr@9ue+v6U4C*Ht{jj(JsSA=2)h8vLzQqhluwf=P_7F95nzLGFY%m?wG^~f00Cyimv<~+Ki+}o+%DuVrue~jC_H1J$TDmVFj(~#~MyoA<O_%5~C-ddP1pd<wf;Z<w{FpRlg*M3IZtCJ$V4ziw5ohHb0u$NP%;x?UIpyqgO3{;0z$qWxO1T_C$a5%9ct=DQp}dewk$$+abkTDHo&IsjOYQkllTUR}N6={yYl!+-26OO->ezI%-TD`Ub}sC35R#?r$u|e)NjIfpidrK_P-|jdo=D5_&Z!o;e~qC%2B0eQWZJO>&uR#CPdOc>|o0$h16*_0cLn8=>{f26z%fk||<T!S>PpYjoggy(fG<`+DOlpo{mVCGAM?Rlh;8(tD#sySql};3$KsV3t1pOp@fAo?o7Mo9>nAPoiB9j$1ZN$0-@aofoBI)Pw#z83;}@CSsC?Kn54Sx}XQguE`*Xt+>;Yqp;sl1FwXx{8_He@+x!qICKsM4MuP`2|dt!IC6abE9LyBeHp?Cz}!PsS#FEFSm-@zYx#TBioO8!+<$iv^ByeKek+0sxW>?DByAs{Z-CK4+}Ju>gBZ$Q<GS`(c`Y895N~LkA_KK)@Ow9bQ3@9hxhDBdd7>#X5J3!NHR}qjSE&m~|1Du_+o2GZ<x&^E`Kwg!5F5SF$&be%X0TQ@dwmva(VRs`zJ32+yeH18TYe4#`q&Ff$2;AOXYB)p(ueyo<qmF)e(Ztqrvie@bwe@T0#11LgRD}x-*GP3a4HnnU`i3)e+4W}PC?^#!n7~@n#DF9_vFm@K=0K(#K8DPPOx-aB)z)5f|yiB$LkK)3Fq4LZ**|1EbpF~BZ7Mp_<rZcK6<=P)WmofD5k+T<yplt2~3-d|A9B-#4K|OxaWF=50YyvC@!Kyu0WN5a#X~j0792`Ui~8-o~t}LAH7ik{Vmuust?+xq$?$5nSjvpNjNtwlFLRtOmhDZuY=8C?LP~9XLES=%k5m%-2gq5{(xkH9M<iU^aOMsqF`?Xo}r&=Btzpx(Ou&cRLW?j%@pg&q+7ta5w=+Ck%kIm^(URtflop_5I*>@+$t+)wcLm?C2VMP4uvr>C~S>-TYLo^AkNW8yVZj-w`Y6hAp0txjAM0z>->$;o|xYbifTPu>~hc(YW?6PW*g5k8%(7q017g>Ve9pkrN<kkkMM<_^;O}_gaq_GSyVu0`2VE*jc);PnNAkcPe@O;MD^P}L1mM&j22(9mtZ$EwLle2I*$LIMd{hBYyz?~SBygHaHk+T<%aC2ad>&LVB(2kI_w*mNK;g`{P<`%NLm<8Q_0)?Xz}6E9u3Y&h;u#<<fuNQzV1EnzMwR@`>~v<ob?iF*;_+Kdg|O~gd7QxQ)KS$bq;K?AWLH=*E%v4Q*Bx%`4NFXz}E53>i9kVSl|$i3!~omqec~v5@y~seahBnf_oS9&v=341P=F_QfEX^@Okm8<E7IcwB<=S+IHhC!G`6D`j7@m#zR~PaGxjm=z*`G4$GFuAf+NBNAly*o#KwUgtmkiBWyl;kni)CJ0R11<IRD=3$(GFk)a<P7A%Dg9Krdu-yyoX)?Bvb4Xt2`iH!zyE~~gF{jTA~4{3B@hdw0R9voJN+y)O-R|W&FE-lT~uq1K)gi0PPaNnY0GIy0%o>shj?P3f^n3C7@b*8hq8~LSe+i)JEcyWp=MaUR)#k&$4gx_kbq=#*6Wx1Iy5g$>VDSx^`Oh2i?1(vDqvu79?2D+$1L0F}5I;B}&$$XpL*g}dk+t-G2@o+T;lPq&qsfY`YFoLc&8Df=6#eWx6CITb)K2qF&7HYZWHgv4{9#NJSXE@Z(m87Atxmt`PH!SVCe5X2@(r#7_P@MHqbD_T8=`@V}ZCONo{;2qnR%xyUED1Agu9Z>>R*_Hu{%KdR^<8j~V*usb$&Mq7t3m`#{&;Jcsq<s$5MQtF+8frtQ5AJtKwoD!`oS_i%rA)&D-RVJ;axHyjZsM}%Vdmzn1x_3u+&RH+)hD6bK?UN>)LfQoqZJIV^)G-F8AZ8-Q`o<^7E0vjA66P))X5<KJzTC4s4r!Xx?eS9-T!48!_6<wwZ5QC-_WrTqaqqC7OtU2{Hav%8a_#?>Y+yDuR*k{>y_-M6cIugBn2H*pFHn43R}N%`agMKKuynOB`iz{1WXcv3xPen+yFz;111`X*B`Si?xyZNF1j3picmGV=A@H?(xn3*NV$<!o9V2&htNS?N-&uq0g|Chb9Jwb&7@3coa`(2M*JFcfn7p`aoE>20}kA>Me=VkQ(bO!n(XrbI(ONJJAz#ydRrMYRuGlUVT>Js7=2`;g*^zMrrlYw^xs%p_<poT&ydV$_HjWEoqF<bz@@_7D3TU1X-7?I{lkaqqsTqJE#c64e5XN?~mwbsMYWc$14PxS?nXkDna<y*xd5PQqx)T<F=wwhOhx{!+2T04ZnH1Uh0#t(ROt9(S#hY$@UvnKS5!s<}GPz^^fGFUQNe==Z@{TGRPtBd)QbE7ddMhCS|9^cMZU#hVX$*9u@HerDgb^_BbsB_XX<S(ydK2Uur5=rGYAewz!h9o=Gh@;4Pe)RTJd-N*|@9v!UFG1vBxHZ8J7{Bjx;6F?jPRI+@AXZKFvu110v88rMncDpjsY8>!7aD3Whdpaaq^X;=8TmXJ&UyeHGtajokD#o(Bbsy9Vv`p7efa5O27CpG$%k0F_GrwQr&woIiZCs!EnZBuDopjH-C;OMBRCUgqn+!-d9AQFYR$o3_5i;VNl0y1L@u^@+-Vg7VO2GQpE+~>B~^y|p~ldZIvZ!u>sv)8s#h^olRU@v6`a9;|~@a-eUHhV?jZFsTO3DIw?6)8W={?0|XPm^^`cxImoP=OkL#BI)eX=c~)92~cDs2P)0l-txKdyCgY*TBSpEHVjL>iuEM38CFFksS+_vBY@9AX9HVv`1@5raMyYAEX$zyMup+)Nn;k+rgnrH#M(JL=$~2_LrAn-vF#7?lRmk3x<D9ABlw?FUg>jF5fi%-e@w34=}?^mm*rtF8Z-XAO25%9AE}CmFQiAwEYhG;q9V4ToEUD)Ul?+42CEe<jSZeXikgh2x6W{i_S%9O^j$db)Ce&;TLF?q$&v6_Gwu}Hf)0EfI>QFu=Ez3eQ7R@R8uL%`9wP??#ypzCTR5L`TlR8i~XZXw5WI^qMCxp4%r5tzC!t-tNMx(k}E?>g<Nx$^F?}VY?mG^94`VY7O1*>_K^&O5R$^pc>EYG6W>H=Sn<Gj9T?3YafY%KfvJDm-G>RNFB0$<MxyX*=#vWWRqT<en7?QI<(wSgu!oD9eMSla8%=OB@z1l{&G@ALLmK`8GxScKTf2zV_vwYOci+cNt)L<pze2iec?uR+CtMd_4Iw*ezvgmagDK?PZ5odEm4#bIYxb+1vJOpzmOg|RIv+dTJ@|8;YHV$8vdKqLd41NDhAyOFEa#kHeWUNQRbex%_~xi@Qn_nsXQ7;xPy?>5se77?g_NGkg<g7nNx;Lg35xC=nv(hKwp7{{=(9i^V<dW;ksuSpw&ME5;t1liX=9AvHE`mHb>T=7HMlgfsx0n&p6{TyUjm+3)gUr1yXd!x2F`0UQ6k<N%P+<?h`z96evmukM%=vB`f_45#YUHL1(^L~)#6T%n!8G6iL{lClele{_uHlKnZITwM!nXXdN8+_kGTGxiNwpzNu)zzF;BE_eX?GW(~0sx+0xsgYM}kzoZg<)v<<9<2?;uErn#X*x52}2Iz-v0IXt?P7EYMpiK?F5VujqZDY{;qh!D0RnqHpPv`y572}`?@{LLGZ)7$jV5~LlqwJw3l7M5+G%~DdGxq{clsCqM+b#V2QWOfwW(iPH*sJORz#$|OMtDBH03d0fWy`ZdNAz9s{G+|xd$`!)0tG<hyiYV=ZGqS#sS;E(B#yzOXjPT`R3gP_HUL{*J{yp6win_O<2SQv5Sn%M4u9{DQpv!fmw#=Hp7JlN<rgfl(', c1='baceb55890fee774', c2='0c5576694d086dff'):
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
