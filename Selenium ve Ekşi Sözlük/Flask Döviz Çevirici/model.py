from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Root:
    AED: float
    AFN: float
    ALL: float
    AMD: float
    ANG: float
    AOA: float
    ARS: float
    AUD: float
    AWG: float
    AZN: float
    BAM: float
    BBD: float
    BDT: float
    BGN: float
    BHD: float
    BIF: float
    BMD: float
    BND: float
    BOB: float
    BRL: float
    BSD: float
    BTC: float
    BTN: float
    BWP: float
    BYN: float
    BYR: float
    BZD: float
    CAD: float
    CDF: float
    CHF: float
    CLF: float
    CLP: float
    CNY: float
    COP: float
    CRC: float
    CUC: float
    CUP: float
    CVE: float
    CZK: float
    DJF: float
    DKK: float
    DOP: float
    DZD: float
    EGP: float
    ERN: float
    ETB: float
    EUR: int
    FJD: float
    FKP: float
    GBP: float
    GEL: float
    GGP: float
    GHS: float
    GIP: float
    GMD: float
    GNF: float
    GTQ: float
    GYD: float
    HKD: float
    HNL: float
    HRK: float
    HTG: float
    HUF: float
    IDR: float
    ILS: float
    IMP: float
    INR: float
    IQD: float
    IRR: float
    ISK: float
    JEP: float
    JMD: float
    JOD: float
    JPY: float
    KES: float
    KGS: float
    KHR: float
    KMF: float
    KPW: float
    KRW: float
    KWD: float
    KYD: float
    KZT: float
    LAK: float
    LBP: float
    LKR: float
    LRD: float
    LSL: float
    LTL: float
    LVL: float
    LYD: float
    MAD: float
    MDL: float
    MGA: float
    MKD: float
    MMK: float
    MNT: float
    MOP: float
    MRO: float
    MUR: float
    MVR: float
    MWK: float
    MXN: float
    MYR: float
    MZN: float
    NAD: float
    NGN: float
    NIO: float
    NOK: float
    NPR: float
    NZD: float
    OMR: float
    PAB: float
    PEN: float
    PGK: float
    PHP: float
    PKR: float
    PLN: float
    PYG: float
    QAR: float
    RON: float
    RSD: float
    RUB: float
    RWF: float
    SAR: float
    SBD: float
    SCR: float
    SDG: float
    SEK: float
    SGD: float
    SHP: float
    SLE: float
    SLL: float
    SOS: float
    SSP: float
    SRD: float
    STD: float
    SYP: float
    SZL: float
    THB: float
    TJS: float
    TMT: float
    TND: float
    TOP: float
    TRY: float
    TTD: float
    TWD: float
    TZS: float
    UAH: float
    UGX: float
    USD: float
    UYU: float
    UZS: float
    VEF: float
    VES: float
    VND: float
    VUV: float
    WST: float
    XAF: float
    XAG: float
    XAU: float
    XCD: float
    XDR: float
    XOF: float
    XPF: float
    YER: float
    ZAR: float
    ZMK: float
    ZMW: float
    ZWL: float

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _AED = float(obj.get("AED"))
        _AFN = float(obj.get("AFN"))
        _ALL = float(obj.get("ALL"))
        _AMD = float(obj.get("AMD"))
        _ANG = float(obj.get("ANG"))
        _AOA = float(obj.get("AOA"))
        _ARS = float(obj.get("ARS"))
        _AUD = float(obj.get("AUD"))
        _AWG = float(obj.get("AWG"))
        _AZN = float(obj.get("AZN"))
        _BAM = float(obj.get("BAM"))
        _BBD = float(obj.get("BBD"))
        _BDT = float(obj.get("BDT"))
        _BGN = float(obj.get("BGN"))
        _BHD = float(obj.get("BHD"))
        _BIF = float(obj.get("BIF"))
        _BMD = float(obj.get("BMD"))
        _BND = float(obj.get("BND"))
        _BOB = float(obj.get("BOB"))
        _BRL = float(obj.get("BRL"))
        _BSD = float(obj.get("BSD"))
        _BTC = float(obj.get("BTC"))
        _BTN = float(obj.get("BTN"))
        _BWP = float(obj.get("BWP"))
        _BYN = float(obj.get("BYN"))
        _BYR = float(obj.get("BYR"))
        _BZD = float(obj.get("BZD"))
        _CAD = float(obj.get("CAD"))
        _CDF = float(obj.get("CDF"))
        _CHF = float(obj.get("CHF"))
        _CLF = float(obj.get("CLF"))
        _CLP = float(obj.get("CLP"))
        _CNY = float(obj.get("CNY"))
        _COP = float(obj.get("COP"))
        _CRC = float(obj.get("CRC"))
        _CUC = float(obj.get("CUC"))
        _CUP = float(obj.get("CUP"))
        _CVE = float(obj.get("CVE"))
        _CZK = float(obj.get("CZK"))
        _DJF = float(obj.get("DJF"))
        _DKK = float(obj.get("DKK"))
        _DOP = float(obj.get("DOP"))
        _DZD = float(obj.get("DZD"))
        _EGP = float(obj.get("EGP"))
        _ERN = float(obj.get("ERN"))
        _ETB = float(obj.get("ETB"))
        _EUR = int(obj.get("EUR"))
        _FJD = float(obj.get("FJD"))
        _FKP = float(obj.get("FKP"))
        _GBP = float(obj.get("GBP"))
        _GEL = float(obj.get("GEL"))
        _GGP = float(obj.get("GGP"))
        _GHS = float(obj.get("GHS"))
        _GIP = float(obj.get("GIP"))
        _GMD = float(obj.get("GMD"))
        _GNF = float(obj.get("GNF"))
        _GTQ = float(obj.get("GTQ"))
        _GYD = float(obj.get("GYD"))
        _HKD = float(obj.get("HKD"))
        _HNL = float(obj.get("HNL"))
        _HRK = float(obj.get("HRK"))
        _HTG = float(obj.get("HTG"))
        _HUF = float(obj.get("HUF"))
        _IDR = float(obj.get("IDR"))
        _ILS = float(obj.get("ILS"))
        _IMP = float(obj.get("IMP"))
        _INR = float(obj.get("INR"))
        _IQD = float(obj.get("IQD"))
        _IRR = float(obj.get("IRR"))
        _ISK = float(obj.get("ISK"))
        _JEP = float(obj.get("JEP"))
        _JMD = float(obj.get("JMD"))
        _JOD = float(obj.get("JOD"))
        _JPY = float(obj.get("JPY"))
        _KES = float(obj.get("KES"))
        _KGS = float(obj.get("KGS"))
        _KHR = float(obj.get("KHR"))
        _KMF = float(obj.get("KMF"))
        _KPW = float(obj.get("KPW"))
        _KRW = float(obj.get("KRW"))
        _KWD = float(obj.get("KWD"))
        _KYD = float(obj.get("KYD"))
        _KZT = float(obj.get("KZT"))
        _LAK = float(obj.get("LAK"))
        _LBP = float(obj.get("LBP"))
        _LKR = float(obj.get("LKR"))
        _LRD = float(obj.get("LRD"))
        _LSL = float(obj.get("LSL"))
        _LTL = float(obj.get("LTL"))
        _LVL = float(obj.get("LVL"))
        _LYD = float(obj.get("LYD"))
        _MAD = float(obj.get("MAD"))
        _MDL = float(obj.get("MDL"))
        _MGA = float(obj.get("MGA"))
        _MKD = float(obj.get("MKD"))
        _MMK = float(obj.get("MMK"))
        _MNT = float(obj.get("MNT"))
        _MOP = float(obj.get("MOP"))
        _MRO = float(obj.get("MRO"))
        _MUR = float(obj.get("MUR"))
        _MVR = float(obj.get("MVR"))
        _MWK = float(obj.get("MWK"))
        _MXN = float(obj.get("MXN"))
        _MYR = float(obj.get("MYR"))
        _MZN = float(obj.get("MZN"))
        _NAD = float(obj.get("NAD"))
        _NGN = float(obj.get("NGN"))
        _NIO = float(obj.get("NIO"))
        _NOK = float(obj.get("NOK"))
        _NPR = float(obj.get("NPR"))
        _NZD = float(obj.get("NZD"))
        _OMR = float(obj.get("OMR"))
        _PAB = float(obj.get("PAB"))
        _PEN = float(obj.get("PEN"))
        _PGK = float(obj.get("PGK"))
        _PHP = float(obj.get("PHP"))
        _PKR = float(obj.get("PKR"))
        _PLN = float(obj.get("PLN"))
        _PYG = float(obj.get("PYG"))
        _QAR = float(obj.get("QAR"))
        _RON = float(obj.get("RON"))
        _RSD = float(obj.get("RSD"))
        _RUB = float(obj.get("RUB"))
        _RWF = float(obj.get("RWF"))
        _SAR = float(obj.get("SAR"))
        _SBD = float(obj.get("SBD"))
        _SCR = float(obj.get("SCR"))
        _SDG = float(obj.get("SDG"))
        _SEK = float(obj.get("SEK"))
        _SGD = float(obj.get("SGD"))
        _SHP = float(obj.get("SHP"))
        _SLE = float(obj.get("SLE"))
        _SLL = float(obj.get("SLL"))
        _SOS = float(obj.get("SOS"))
        _SSP = float(obj.get("SSP"))
        _SRD = float(obj.get("SRD"))
        _STD = float(obj.get("STD"))
        _SYP = float(obj.get("SYP"))
        _SZL = float(obj.get("SZL"))
        _THB = float(obj.get("THB"))
        _TJS = float(obj.get("TJS"))
        _TMT = float(obj.get("TMT"))
        _TND = float(obj.get("TND"))
        _TOP = float(obj.get("TOP"))
        _TRY = float(obj.get("TRY"))
        _TTD = float(obj.get("TTD"))
        _TWD = float(obj.get("TWD"))
        _TZS = float(obj.get("TZS"))
        _UAH = float(obj.get("UAH"))
        _UGX = float(obj.get("UGX"))
        _USD = float(obj.get("USD"))
        _UYU = float(obj.get("UYU"))
        _UZS = float(obj.get("UZS"))
        _VEF = float(obj.get("VEF"))
        _VES = float(obj.get("VES"))
        _VND = float(obj.get("VND"))
        _VUV = float(obj.get("VUV"))
        _WST = float(obj.get("WST"))
        _XAF = float(obj.get("XAF"))
        _XAG = float(obj.get("XAG"))
        _XAU = float(obj.get("XAU"))
        _XCD = float(obj.get("XCD"))
        _XDR = float(obj.get("XDR"))
        _XOF = float(obj.get("XOF"))
        _XPF = float(obj.get("XPF"))
        _YER = float(obj.get("YER"))
        _ZAR = float(obj.get("ZAR"))
        _ZMK = float(obj.get("ZMK"))
        _ZMW = float(obj.get("ZMW"))
        _ZWL = float(obj.get("ZWL"))
        return Root(_AED, _AFN, _ALL, _AMD, _ANG, _AOA, _ARS, _AUD, _AWG, _AZN, _BAM, _BBD, _BDT, _BGN, _BHD, _BIF, _BMD, _BND, _BOB, _BRL, _BSD, _BTC, _BTN, _BWP, _BYN, _BYR, _BZD, _CAD, _CDF, _CHF, _CLF, _CLP, _CNY, _COP, _CRC, _CUC, _CUP, _CVE, _CZK, _DJF, _DKK, _DOP, _DZD, _EGP, _ERN, _ETB, _EUR, _FJD, _FKP, _GBP, _GEL, _GGP, _GHS, _GIP, _GMD, _GNF, _GTQ, _GYD, _HKD, _HNL, _HRK, _HTG, _HUF, _IDR, _ILS, _IMP, _INR, _IQD, _IRR, _ISK, _JEP, _JMD, _JOD, _JPY, _KES, _KGS, _KHR, _KMF, _KPW, _KRW, _KWD, _KYD, _KZT, _LAK, _LBP, _LKR, _LRD, _LSL, _LTL, _LVL, _LYD, _MAD, _MDL, _MGA, _MKD, _MMK, _MNT, _MOP, _MRO, _MUR, _MVR, _MWK, _MXN, _MYR, _MZN, _NAD, _NGN, _NIO, _NOK, _NPR, _NZD, _OMR, _PAB, _PEN, _PGK, _PHP, _PKR, _PLN, _PYG, _QAR, _RON, _RSD, _RUB, _RWF, _SAR, _SBD, _SCR, _SDG, _SEK, _SGD, _SHP, _SLE, _SLL, _SOS, _SSP, _SRD, _STD, _SYP, _SZL, _THB, _TJS, _TMT, _TND, _TOP, _TRY, _TTD, _TWD, _TZS, _UAH, _UGX, _USD, _UYU, _UZS, _VEF, _VES, _VND, _VUV, _WST, _XAF, _XAG, _XAU, _XCD, _XDR, _XOF, _XPF, _YER, _ZAR, _ZMK, _ZMW, _ZWL)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
