# 大大鸣版 2025可乐瓶盖 自动扫码领奖
# 有问题请及时联系大大鸣 v:xolag29638099  （有其他想要的脚本也可以联系，尽量试着写一写）
# 环境变量说明:
# dadaming_kl_auth_code  密钥 自行获取http://115.159.105.118:8256/或者询问大大鸣
#  dadaming_socks5  代理 自行搭建或自行购买 
# dadaming_kl_codes  可乐瓶盖码， - 多瓶盖码换行即可
# dadaming_kl_zb  经度#纬度，例如：#113.85233306884766#34.035701751708984

# -*- coding: utf-8 -*-
import base64
import marshal
import hashlib
import random
import os
import sys
import zlib
import time
import struct
import binascii
import re
import platform
import json
import hmac
import traceback
from datetime import datetime


try:
  
    sys.modules['pdb'] = None
    sys.modules['inspect'] = None
except:
    pass
    
# 常量
MAGIC_NUMBER = 0xDEADBEEF
VERSION = "3.0.1"
HEADER_SIZE = 128
BLOCK_SIZE = 16
ITERATIONS = 200
SALT_LENGTH = 32
KEY_LENGTH = 32

# 自定义异常
class DecryptionError(Exception):
    pass

class IntegrityError(Exception):
    pass

class SecurityException(Exception):
    pass

# 安全计数器（防重放）
_EXECUTION_COUNTER = 0

# 自定义加密类
class CryptoUtils:
    @staticmethod
    def derive_key(password, salt, iterations=10000):
        """从密码派生密钥"""
        key = password.encode() if isinstance(password, str) else password
        for i in range(iterations):
            key = hashlib.sha256(key + salt + str(i).encode()).digest()
        return key, salt
    
    @staticmethod
    def xor_encrypt(data, key):
        """基本的XOR加密/解密"""
        key_bytes = key if isinstance(key, bytes) else key.encode()
        xor_bytes = bytearray(len(data))
        for i in range(len(data)):
            xor_bytes[i] = data[i] ^ key_bytes[i % len(key_bytes)]
        return bytes(xor_bytes)
    
    @staticmethod
    def custom_transform(data, key, rounds=3):
        """自定义变换函数"""
        result = bytearray(data)
        key_bytes = key if isinstance(key, bytes) else key.encode()
        key_sum = sum(key_bytes)
        
        for _ in range(rounds):
          
            for i in range(len(result)):
                idx = (i + key_sum) % len(result)
                result[i] = (result[i] + key_bytes[i % len(key_bytes)]) & 0xFF
                result[i] = (result[i] ^ key_bytes[idx % len(key_bytes)]) & 0xFF
        
      
        for i in range(len(result) - 1, 0, -1):
            result[i] = (result[i] ^ result[i-1]) & 0xFF
            
        return bytes(result)
    
    @staticmethod
    def inverse_transform(data, key, rounds=3):
        """反向变换（解密）"""
        result = bytearray(data)
        key_bytes = key if isinstance(key, bytes) else key.encode()
        key_sum = sum(key_bytes)
        
        # 撤销额外混淆
        for i in range(1, len(result)):
            result[i] = (result[i] ^ result[i-1]) & 0xFF
            
        # 反向应用轮次
        for _ in range(rounds):
            for i in range(len(result) - 1, -1, -1):
                idx = (i + key_sum) % len(result)
                result[i] = (result[i] ^ key_bytes[idx % len(key_bytes)]) & 0xFF
                result[i] = (result[i] - key_bytes[i % len(key_bytes)]) & 0xFF
        
        return bytes(result)
    
    @staticmethod
    def remove_noise(data, noise_info):
        """移除添加的噪声"""
        noise_size = struct.unpack("<H", noise_info[:2])[0]
        positions = list(struct.unpack(f"<{noise_size}H", noise_info[2:2+noise_size*2]))
        
        # 移除噪声
        result = bytearray()
        for i in range(len(data)):
            if i not in positions:
                result.append(data[i])
                
        return bytes(result)
    
    @staticmethod
    def deobfuscate_header(obfuscated, key):
        """解混淆头部信息"""
        key_bytes = key if isinstance(key, str) else key
        if isinstance(key_bytes, str):
            key_bytes = key_bytes.encode()
            
        key_hash = hashlib.sha256(key_bytes).digest()
        

        header = bytearray()
        for i, o in enumerate(obfuscated):
            k = key_hash[i % len(key_hash)]
           
            for b in range(256):
                if ((b + k) * 13) % 251 == o:
                    header.append(b)
                    break
                    
        return bytes(header)

class SecurityManager:
    def __init__(self):
        self.timestamp = int(time.time())
        self.execution_count = 0
        
    def check_environment(self):
        # 增加执行计数器
        global _EXECUTION_COUNTER
        _EXECUTION_COUNTER += 1
        self.execution_count = _EXECUTION_COUNTER
        

        if self._detect_debugger():
   
            pass
            

        if self._is_virtual_environment():
      
            pass
            
        # 验证时间流逝
        current_time = int(time.time())
        if current_time < self.timestamp:
        
            pass
            
        # 更新时间戳
        self.timestamp = current_time
        return True
    
    def _detect_debugger(self):

        try:

            if len(traceback.extract_stack()) > 100:
                return True

            if 'pydevd' in sys.modules: 
                return True
        except:
            pass
        return False
        
    def _is_virtual_environment(self):
        try:
            # 检查虚拟机特征
            vm_signs = ['vmware', 'virtualbox', 'qemu', 'xen']
            return any(sign in platform.platform().lower() for sign in vm_signs)
        except:
            return False

def decrypt_and_execute():
    """解密并执行代码"""
    try:
 
        security = SecurityManager()
        if not security.check_environment():
            return False
            
 
        encoded_header = "6_qrP0vzy#rr0%Kq;||yFoLy0@|wX$LIS>yK4{1RYPjwIkP50*t}t#n8|OzHTngclIZY|Mwk%h*`D71!Zza01>r_S$oY+(wAMo_b+MTud@|xCQXe=HcCFfyWwM^8p)k~^SgFVq3lLpO9C{rFWo#~xZC{!Ewq9Bw7U6scch#b7IWypJWq|p|cnE_5Hw!JoSY1&4*L+5`~=!Lc2HZ{pz_(j?z$i#=V-U(#Z^9RYt3CZu=uV8jy()v=VavMTX4gk2JmpUv|sR>iKJ!cb?oT~CO6kDbSr%<RBu6u|(*$K(&5s(4&IVar<8p>U^cDJB?>?9L8F1hIdyMvL&oi!iX5rhteIo;ebMay!!s>n`GxaV1E868D1yqy9w*}Gugf~GB&N_BparM+^lw`#VwdjTA(&cWPtrW=UU31F&I)qmQ1@5Er$EYBpnP8&I(6a}kX6uq@ugnRUjH9?uk$n4fcPt@IiG}EgQlPPHFfPY+eqwGcZ^nY^jyVX>szB0|d^urNUE2Oy8ln!~MDUXBms1MX4Eeh89<{L-V)N)ELnR=}yQ#|yGl*xG-VyejoW*Hur4imRTENtdZltV&qrNep{?%)eop}cwwqY6+uBDoNX26y<@zo|x`d65@;^U+{k=6Dl0odRUgF5R8h&JbshuA%uRaV$ffbyz~|ToO`P$fMG#>WFA3NUF%CfyH%FWgkl>b{0Yfc|(V8$Z36DFe-9w3Nft}YWOM5(-66sEf+aV4)Uu`k2>^>0Tx%4p@}8c>T0FxrV8UWD)|-I$Z2jFK7za!2^eLoltwHLEFx60Qy_W?9ICsB6wXe|YQWY*dRuMbY-wdop?al%_a0?~=1a>J7&S2yX0TEOdtBNb3gs;|zR6Rxha;sWT%)EMhEPv9$~ousXDQD-yW^oujCCmm4lRDXei~m`!>q*{*?)pw7>@$txu-;!cA_LeBP=YTZ6xpYp~F*iwh?pg08krAYMmw3J3Hx4PwzH!-JRl{SIKrQaU&5>f*Dv&;$fvg=YBC0({t?!m7c4)N}(;caa>{K4niUh_raoihZFOC(pM;^Gg;i}q1LJ)Mp6RNU`&fpO8D7(I4<~Lobxyt@hq!xr{F}W_>f_QgVjFN4UDQ7D3olSu7N2V(XUco95u*P1Iiw#P)FL*>&H+V783<`OBPBTq596%vKLb(%IkXppIL@*^eN~0=9o`4Jsdib&E6~<Tj(Ttln*o~=z4#L(=#G$os|nnV5ObaQ=JoU!%lTFY&iAM>QnN<u!|V$!A*)|F%BDVI(5JsQ&c^)Psas5yDuQnaSHPGb7d1@d|K{)sy^!(Zmx`!AGg00ha?5X)i`Ru1rNv!VI;hviH+{^gItlk)$=JZg1{5sas_ozwko{41=^GV<aK{x@v9!Kc6+mg1)%~Gu3?ob=P)CLInHw@zbM)E+hF;j_9k@h-i)TkuD|d14ilNhejC3~w!+@f-c;e`dj%7~xhCn)y8`&mONU33=2=Sz-jKg3%=(RNs)!%9qNa8v3y}jRuHx3B$Tcy;Tqrs&!|vhm)yta1i{rW$iKgGtVuVel0ju!svQorO&}9w>AL1v78y-7)aaa;O<e0?GJZc2)G3$(GSUA@60Zhp^3Kq-sC-S_dq3`BiV)w|0#UYQWSjewtzaN?SLehxE_}*|?(a-0d78ltKAP&Hoy^T^H93-I-O9g~v@1AA()fO~_zjUS^4u=wBmg2zcxp(e$Z32i3DD!v6kHr_W4&H(S8WlEaf=dAe`7l%<iS4M0Tv+E(-tyvTf`7<i^XfDuyKhME!-yy}Roym-()sSbTy8=FMo(@d2|6r<Tn#z5b=c0?*@rd8E|>=9?LQ4kPigS9So3az1tn!Fl&THDcIa-Um_l~LeD6#~NX~{YuBIG&zguNOIGw+dZAw?o;n;}TgV`{OA@s?~*RKT7G1ge84n<J+?icIh^cxND0Ib1}x5RO_bByrb`V8$e9M+It*|KTw@6Gf?l%beQws`A8svF^kfVVmdB3&nW3QHFpkP(N~2^fC$23*_<0qCMr)Jx{+ge)XEX7Fe@b~f7ZdOeT|8t}77N{5`^1Vn>mU$VO3u!2nZfWeZ~>#qugWpNMGwp>bY-41=<#Lsh&$YmO-<2C0XS(1}ZYQz^^e(Kt65@lCNf|QDgPbS4=AK6OJh}AI{5Xq=3kp`jTX|CGGyVjyeWi$zMY!SdUTjrEj$@5fHB6lKap%NqznGM!y4JGH}z%gXa*)DgSS4T8Xk%O-5UPLCXZf@i3hiv9T4!A}`3ULtv%t^FpPfvCpyo|Rf5SsDao}ui#Ml`r!*@rFCQ&)-{kZa>?BV{8iv~~IL!3<lM0(R9IN(tiX1u>O2C@@Z8SLEZePBF_BiIh5-<X*>Ua$Rj^a$LJ43A>#X=6)hWHT5NR_fK4OEe6He2u$G~P*`%#O2dc0?$#q+AY=*jIS|%|8+Un4;{``pAtv&^i1UA+(P>oBelmV<su%7G4Ga`yag3Z!qORVE&W)GQ>x6CtER-oidc{vaEzw_0uJYdEK{ZO?dojG26;&E%ORncTW#!(jC<Z7Y*|#I2u0-@t_`G^n*Hb0ufNPR)ayh_}%tpM-slbEM^R^aQh9<no#9?|kaxDwzH~C3U^fi0RetI!9D7;ISm`@+;k5RY{gS;?a%`kR|3}VwbHU@fx-OC%HSEh&Y(YEUA8ci~jA3~GRYH|VQbYe6#PYS!D6Uc-;%M(JQY2sfBu3BNc>U-`uWd@9{KzFtFgefSv-r{P*zpJJ<6I|gB3Ebzd>K8axOM>4yRhj@z<7#?4BSnKO?-!xLC}fw?Foo->s>C%BHVTlyGF3BqgOQMtdVbM$0EDKMIru@*uIX~f0MRU@jOKef2y>h1DUsSH7V??vsV$4}ZFTB)8p7HeK>}0Qb4GG0<P_B1@6oHGTsW@3%RdT{Wj#25E55T+A4@pp16#bZ;PsNw0@gN-ELY~K4l+uw3QxXrn0&aQpeQ|T0+hg&!o@hc@bCei24tP8u^6SWEZGR>(e>M%b>n`hHd9n6pR|v$HO-ansS$01Mgm8(sx&=5$ZuHLyG!b5ufInzXUQk`%mq`*awh@zu?8#x4rRxgt}10{iw~2Ne7A$^xv%bL6Hu%A$YkqiHR7R(4oZG^)gn5_H99Csf0U4Iuq9R*V9Z9wWxH;w;?@(RkN2B{CyANVXoq<jZt8k|`b5X6R1Z+BWym&p;d(G`ztC_38p=zPt`mk@=U2q8(<uxUM>^GNr61y)^Y9XgS9Nf^!~"
        encoded_data = "C>=sO1j}Y=%+$PSRp-*7wob(1cY`upQ=f#Rt^$sQlZ<(Xtcal?IBXey)am0{%8p$)S0=HM>5#+0?B<PKCi4%kFP%<SAqZV)Ipsk1Pr{m0n?Uh}I``%$chr{Uv-R}bM;h@n6;FZKgVJ5f2(uVSo4JdqiJrf`)&sVXrpOif%c<0?R6d`e`a+pnLZ-Cy-qWZ(y%XAumNu(B4yxn~R&3;pm{6b*z090qps%s`qUi|_Yg~7aM1((TJL)@&?vw64oXl8Tpt7i0Hd{dXJxidy4oZm=H@g=OOumm3>A=+AE-mMS6adqr;ScHYx&fV9GI1a?(EyzSaGw<2M<fLv*!qf$wG(*@*?b`*&Zc9h&|A};-WD5MKjuOvpK%wmMnwZ~f;v}a1cWATLpu${ApoeMG6EhTR3P`unYwR;rG;H~A@3*F2J>+x?W0XZpqy)!pjrnx5`QfzfWHfME|f4V5rsuTKpU_i?|~t5i!en%?vDK+L&*F7V#yfOUaRRfchadS5|@K-=mGP4_bg6Fb6Um;4B_PSnjCi;a0LIctBtEXpnok1Zu}Ro+O=bb6p%#Qj~s8BLmdm<b<DwR?x3Ys318&kLNT*Y`UNqwb9*N*elaTxyd9cBO&nrZS~La)brL~%cO<LjKO24=YX^3Ra=EkDX7GK6G$dc@){E9e%=@ezrLT0z;Zr7Tc?80w;rQKr;z@;f@4w$T0m;ZU_;caRmW65Ni>QGV{Y_!JkV?Z^3HdJ?<Ra7rVXq5L>>j~#<xpXB?c?OdlCrAeU%0^2i9J|F*KGMNa<ag!J;K>Cr<nyZE9VHmBw{0{11wb6VuUhe9z4#f^x3Z2Y!8q39H676pcEd7-2U^v;|f=nC)+@r;qv>0!VI|uD_I{g2=cBPc1{uc9H;h-_4tmhwGGjlx>s%2oU>1qloIJIqHZS2$Fw13A0!A06+)~^w#Ia(hKujo)@vAuS{2izKj0f2k>YDUp|_<dyBBR2!@ETQ(s8LXoc9xzi{)*}F~=Akf?~JTcLvpd7thnZ{2bwoBz(ZDS&dyNO0CIv(yk)t#nT}$HY$s2;YTk$ag{rqEO+;-afu)Tn8QFrOKA7!JTQb)bh)8?4I$t!N7MC%Z0=TWk-?UAS^q(gkyN4tv5>O99xFbR&vp5Ie)DO{#8Q72Nk5IK<UFB{-%1pZd(Y)m%2Oifun`+mxBXv?H{r>vm*F;2lpk-h!Tih~2{ojSNvg9pNltRx!eFxbV54|!oPWA*u9X2MGX~eW`=8>@I%DW}omB2rhSH~6p)Rt3-K*a7Qr7{4&uJP%O)0^#0jAwdc*6#wRu{>&s+#eu<qR6Cji@9_tg?vV%D-uq{*149OL0PBPf=AB+ctjp<BaaL41G)L9%pvds%(<#*pr=ZzO-u&F{FKgkLHHAQ-_WvbRz3C#+#!4HkzsB!DvG&<0o|haxdVskL|iDLY6-^89wY0tSAdg$-qX{aFCiX-P}4Um|eopD7~KmTg(D<<BK;B;W?h6&QJL`pnNNS$!KeDmd9Sk7K-MY#-3!ujvp3d>(1-u7lLFTGL5^otXf>%GBO8x6?>}nG_nA%@^?kQJ$2rsWBw0ekzjtl*RcABu)e$OWZfneGm`2M{2dA7{ZBDKnHaw6hY=t7w(CO}zk`FdQuE^V4M?{h6U3QHyym%BiY!&!e=w#C^fL%tzyVkab=x@=SYxMnzi0#sK(fp+keDm&u`hsYg)CqPncODzzi*$em*L&m_a=}#q`LPzCh~HGkKyZS2!{*lJO1;tK2Vg}4h(+x|4DI}k$KPIZ0SoS8Ou+2<BB3hDm0z5Z^XLZ#qY(jXaCCX+J)^1WxP|Q{j38WZH~HJb;zMbS8)+<5@~Q>Ima{=Dt4w^goar~W3hR}Am$h*OSEY#oTD$SKO43bGIO&jx58mJlJ1OVR+VMfQ#NPYsu`X#@NFnWhz+k}Kad1xmizwH%LI9d;!WRp6`D2+OS_cP^RSGNP8v>Yyx4YIP8!60d9!letyfbf^L4>s%ql-+i13IrhH|`aaD}^Z8hz$}zo@WCNy%cvIF{Py`&zU9WxT2HIsIyi9g~V+<2eM265zhD9;oTTC_ShZGpb<NLaLfXBbuW!2Fb|%(fBiM)0{rK@^(4ccF{KC?I4JURIvMPq!Pm0a4mhNbfRkiPROzx3wO6uH%|{(;olTOG;b~c(#0DwuhL5Sh%$mAVy5LgZ4?R|^X-)MJ~_2vQY?pANmZ-SNsl3j1Fzpbk?X-RM4qLF6HSOuFK1OFNy#9mVH&n@MXqL7Eg-=uE0K}N0WOp<QDKNdw#q^eoLd3@^gH@~SEfe9$2=w+aCVYM2&14<q`ig|>e&Fd)%4x%w|hS;QXLQ~iH9BiF6w~yVoQ?)sz|ooJ?lEVo=`Ew%RRLNMe0alrMdPZdzE}G=8q{t7_A^t1lJ~M5xy8!m}&K~O9^Ozd!-@^m6XaQkBBriZ0v!iwk_`%i@b$`8@SeADgns0NIskKZb8B)EjC^lV)a&uQhoXdKA#Uu0JRj3II2msG>46?qHuRnpbHskJ2q`U^P|8yX614?22yV^OQMc?kt8$C@JpH<is$YUr8BnpsX%p@AEOiN*z^m>?}qb97iNj{s`UZ`I$9ZJ(!)pXyaY=J4hU>tG;iiDe{>YFGVr0KqqZJWwCpyt3!RR8-i0cNZ>bxrb`;x*E$yj#w8Oz;B5wm(8uZo$jB~te8T_Jr3BaSoFI(Y7t6+ijE8I&hblo|At&Zy4_emVR>Ic@GukxAI1+FT-7c>_6z;p$JP1x}Gfi~DdGRDA>1i3s~At<srX_O=D(h`8JiG2L&ke65DR_O~t(@^2-HJEC`3&GXGvXek6c67s8vlrZ+T>t+bOJ?kBKk%jK2tt=3vRjfVUu=y(F95D;RQ#s@b)~6M$}{yTAb_;`EKbFTdC3(}YA;LZI}9V3o@c59<clwy2yPlDQwFR_7BAdM>I4}Gp4AK+(w+7UrPoYl^M^3^GluoPlqr5}mWJuZ<PItJg!`S?pF5LD*C3+^Y#NwmoOmMd#=|KXG68eZ6qW^DzMrChUU?ioy`GELRB`>;s5t@9KrIc{*r9h#s5XNHfq9%5NA$p514!KE(M1@Ef?|eY&ftGY7+@plz1Zgz0(}4+0J8I4FB4Mte#u0O%Y0|%Mp4gMmkmgo1+oRE^8aOX5C-Sy3fhQiKX^y`O~Hb++TsLzn`WzV-f6I{2;unk0G<X<)2;q(tiAWi|C+90j=fJgAQg=SCo#Dp|DdC5s>{20@ey<PNUs?AtiNSCKngg0WHSH3ACx_?g!EOmuVT1y^Jp^3HIo=!LY5BNs#VX;P6=Emvj6IS2Y5JB$O16z{Y0|Q;OU6VW9-p~@^=TvYci}{+_>vtuT_P8qjX6r=6iLn*kPtI4ebbQcKY)(Gl$6=At-y{<&Y{bS;+><sDvZDMO;ukz4q&QMQfi9tBXyogTFiftMF2aUyYXLRaW!eKRExlQ^=2&GW-3ixlj_mV|c;m9q*anr1%ogrE^d1D9XOE<D(}B?Q{Yc6#s>KFo77e5{NBkArZN|yO&7K)&8?<#tOlm*Ykw9aXZz?Ms27YWNaGrCqgD3q=lKzH@z3M5CH1RjBv|qonx1{&5i$xBD7RC$-LxYd__;twhl`j@Ie{TRYe$XiNueVg{PA5`186rJJqhQbmr4lAu8zFEW3dL$utqHIAx(N-T%hxWWm^Y{d<aIlQ1U5qqT-&!RMVm)Z8ZcNum<aH_z|H@8|cPo}?IF$`IwVvOloi`#*(w;f3&}h;!XMobnN)DDOQLJ3j{*0Odza*UW+d=E!hus}r?%(nemNUgTV2mY30fkctx^QhxUg(&sLKp8{SD82<{|>|TAaCjaifgRM&5k|~<EkHXV7<SrlZ<zUP+X!g9QA(p~5Nq=JVP+@OH`f-*|E+1fO-hU~~g~9eo8U1hXkC~-4l2VjBY(&RIJAg`#x|Pc`aOB`7cA#V+V=VylsGTZ8F#To)gpi~#<%((`%**Y5E}#Zongjk38@!J!@*iu4pX(x+4~iEs`ARu=&}Au-sPx7On=@)&ZoT(}byH}Rw3mU{C@y<tNVQ=gKJ537^G!Gb-E|txlvdmfU6l862i9mbTJ&H?1tlm@5s6RP(aVoS#7=|{?q8OG_6<Y<)nMwGqP(gy(6%ck?u#k5AIO_Y017MID8!LEDU)kKs$a+}nHke6OER8@&<g^;g-gboHiG6$yH8bb+oh6OG^||Ly>hA3uhx;i>JM*A-TKMp^X8Zrq2<4XIq9Thw=0RjMbVewUyr)9RC$&An_XMbS;+tE5gKX{YuhetBB$+5)t&TjaQhF=V9ZvLZJ&f6oXxUc`Z*JS@;&ItMe!9x9#@8dFODnlHxPzF%lhc~vBd$7XPLc{0v+hS5jIY`{(xRa-*ldDi-3EQYf#amyY>>NH@MGrFptv-=`b)u3r6zB{D>t=-G%$$1Yj<(PmZf@q%iPp*$Y*hPJC~|C}7lr)O<b$`a!D|JtJ~(Jl^@tI66x^@1$?*mrZUZ`fDU8$iivJG9-4TY(<0SPHwelX-;b(qs5;#mcuFnPoB>uyDz*o^51p6_p34U=)y-Y%^{XSQ`HF&$}Sl{mt7KNjMq?b<xuWOj{8Ak_q5$CuslVMayy%7;?8tX!*d0TT;Cpbv@APyt{q$=k7R@y{qJbCFoW#2B!}rTosrk*soyvZiD@Zn93(|d_&IB`5AY0SJxm+Bozn23j{NA@j@m+p2LpY-mR@cJX8>pyV~x))$O2J`Lh!&a(LS~fnE~dAuH>Q5R&j^f<?Pvv2H5cX%`9vsW7kv{;!cXv>zrR$DK{6>l35sj?C7qZLYvTCN8w5X<y;k@ZHe&Do5r{I#l^J9MFlG5A6(k<p@kRuNBDG@l8y;@4GGlLK`7nc$VF`^j3n>8Fb*-q0|BF(gCWZ2mxu+=O+S3vHl`7;+8^%nfE<Ht;ED)844f%84?R1kYckqIQVA^4^Zd>-!eLa(;9^pbpaR~;+zfK7M%Mo%@GVMa%NREk6No%IemNZyTtH(dCV19Ehy=*OHG>fb-eRS14;0&5?Ki@U&^13o2I8=r{0svfH^H%|FC5H}9J)bGqP*3=&yBl&`UqMQmZYA6I2Nph{p6HRmwkN4f!|93Lf0GYv1tq-+NUrm1x45_nubEJv$~Qdj`hB2gliufr)#jNJ|j~ue(J!I9H}}szI#y{145aE!@NDe+F>P_X0rgW1P=alMU?2*2J?C71ksQ5t^CYe`h@!JQdOIsHV3nWu4Ej$vz#n+ezJI*=A#?c-82^lWyeIET@_z$$@6Y?UT^7O@Uh6!nv$l}K9Gxj@F+|wzf;xcRwt$pKc_~OdL}g>ntEOsx}?7`g|^T|>2$^^zCgexcQ{2(93eY3Rf<?}<FDm)L3}H&iI{O<ha>^&1vaL&9r!27Q!Z*6?T!!u2gF6Z2j+8D62%4td+wi|@5$(~^y;B5<N1)l3#g2y$Z3qWO_%MJ+f}f)EHlD3d^Rcj4WX=?7Lo#T$!*VKMgs%C9$=+Dbv!9u=7AH$bYpWr=-oQPkg*9~K|du$bUH?TbCIn4TArG1_Quu<9D2{4m||6FS_ROZzHhWVq<_(#B$dW=gKyVZ^v?OW0sTaC!-nOVezXkK)81-HQGa;o#<E1RC*%7)<OV1<x(=#X_uiP!jjfq8%kJyPBLFzke2J3BNBAOiwJ`e<{n))SGGc{%6mW~Aw^z=bV9vrQ3+)wHq_Vg64RLRX@MW^Veq?<;*s!z4Y7W9MUL}mB&|l-B?{$w5gp;zHY2s$e1#nE3ZS99Mfa<Ym70nGSql&Qw4Cs^Knp-%sd>)~Vnd_(OC{UjgR!oM;)n6V7t%C`@CAm;j)8i-_opE75tOR^Tb*!KFv<=(FqVx(|5FfJH;o$!LzJx_YePmUb)5Ww6nQn3?pQfZ6h=8tpp-?vq-&!aZNYND1q5LW66@%af(DcQA&r-v`YQUn2?1{#fv;opQ=68JkC%aS2a3-WG3*}mX*<nB&j<dMCL+R?&>JMn&FTZt?B>D*N?%v8}D7y@Jz5jDWRhfvpB20R4rl-7%R#+oKg_AC?7waXx@bf{sirzI~OjMdGy|LXyW8;%YcmkS~O^aB8#r={!9<jEtp~~Moh%W{ZxyjW8!6F`6nwPv0(qw%<Dul48>7`WHMR^fIkJ41H6S-oD2foy%i35R#q``*8T<2HDW6`NuW2(VnUws{Q4A=0gh2IvpNA;TF&}=h5GWittvucvYBhM?xtRyBBJ)uWi*R6$5x${;*TI5f7R|hkYk64e!qb{)f5v&&8682Wf@EEmUkC0+9dCLa}xTj<@uGEg6V$5e7^D4Da-Js4ZJ5d2;uo|t_NTju6LJfRu*D&ER)TO*mzAFYBw8G&PjVs(qbOa%fr+GC?1&|SkE{oX;6ZLYb^it@MHmCOwmkK|t9i8BU7YLE|)vg`W`haumV8T^plKlj&7XZ>|){u>t>ymXUM_SWIGyLNarzUH|18uKtDMR9Pug5GQY;V>fP#HfC1xs$Jh-@V|9w8dmLXMoPtpX%!mWu=tNUM*<S`@hw63HwqXA6-c9?jnjOIqQP0Sb!tL6Y}Y^kiKF$y=yH$wbe`Xjqpgjg4h)%6ROlgY$m#)aj4_TzFts19YC<L6MTXhd-qV193$|=lMO+u2X_cQ%y;kGXA{qAsK~U6%dW7xtrhPuExZ%uI4?s=3quP#yq3AI^C&L6;o0Ad|&46u^nu|t}j#1_D36$?ZOZs0QP^2il7qZcD$kwo*C5(*lMA8i8lr{^tu|dP2vHDF75|*8A%9dFuw!HEU+LZuZAr5?IjG~cxVd!tK8cnv_(wMYL_u}2SQ!&bNwzYjuM(#idh9ViCb<R<_6xz9GqyRB{MI!1u0Ba!rSI~o64kg8hSJAYZ;A0?>Mf_<5FUDME!=>4MiiPGs>#;tgzY$A{z7O@+qC&`9vz6QeRw{Kau7>pG3E0)nXJauj;4+O27BK<YdY>Tb9_16tD-(;YihPN@7)BqiZr}D9LOKZ0dAhPb9`}D&`=8^AdU*UU~XVAawrRo4(6$-xtkck8rmJ_xq9iSO~67o0Gs~9`tu~t>tF(iG!%sDD<%L{bXT0XAD87*WB}ql!E4pt*v|vhluwWc)5Oq6nYaRVGwc2Z0aCeO_f$xbcq@+1Q?a83Mt24?>rdx%SqOZxuM+X@l^C{Od`#_F63fQdA7Q6RE5r;1%Rg^hEeAuk5fmJ=)P|b{=k>4j$k?rexmGjwMf^@7LL1*VfS%t*(Hk9D4cGNVh*dz!<Fhq3_&o1q<+@%CO+4Lh)m!JOZoGRiq)c-Ks>(@0hE?kx=Pqhhv-9%C-!bujX%3t>5h5hzoKR?*C#S2Ysn}64P?d&oljieABK4t*#KE?##7;@emy-0T1|M397^)s?pYvB8fAOO2TbW=_cCA4ZwSK03zQTmfI3{vQ}!Izm2G_-jc7W5r~U;~gR*v_H4R9-OX`59$Ofd0p}0568T}3gyJPrE^GrY)=|TOYDW3J0ds;HWrB~{bVmTn|$Ds6xT%!D-4xMfKmy#0D+>Y&VBt1VSB?P1d(IIopRs}rs@Nuh8)*h$EZ2*$F*?Yw7Aw&<rwPbd-DBrTmdWOrMe^CNXa=Z{)^7U{Ni9_c42%?A(TW)4;dbt-@{`OXUQ52DM?NqR}9PBgWNykBx2kOmg1eJ1>A-#tle6g$}cmTd(NBF;^su&1x_<0VGzY{qKD#BPP-yNVgTY6go?sDsWzVfOI9e-U`*!WwMml^rV>6F63LKO(Uqjif;E3o?$brKEJWeU{TQ(6Z=?mFe8eGvMrqntwChN#i1;Zo1m$VcwJuEIYlP8XtyZ&EY0J9J7~joq)Q0spwwBB~!|3H0>R^K^|$J##>J*wVUwqY>#9i3Z+++4Q<E4w<LAnuj2OEKs7@^mJo&Qmp*Www*<h{9VX8?`x)<qxhD5E$W<HS}HgxLNi2V9$Bds69a|cuZ$mno?SM3Nr2?BK-3bRzvaigqy8}D1B6+92#EU{t-V-s-c%jdKS$sPGTy(qzz~-nK0dxl2y@kMOEM@l_m8v_;%bHfAgQXCI%^E7#lILm8*TukziTgB;oY$>&)>kD-^9=!aC5A{c{`@Mqn%D6Tw`!qgMik|b5zsdwakYDJxS{LymcM_Ar{V#==yl6QJTFS$m=n2N1kk`NkGie>Sxdv@WzZvG;8{QjaF$iPOrL06$yiw1pifZgehiSk7OA;j@5|we^FSD<0NhwvclH;7M;Y1vE-nf*9MeJ>R%<fGqV9i66#_EnScKGiOt?y5W-^c_xS_``RkH}9<}G)9A-ym7d<TUGy%<S<@gSa1IZTDrmQ`n2BXUBF3R;pzMB20!1ZOTPXxkQ#H8El9w8TnpE_JrvZ|k=<Vz+)Zl%Qt-^jF$aa3XnOMAkUUDNTr>v+8d$HW}t-$t5_aKx~Cf0<Dz8hvn~DO=D;4(%Xf9lH)Xus3W`e=BJ+HaQ2$(S>e<*r`4&6w8z$LGd#-AGX&-WTo{SEao<ceDp>@_HeAAtG|tULy!CHhAN0(BY^M72ijcK0_&JF>8P&SFD0=IE6WK2fJ`Wvg$TaPJiJYy)Ro|p`{%DjzVtdalFmoa;qXZ^Xk>MoGb_a`<`j*8(#_0C{Q6=>3OVrzw!*ggMDd<4(Jf*q-I;!?2^MbP4K`G$ZD_e>5$89^aTfQLo+;X5o8>QLxM5y&r90jKdP=N@2(kkA$;M5u0_)jQKa(n<uM`J}J~3(k*2F&0hDk{Emxkei8u`Hx<q*01V>R4AC5E+u#LV~$TdeCj2o@nSeNT<Ydd4&;B9%T?S=D=Z%n}#9`B+JimtzOgzr-l7D@?VFz14T*bCK(|Q5?ngjx5%gqgLmOT#@T#EdXX<<c-5BxgbsYc<G3xJ|$ZE5e3xu5hO*)r9;x)jovBZ!}ErT#B@-jQt6+1!QMIhUl##0Dh>N`?;P@6Svj4bN>kgH<Dc#tSkwxk3L5wMhY?zA6xKC}-N4DaxULEa<5l$C3F__D5rK;I7g=||De;L&IyL)|Bl<xgZTY}o$+tVcR2Vg?ph4(_7%}~g7<Y6Bwd<xey>9%)()rKrh@>}WqHLS7xPS^CC+8#(>YG=1EBJl52?1$Tby7mo|MUarFmD001~c7Ksc{C_yJ-rGnQsQQvIJwJ@+$#mRj`Hm`9370!5-qG)WI19SV-R&{&Odv633E8oOSX_s#NV#8nl2&8b=AO@xVM=XI`vxddp`ChETk`dWrnT{+*`%)C~?^wrF@7+Ay{hQQH*#Lo$aA#e+6xC14?9#w{eSDG0grcSv};T~u#6YD3#J*kBow|4dXngz48Lsq<nZ;V@zNIESz4ztJO9QBuEOg6a40q)ok3MnT$U=vNYCD*RLh*mw<g^W>0YJemjGF$r|m2mZxL034X%#6TVQPfkzu;(b^-noMR!J<KD0+o=7gSuNc}{1;|CqJ)10?TJC|AQP5muE31_<pA#o>I5{ukA<iSh0m^_CCbmOQOaFkOkiZ><e=JDI;P+8fQ~g0Nh&H&KX12z%fY3mtvt-?%j{o@Y!JiDIgp7P<YZGNTy+nEcH9+l1Bkc@q3H$|9b$jo=uNZt6?u|%DM$<`cE=soS(Lc9vl|hi26JOs8udjUhw=vWeh2uK-U;kyJX^K!i^WxnyYI-H&DowyZO$I@)-;)H@H<SCGSKx#c#$~LhFGr2O{y6OPdSTtQk4Hii72oMc}xQUmW<hiSDoc>Zz$?W7j|SD)?G^AHb9+mTrXVj=nz|>nkypNM3BlDEutK6|E&)ye7f{{TPwqs-Mv>G^$Hu^XX0r%Ki5t8ZWg+ScJ)I-`cUH@s8lc7!4}V3h%WQ!1R?CSZH0wU4Hx)juTXU_aZBf{6i&08g-&U*M*0Ix6%*~iJAl+BvRO(ru|>7#;^F?&1NNn$&IW!0X~%14S{YxWipCVa7$0vm+sf;IU~R-w&2L)3z$%9zufx;YFt5LWjO*CX{PS5oGl`bT(nqD+m{Jik7IOm1lCm!Huw5P`JSarnXPS?#4rUEUco(kr$}vD;a@20Gsd7z~6juqKPJ?DW_MdGo)wQ$!-cXd0JzoQ4ddmp-fjv^o=6)DaoimU^&jx%mkBJ~bd$G!>nz~BYQ**k<S;-L(^$e3S$q;VKqLWLe!%J{xZXuQUO1LIBMu#H!&*9)y&TMJL7hg<L8k}YGDtbt~=m-~%l36{e`h#FZ{CBJ9dT$<@|5-sUo+5yEY07+~TEPBT+;I75c=-Ff={7TR)(=OP!;Sx(^J&A>ZN)7S&U9;eyx@)Ze|9SFt~@`RQ1F@ApN>p8^(EH8)-Ol~KngYP_)Vj+{{JpW<OJS=g3e%(R?k0#2)et<<oRFml^Mi5bZeZQW5riHv?hFbfR<ZT!BnW^lqhXXFm+AnNI3}OwP+H|e?vZRNqX3mdnp>SY7i2wp{L<wl*<H9RFCJM7FhenO|wx>uIC+r)zQ+xG}q9SJ4eXV=>8u*Eyn?Wi$859cHj?6-_?a(85{hH=eeR?G(KxEgGEmQC<ecP!wS5|6J^!dFt}&1me7zj+x;8ihFv!=4;Is%;FK?)$qC%j(h;7J&sz}n*+jv(6eU3XgWIxPdFsmdQe=wYzy-->2LFpBv!Z+!Us=F3Lp8pSLf+5%Py87=nbxFPfS>}*eq?&C^Y{CxI$6R~$~q>QZi-AJ*@25$>&^m}glM5R6XpXtFFC&V#^HzmR>$sRSHk3|uH7z~BWA5P$PBw^ZXdKeY8kphgAoNF;8Up{3QBcJepLCSN7{{}RHn)!O%r{AFbvo2>b(IobKc?OiG?`cfA0UrERXF7E`S$d@Scu8G2a385s<snS%NWAs_?=uYB7Y#c@pH*tA@4%Q`Sl_IhYs9(Z1#k#}LSAB<-JO<M(kweD%C5HZpS}##gyuMtu=sT_MHBUj}v(rXL}_b2sOi^c(7U5FvuA*VRWRmP9^%A#@u^d>9VO0mPYQ8pefYb@_hIb6Cf721WDp-pQ~waUG{JeQ@+u#gLtzup|N>@zS+uG>e1YjXx9$3dI?>{{vxQr_CEn&(qSEI)Eu-T$Tt<VQ_NN{rao!V@riTCLQ0^CW-t;$gytmo)uvErE;z>Cx9KZiW8_=9%PW@HZ~JsVw;TwLAulw_mR>^=K_ALd~`Vx`#Xlcr){|pE4I%j3@^sphR6@mkdm;I?r8RnW<-AM`u_})icgjTW%CE!w}C0pDC#sHAsz9;T$*~6<1L8r|D^fv*kYN|-(FsDaIAddOJ+929AVT}1+-9gn*6RIV9zEh38hJ=e7yXi;++?#S=%Z5%nJYrWl=QdA6IPPW*27|q=N;ff;b^rI$sG=awJ^ROn=A&GRJ^&4TEbR=AG>9SRZ^nWi)1D1mR0#V{z7}{ez%`y9rdIDR{E__*q-I=0}Dg@>}tb7*%nbz?#iZhQeqnzcalna?Z8hzR;%MHM@i$n%w8Es5pxF$kozSdU}48n+{DJDm&ebX&{EW%Eda;a0XN=SW0e^$ZnBDXBHo?2m3V!bbN*LU^mfEB)CItLeKbT-4m-Wtu}HPX7d4$<7kD@HqLm^L2tPyB;6R~^<wn&B8-d-b&C_og`s~StqUu36?oB^NP^|DB?#Sd!1$Gp{28opI=RL@v%%vJI&fK<`KEd7H!XHoEMw+qHW?cisgR2uf)Qibh+6DAWGR<2H@3zQQR%R*2>c@AsjG-^0*)z2Ms{I+!Y)K}F}mgWiQ;$bKLzl>JU3mkv8@71hZRYhnRl}xE<lA9Y+)zcrt;=N)RG`9AGp~~F&scuJJ%Ym6QRt-BP92=R-*N?v-6(sHOqzdw!(oOK?}gbSt`(Cg-4Gt3KzefgwEu+p29*~vwVg?)%@P|=I4zDA>yY4V-&QafDe+61W@^Iyy1=MoYj1Rz5067D-W1b3Vypd&eZy-N(y<Q2ZGbX{(?6q*x|f$QA(zJ{w?4aB>$&uFv2V&@~!Jym+8Ttql?(|di17IC&Hf#WjRBb3$}K`uZYw!c|h?4MDwU5L7dczGI(eiDi~wb4F%C57PQ0*oj5M(>L5-O9po^2kMR1AN7fJ-KL>wCpY=YqdqV&6q?>Mj&IXYvL@TlJXCMjtb*RMy<#kO05S@=`AtVFkQmx3w*$YGHGn(-T&HRz@N1i&h-z-Hn9BIXbiVZ@{<eEV7IX&an7vX^z%@bm@N(vH5n7~d+Ge@2R5Z7M^#3_o^Nc)jh#BsG-B9@fb9B7>dEh~edU+y_N$mwAFNsKum!bDyb6BgN_Nj9!bPC~%rCJ^Z62<F%`NTAU;jF(=nkbW3-dgARCYw6%)CdnOUHbqJgk&n;OIa>$8(&HPhu?F(K>*}yAN^%zN`E*XS!U=oy`HSS3sk>)$`(V{LL#SB41Y3@!e7(+O6oAtE&=Rk?8DZoNK_yp%H*Q2XQEYm?Hd*`J%c=T#K9h>I|5#G1`n4Wt*(<+dAkc=Z5eP^`u?lcM6qllN@WLB$f77@Udp+>QBJc3RNT+$fxaMMCmwsu)#}sf@>hKa07;JYyA@(SwDr`Ak0<+?{KvH*!lRxE6I6h_dzXUgV2}cEzrRw%^`Ox$?i`Qe}#ZPP2|1Ci2wf|ryTW*q84QSZ`qoe5<eVTu~6#Bf7i&ImcVj~106Qp2&Tp(&~WkqbwV5s*Hb(p%zh>O`|KO95dF#q43J^^;=*DsOLMssrlJ2x_=EdkXr_i!`)SOZUacb>*ehX5UJ@_Jydu${G>@=L2p#Zq9n@DX)V)@^9k0)bGIse_3vOH2%XkWSl^uKHMlW_!?tb*CRvjws#AKP(PONj@OK0G$iHD5H+8a(v`WO8=^hBXz`|RuU;4QU=n}tBYzh3E&YhcSW<I(i|HiH0jFtBI`99ezyT75+mysb9t(C?*{}Hrk=R6cT8SFhjE<+?35^Xz+GgZKEviJnltF40p?EsoCuGBGpjKaNxIEkmvl{B-a{e8l^e_2ZM4q~$<GMs<YF~CZN!T~M3Bqzv^st5@4%@bpG3~CQCL1m^h~>>9f%-x>zZ68@c!Kuo{8XAx#ENvf-L!umwrvdJuICKkfSyZrts)90Rp)G47P(vU@I22$r1oK=N0dg@?%QjWa}XmXJl@;A?vE$y}fs6>_M4|8T$y>JlqX;$@0KApg=yQUAy}Ow3k68Q$l$O4*v$P9l=oemYC4yJiKkN4EeB$#ol3gnM<19a^`}DhF*)jgTa1l=!7>qh*2AfW*#NezXhrowH!iBU|&l%bD`d5GHR^0nt&h@&5yA7?l2!Z@(``f#_lGFcYWYw5)mBq{iD%$(&re!9>PYfTF*`Bzt#&r!7`~_ul-)LQ-~MsNnt~K1KaJB_ZUBwn`=?(#5UA9x-a}UTVV4N%^AZ;r&`U1tc?K!)I}#2t?1Uk52(OXxay6^=;i}-GT-oWOz<i^vgbGL6=YU<BEYO0Xd1kUBTsv)E@>gR@>i?Iykc_k*pUKW;R$}@Jj==OS{7xtOW1PQL0<2Ol6t$}VAGw(@cJXB0%A=<airHdSh7D6GJlv-DqW1RCu?Q*f<ah&F{4)mtj;$xC5P8JZn^2+&t4YU!(Z&r_Ft|(r2tDja-dRO3fL9t!5WSXm-y<dl%wL!py_vI)55H)&BYN>j-HJ&?YYV^sX=B0(=xYjrYtpe%J5-@^iBsR^TKQGY(3{eg$z1uV>APBsGAjDfv~#L<B4evNLPQEyj38l5r3XVB7MQXV&n|^w4m{8wW{ijnaOwL)tk1L@oJP9JR|7z;U9o2jpWteeorKTTL5TWRywZjBrGXaas{%js|dJyg~dR3<#Gt+!AxeFy5!jQQz4?Td)2M|xeIrqK(KgjZ9oSOJ#Et1uXthLS|fJ;MhdALl2g5%!EhpK*I>4F$i5pS6(dv&|H~*%YQj_i9+-~9ctM@{0e6nMg<tGQgIFm7u{&|bxux%iP%4VkC4h?Ah&<xGg%AfUxB;oNUG%Q)y(Y_m8}PZ4FA}O@BUkP2g<2H?n0|dd+H@bq+cO}9fWDdaFQ{8WkI0ifCd8w#--0e!Zbor`RC$XQ{PyqXbsoAgFS*mqtfJ%atK=X63%XF2ov(%lgDtYyL+YcOGl{D~M&W=i!fk(Txo$i{sQ~$X&9@F1T`>?O`jzvFgv=`S61orcq+4@*WYDu1Qq+m@+&@;|k)`#OR>-YJNw&U{kX^X->vX7m_Vm1jMWLC3!>KpqA)2aF+{y9%c5m58BHdrp#k^OCjaos+e67ZzXWOFZg0ei3V)L*JMuazv<imu8s}HiAs1iMyANRPFA2o8-^;GlnT;z(!byRGPX;X|AI|sFZuo3K@8%B(6luQsJ&mI?<QL-~}B$+|G5HX~Y)JcS|Ptr|kRhZmgYcAf8X$vg#qmZwdYO=PD%FkP>l2QsHciG*DZ}UlcB5><3T$Q4+iSs<D&|d);A0%G}vd<5(5uNm2X&)toL6?&2l?ZOJZ89OD7$KKrO32p(OI(}X=w@yNnuE%_D<bw#@>ctXPL&W-W{NZHHf_-VJKYtT614#MOL6~UWp(UxIt^fihKt~R516KLC8i{5?!MFK#g_8-?B;9Tn_b8hC4dGa`fmmxSV`e_yGbH(E(Uh}3Au%$H|QN);bTYUPV{(C_sqDKPcLAXO}M^1^PY*QQ0+tzSD*ny<k8o2UINU+!Os0b*VlD26Wq;~x79xtZU#Iw)9=c+;f3Ml%x9VEi=+z>@NKgbc|E`Eg3wfGT;*D>ET5FN@$~b?W54~d98v}hgq~w#WHDmh-!^ZLF6cWSaBvs?T2kr(t3ODe2w?2iHn_g)jCr_GvLp>h-ZC)G^7O-lYYWf2ayUtNd8#U@^gYL^-tI4BkX+tw<Jfi{m|rJ=3hSa=%~HzL=);+{CyM}vXQ$FN6Dg8Jy6HOd*ZH3PprN>d?Txw_ZTA~-W8fZBymUCgU3KtMfiCGp!ZeTA$zVUA(FE@nuw(n*uW6wlU~fj;nge7sEL7v3^9=eX1J5P|k6DB)K$P~!g{*pu*)G5KK++G8X}y|P7y}$fSA7Uzy}2M^W>)icLwg|uz6095m_w0tnlv;+tG?rVMV<j|ui$Lr;{nP904fO1Fh(1`dpyY%l4=MtX1U74;^JTM2YMO7^L-&UeaPn8=y#S;aI{F@0?l}FVt!_fhk-7i8ljzM4`U(bBMMa-D6LDhKrnV&K>jZ*DJXA?vRVi(Q8!73DD1-LA?Vo25ZSY7URvrO@Crv;pGwj=&}ZXI3D1@J%F`N88ui*q8c#*RRSpiP$&3wk43Z>)B8U0#TE8+UNcMRbu#8#SBhhzv2p_cG4QYjGB0mQFX6qbzz*dduQ1~ymJ>W(erfjQGpk9kS%qWA70O1uATHngEFC^~;5(m1EHP(LS2Z?@oSA`<aLqXOy>5-3Y*C2J(l$?tZ2;3C6HCcq3?Krjga`Mm{c-cyx!*zgh7wagfvHE<#c{oxURa!RC!U{tcDcRMpNlWFQZziPIJG^LG?|yBszT49Yz7y$UM6Si?h|r;32byTJ`yY%q0a>=Mhh?7NEQ}Sl<gPu~zB^jUKb{`tMYIkTC)=+0Rem>Q_CZUIqQeq`@bypn`yjlw7wCbT^y5o|?;$FIjI1`XjgRf>=^fk6G%|%vKgg@|x4b5o6Ffo@DJfm7C1&U4xU%rjz$?OEry;%cV;=<%d6=sN7wQa2tDTnky(_<>`Uwguu?1JaZCjIBfZFuS?uF!(gGEH)l^0k4xJB#hoff?`K;TcP&bDNa!Ax4HQhI7RmxvtF4u+<_7!g^xSpZ>wYwO(1%gVG__i|=7o6FWQ-BC4mn14-d)8qkq;~cNmpv2L~wo#TR`GhcB^T1P|I9<tm_KpV9bIl*OLkT*&n-S_tUUS(r*SE@a$gRNSeHFMtI2p9?T7(&HG>?8J6k*K<R$k{}yRCl}#zWz)Xu1pSmgjwcEUvE}amOJZ3*d6O%Q2k7j~3C{Z-rM#4C*S#0(d4O%D>@i^xkmY=Xmy;<qw>1l~m@7m?BxT65eiMxp`$Gq9J;T?WD)n=C{suP}@9SfS893#X+mXDGd)Qbm>d?e5qR4+|uPp%RhJC`7|!ACz%*v<*db-*6LWX(B6EW23?Mls1HY`HH>!5Ncj6j2zeC8J9h!N!E7Av(rr-re-s+fiC@Lp{uQO4VGrH<=u;k_eSb?0e|HebR#E5+Fb_~4g&zgBfPQA<+Q#tn9ruPkKO!m%C`BYL*@DDTE8tQ29gqqSuVSKO6O?$y#c!{4dolZQ-GgA2N5*5}WEjBzRmUG|wi^*atXsFydK5*H%AM(yFcD;Z(t~0u4fN#$%CF+?C@-v<j3IXs-#8#(GfEB9xAM%-XbT=m&u0|y82aRJ2<%6<u5OXZR0h_`RuHo)fQbq75c%SiqqUOjBLXATa2P|`3Zu7kwu=yS=2XxO_>okmSU_hKQcqjst>Ks=DL%ruBXYv^`CsZGg=t1jC?c2dH~-4r(E6rCmc{OFuky4{0%?>(@GJ-Uba&80>(<B~Q%H(12u}ekQb;gOzk4n1v;nGMY_qPI&07_8c)b5LG2<bR;>^c2hsbO9j4tzKDsL|<IO{~7qY^E;K=pxdPYCZ*eSKWyEFB8u1x$)WeC`!z>tp5FQqvUA-nEZ^O7a|Gn(L@?{WqU-oF1wda~Qd95kR$*_432b!{}s-6BMdnY=%}kgoo^CLhq+T`d8LgfuLUNP`f7=C;iAjFd@fwt^+4Xc97PpZhbXF-B619j?$Nm1^vMgy0_CwFDvO?uL0nwJi8Glr~~OOoRn*F2_<dN9B_N4b0pMvg*RxHO0vVQy<MPSSDA~K-eyb$SY-;lx?tr4YB~OqRZ1uD+5SYC@|2O$^yY+!nNAMU$RVaI9dy;6Y>{s6;%dhRbT!_wHb@*6e`>3XPOmoFGbTu6n;lv=D_~YNSsm?CDb~XQmf@0IDy{et8HMv+h;f6G){0p58{r_Lt-cr-{5c;*ibv|c|291sY^bwq%0i#o5T*Q?ah9@CISnt(n))~-kVoF&ana@82<B)BQl+AoB9mo~gEAcz_zht5vqy@3iIg!@;>u1je|fxxse%H1#)iFEWw9Hb*x)C}vx2Q>iOGwlaiAyam@rMjiBV+ZkC)4Gx>wFdyWCqNgxD9u)&~C+SeRB549C#BS=s+suZ4xG)H771L{eL|4gs>5L!W8Xo>HmTbuwV^6QY%z5t5oy$JO#TB*@5}vbb8bx<BX?pHAK1oXhq8Y_CE%iy*?gd(%S^P2V@fv1i$p<>~9Ety&%q2XBnPkUEWDi$DoCPk&Z0gp!&GA&Yk6$Sb0F%!|RVx%6HP8k3!dT~g-uyRH)7Q>A-<LSqup3ZDkvq{=3)))$YSQ*3Kx=DePiF9GiVkNa}B7%76pgH%QK6$AB^KcJ`q*U-`)segpfJlN(0c?y+q!`H-i`a}^l;5wX)zfc^_IE>cqAZs;JcqERm=|CVw9z3Hmfocc}Z6S9EWEye!2P{I_JxdAsbc0WD+JWm8M7ir_=6!ZP!Qf3bsv9=GC59iQ2htvg;0H7WGO)1(xTh1So__vI+2d21I#MjCMDypa-SWp^m!(d|SxHLz3~vN*>>6+J{xwAo7ExcPVzgd5dZOhU(RWBiexL>VDLGG_I{%|?!S7%#gMc`_exw)o0NjVdFrsxB{K+~VgmOInDGWz&>M>YuBDre|xuPDxp6P3VSvB<m4W1L{>_lgZF^|@@dT&*K-s~xlW9O?1ZM<WEGY-j<WRKfzoU#T<xd5?$RPrn{Ywqt7j!888oPUQ2M|uW-ZFhYLTig}%c{u$mkqz0igdUnMsjky|%@M4-MM<l_w5dJ*ZdU#?3pn6(?;_+zd;@f!PRYX&)ARJ1{#Emn<==MTFOPLSKyEHiUG*^jV^Yp%^f(w=<pcy0NMPvGot-D}_<Ye=<p7a1;d{}rETGH+Z6*+QFRg3eH`ow&ZATbyjo4Ob6foA=N}CBSeLXh^3fS44Rf?Cj$_rd);DIfQ<M+VAb*{K9rtydwTGe%&UKq_o7cWbis+`r>mo;O|DDi<My@%s>_$nbx#b4~QN-DAJ)hjV3%>bC`!eh2wcx}OWFKsVBZy?JT#V=2B9M53XgG&e*l6K6MO|h$9WCiGN6XBP<sQS>dVd9LCT{*zix_jZ>DOBn$B$8?oN~0*)s-+p%Yh$Qn^LBt1cW*$5cjGt_G~a7}d|$XsTCa5OSd1<G?C(kQ*o7;_pZHp(7t=cD-4&#AzIfONcU_UJ6}tB_YjhX)@fw%Cp4&xqzG?X1QB+4^$sU|u{m`AN_FVwC<V6ME5VSv30!(gJXJmy8d^lX8l-%|<QZYJHEX@xGkvNICX?8qheTKxg1#N~*lzL^hlDHvX(9mz}B#u%#cI%@O9O}iyi@;A_q<+>%VKExkWCfNycB_bKj1Y6C!q8qTYWCtf*W#aXEqb{cr<bcOGiw6bwMfy+wj)URAV|{ixBRUDO48qIY7P+dCnv>eT<M0Ysam$DSpW*I`b$;^$XLZjBF%w|Ub~ait#(Eb>mM<pa&%J7;EAd%@eXWC09w%Kbt*Pps)f^nNUMMTnsr_cqc6?xK`MJ=wy`maOlj>E&^-M|g3)EPPa_10yTE|K^ymLRMEA|GgDLDR{_sE6WI7lqR~2hoYz&IOehAg(qR7&JvM@@QCnc?{()zy@2ndjKJ17Hc|84e#aVrhMT<Xlw8$^@XuNFbPDeh_D49dYo`6G4=MWUSOQ&(`mOO8k_6gx-py0eZ7-3HlmoK@}-w;K}+-_=-TBd>W{=pyABRm+Zr2`NJRE}m8<HEvdDU12vV-^jBS8UI3d=Ve5}0o6{r0ZSvJCs@`9guQZx{+P4@4}{1cD7rUh`y>ZdwIS2NRxZ4hUS{lz(O?FTuhkVMi}&!1!m{j1eL4+S-lAcE3Le>m_L;xUxg{E!Us?BSg;_Zc_ixkK>=$@OJWyJ!#zGrk^g+>}{>H03Xr2T?MskO{E|c>jcl=VjJLvC*jxm-yom+Rp5R)1~OOoPCwIYD?c-fcWaPv?}<d7`M<GFUCP)`T#XQ}Y32=r(`oTI58lH>l;b$xzk!DjQj7YM+=LJ262HS5w3w&B>PxSyyP8)in4UG_~~1*!Ie)Cr88K_0qJ`fYg7*!@-_k}9N}Zlz<>8!H+#rh~=u`9sRXj5!hd1}>7$47Bdn!Bye%uNDVQs#4{<s|FeUF4ltcM#!$O5n1Oi!cxL3a9!6~_~>#r3GdH)Qn7L@kT#b<w~5s9l0(gw(e`JUn~<=2to)?)YW6xGvxjZhY#OBtYETwgqv3I!#muaI0H{r?nRCB`;Z7oB@zm~e_iK$P={By$d@-4M4_Nre$OTyc#|<giL&K*EIKPeMTK(3|a|t76x8L;0$LNPMJo<ZV(d|~(sv0n)*T3kUL>31)m0kQ=MM(BLTq1i}ozS~y6ZMQAnN7%f7(z3dScPy9_uWI|z%!~&QD-<$F`FUWwWCJ?S4x6ntmj~qIKZt~q*wAih^obq1hXL%aXrji;Gm`DLM^y`32k1w8KxMCfJ2QJ>L&fxO~}j$<+d2lmCnKOMElvx;Lk&~^8ebm2JIbUN$ei<=yl1UZt8%3HRC`d?(`Lbz>nUE=xl@ZO@L1>8MWp@HRz{^WGE~xY!=Gt+)=|b%tg#QkM|%bjZS{JeQ5jm&>gM3%DP&`_6Vk#|HmS@7rAYoA`k7T2%O^;AlO1Pw@BWKWqd*lfA^`2FNyLHMnu-iKZOh&)LB`+?o-@VWb#Eb8~~mLS6g`n5k>gQCG2Fs-_&W&H3k77+>d;Rqyt3e>pEGZ68gP9899!)qxf9@!V}Vk)zL%0uUMNT$H^?*(+&mIhxAnSLWt5-23wNCkCF=A-K?w=eyi?avg46;Le@;{2?v?986!u<|G%o!E<>FNs#E9iIbG{p61x#RN~brYkBelQh@bSGFgM1~bgiv`*)tEg&}Z4xB;~bc^;na66_O_Tz?;;?k|zNnzg}?tDo9s5{g{QY!WEJ!PQo#>UQ*tLQ{VYAL8J4adBj1DpQS0F6_>|X1|+`}`eB0rtQpf@^b%Xh@#3RgAnJp@dbd&%E>L>xMv$+JqcZK+|HXSYaV7`!S$DQ6Vtk=vr5#HAxUIFBXVPDv4rV(vY>nf$MmZ<f1n%#3rnnM_G*(;)^gy5(QPHZLgn;-Hilct)tsq$4U`biRHbl;4b3V=eJi1JPeR_e1bTn=?JSzLwcv_HMQj?8u5r@2)ki`v5H5|UFukQ8j`)ZT+zeRg><$trUA8wVaSklSNhERb9J@o|H$Y!y|*3>DBRn_K?<tQ}RQkcepV3(YEzdF-KusAP<JpxJ32&sJ6UUI}IRLwQ95YacyVwJDm8FWl?W56PRK(u!}B?F}|bOBstq0r;Ve50=;?6tFLo`$@Ge6G|{qGX;P%zlB-0&8d6=O_|XNpm*+t#>4UojiXs^BjnC!Ixm<G2Vp9VI`*Q{s1)GRR({N1~|io62bomJw94<#WT^#Z1JquV+IC3hl)Rz{q%+LJe#9hsUky&gV_dj8Dx17P-3CqLO4;im^-{r#~pxtGsA;4dgUK>axd{dS0x~K`Ef}X=k)WObm}ZzfQymJzTyr}qIh62t<9%?qHeZCR_wMvVy>x6tmCc=YXr{CXG{8FT5qTngo)Xklt(!ihzDOnA;rzpZ?$@bw<WPqOZm({??+1+VGTB%4xC-r0apUA8`WkD91!_=0X4~YhTFFaG7>7p@IE0>3kj`?viev)c-ahqC7!mTZwyvU{424xdMXDT!Tc8^eRA!Ktj%cxYCg3H{=+9If<!BvI4!@A%*D0ZS!!+a{%`%Tu#q0fK618vYTBz0nutF>n$G4`oqANe!CWid+Nin9Sempjqn7T&QY{yve7xPE0{X&TxcLiBlUs{i?F~+GZ_6f=l|yk-6pF9U^RM!jfiU;G#-1M~R~5_QMQ9NJM3Vx+f`D%RTxoVqUR6PUMffh{SNrelALBfaY~&iZV-<Hk*w?sR51L!>JShq*0lo}rrAQC&s<Mb@vX;04PjtN!C3#5RmQrZgSE^JdbiQKcgRdOO<DlrJp%#~(_Sa&C6$Em;cP5SKB)lPh1r^noZ3B1c-7JHF>~;+Z-D*Y{G1XDi<y`*TFiwQzC98JmMGKF<HfcqXsL^Vxi~?3506iP@I#k5hRzN<C*>7@Ld$>MwkfAe&Oozz23kU?dGu+3C53WlLvHjH@Ys{)at^>IG#b+itGhH4;pHYA(DY?(FS>vHMZ2MZFp~YK-l!wdUfYlPmCL6_2ZyD#&1Xf5@o%#<#aF>_7tbS)lOjZ1JY<)dLEq_Cdo^{Epp~vi_o#M2kr*=)x0&1xD8uWA*q8s~Wa;)DBG87n_NozNbP$)QTw&%u{aYOBA;Efbb6#Yu~)bqS9hh<}q4x+p;#A8>@2UK@0goEi+*W_adW9l+V4+W!lkDbvDRqcASMgs#fQJ2>SnelW^yvJ7=;My1R%2hi6{{Of!IKTs!L5?3lIvk}J$_$CT7HA#(TSDnop}VYV$y}o)1QAN~JCZrs6ox?tf(`g!+wm%vSMSxPz#(-hjFSUwLOCOQqz3AbcQ<gp6G0|qqSEY7Y;dR**<$NR5pc&vguhcTn{EFJD^r<KpfpU`+rh|vj-EC#kR@&GN;QVlh~IQxF7rcp9=A}%|D{<@O5ABV<-xi=Ys(6}ZlPSaR)f2x)@%Z5`%_33l6H#M&Dm)qkUY+zt-_xXE=R+AG>bVidp9B7gR6dY7Nw^7J>YK4ndInvTjMZzG$VX!#XUmpD#m*-kZ1?};M^RgW2vokPxbJ1>Lqd?WjK@dbdErIeQS@N7{ukB2}BFf#)D6CQfUX7`ub>U3OZVuGt$thn54lsP*ohrB;1iToK7Cgg6HboCb`ie8PI0f7jq7Ic44!xGHR+YndK{X>Q@Ipi*0I6c6<mkJ2KElz~yEBGiW$A?Yz-;TiTSu*sVJV9#@4$YhPjyxzBKbGXi1igeDd_uKFgGlr0N4oQTz|AZm$7cVGCEJAkW^4|c5B?_$#k8g$!Ntn&&IPamz9>qFuvY3ILdr=BYdrY6VTw~=Y7N0-$I8`CpTSIzl(5($Y+Esn}=lw%|MADt?_HZQ;Il%Md&U;3Ch0%=KjyqW-k&?xGq<>=V%oNPy`eyh5YE=09w!SEF}wm0-Glg&zkRp$X521)#RyNU}i8$f+sYzvOg)30oviU4dnyZ1pQk%Y5%<i^at3U*G8ZO!c?US^9*hTa}ULfLTgv_jV51U!rf+BZQ;K%utr8L>>E9O0&C0uIW<F#`Ylimp^B_$JMlux<mq#2@`Sj<(B6hqw<xKf=*D!YCan*d{|*m8Qb6e}Ni*oJ#-KdmM-3WmnCghi49N<!RpJ%dhso`&se{1krSc7H>VO9iDi7wPpeY&zJbd`wVFv!2yAVyZlyMY$~G4wQncs>|*)lDQ>&wI3cTgZ&Zf#jAFGLtpa~-=-*J|jd|o8gGH0^qrm%?l0ESbwF^BYN2Fs-b{>*7ukc2lvmP#Oz~zigB`>h4FfQbq0w`733@k~1!*O&3k%7U0pJw*|>$f^sXM(f8#>43)L}@%CKMYTBHoH#nW(28>`;p8bMzdcl?tUq>pPnwFl;NS3s+@l<Y5moFV;N0BtqH_p;-bOmpFo|DwQVSQ`+&>v955U?)33rFJ?OKnx#ezdi6b26EfkC%gPxREqbd2)7s3{MQ-3FiRtWbUoI!MxV}e_%Xo2(<sppxO^teio@aa>n7Yla8g0t9h{^|dkh7MPRg{eK3ivDZmAOrH_Ku5C5@@V$OF~$p-Z>0|44?Mx-TDZEXUPX~N+G!(4PnNqy;pQ#Wz}XtPozaGtqK)duPrW8EWSUX<bmuub##?bCwJEGcP%D_Yhr?#Whkj5rF18Aki!XTbjSa<a!#*WnKHi^bGjn8&Bf|SS%@n{cDlpR;ZHtZEs3coaC6*65giEGH2s|1_Ow2^8A_=^>i8w&)a-b1F41oq6=GdYKyy;4lZ0<%V14JbRK)X|sjSN9asX2^vbUP^*(BO)__!TAp+&jg6L&e1;AcknPA%c$|RR@oO@KO3s2DQc<<1B-LVDYy1QFYp*L9?F8Kjegl?b;=>wikzNG9tkua+qa7@(HOeZ;s+H;PIx%6g}^w_=sdBsD6AMXO$|y3NIb~r8PgfvlAA1fhjk1pm)NQZ_awjmr_#lXSI}lG8B~$zzB;S6;Zzws@n8wRA^<gt~;9ln#!=<loin;ov87ri2oqEW7!Y$B`R&ByVfs)Lg>qnki{J6<m5++tWOZ+!#e<37<k`p-nMG=ZdQ7&epa%u>o@|{<G&_1-dDgb1__+621ho|;*t8|t)D{Vn--0`7GhOs*>wps`Ol|WC6Q{nuwPuE7;F=*$yo?QdXC>vQWt>IeMI>s`&Svd+$3YqzK=^a8wZH}3rZwx%&vuV8ZhQQ43M4c>($mP(V?9X+uF)m)objWm`f{vR<uIc!nWH8wGUPq0qAaxJ<!Ur*Uk}AQkYd(e!$GI>|R-8VjRIGVE0H1*_0dS-GZgyww|`0gI!)$SGrGNh&cGjgFHMnWD}*Zf|zkqpL6_nmUd9EMYDDq3Yg_+#V0HmZbF06w2Q8TaNieBuO^JH115kvJ`u8%m;K)@i{~^YN(~){@L(SYWApd&zDFF{)jA66+u^I%{p=0;4l2LYersJx3rma*iJVJJzM(#hCax+7s1?IB-dpS0o_45$u!J9!Hg%rX`GQVm;3tq+Vh`S{B+T-+UF=pj8M1T@kYb{}s)9|)cOWnY7sD3GPqvo7z2}O<OD06T$PKQksp_&Wi?Jwa&({wUal5)mnLk5Y*xls3z>our!ZeFoMli&|hqCl_I-U&Zdt2`vTVf(odItRm84g?k^jNTcE!mfIVkqjkekP~4U7Vo|gl{LvmoM1FM~QTd_=`W~N2RtA_E?Nr#6yiBW^BcwgEZQc@=CUCji)2v5vAD~v})q}RhVEhTuVcp*h_E(Jim_6x9~m-9=lPV7P~;?@aUdAB$ahorm+gC;+=lnV~F7UK`SYt-R{@170v-dm9V?Oplov&Z``Ee(t@W!`$qF4o0)AqjsK}WT!9@~?J$MuqFBIq836oZ;O-AAf-qaB;TO&k-iG@BU#5@%Cc3We;ZwJ}3aoyW{|Mr2sKE|?zLuffX!I6#2ViSTANaN)5gQSkbP#>~6>9vUs2<Cg8qzUw^m01e+*g}i(HuPD*Jf8tbY||O#-(sHP}QA`If>)}9sV6WA-(_%+^NSc`wEEZPAVvzcYA<vZ;KF>PFf2;Q!xb^NECXr#=l8P`hHNv^Ba3^KakJnW&=e*>y1DIRwf6LcGGn*->!YxY#`v|s?y{uBt0>K8XoQjRlrzl$@t|27G5FAI<Ocdy=_0KaJRaJ)J5#e-;E$;InbDF0uH8iLTvr!==n>zy^$Bimr|UM-g8sr>->$ilpzG~j^>{nYF^b#rBIvJjJhx@`cxHD4WxJBLvANh2nqXn@%-Tf8}~+`A5sjV&)?@$A7ir6)TE~2iokIe!0%;jELKfYJ;Jy$GSFzrC5vR2GLD)})wb?0U;qnfOu~cSLf-hBP@6Wu%+nq(h?w_!P6+8)&hHxwX8S9=$MC+;wiDPJsPg@Rj!!SHBkjQw=_7FCF$s<S7|-;Q0mb5b=agQtTUR$(lS)&V-QxSRqNB4g04ehg!6~C&&Li9bI`;TX<Bnbz^@|tKhM=V4c?uQJEn~m<?A)^1(YGgs+m8}P$pByuJzEK5k|&Nkf{flqc@U$RMsnFkp}=uG^o(~TBx=!m2=G(c5<ZFEbQ_I(N<Vj7UpJc}gB&f<VpgY)`_kh;BMf?{SI(p6Dc<#|;3a~C0W4tZYV6s=jQ-zKdZs`mXY6ONseM+gN-}OZuD_=+S@FJ5R&sB!uHy;H%I9dzU^kyXuUol*2ok*O|4t$w!-ZI^xt}^{_M2CK?Tg$QXkkiO*lI`tsZFOfqq!bn85RbXZ(T?Q4I&f~FWRdNd-fd8ALN=m>SkEL;_?8jAT1hfq4?!gLTtbXm+k"
        master_key = "HF:iK(?n*jO=!jtn.y%pn9h#23rBB7(>"
        
   
        crypto = CryptoUtils()
        

        obfuscated_header = base64.b85decode(encoded_header)
        

        try:
            header_json = crypto.deobfuscate_header(obfuscated_header, master_key)
            header = json.loads(header_json)
        except Exception as e:
            raise DecryptionError(f"头部解析失败: {e}")
        
 
        salt = base64.b85decode(header["salt"])
        expected_checksum = base64.b85decode(header["checksum"])
        noise_info = base64.b85decode(header["noise_info"])
        

        encrypted = base64.b85decode(encoded_data)

        actual_checksum = hashlib.sha256(encrypted).digest()
        if actual_checksum != expected_checksum:
            raise IntegrityError("数据完整性校验失败")
        

        derived_key, _ = crypto.derive_key(master_key, salt, ITERATIONS)
        
  
        decrypted = crypto.xor_encrypt(encrypted, derived_key)
        
 
        inverse_transformed = crypto.inverse_transform(decrypted, derived_key)
        

        without_noise = crypto.remove_noise(inverse_transformed, noise_info)
        
     
        try:
            decompressed = zlib.decompress(without_noise)
        except Exception as e:
            raise DecryptionError(f"解压缩失败: {e}")
        
    
        try:
            code_obj = marshal.loads(decompressed)
        except Exception as e:
            raise DecryptionError(f"代码对象加载失败: {e}")
        

        if security.check_environment():
      
            globals_dict = {
                '__builtins__': __builtins__,
                '__name__': '__main__',
                '__file__': __file__,
                '__package__': None
            }
            
            # 执行代码
            exec(code_obj, globals_dict)
            return True
        
        return False
    except Exception as e:
        print(f"解密或执行过程中出错: {e}")
        return False

# 混淆和反调试技术
class _ObfuscatedCode:
    def __init__(self):
        self._values = [random.randint(1, 1000) for _ in range(50)]
        self._index = 0
        
    def _next(self):
        value = self._values[self._index]
        self._index = (self._index + 1) % len(self._values)
        return value
        
    def _process(self):
        result = 0
        for _ in range(100):
            result ^= self._next()
        return result


obfuscator = _ObfuscatedCode()
_ = obfuscator._process()

_var_0 = 8344
_var_1 = 4534
class _Class_2:
    def __init__(self):
        self.value = 88
_str_3 = "37bd21e3-6534-4fbe-b8aa-fabd1f521caf"
_str_4 = "bb897422-1697-44ee-acdd-247757aef9c2"
def _func_5(x):
    return x * 7
_list_6 = [31, 20, 78, 60, 16]
_var_7 = 9664
def _func_8(x):
    return x * 6
_str_9 = "1514354a-4e6b-4e7b-bf2d-09fa1a1507a1"
_list_10 = [18, 44, 15, 10, 93]
class _Class_11:
    def __init__(self):
        self.value = 14
def _func_12(x):
    return x * 7
_list_13 = [83, 10, 12, 69, 92]
class _Class_14:
    def __init__(self):
        self.value = 60


if not decrypt_and_execute():
    print("大大鸣监视你")


for _i in range(random.randint(1, 10)):
    _temp = os.urandom(16)
if random.random() > 0.5:
    _hash = hashlib.sha256(os.urandom(32)).hexdigest()
try:
    _data = base64.b85encode(os.urandom(64))
except:
    pass
def _fake_decrypt(data, key):

    result = bytearray()
    for i in range(min(10, len(data))):
        result.append(data[i] ^ key[i % len(key)])
    return bytes(result)
_fake_data = os.urandom(random.randint(10, 20))
_fake_key = hashlib.md5(str(time.time()).encode()).digest()
