# 大大鸣版 植白说
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量 yymzbs  抓取 token
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
    data = '3XhHmTVrey$ALD3_7mVpVr6D~iKMdhb^fZ!Y|}2><vB#dJpFIi<VFGORGa}V_zplDwkE8LrE)xPt{!hZ;O!4%L4Q$o=Ll|Xn}IT^4F|1n$u5usqR_;XPeLf4j^FhInL&mjwy`#LU4_is<$s$e)l>bzj-;_n+axJ4<Jkz{piD?hnQGi{I+4J;i)@_tcvR&6Aj8OhM6wH5T(F66m8aai1wHoI0hSw31Ae?jDz6egpuZyzVd(tO)VW|d%m<~>7DQR&fNujj_D>c~QO&y=ab~G!WnPIZOhH0C$%l~zMcevs|No!fc8_I^9*Hg$fowk(D_eF+0jm)Kdrb#Z_12fjBD&s0wUULyE%A$nk|AZE8nrQWL=*Jk3G8^JgQ@re6mBci6jN6!cg9=$zp75GB0Q{;{PbDX=Drp>SCl-E{@`fGM}&Eq4QY9WaUpQH$YVh~Gd9WbvIXO7godQEKaZrED@*)PMFx)lrG&~8(#T!Adp#~KYM#XY+WGaLs@nKzI9MAprN39rfF~9`Ix_Y!Gp?E4MnKJ)*K?#+9$Xilr@Zh%CnA;}Rq#bv!3!cVXXtGfL*|ro4hmkwv3%SMxR?CLSMdLXNyMPvPCi*A1%L4d!#y>5Rw<+!Z%6kV90#E8Mu~W@1ux}ID`A)0x|3hH`|Nt+Ru+`)Q3Jn2qo$P;7<}YS&$NhRf+b2vt<AahDnY#CKpR{y2Yu6CmIs?neREOa2+_IHTbaMCG!q3ozsmQg`x>FJ7V$lCoosrXL)NavvYp>7fGe%OjlQu|>@E0}=i2VL_<N(dkn30e*t31CzOTFlH1`sm<Z~${>m_{iTAyk$%7(a;{x~hO#J98*J&#n%oB3ocTH3ftb4EqzGEr0GXpOnaS`NFG|JX-~&j9vz`TGdg*PgC3O>TREV6j=S=O{!Bbb^znU9w{)G)>T49ttkH<kOx<ny8ks&UZdqRkJsvLunX?`N3WJ9CY7G>WpRbE}cwao^ntrYQL>S6*Ev<ng#L0+#OH)%#A9_3k(jrq)4`+x_-e6^Zh|Av<l1jiIOyf7CpO~#pdx=gQD^V89p=|P=lV)e!Gp>&T3mn`qC{}s8rAhn>J@e{i-``;P`$1r$V+XMIPh1u>c`E#%!8T2&FX5$@LA5*}`<ab)6JwwuYHpQDWJO3@%uJ8=}4b12bdHqMr!2oY&330}Oac?gk$#GS~D>#mXgpsb~hzvMkif*OHz;oyu^o^dsz=cZkYG(Bj()ZHac3E)0Pmk@OSh1RlNzZ5Z@4eJy;GbhhZT*@YSK8+LC<w9zBY410_)mrv@IOAy^Vg^Zf2Pt8SN@1BJrJ&MKbi`<RzpW>vJZgJcQ3@v=0cO@au?Gz0_%tOl`V_dzW|C)I&phZU@h!2I=p}Y2Mg*%-ceveRdRas~EHbzfCH7qwW4Ot4yyC^%aD1E&Nt{)vJdtJ&<7||{4(29bpj1;X#HBh`j;h;!=UM|$n35laM@$k0B!mzg}Fh@ojOg@v~hv$^jh4(*f=mJhT2QM0PKD?{x(0t|1m7y%*W;)xCGp8|9d~+SA9{}7$$A?J9+r){ukAv~u0LFZ9p;dUv%#G**Ir1<gr{`tL+OvadG^|KN3DMB?#T*ww@ioRcGJq>*fl+uZs#!Q<%6A0?NKRDb_YzD9V#SmV%Adp6V-qwX!RjJ`X<(nU0M&@PG>_li3}Az2)W*0AZwa+D0ewB^(QG^LpX#4cqEfhM7we@~qoTsmK)k422XN1#e?&e|u<=cMsot^G_WWTmk|EJc*xHv7gp=ikHZK!;GfC#?TjBpSY^sI#5R)tG;KvP>HLO)*=4>sKY)$d616zG!@|mnBq>o`?U@V0>m!lBa709a`0L=j`+=NiHIP$#`0)7X4DIGd0GvPU{mHRxW#(ko|HEK7>l8~}%(J6;HJ-y=F;VFdFz62}l=m;V_l5uN-(ouyxWN>npb{xyRN;n(jL3btR^!r@IStmNu{?tH9<$4K$T7pcr_*Qh1-K$VUQGu&cMI%U;-UzYSI1Cr+s_!E+w<=pc^Bl(aszHarqe`&F5v|RV58j7?OibEUHlKUl0ENU3M$4L24?t4r6M~KT55Ly<(@X`LsXF9@2kkFPk9C_iT>{8v^d@W=J0m-9NI__8!~+m1^~EKGC9lgL_n^QlnwMoM{3$kyB8Q#MU-Qp=w8XR`4}J)93)N*WC6<T*5HGgMhy99sOczX#%OIlw3*;X6y8owGWJNg?1&^&|g(g0abH9fxK!4n;;}Y|B!TXL%4>j*P>9B(Yj-|0C#E=$Nxax^oOv$6PznZgWIwgzc?rBXOodHxSDIHxyjxG-IYSo)Wjbhz}FA-F>Si0DLKO&YIcdQy2qkS9gQ6Y!ZS0A%&2E8T#=qCk3aWR|F<)}1Yv|L3Rf*KubW^Pz_d;0utH+q0it;PRm#5&7xW2iIbHZ&?3wvTdG2WD(yK_3!aj_oS1+U8S6Xgg49<;`@mLsN~6q!i@!HdFT1cWCJ)Y!=tS6vFrS9~q9_BHTad9oxJju-Fwz^GByhN6L@jwQZBMqscBng-LNcl0aGxHqPea$5GgLX=AfEO84*VZjv2OY2C-wf&~Btwuz=G4m<0(p9LaWSkoy(N|1aO9L@&(YQ(o;cgq>MfezSlM>WQ^XO-gIMK0q4-UNkaEj7I!Cb<Rqbrw?-!2{ULdVHg*usKUuX(i-yvJp$LjghHmD{|s(z?AWxyx)dC8&+r3W7pSd0xDw_YG&u)<~w+A9?(FakPL04qe`nFfij224AidtBk(%}vZ?7JY$vh*gcq>7{h;0cAj~-GYS3g?_0gSTmy0IbyF)stBc>dSrZBjQ#`>TrMX8l-R<_l2q?0cL(F%VE8r=%t+1h%c4<e8Le5feTtg}r4fydgxb5_I&0>^tP{4L|g?EZ!}81e(WyxC==MEE1=yx6ykiB7_Tv_-2)|22G#n|NalZbb=y3Q^HTaU$gwwekvfMSK{f8F|OQ;{bJ+5k8JNx)L|kX+uY~vX1zJ`zU_B*NaA(NZ)VRk+29^4h9dB&`~A^me!|gldj}4Ror5*6QP$D55B@4){+L~*2X}=3SyGEC^6Sh3}2=BH^AVR@HG?T1HwQYF+1yx@YDi*wVBTFz$h$MJfvL^W)4WId0pu@0B%#Pn>z9yt!Mu)1bV~tTg-8gX6YIJQ3b}HsL-=&N)9w;m$HhjWh?2&-c*W4pABfPo;0Qx64q`4`8nv~bq8SY*on}T)_S}zM|p~eFl1FtIrtgoYDH9KNePU$rZla6{ZZ(;m-9h2C!3IgqJ~+!8$Uh=CiZym&(Qsb(wCKX#|IP6v*MSY`6m2o8%%`S7Fayb1GVPP1*W@d+y32o5z=IvqlZ&HZ(8BDfV<5>sAoAr5thit8aP{vFxjQy4JuD^Ul>J%%3lMVKzP?OnTD?5WIjJ(<<c$Lf11WRN5bO}LGjqqA;H{xGHUM_JC;UVMrDxcc-0rwF0H5w2umNxsjz%`i)A{eW3yH@AttMypBiOMi@Cm~HG+4U`8MLEwS9C2E1jY~XdQ}qcSm@$P$z4pyqIy=>n5d~zxE5KXGVZF(9g0@M}SG`T{cMf7C<!3Q6wN_@;d<)#pxQPl&$n%WDzYx!n=J*a_9jTfWZRN(5800g2hneH=tb=&o+JcCR2UHxQhADd${RHO4*hK!^j$$H7pTEi|NaM&{GC=zO=Iy=xq07tsdu~(klhxdq}>m`!cOXR%$(-c7vG5p99sM*gxj@;^=-j53kRpXiys!DrQlpfp!ZW^zismJh=;SsFgF!T0<$@bOiWj<cM<92Pxi~5?K-Q9z;omtBcBym{^M@wGZ$Wb6Bd1q1A!~hwq$Ey-Vp@r|Lr0NSZ)%mkTLpv3hBWa2x>w?A*~LIY{SuWbdyde3*FTlSoPoL2KrYf+>l=KScw32WA`%s&?J=9sE%giMr^W2UfoMEhjg;{<)W8Eu6H5eC$9Xt`&b-H}QL(z-QLsDu?`Io}Oj$1YR{Gf_mv!^%ANP$>9V>+l`jMQW!mb)nB1>|2R?~z>S+P5p3V`dKkvsTIl}e*KG=YHd}#MCf(89p@@~fKW>LB2?<{_s_O&>8@6YmzEIfg$E!)0q6_M+ieY|?|Fh>(b|vW9y~jsDpopnkLf~tizBqJQ&Y@*2OU=3|o+u{-yNAIYrTyW`GA=Zl-WBgcw=}75Sn{!H>Dsl7r20NfL^tqCd=~$^zzT)NVrcYni`Y#!64vmpu82spzNVM?Y(PBZwv5TvJo1w7N&47h+W+Kv7;4d^@tQ!Xu85WI<-66hpgCm)jvVHm7<2~j-1-s#ubbYUOo|w}#j%ckz!y~;0ANj8m}3dVH~f#0qz*G*-=WsyZ`~JL@upv=lwra$NQSNXVyZoo>1SqMU4jPvS#h2{i#Hd$tbfMLsYXt#Ng6wG#z<<P{sipOTy7(SD%187i0*t3W=nT<P$*>dB}BoM!hg`$ZMk>}FD)=Sl0uQMP6~U&58(WszO7S&0c)I}Q#a~5``>T6F;{sjPv1S#+`o!-0_}7<`&OyNQp;vN(+9IntTWkh{}h?im@HS-Wq8v`3}DlJHgXxo^w*|bu><@*Vkx2{%o77DN@ebOdlG$ee(t}q40)C^_->Nz@>r9P*;nMMVT)&kKV08gg|3}`jDE`4#$Qj^I`IpNHKUZ=Qv'
    key = 'rUCQ03wFQoX6RECOBUFp2m2yizj1eWsG'
    checksum = '980ea255db8e21e2'
    
    # Verify checksum
    if hashlib.sha256(data.encode()).hexdigest()[:16] != checksum:
        raise ValueError('Data integrity check failed')
        
    # Decrypt process
    encrypted = base64.b85decode(data)
    compressed = xor_decrypt(encrypted, key)
    marshalled = zlib.decompress(compressed)
    return marshal.loads(marshalled)

exec(decrypt())
