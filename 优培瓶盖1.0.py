
# 大大鸣版 优培 积分+抽奖
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 dadaming_yp  抓取 用户id  dadaming_pg  自行获取 瓶盖码
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
import sys
import zlib
import base64
import marshal
import hashlib
from itertools import cycle


from itertools import cycle

def custom_decode(data, salt='nE3rJlI07i1zwZtp', magic=4777):
    result = bytearray()
    for b, salt_char in zip(data, cycle(salt.encode())):
        result.append((b - salt_char - magic) % 256)
    return bytes(result)


def decrypt(data='kH~S9PT}3LRq)v&2R*cr<-!sLmzHHcDV74fBaJVP7!z$RIR88&f;z;dv?XF|J2PdiYvxa*DMKH<LNK}6+~!Rsr(1lLn1SQ7-0F^Jhi>*-Q?)WUa!K7}p~Y<OmK1taY3TUAML$Rp-PsrK^;t`;eiYTeegDH^5W>87;8ha^fR8Ph`H!QLXS$3M^w!Eqa!G7`zI$o-XWcLk$mCQNN0Q{i!{aR&393}Qeq|H&<^b!(r)d|W7MK?}_Dm<zvO&)`m4-><hk_JocisEOr99CXlE&8{b4n1E-bBio0PmIHNVx?ZqrU8iWu<%i?|99KdJd7A{-(?X6}!0)Nz(7lnF+oQo2q=AY^>Fqbkp>gL#MTx3_#eop!GZ#h!J_Trss)H*q)pc)XkaQGW3whE{Rzi2zLn9I^kogacbMT%I-;_b$%5I{WO#m-wWu!Z<NHQ;a)S<)NK&*Uj^gVy*bJt&3v3h_N`M0oCa3NNx;<`O85`{;zgU2k%%v#ln0zr{>}!o#M?4y)CJGBvMYtX0`GM9KBv`fg#2K-bHT(yTG{G$;O*A-j?}MGRRy1}_V^XZ^*yqh5e>7TA1c_39ilL}2JJumGAdBmE)J*KvD!R5b|h62>k#?5z_r!Ny0A%Z1ni}DQw-rkmeHy|`PSWF<*^h~0%ecr|6UlKE1iv(`nbzlYaEr#t^IeZmT?mr?3s7Eu?^Tj&k>^@pa1?SR%$U8%p4)N6%H{T-vRS@6U;jq(F)|wYv^@O9itNen#A*}PUAT+N%yzwnE&W0fy|ny;qc{VT8Wr=KcEcvG>f$e%C_Uuy;1jt-#xRqR_KF3p$OT^pU~Bv<WiLHau>rs;?ki$v^km08DjdAHmY9@+!P;Kuc4N*{tOI+1MAcUxU_G+sSAr55k8mK$!1m;UXPGbzmS0dce!k66@3K^hpO?`mw-ss3!tGog=;mVJF}%j?UJeyxSWO_J!S|9W}tB7E4Zu=Y4bu%qYP0!o;=pUAbzG*r^PK&eyC$`1mqB3T%64+&b<HcLjLrlrnk+wEjN=(Gf<v5@L41c`}7eL$9iV|vvxXv0E=dUj>7-vHdE$Bm3dstm_doKg*aYliyTwc+BTtsN}8b3NmZjUkFKl5lK-`0idC2KD+p{_^_7ZGO*^2X3CsjDq%7kuepuQj<`Dw_H(s>pFs1{L@Q*WDH}}uLY_vhk;$Xt#M}!x^e@5mF%SMU^;A5ol1hu2JZ3`$#)=jrKYx5wlc{q48pk*^AKwcWe?D1Gylpf(@uW#T}yD}qoh!%0|t+VrqooqBN>-b#oFly94D<PiB?P*K-#NS1r5l&lN9+uiy@y7qHa~olFVny@q$Ih@jCP-Zqr}oNxXm4Stds<J`4YHTZiOAD6x^r-}X(_#tyRlQDX^dP}NF`+2zXP9h7Xu9A`hgT_4?RD7_MH+`2yPC4+Bo<eGRIMGx_#tQz^OJMrNV9b7o2JoJ)tcb)D-S}x<}=Se;WHauFc<>K)ibAd84Ld9Y{{~h{Cm%uasZ5N`)o$n~sXnYZhudecL5$rr81OC^m;^HPXwIcu?dnE=@w)WdC|(^*rv&6pVl>FbQU{t=DEoN?GVBu{2O9d+t6<Os&uM$GQCqnk~<w-4ZaP2_Lh(m1|Gi(XCHrJ%VOB^yiikKCaU5(K>0lL~WV)b|4f=n5G?+unUnoCbLgS5E*WK56l8K{@&86BGs069^haDVlBLeVfZB`yGDce5bB`!lKl)`yD@KdK-)w;DXs{o;Ux;^N?uzleiLcVR#Hsy@EsKq?2RT-fdg$PtbuBl7=dj2`QKm^&2n=N6-Y=kD~XVQ%v_Fy3nH<LWhibBs&E1Lp1Wwr?a4VAGqK{C7;uSb*9xHyJqbufn}2Krvcpr-0eupoFFqEL6)q;LZ7xs0zfu1w1*ehIBcNye-mnHYN1OCBradxF*B`W@Dxw(i4g)*fy_q)WQh!)eo&JND#yN@Y%W?agdEFzfE+~GRS_g8Pd981st*)@8?E`<)Jp<&+Xv%Ri4zL|Zr`Yeom|Jk<=MWc(dmk|V=j#uGg^gONay$8ztM5+Pl-4zhCE<>Qx>xuO{PcQt&7Nhcm}uo;6jrh`t$LjgXf_q#jK?L=p&#}s9fmPJGZTn7#q5DiFoa<zFqv;;s#ALKhxn6*$v3dRK@(0i=Gm8QW(lJ@-5C|g<i~;|I~!X3WRjn_g8!rBEGMp~pSX<~S9?;w%b;YX&I-E`7_r|ew{wD+jlKm|ck9k^)Rb1EXpInF3i>7<LjP5XS?es!s+O<=NV8@8?pHVRby$wTO)J<Az;ls?AI3;S#G9Fmf;o0YnnF?=9Y=L`Y7|b3ul0*YO+mSol!4eQN=m^In%>=+a|@AmI6wxZ!QcYbsvs^T4UjIxf`#%Dl4-`xTSRcCF~}WkSv-~W1y0G>8^}P;MceMsJd9yeb5K>w01D^gUx6ja_cLUwV;8LH)Q0YFxA>&P!Duqz!)W){cGFF)QQ?8LY$u=j9dQ4ZeQ4PMFy`_xnMzdjs(1hT&kWdm#{k8#f<cQVI8>m8^cJuTVH>uujc@@BvN?1@)VW_{@b668YfTCBeFR^|S*=5c$1u0_pn&UNazHZu`ruNlsK_8GAr=qXGZWz~rI&llEGIX@7P>syVU?hlcs_L*cR7`C#daB9767jf3&w6#B!I<qT|H?%ivSSEx>S3i&q@W5N~Q?#3zS3Cd^;A?zwpi<uf^YPcW*BFM8tEn=pJz>YEV=DAt#+a(iBKz$)Un9f1MFL$A_Az)U0l=+{TL4qn;@CNQ4JVQ^~YSt)L%NDodVVppT(o`c|63qr7^3kneLsOzNhm;N4!bLi+zb$jU}aQDJzHZkxu2D5aV9*r0oLdXoetkJ+x1i6q=cIJ$|XB8OJE{i!zwr^1AMrfQ^xqF*rn10M<S&MUi+hVqAfF<{0^)9fCoGl;pS5WqQ4{OWn}1~h~F2Bc|4zPyMsh9z}N^=0udtI=F1D#9}R@f#zFoY{-$+Z<Ehwi>L2ciED+K@>&%Mh}di1#c4j2+(0erTJ|v{@YKO4kw)dJfa>+^cQ4e8_S|hTY;I8ZX!o;-DG3gr<S-PH*PzMG&GPINhMI4pfDaH)`cKyz(iNqRnPInl&JgZ>MZRx1!CO|nhwY9fJJ4$cQ@SV!6Y$|R}%_hbEwXgfl7C=ibBG8*V92th%j$`Ygf0`;a(>DJcBF3q7i4t6I0cRX(F65t5;6$boY;NQ;`@dQKm`htg%LKWj~X{R#PkjnYUlO{F<?4(kUlL0BOcB1$HmXwoCMn(96Ali=y!3EG`mQC~s75ftuGoB8|Y$V@pC=BrEuH+++YzwSgN{?!VVuEY5|eYT_xpUWen2K>kg8$ql~TVa91~5PHz3Z$;oW2#0fXiQVIM=|@q66}e7eZ@Twj)yWfvsZ;{Lr!YCoZi87zlBhB`$DLF-{iJ|+S#3s<T{B47%{tsd1o6f36{l+Xw9;txmD<aVAZk;bFza5f;O{-Hig7*yZ45I&LjQ59p?v)vFJzTs3Tks_vW6>o*%PR`7$6JS+87-sLf)V*!MXC@daXtq*ms2VDBF)?3p)~8{^2x*J0JS4P9r)QRM#w6HS!0q5TK}r<5M*qtg0?LE{CDMkP54B&W7f#YbxfIZhbXg%j^Rwrwv1A(`ZxRw~ymP=>1%8k(aAG5o0wy`O5yM{pXliu4WUV2*Dq7T|=$5oc8I|xSY19_xlN-ETy@dz5g)#5od2)y)f@))_BpnLSq#>y33WMuy+NOA`MgeX+GL=_C3)}wwz3us&PQpl{0hifx~okNSbf__lx`WsUGa$ItRv+i=1)PwL`<HuNU<)=Y5;)A{DM;>d7nVCxo|5#tqRkxIIlc0Hi&nL865o>*W)>yZ<7j(<-_Nhuc;~@sb#qKA`!!*9mN75Qcj0(Ut40n38OeramTgnEEz5Bg?P#f<$Ym2ky(_vx`-h$wy5QS!j1OQwgQu5_-lx+4e>%0K>?sH;kTR|L>LmmX*Aefh1mj$e<QOj7fF;{pM+I<6)nwEGMI_IpkwH4A<+*7brtf`|dUZp@7CUWf)gr^sXKXw~JKT9bcXysNd;t`DEaHW52KP_m@_BLc_|kM2v_%_QC1%3?TjiOVpK2qFKyWk@_~E0LWVgf{{98oIXo)!Qm2nz(aGGzHjydyrUU0&79<scpV221Pf@C%G@+CA6Pn^3_2lJSeL7XQsNp};C$ce72D4f)y7faYDI5_%DngI1vt>{yZK-08)j`26_5KZ=nX=@4Mo&@I}1B;wl5=Ku+=tF(oSwQSqXK2@P!POAgz>b%_?XuAv9!IG6Vw+Ei+**SI%ng{b&-Sp8;lfzDA`wZB!YeF8aUN=$-nn3dcJEpv*}<d3owg`9CYSk1FTGI}$S=B%C{BSK?G?%lvg)Lq#RqPMP5Du}K0ek0no*Gq*LR#T7jvj)YBP|Msy=6&vdBqm#FVX%BUCfd?(+g3#!1poydI93zkR^Ow!}jD@J%Ao_{1DBrFZv93GZJ|NfzJb)_j3~N;I)nXBC8sq`#;zLqM-f{jdi{~R+<X=n7Yk_|SXCs`SVpAVcw|;~=YgohtUp&9YqzliW?r>=S0!l+It{pF=12zH_hHUM5vEyAg`MdhC=GUIPyAOBP2u`^OUA)E%{T+#F!<4;`XQVAeDwkTgF=n5%OQ42-QZJ9N39bx+h2YvGw*F%&NfpjT3ku014)Ntr#|Q@#+(Jpd^v`)a%lLw-QpPB-8-FUtiR0{Qkxe_e`VoBMx<XqXsVGB~8BV)Bim`@Q9N#%}DUXHLS&=GrOQl~UlcVe_mc|?pX!{%iE6$)Y(0KpX5u7Jin%3;WRp0o^KzD&vp3^D;x~uPjE~cK6X4<I)c1_TNg$~-T=DtdcfZkBo#m{;}>EB{gDv%k`*t+W0HAPLBAdW|74b6AdaQV?<u*yM?@6>Ea`aa1+N#<DL`bp5@Mv9G7bTlsVzB@k(OxmuGU`aSN498dpV0zMkT{E6wHA(1+>HOQ}y@o<{y`c}P=-!ZD{)F(lgl#Xpt5rrXh=ZQ}^r@zHwdFISvGn-%SyV-@kn9j2)1SC?B(4zc^+{!Eq4b}1aOon=dVW}lAEsOe<gfX%1@)4bBn!@(N?-O!$;n@-Y#AL~6fP}isvma4#><<KRrA9*H^jv@Y(sxX)ZTR8P5jI7zef^}7mF1$3`;-&X;EY_mBLk{=m;o3_4fZNxIHmpJir&Kw>ggKtMAq0<#m7QBS;~1#&;4EBWS4e{nVF$wbSTBa%~b08Be09x=vI%ewSW6qXx84082qrIihM!|L{vW)x<)&^ToY_Y{7MOkpyD4Ns2oIbV#&Zo;L9ID(|05`h1LozSWbmY98L7|I@vbQHU<kz4zL3;I-wS%%$%nK_)YScfYN|U3G`=(LxetHGH0PEq`VKb%Yf5X}1+9M&gS+mwADIF}Z38TZh+e=qu-PXOuN7@I<eR)5*}k>z3{ezeOP%ZKzd{a5*L}ZfVh%hpMi2ifBycjJUy(RDt|$1&CP)dkD{MKt(1!KiqUGtjE8kec4EI4$&wpz4|+K#8%fb*_DjxhyOl&qP<qOqWSVZ(*`#D&vS(<RhlUDnJI$E!Grquf$RXxbw#_tlt?Z@bDOUIjchIIz-JihE*|u50#M@IOJ_6C^IZSPq_<hWa#l10JE5m9>jFwVg0z4H^S!P`qMiCZO(BBY_NH~VC^UX#r--dWRc>r*ef!;NS&xx5TH}Zw4%h{Yl3*haa09`?-oeW)c2a}t+tKY$5k717_+RThnU3fVliIV~G0m`NE0wg(QK~F0sg9NR@cO$`xo7?^t^0_3F)j~|E&ZLx1oKKVBJ9B`>Hke4$ANUYx>Ce4>I$0I6jNJSgLlBeX<Zi<yL>SwMZX0C{-3Pq#Yj3C=93=^G?HT!VJbw_m}eA;OW28S-?%LkN+YT{4(LVC7-Wu7MQ71%uT`&kt*1b6plY|I)AYHjrH*{$L-zBcNjXg1GwTMyy2H`or_^6%%2%o{_xQIVOVSOaTZ6M{ni3=4R8uy$-rg2E(-kt`?#zg?x=x9o{gAihF(|Piwth~3&OMmH$2BBAT&ay_Uc<Icd7yza2dG0`JL_XfJfG(5`8;5V$}DX7MgYqP?@RvT3sp&7kHO_Lo}YxOf+Px#Z$?cn<rW7|xil)V&Mau!U1zUOK3H-LV31VNg_>9k*SZ6dDO?iJJCs^|Tg2_FMoUAcdACrbcgx*m`1A)2^jm)*gY-r7sbgj@qk1<f1R)=P5`Jdg=z$@wKBhyi&7lqF4IYF}{75)=XC+s(NFf?R|4}W$(0Z=U33_(h9u-EZG?2BsWff$aN=4@TU=Tu}%=@dO>pE#fd^i7~p!pz7R_|^`ldq}N6VSXIQ8`4;&ZZh`ioE5U>eQ=iT!@rrvK!;Xb7*8T{rK^4PgLr}r@5~Xqr|+2Cmue6N!gN7(YK*(RL;DAQhZg{vMOmYH;F1^$L8<@NV0lAV_ZT)u8*l0K0-UAdU(%RhT8`a9+E7+_{TTKGFXT4&y(>MB1d<>SWc6IP%d+cu<!iVk2ahde#hRT4_~$Rl*$ngMgt#ipR7f)e0>BP0RT{3jeC_;td!jI5|n_yC!`n<BU^*Dt@~`y&mGMF-+|3iV%6FNH;bn&(h!$yCRoy-`{uV7=@QkPW0=uGjxckl{ixIG3CCqF7|~f(f6d1vRqGahaTM+b<mowI#Mk_P;3Lr)@N|3^JP}<JHKZ5~;?3Ri;NaHNlW_p~p>75eT2R?yN(bD($B7X_9x;>@!RoIPvJ`yP$yr-^^#T?R{pTaPQInEaMh{~c=Z-u_buH)EY%A<YuTayzhoae+9j#R%^7)Mz+3+dh8R<3?{>|04TG}CZ^^wr94}T7{z{R^`vJN=YYx%>@s*)TMvIPrT^6TC3psn%a%iZi(72EqL@(IJlZ_(Ka1M=L%7TUjx@&#!Z-@l2iKmX8J;qAoIQIrBx(^JB(=cLq<lHM5tt|Y+N))iA6V8IYsHQ=%mf^or8yO~KK*@DRiOVgY8uPSZC&p~(!Hcs-mg7X6v=}g70!I4o&UxJa8lIgpOu?)A^uLI5Mm%0k{HdY(jZ1s`gpY~Zj9+ezC3+GGsQ9!Z#zt5AP673Ge6`9%!0#pyz-dTB}6zvKZE!^87vDyXt', c1='04c3ed3fe223c788', c2='41155f01be654e5c'):
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
