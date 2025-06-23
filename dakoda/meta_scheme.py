from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlPeriod

class LanguageCode(Enum):
    """
    :cvar AAA:
    :cvar AAB:
    :cvar AAC:
    :cvar AAD:
    :cvar AAE:
    :cvar AAF:
    :cvar AAG:
    :cvar AAH:
    :cvar AAI:
    :cvar AAK:
    :cvar AAL:
    :cvar AAN:
    :cvar AAO:
    :cvar AAP:
    :cvar AAQ:
    :cvar AAR:
    :cvar AAS:
    :cvar ALB:
    :cvar SQI:
    :cvar AAT:
    :cvar AAU:
    :cvar AAW:
    :cvar AAX:
    :cvar GER:
    :cvar AAZ:
    :cvar ABA:
    :cvar ABB:
    :cvar ABC:
    :cvar ABD:
    :cvar ABE:
    :cvar ABF:
    :cvar ABG:
    :cvar ABH:
    :cvar ABI:
    :cvar ABJ:
    :cvar ABK:
    :cvar ABL:
    :cvar ABM:
    :cvar ABN:
    :cvar ABO:
    :cvar ABP:
    :cvar ABQ:
    :cvar ABR:
    :cvar ABS:
    :cvar ABT:
    :cvar ABU:
    :cvar ABV:
    :cvar ABW:
    :cvar ABX:
    :cvar ABY:
    :cvar ABZ:
    :cvar ACA:
    :cvar ACB:
    :cvar ACD:
    :cvar ACE:
    :cvar ACF:
    :cvar ACH:
    :cvar ACI:
    :cvar ACK:
    :cvar ACL:
    :cvar ACM:
    :cvar ACN:
    :cvar ACP:
    :cvar ACQ:
    :cvar ACR:
    :cvar ACS:
    :cvar ACT:
    :cvar ACU:
    :cvar ACV:
    :cvar ACW:
    :cvar ACX:
    :cvar ACY:
    :cvar ACZ:
    :cvar ADA:
    :cvar ADB:
    :cvar ADD:
    :cvar ADE:
    :cvar ADF:
    :cvar ADG:
    :cvar ADH:
    :cvar ADI:
    :cvar ADJ:
    :cvar ADL:
    :cvar ADN:
    :cvar ADO:
    :cvar ADQ:
    :cvar ADR:
    :cvar ADS:
    :cvar ADT:
    :cvar ADU:
    :cvar ADW:
    :cvar ADX:
    :cvar ADY:
    :cvar ADZ:
    :cvar AEA:
    :cvar AEB:
    :cvar AEC:
    :cvar AED:
    :cvar AEE:
    :cvar AEK:
    :cvar AEL:
    :cvar AEM:
    :cvar AEN:
    :cvar AEQ:
    :cvar AER:
    :cvar AES:
    :cvar AEU:
    :cvar AEW:
    :cvar AEY:
    :cvar AEZ:
    :cvar AFB:
    :cvar AFD:
    :cvar AFE:
    :cvar AFG:
    :cvar AFI:
    :cvar AFK:
    :cvar AFN:
    :cvar AFO:
    :cvar AFP:
    :cvar AFR:
    :cvar AFS:
    :cvar AFT:
    :cvar AFU:
    :cvar AFZ:
    :cvar AGA:
    :cvar AGB:
    :cvar AGC:
    :cvar AGD:
    :cvar AGE:
    :cvar AGF:
    :cvar AGG:
    :cvar AGH:
    :cvar AGI:
    :cvar AGJ:
    :cvar AGK:
    :cvar AGL:
    :cvar AGM:
    :cvar AGN:
    :cvar AGO:
    :cvar AGQ:
    :cvar AGR:
    :cvar AGS:
    :cvar AGT:
    :cvar AGU:
    :cvar AGV:
    :cvar AGW:
    :cvar AGX:
    :cvar AGY:
    :cvar AGZ:
    :cvar AHA:
    :cvar AHB:
    :cvar AHG:
    :cvar AHH:
    :cvar AHI:
    :cvar AHK:
    :cvar AHL:
    :cvar AHM:
    :cvar AHN:
    :cvar AHO:
    :cvar AHP:
    :cvar AHR:
    :cvar AHS:
    :cvar AHT:
    :cvar AIA:
    :cvar AIB:
    :cvar AIC:
    :cvar AID:
    :cvar AIE:
    :cvar AIF:
    :cvar AIG:
    :cvar AIH:
    :cvar AII:
    :cvar AIJ:
    :cvar AIK:
    :cvar AIL:
    :cvar AIM:
    :cvar AIN:
    :cvar AIO:
    :cvar AIP:
    :cvar AIQ:
    :cvar AIR:
    :cvar AIT:
    :cvar AIW:
    :cvar AIX:
    :cvar AIY:
    :cvar AJA:
    :cvar AJG:
    :cvar AJI:
    :cvar AJN:
    :cvar AJS:
    :cvar AJU:
    :cvar AJW:
    :cvar AJZ:
    :cvar AKA:
    :cvar AKB:
    :cvar AKC:
    :cvar AKD:
    :cvar AKE:
    :cvar AKF:
    :cvar AKG:
    :cvar AKH:
    :cvar AKI:
    :cvar AKJ:
    :cvar AKL:
    :cvar AKM:
    :cvar AKO:
    :cvar AKP:
    :cvar AKQ:
    :cvar AKR:
    :cvar AKS:
    :cvar AKT:
    :cvar AKU:
    :cvar AKV:
    :cvar AKW:
    :cvar AKX:
    :cvar AKY:
    :cvar AKZ:
    :cvar ALA:
    :cvar ALC:
    :cvar ALD:
    :cvar ALE:
    :cvar ALF:
    :cvar ALH:
    :cvar ALI:
    :cvar ALJ:
    :cvar ALK:
    :cvar ALL:
    :cvar ALM:
    :cvar ALN:
    :cvar ALO:
    :cvar ALP:
    :cvar ALQ:
    :cvar ALR:
    :cvar ALS:
    :cvar ALT:
    :cvar ALU:
    :cvar ALW:
    :cvar ALX:
    :cvar ALY:
    :cvar ALZ:
    :cvar AMA:
    :cvar AMB:
    :cvar AMC:
    :cvar AME:
    :cvar AMF:
    :cvar AMG:
    :cvar AMH:
    :cvar AMI:
    :cvar AMJ:
    :cvar AMK:
    :cvar AML:
    :cvar AMM:
    :cvar AMN:
    :cvar AMO:
    :cvar AMP:
    :cvar AMQ:
    :cvar AMR:
    :cvar AMS:
    :cvar AMT:
    :cvar AMU:
    :cvar AMV:
    :cvar AMW:
    :cvar AMX:
    :cvar AMY:
    :cvar AMZ:
    :cvar ANA:
    :cvar ANB:
    :cvar ANC:
    :cvar AND:
    :cvar ANE:
    :cvar ANF:
    :cvar ANH:
    :cvar ANI:
    :cvar ANJ:
    :cvar ANK:
    :cvar ANL:
    :cvar ANM:
    :cvar ANN:
    :cvar ANO:
    :cvar ANP:
    :cvar ANQ:
    :cvar ANR:
    :cvar ANS:
    :cvar ANT:
    :cvar ANU:
    :cvar ANV:
    :cvar ANW:
    :cvar ANX:
    :cvar ANY:
    :cvar ANZ:
    :cvar AOA:
    :cvar AOB:
    :cvar AOC:
    :cvar AOD:
    :cvar AOE:
    :cvar AOF:
    :cvar AOG:
    :cvar AOI:
    :cvar AOJ:
    :cvar AOK:
    :cvar AOL:
    :cvar AOM:
    :cvar AON:
    :cvar AOR:
    :cvar AOS:
    :cvar AOT:
    :cvar AOU:
    :cvar AOX:
    :cvar AOZ:
    :cvar APB:
    :cvar APC:
    :cvar APD:
    :cvar APE:
    :cvar APF:
    :cvar APG:
    :cvar APH:
    :cvar API:
    :cvar APJ:
    :cvar APK:
    :cvar APL:
    :cvar APM:
    :cvar APN:
    :cvar APO:
    :cvar APP:
    :cvar APQ:
    :cvar APR:
    :cvar APS:
    :cvar APT:
    :cvar APU:
    :cvar APV:
    :cvar APW:
    :cvar APX:
    :cvar APY:
    :cvar APZ:
    :cvar AQC:
    :cvar AQD:
    :cvar AQG:
    :cvar AQK:
    :cvar AQM:
    :cvar AQN:
    :cvar AQP:
    :cvar AQR:
    :cvar AQT:
    :cvar AQZ:
    :cvar ARB:
    :cvar ARD:
    :cvar ARE:
    :cvar ARG:
    :cvar ARH:
    :cvar ARI:
    :cvar ARJ:
    :cvar ARK:
    :cvar ARL:
    :cvar ARN:
    :cvar ARO:
    :cvar ARP:
    :cvar ARQ:
    :cvar ARR:
    :cvar ARS:
    :cvar ARU:
    :cvar ARV:
    :cvar ARW:
    :cvar ARX:
    :cvar ARY:
    :cvar ARZ:
    :cvar ASA:
    :cvar ASB:
    :cvar ASC:
    :cvar ASE:
    :cvar ASF:
    :cvar ASG:
    :cvar ASH:
    :cvar ASI:
    :cvar ASJ:
    :cvar ASK:
    :cvar ASL:
    :cvar ASM:
    :cvar ASN:
    :cvar ASO:
    :cvar ASP:
    :cvar ASQ:
    :cvar ASR:
    :cvar ASS:
    :cvar AST:
    :cvar ASU:
    :cvar ASV:
    :cvar ASW:
    :cvar ASX:
    :cvar ASY:
    :cvar ASZ:
    :cvar ATA:
    :cvar ATB:
    :cvar ATC:
    :cvar ATD:
    :cvar ATE:
    :cvar ATG:
    :cvar ATI:
    :cvar ATJ:
    :cvar ATK:
    :cvar ATL:
    :cvar ATM:
    :cvar ATN:
    :cvar ATO:
    :cvar ATP:
    :cvar ATQ:
    :cvar ATR:
    :cvar ATS:
    :cvar ATT:
    :cvar ATU:
    :cvar ATV:
    :cvar ATW:
    :cvar ATX:
    :cvar ATY:
    :cvar ATZ:
    :cvar AUA:
    :cvar AUB:
    :cvar AUC:
    :cvar AUD:
    :cvar AUG:
    :cvar AUH:
    :cvar AUI:
    :cvar AUJ:
    :cvar AUK:
    :cvar AUL:
    :cvar AUM:
    :cvar AUN:
    :cvar AUO:
    :cvar AUP:
    :cvar AUQ:
    :cvar AUR:
    :cvar AUT:
    :cvar AUU:
    :cvar AUW:
    :cvar AUX:
    :cvar AUY:
    :cvar AUZ:
    :cvar AVA:
    :cvar AVB:
    :cvar AVD:
    :cvar AVE:
    :cvar AVI:
    :cvar AVL:
    :cvar AVM:
    :cvar AVN:
    :cvar AVO:
    :cvar AVS:
    :cvar AVT:
    :cvar AVU:
    :cvar AVV:
    :cvar AWA:
    :cvar AWB:
    :cvar AWC:
    :cvar AWE:
    :cvar AWG:
    :cvar AWH:
    :cvar AWI:
    :cvar AWK:
    :cvar AWM:
    :cvar AWN:
    :cvar AWO:
    :cvar AWR:
    :cvar AWS:
    :cvar AWT:
    :cvar AWU:
    :cvar AWV:
    :cvar AWW:
    :cvar AWX:
    :cvar AWY:
    :cvar AXB:
    :cvar AXE:
    :cvar AXG:
    :cvar AXK:
    :cvar AXL:
    :cvar AXX:
    :cvar AYA:
    :cvar AYB:
    :cvar AYC:
    :cvar AYD:
    :cvar AYE:
    :cvar AYG:
    :cvar AYH:
    :cvar AYI:
    :cvar AYK:
    :cvar AYL:
    :cvar AYN:
    :cvar AYO:
    :cvar AYP:
    :cvar AYQ:
    :cvar AYR:
    :cvar AYS:
    :cvar AYT:
    :cvar AYU:
    :cvar AYZ:
    :cvar AZA:
    :cvar AZB:
    :cvar AZD:
    :cvar AZG:
    :cvar AZJ:
    :cvar AZM:
    :cvar AZN:
    :cvar AZO:
    :cvar AZT:
    :cvar AZZ:
    :cvar BAA:
    :cvar BAB:
    :cvar BAC:
    :cvar BAE:
    :cvar BAF:
    :cvar BAG:
    :cvar BAH:
    :cvar BAJ:
    :cvar BAK:
    :cvar BAM:
    :cvar BAN:
    :cvar BAO:
    :cvar BAP:
    :cvar BAR:
    :cvar BAS:
    :cvar BAU:
    :cvar BAV:
    :cvar BAW:
    :cvar BAX:
    :cvar BAY:
    :cvar BBA:
    :cvar BBB:
    :cvar BBC:
    :cvar BBD:
    :cvar BBE:
    :cvar BBF:
    :cvar BBG:
    :cvar BBH:
    :cvar BBI:
    :cvar BBJ:
    :cvar BBK:
    :cvar BBL:
    :cvar BBM:
    :cvar BBN:
    :cvar BBO:
    :cvar BBP:
    :cvar BBQ:
    :cvar BBR:
    :cvar BBS:
    :cvar BBT:
    :cvar BBU:
    :cvar BBV:
    :cvar BBW:
    :cvar BBX:
    :cvar BBY:
    :cvar BCA:
    :cvar BCB:
    :cvar BCC:
    :cvar BCD:
    :cvar BCE:
    :cvar BCF:
    :cvar BCG:
    :cvar BCH:
    :cvar BCI:
    :cvar BCJ:
    :cvar BCK:
    :cvar BCL:
    :cvar BCM:
    :cvar BCN:
    :cvar BCO:
    :cvar BCP:
    :cvar BCQ:
    :cvar BCR:
    :cvar BCS:
    :cvar BCT:
    :cvar BCU:
    :cvar BCV:
    :cvar BCW:
    :cvar BCY:
    :cvar BCZ:
    :cvar BDA:
    :cvar BDB:
    :cvar BDC:
    :cvar BDD:
    :cvar BDE:
    :cvar BDF:
    :cvar BDG:
    :cvar BDH:
    :cvar BDI:
    :cvar BDJ:
    :cvar BDK:
    :cvar BDL:
    :cvar BDM:
    :cvar BDN:
    :cvar BDO:
    :cvar BDP:
    :cvar BDQ:
    :cvar BDR:
    :cvar BDS:
    :cvar BDT:
    :cvar BDU:
    :cvar BDV:
    :cvar BDW:
    :cvar BDX:
    :cvar BDY:
    :cvar BDZ:
    :cvar BEA:
    :cvar BEB:
    :cvar BEC:
    :cvar BED:
    :cvar BEE:
    :cvar BEF:
    :cvar BEG:
    :cvar BEH:
    :cvar BEI:
    :cvar BEJ:
    :cvar BEK:
    :cvar BEL:
    :cvar BEM:
    :cvar BEN:
    :cvar BEO:
    :cvar BEP:
    :cvar BEQ:
    :cvar BES:
    :cvar BET:
    :cvar BEU:
    :cvar BEV:
    :cvar BEW:
    :cvar BEX:
    :cvar BEY:
    :cvar BEZ:
    :cvar BFA:
    :cvar BFB:
    :cvar BFC:
    :cvar BFD:
    :cvar BFE:
    :cvar BFF:
    :cvar BFG:
    :cvar BFH:
    :cvar BFI:
    :cvar BFJ:
    :cvar BFK:
    :cvar BFL:
    :cvar BFM:
    :cvar BFN:
    :cvar BFO:
    :cvar BFP:
    :cvar BFQ:
    :cvar BFR:
    :cvar BFS:
    :cvar BFT:
    :cvar BFU:
    :cvar BFW:
    :cvar BFX:
    :cvar BFY:
    :cvar BFZ:
    :cvar BGA:
    :cvar BGB:
    :cvar BGC:
    :cvar BGD:
    :cvar BGE:
    :cvar BGF:
    :cvar BGG:
    :cvar BGI:
    :cvar BGJ:
    :cvar BGK:
    :cvar BGL:
    :cvar BGN:
    :cvar BGO:
    :cvar BGP:
    :cvar BGQ:
    :cvar BGR:
    :cvar BGS:
    :cvar BGT:
    :cvar BGU:
    :cvar BGV:
    :cvar BGW:
    :cvar BGX:
    :cvar BGY:
    :cvar BGZ:
    :cvar BHA:
    :cvar BHB:
    :cvar BHC:
    :cvar BHD:
    :cvar BHE:
    :cvar BHF:
    :cvar BHG:
    :cvar BHH:
    :cvar BHI:
    :cvar BHJ:
    :cvar BHL:
    :cvar BHM:
    :cvar BHN:
    :cvar BHO:
    :cvar BHP:
    :cvar BHQ:
    :cvar BHR:
    :cvar BHS:
    :cvar BHT:
    :cvar BHU:
    :cvar BHV:
    :cvar BHW:
    :cvar BHX:
    :cvar BHY:
    :cvar BHZ:
    :cvar BIA:
    :cvar BIB:
    :cvar BID:
    :cvar BIE:
    :cvar BIF:
    :cvar BIG:
    :cvar BIL:
    :cvar BIM:
    :cvar BIN:
    :cvar BIO:
    :cvar BIP:
    :cvar BIQ:
    :cvar BIR:
    :cvar BIS:
    :cvar BIT:
    :cvar BIU:
    :cvar BIV:
    :cvar BIW:
    :cvar BIX:
    :cvar BIY:
    :cvar BIZ:
    :cvar BJA:
    :cvar BJB:
    :cvar BJC:
    :cvar BJE:
    :cvar BJF:
    :cvar BJG:
    :cvar BJH:
    :cvar BJI:
    :cvar BJJ:
    :cvar BJK:
    :cvar BJL:
    :cvar BJM:
    :cvar BJN:
    :cvar BJO:
    :cvar BJP:
    :cvar BJR:
    :cvar BJS:
    :cvar BJT:
    :cvar BJU:
    :cvar BJV:
    :cvar BJW:
    :cvar BJX:
    :cvar BJY:
    :cvar BJZ:
    :cvar BKA:
    :cvar BKC:
    :cvar BKD:
    :cvar BKF:
    :cvar BKG:
    :cvar BKH:
    :cvar BKI:
    :cvar BKJ:
    :cvar BKK:
    :cvar BKL:
    :cvar BKM:
    :cvar BKN:
    :cvar BKO:
    :cvar BKP:
    :cvar BKQ:
    :cvar BKR:
    :cvar BKS:
    :cvar BKT:
    :cvar BKU:
    :cvar BKV:
    :cvar BKW:
    :cvar BKX:
    :cvar BKY:
    :cvar BKZ:
    :cvar BLA:
    :cvar BLB:
    :cvar BLC:
    :cvar BLD:
    :cvar BLE:
    :cvar BLF:
    :cvar BLH:
    :cvar BLI:
    :cvar BLJ:
    :cvar BLK:
    :cvar BLL:
    :cvar BLM:
    :cvar BLN:
    :cvar BLO:
    :cvar BLP:
    :cvar BLQ:
    :cvar BLR:
    :cvar BLS:
    :cvar BLT:
    :cvar BLV:
    :cvar BLW:
    :cvar BLX:
    :cvar BLY:
    :cvar BLZ:
    :cvar BMA:
    :cvar BMB:
    :cvar BMC:
    :cvar BMD:
    :cvar BME:
    :cvar BMF:
    :cvar BMG:
    :cvar BMH:
    :cvar BMI:
    :cvar BMJ:
    :cvar BMK:
    :cvar BML:
    :cvar BMM:
    :cvar BMN:
    :cvar BMO:
    :cvar BMP:
    :cvar BMQ:
    :cvar BMR:
    :cvar BMS:
    :cvar BMT:
    :cvar BMU:
    :cvar BMV:
    :cvar BMW:
    :cvar BMX:
    :cvar BMZ:
    :cvar BNA:
    :cvar BNB:
    :cvar BND:
    :cvar BNE:
    :cvar BNF:
    :cvar BNG:
    :cvar BNI:
    :cvar BNJ:
    :cvar BNK:
    :cvar BNL:
    :cvar BNM:
    :cvar BNN:
    :cvar BNO:
    :cvar BNP:
    :cvar BNQ:
    :cvar BNR:
    :cvar BNS:
    :cvar BNU:
    :cvar BNV:
    :cvar BNW:
    :cvar BNX:
    :cvar BNY:
    :cvar BNZ:
    :cvar BOA:
    :cvar BOB:
    :cvar BOD:
    :cvar BOE:
    :cvar BOF:
    :cvar BOG:
    :cvar BOH:
    :cvar BOI:
    :cvar BOJ:
    :cvar BOK:
    :cvar BOL:
    :cvar BOM:
    :cvar BON:
    :cvar BOO:
    :cvar BOP:
    :cvar BOQ:
    :cvar BOR:
    :cvar BOS:
    :cvar BOT:
    :cvar BOU:
    :cvar BOV:
    :cvar BOW:
    :cvar BOX:
    :cvar BOY:
    :cvar BOZ:
    :cvar BPA:
    :cvar BPC:
    :cvar BPD:
    :cvar BPE:
    :cvar BPG:
    :cvar BPH:
    :cvar BPI:
    :cvar BPJ:
    :cvar BPK:
    :cvar BPL:
    :cvar BPM:
    :cvar BPN:
    :cvar BPO:
    :cvar BPP:
    :cvar BPQ:
    :cvar BPR:
    :cvar BPS:
    :cvar BPT:
    :cvar BPU:
    :cvar BPV:
    :cvar BPW:
    :cvar BPX:
    :cvar BPY:
    :cvar BPZ:
    :cvar BQA:
    :cvar BQB:
    :cvar BQC:
    :cvar BQD:
    :cvar BQF:
    :cvar BQG:
    :cvar BQH:
    :cvar BQI:
    :cvar BQJ:
    :cvar BQK:
    :cvar BQL:
    :cvar BQM:
    :cvar BQN:
    :cvar BQO:
    :cvar BQP:
    :cvar BQQ:
    :cvar BQR:
    :cvar BQS:
    :cvar BQT:
    :cvar BQU:
    :cvar BQV:
    :cvar BQW:
    :cvar BQX:
    :cvar BQY:
    :cvar BQZ:
    :cvar BRA:
    :cvar BRB:
    :cvar BRC:
    :cvar BRD:
    :cvar BRE:
    :cvar BRF:
    :cvar BRG:
    :cvar BRH:
    :cvar BRI:
    :cvar BRJ:
    :cvar BRK:
    :cvar BRL:
    :cvar BRM:
    :cvar BRN:
    :cvar BRO:
    :cvar BRP:
    :cvar BRQ:
    :cvar BRR:
    :cvar BRS:
    :cvar BRT:
    :cvar BRU:
    :cvar BRV:
    :cvar BRW:
    :cvar BRX:
    :cvar BRY:
    :cvar BRZ:
    :cvar BSA:
    :cvar BSB:
    :cvar BSC:
    :cvar BSE:
    :cvar BSF:
    :cvar BSG:
    :cvar BSH:
    :cvar BSI:
    :cvar BSJ:
    :cvar BSK:
    :cvar BSL:
    :cvar BSM:
    :cvar BSN:
    :cvar BSO:
    :cvar BSP:
    :cvar BSQ:
    :cvar BSR:
    :cvar BSS:
    :cvar BST:
    :cvar BSU:
    :cvar BSV:
    :cvar BSW:
    :cvar BSX:
    :cvar BSY:
    :cvar BTA:
    :cvar BTC:
    :cvar BTD:
    :cvar BTE:
    :cvar BTF:
    :cvar BTG:
    :cvar BTH:
    :cvar BTI:
    :cvar BTJ:
    :cvar BTM:
    :cvar BTN:
    :cvar BTO:
    :cvar BTP:
    :cvar BTQ:
    :cvar BTR:
    :cvar BTS:
    :cvar BTT:
    :cvar BTU:
    :cvar BTV:
    :cvar BTW:
    :cvar BTX:
    :cvar BTY:
    :cvar BTZ:
    :cvar BUB:
    :cvar BUC:
    :cvar BUD:
    :cvar BUE:
    :cvar BUF:
    :cvar BUG:
    :cvar BUH:
    :cvar BUI:
    :cvar BUJ:
    :cvar BUK:
    :cvar BUL:
    :cvar BUM:
    :cvar BUN:
    :cvar BUO:
    :cvar BUP:
    :cvar BUQ:
    :cvar BUS:
    :cvar BUT:
    :cvar BUU:
    :cvar BUV:
    :cvar BUW:
    :cvar BUX:
    :cvar BUY:
    :cvar BUZ:
    :cvar BVA:
    :cvar BVB:
    :cvar BVC:
    :cvar BVD:
    :cvar BVE:
    :cvar BVF:
    :cvar BVG:
    :cvar BVH:
    :cvar BVI:
    :cvar BVJ:
    :cvar BVK:
    :cvar BVL:
    :cvar BVM:
    :cvar BVN:
    :cvar BVO:
    :cvar BVP:
    :cvar BVQ:
    :cvar BVR:
    :cvar BVT:
    :cvar BVU:
    :cvar BVV:
    :cvar BVW:
    :cvar BVX:
    :cvar BVY:
    :cvar BVZ:
    :cvar BWA:
    :cvar BWB:
    :cvar BWC:
    :cvar BWD:
    :cvar BWE:
    :cvar BWF:
    :cvar BWG:
    :cvar BWH:
    :cvar BWI:
    :cvar BWJ:
    :cvar BWK:
    :cvar BWL:
    :cvar BWM:
    :cvar BWN:
    :cvar BWO:
    :cvar BWP:
    :cvar BWQ:
    :cvar BWR:
    :cvar BWS:
    :cvar BWT:
    :cvar BWU:
    :cvar BWW:
    :cvar BWX:
    :cvar BWY:
    :cvar BWZ:
    :cvar BXA:
    :cvar BXB:
    :cvar BXC:
    :cvar BXD:
    :cvar BXE:
    :cvar BXF:
    :cvar BXG:
    :cvar BXH:
    :cvar BXI:
    :cvar BXJ:
    :cvar BXK:
    :cvar BXL:
    :cvar BXM:
    :cvar BXN:
    :cvar BXO:
    :cvar BXP:
    :cvar BXQ:
    :cvar BXR:
    :cvar BXS:
    :cvar BXU:
    :cvar BXV:
    :cvar BXW:
    :cvar BXZ:
    :cvar BYA:
    :cvar BYB:
    :cvar BYC:
    :cvar BYD:
    :cvar BYE:
    :cvar BYF:
    :cvar BYG:
    :cvar BYH:
    :cvar BYI:
    :cvar BYJ:
    :cvar BYK:
    :cvar BYL:
    :cvar BYM:
    :cvar BYN:
    :cvar BYO:
    :cvar BYP:
    :cvar BYQ:
    :cvar BYR:
    :cvar BYS:
    :cvar BYT:
    :cvar BYV:
    :cvar BYW:
    :cvar BYX:
    :cvar BYZ:
    :cvar BZA:
    :cvar BZB:
    :cvar BZC:
    :cvar BZD:
    :cvar BZE:
    :cvar BZF:
    :cvar BZG:
    :cvar BZH:
    :cvar BZI:
    :cvar BZJ:
    :cvar BZK:
    :cvar BZL:
    :cvar BZM:
    :cvar BZN:
    :cvar BZO:
    :cvar BZP:
    :cvar BZQ:
    :cvar BZR:
    :cvar BZS:
    :cvar BZU:
    :cvar BZV:
    :cvar BZW:
    :cvar BZX:
    :cvar BZY:
    :cvar BZZ:
    :cvar CAA:
    :cvar CAB:
    :cvar CAC:
    :cvar CAD:
    :cvar CAE:
    :cvar CAF:
    :cvar CAG:
    :cvar CAH:
    :cvar CAJ:
    :cvar CAK:
    :cvar CAL:
    :cvar CAM:
    :cvar CAN:
    :cvar CAO:
    :cvar CAP:
    :cvar CAQ:
    :cvar CAR:
    :cvar CAS:
    :cvar CAT:
    :cvar CAV:
    :cvar CAW:
    :cvar CAX:
    :cvar CAY:
    :cvar CAZ:
    :cvar CBB:
    :cvar CBC:
    :cvar CBD:
    :cvar CBG:
    :cvar CBI:
    :cvar CBJ:
    :cvar CBK:
    :cvar CBL:
    :cvar CBN:
    :cvar CBO:
    :cvar CBQ:
    :cvar CBR:
    :cvar CBS:
    :cvar CBT:
    :cvar CBU:
    :cvar CBV:
    :cvar CBW:
    :cvar CBY:
    :cvar CCC:
    :cvar CCD:
    :cvar CCE:
    :cvar CCG:
    :cvar CCH:
    :cvar CCJ:
    :cvar CCL:
    :cvar CCM:
    :cvar CCO:
    :cvar CCP:
    :cvar CCR:
    :cvar CDA:
    :cvar CDE:
    :cvar CDF:
    :cvar CDH:
    :cvar CDI:
    :cvar CDJ:
    :cvar CDM:
    :cvar CDN:
    :cvar CDO:
    :cvar CDR:
    :cvar CDS:
    :cvar CDY:
    :cvar CDZ:
    :cvar CEA:
    :cvar CEB:
    :cvar CEG:
    :cvar CEK:
    :cvar CEN:
    :cvar CES:
    :cvar CET:
    :cvar CEY:
    :cvar CFA:
    :cvar CFD:
    :cvar CFG:
    :cvar CFM:
    :cvar CGA:
    :cvar CGC:
    :cvar CGG:
    :cvar CGK:
    :cvar CHA:
    :cvar CHB:
    :cvar CHC:
    :cvar CHD:
    :cvar CHE:
    :cvar CHF:
    :cvar CHG:
    :cvar CHH:
    :cvar CHI:
    :cvar CHJ:
    :cvar CHK:
    :cvar CHL:
    :cvar CHN:
    :cvar CHO:
    :cvar CHP:
    :cvar CHQ:
    :cvar CHR:
    :cvar CHT:
    :cvar CHU:
    :cvar CHV:
    :cvar CHW:
    :cvar CHX:
    :cvar CHY:
    :cvar CHZ:
    :cvar CIA:
    :cvar CIB:
    :cvar CIC:
    :cvar CID:
    :cvar CIE:
    :cvar CIH:
    :cvar CIK:
    :cvar CIM:
    :cvar CIN:
    :cvar CIP:
    :cvar CIR:
    :cvar CIW:
    :cvar CIY:
    :cvar CJA:
    :cvar CJE:
    :cvar CJH:
    :cvar CJI:
    :cvar CJK:
    :cvar CJM:
    :cvar CJN:
    :cvar CJO:
    :cvar CJP:
    :cvar CJS:
    :cvar CJV:
    :cvar CJY:
    :cvar CKB:
    :cvar CKH:
    :cvar CKL:
    :cvar CKM:
    :cvar CKN:
    :cvar CKO:
    :cvar CKQ:
    :cvar CKR:
    :cvar CKS:
    :cvar CKT:
    :cvar CKU:
    :cvar CKV:
    :cvar CKX:
    :cvar CKY:
    :cvar CKZ:
    :cvar CLA:
    :cvar CLC:
    :cvar CLD:
    :cvar CLE:
    :cvar CLH:
    :cvar CLI:
    :cvar CLJ:
    :cvar CLK:
    :cvar CLL:
    :cvar CLM:
    :cvar CLO:
    :cvar CLT:
    :cvar CLU:
    :cvar CLW:
    :cvar CLY:
    :cvar CMA:
    :cvar CME:
    :cvar CMI:
    :cvar CML:
    :cvar CMM:
    :cvar CMN:
    :cvar CMO:
    :cvar CMR:
    :cvar CMT:
    :cvar CNA:
    :cvar CNB:
    :cvar CNC:
    :cvar CNG:
    :cvar CNH:
    :cvar CNI:
    :cvar CNK:
    :cvar CNL:
    :cvar CNO:
    :cvar CNP:
    :cvar CNQ:
    :cvar CNR:
    :cvar CNS:
    :cvar CNT:
    :cvar CNU:
    :cvar CNW:
    :cvar COA:
    :cvar COB:
    :cvar COC:
    :cvar COD:
    :cvar COE:
    :cvar COF:
    :cvar COG:
    :cvar COH:
    :cvar COJ:
    :cvar COK:
    :cvar COL:
    :cvar COM:
    :cvar CON:
    :cvar COO:
    :cvar COP:
    :cvar COQ:
    :cvar COR:
    :cvar COS:
    :cvar COT:
    :cvar COU:
    :cvar COV:
    :cvar COW:
    :cvar COX:
    :cvar COZ:
    :cvar CPA:
    :cvar CPB:
    :cvar CPC:
    :cvar CPG:
    :cvar CPI:
    :cvar CPN:
    :cvar CPO:
    :cvar CPS:
    :cvar CPU:
    :cvar CPX:
    :cvar CPY:
    :cvar CQD:
    :cvar CRA:
    :cvar CRB:
    :cvar CRC:
    :cvar CRD:
    :cvar CRF:
    :cvar CRG:
    :cvar CRH:
    :cvar CRI:
    :cvar CRJ:
    :cvar CRK:
    :cvar CRL:
    :cvar CRM:
    :cvar CRN:
    :cvar CRO:
    :cvar CRQ:
    :cvar CRR:
    :cvar CRS:
    :cvar CRT:
    :cvar CRV:
    :cvar CRW:
    :cvar CRX:
    :cvar CRY:
    :cvar CRZ:
    :cvar CSA:
    :cvar CSB:
    :cvar CSC:
    :cvar CSD:
    :cvar CSE:
    :cvar CSF:
    :cvar CSG:
    :cvar CSH:
    :cvar CSI:
    :cvar CSJ:
    :cvar CSK:
    :cvar CSL:
    :cvar CSM:
    :cvar CSN:
    :cvar CSO:
    :cvar CSP:
    :cvar CSQ:
    :cvar CSR:
    :cvar CSS:
    :cvar CST:
    :cvar CSV:
    :cvar CSW:
    :cvar CSX:
    :cvar CSY:
    :cvar CSZ:
    :cvar CTA:
    :cvar CTC:
    :cvar CTD:
    :cvar CTE:
    :cvar CTG:
    :cvar CTH:
    :cvar CTL:
    :cvar CTM:
    :cvar CTN:
    :cvar CTO:
    :cvar CTP:
    :cvar CTS:
    :cvar CTT:
    :cvar CTU:
    :cvar CTY:
    :cvar CTZ:
    :cvar CUA:
    :cvar CUB:
    :cvar CUC:
    :cvar CUH:
    :cvar CUI:
    :cvar CUJ:
    :cvar CUK:
    :cvar CUL:
    :cvar CUO:
    :cvar CUP:
    :cvar CUQ:
    :cvar CUR:
    :cvar CUT:
    :cvar CUU:
    :cvar CUV:
    :cvar CUW:
    :cvar CUX:
    :cvar CUY:
    :cvar CVG:
    :cvar CVN:
    :cvar CWA:
    :cvar CWB:
    :cvar CWD:
    :cvar CWE:
    :cvar CWG:
    :cvar CWT:
    :cvar CXH:
    :cvar CYA:
    :cvar CYB:
    :cvar CYM:
    :cvar CYO:
    :cvar CZH:
    :cvar CZK:
    :cvar CZN:
    :cvar CZO:
    :cvar CZT:
    :cvar DAA:
    :cvar DAC:
    :cvar DAD:
    :cvar DAE:
    :cvar DAG:
    :cvar DAH:
    :cvar DAI:
    :cvar DAJ:
    :cvar DAK:
    :cvar DAL:
    :cvar DAM:
    :cvar DAN:
    :cvar DAO:
    :cvar DAQ:
    :cvar DAR:
    :cvar DAS:
    :cvar DAU:
    :cvar DAV:
    :cvar DAW:
    :cvar DAX:
    :cvar DAZ:
    :cvar DBA:
    :cvar DBB:
    :cvar DBD:
    :cvar DBE:
    :cvar DBF:
    :cvar DBG:
    :cvar DBI:
    :cvar DBJ:
    :cvar DBL:
    :cvar DBM:
    :cvar DBN:
    :cvar DBO:
    :cvar DBP:
    :cvar DBQ:
    :cvar DBR:
    :cvar DBT:
    :cvar DBU:
    :cvar DBV:
    :cvar DBW:
    :cvar DBY:
    :cvar DCC:
    :cvar DCR:
    :cvar DDA:
    :cvar DDD:
    :cvar DDE:
    :cvar DDG:
    :cvar DDI:
    :cvar DDJ:
    :cvar DDN:
    :cvar DDO:
    :cvar DDR:
    :cvar DDS:
    :cvar DDW:
    :cvar DEC:
    :cvar DED:
    :cvar DEE:
    :cvar DEF:
    :cvar DEG:
    :cvar DEH:
    :cvar DEI:
    :cvar DEM:
    :cvar DEP:
    :cvar DEQ:
    :cvar DER:
    :cvar DES:
    :cvar DEU: Deutsch
    :cvar DEV:
    :cvar DEZ:
    :cvar DGA:
    :cvar DGB:
    :cvar DGC:
    :cvar DGD:
    :cvar DGE:
    :cvar DGG:
    :cvar DGH:
    :cvar DGI:
    :cvar DGK:
    :cvar DGL:
    :cvar DGN:
    :cvar DGO:
    :cvar DGR:
    :cvar DGS:
    :cvar DGT:
    :cvar DGW:
    :cvar DGX:
    :cvar DGZ:
    :cvar DHD:
    :cvar DHG:
    :cvar DHI:
    :cvar DHL:
    :cvar DHM:
    :cvar DHN:
    :cvar DHO:
    :cvar DHR:
    :cvar DHS:
    :cvar DHU:
    :cvar DHV:
    :cvar DHW:
    :cvar DHX:
    :cvar DIA:
    :cvar DIB:
    :cvar DIC:
    :cvar DID:
    :cvar DIF:
    :cvar DIG:
    :cvar DIH:
    :cvar DII:
    :cvar DIJ:
    :cvar DIK:
    :cvar DIL:
    :cvar DIM:
    :cvar DIO:
    :cvar DIP:
    :cvar DIQ:
    :cvar DIR:
    :cvar DIS:
    :cvar DIU:
    :cvar DIV:
    :cvar DIW:
    :cvar DIX:
    :cvar DIY:
    :cvar DIZ:
    :cvar DJA:
    :cvar DJB:
    :cvar DJC:
    :cvar DJD:
    :cvar DJE:
    :cvar DJF:
    :cvar DJI:
    :cvar DJJ:
    :cvar DJK:
    :cvar DJM:
    :cvar DJN:
    :cvar DJO:
    :cvar DJR:
    :cvar DJU:
    :cvar DJW:
    :cvar DKA:
    :cvar DKG:
    :cvar DKK:
    :cvar DKR:
    :cvar DKS:
    :cvar DKX:
    :cvar DLG:
    :cvar DLK:
    :cvar DLM:
    :cvar DLN:
    :cvar DMA:
    :cvar DMB:
    :cvar DMC:
    :cvar DMD:
    :cvar DME:
    :cvar DMG:
    :cvar DMK:
    :cvar DML:
    :cvar DMM:
    :cvar DMO:
    :cvar DMR:
    :cvar DMS:
    :cvar DMU:
    :cvar DMV:
    :cvar DMW:
    :cvar DMX:
    :cvar DMY:
    :cvar DNA:
    :cvar DND:
    :cvar DNE:
    :cvar DNG:
    :cvar DNI:
    :cvar DNJ:
    :cvar DNK:
    :cvar DNN:
    :cvar DNO:
    :cvar DNR:
    :cvar DNT:
    :cvar DNU:
    :cvar DNV:
    :cvar DNW:
    :cvar DNY:
    :cvar DOA:
    :cvar DOB:
    :cvar DOC:
    :cvar DOE:
    :cvar DOF:
    :cvar DOH:
    :cvar DOK:
    :cvar DOL:
    :cvar DON:
    :cvar DOO:
    :cvar DOP:
    :cvar DOQ:
    :cvar DOR:
    :cvar DOS:
    :cvar DOT:
    :cvar DOV:
    :cvar DOW:
    :cvar DOX:
    :cvar DOY:
    :cvar DOZ:
    :cvar DPP:
    :cvar DRB:
    :cvar DRC:
    :cvar DRD:
    :cvar DRE:
    :cvar DRG:
    :cvar DRI:
    :cvar DRL:
    :cvar DRN:
    :cvar DRO:
    :cvar DRQ:
    :cvar DRS:
    :cvar DRT:
    :cvar DRU:
    :cvar DRY:
    :cvar DSB:
    :cvar DSE:
    :cvar DSH:
    :cvar DSI:
    :cvar DSK:
    :cvar DSL:
    :cvar DSN:
    :cvar DSO:
    :cvar DSQ:
    :cvar DSZ:
    :cvar DTA:
    :cvar DTB:
    :cvar DTD:
    :cvar DTH:
    :cvar DTI:
    :cvar DTK:
    :cvar DTM:
    :cvar DTN:
    :cvar DTO:
    :cvar DTP:
    :cvar DTR:
    :cvar DTS:
    :cvar DTT:
    :cvar DTU:
    :cvar DTY:
    :cvar DUA:
    :cvar DUB:
    :cvar DUC:
    :cvar DUE:
    :cvar DUF:
    :cvar DUG:
    :cvar DUH:
    :cvar DUI:
    :cvar DUK:
    :cvar DUL:
    :cvar DUN:
    :cvar DUO:
    :cvar DUP:
    :cvar DUQ:
    :cvar DUR:
    :cvar DUS:
    :cvar DUU:
    :cvar DUV:
    :cvar DUW:
    :cvar DUX:
    :cvar DUY:
    :cvar DUZ:
    :cvar DVA:
    :cvar DWA:
    :cvar DWK:
    :cvar DWR:
    :cvar DWU:
    :cvar DWW:
    :cvar DWY:
    :cvar DWZ:
    :cvar DYA:
    :cvar DYB:
    :cvar DYD:
    :cvar DYG:
    :cvar DYI:
    :cvar DYM:
    :cvar DYN:
    :cvar DYO:
    :cvar DYR:
    :cvar DYU:
    :cvar DYY:
    :cvar DZA:
    :cvar DZD:
    :cvar DZE:
    :cvar DZG:
    :cvar DZL:
    :cvar DZN:
    :cvar DZO:
    :cvar EAA:
    :cvar EBC:
    :cvar EBG:
    :cvar EBK:
    :cvar EBO:
    :cvar EBR:
    :cvar EBU:
    :cvar ECS:
    :cvar EEE:
    :cvar EFA:
    :cvar EFE:
    :cvar EFI:
    :cvar EGA:
    :cvar EGL:
    :cvar EGM:
    :cvar EGO:
    :cvar EHS:
    :cvar EHU:
    :cvar EIP:
    :cvar EIT:
    :cvar EIV:
    :cvar EJA:
    :cvar EKA:
    :cvar EKE:
    :cvar EKG:
    :cvar EKI:
    :cvar EKK:
    :cvar EKL:
    :cvar EKM:
    :cvar EKO:
    :cvar EKP:
    :cvar EKR:
    :cvar EKY:
    :cvar ELE:
    :cvar ELH:
    :cvar ELI:
    :cvar ELK:
    :cvar ELL:
    :cvar ELM:
    :cvar ELO:
    :cvar ELU:
    :cvar EMA:
    :cvar EMB:
    :cvar EME:
    :cvar EMG:
    :cvar EMI:
    :cvar EMK:
    :cvar EMM:
    :cvar EMN:
    :cvar EMP:
    :cvar EMQ:
    :cvar EMS:
    :cvar EMU:
    :cvar EMW:
    :cvar EMX:
    :cvar EMZ:
    :cvar ENA:
    :cvar ENB:
    :cvar ENC:
    :cvar END:
    :cvar ENF:
    :cvar ENG:
    :cvar ENH:
    :cvar ENL:
    :cvar ENN:
    :cvar ENO:
    :cvar ENQ:
    :cvar ENR:
    :cvar ENU:
    :cvar ENV:
    :cvar ENW:
    :cvar ENX:
    :cvar EOT:
    :cvar EPI:
    :cvar EPO:
    :cvar ERA:
    :cvar ERG:
    :cvar ERH:
    :cvar ERI:
    :cvar ERK:
    :cvar ERO:
    :cvar ERR:
    :cvar ERS:
    :cvar ERT:
    :cvar ERW:
    :cvar ESE:
    :cvar ESG:
    :cvar ESH:
    :cvar ESI:
    :cvar ESK:
    :cvar ESL:
    :cvar ESM:
    :cvar ESN:
    :cvar ESO:
    :cvar ESQ:
    :cvar ESS:
    :cvar ESU:
    :cvar ESY:
    :cvar ETB:
    :cvar ETC:
    :cvar ETH:
    :cvar ETN:
    :cvar ETO:
    :cvar ETR:
    :cvar ETS:
    :cvar ETU:
    :cvar ETX:
    :cvar ETZ:
    :cvar EUD:
    :cvar EUS:
    :cvar EVE:
    :cvar EVH:
    :cvar EVN:
    :cvar EWE:
    :cvar EWO:
    :cvar EXT:
    :cvar EYA:
    :cvar EYO:
    :cvar EZA:
    :cvar EZE:
    :cvar FAA:
    :cvar FAB:
    :cvar FAD:
    :cvar FAF:
    :cvar FAG:
    :cvar FAH:
    :cvar FAI:
    :cvar FAJ:
    :cvar FAK:
    :cvar FAL:
    :cvar FAM:
    :cvar FAN:
    :cvar FAO:
    :cvar FAP:
    :cvar FAR:
    :cvar FAU:
    :cvar FAX:
    :cvar FAY:
    :cvar FBL:
    :cvar FCS:
    :cvar FER:
    :cvar FFI:
    :cvar FFM:
    :cvar FGR:
    :cvar FIA:
    :cvar FIE:
    :cvar FIF:
    :cvar FIJ:
    :cvar FIL:
    :cvar FIN:
    :cvar FIP:
    :cvar FIR:
    :cvar FIT:
    :cvar FIW:
    :cvar FKK:
    :cvar FKV:
    :cvar FLA:
    :cvar FLH:
    :cvar FLI:
    :cvar FLL:
    :cvar FLN:
    :cvar FLR:
    :cvar FLY:
    :cvar FMP:
    :cvar FMU:
    :cvar FNB:
    :cvar FNG:
    :cvar FNI:
    :cvar FOD:
    :cvar FOI:
    :cvar FOM:
    :cvar FON:
    :cvar FOR:
    :cvar FOS:
    :cvar FPE:
    :cvar FQS:
    :cvar FRA:
    :cvar FRC:
    :cvar FRD:
    :cvar FRP:
    :cvar FRQ:
    :cvar FRR:
    :cvar FRS:
    :cvar FRT:
    :cvar FRY:
    :cvar FSE:
    :cvar FSL:
    :cvar FSS:
    :cvar FUB:
    :cvar FUC:
    :cvar FUD:
    :cvar FUE:
    :cvar FUF:
    :cvar FUH:
    :cvar FUI:
    :cvar FUJ:
    :cvar FUM:
    :cvar FUN:
    :cvar FUQ:
    :cvar FUR:
    :cvar FUT:
    :cvar FUU:
    :cvar FUV:
    :cvar FUY:
    :cvar FVR:
    :cvar FWA:
    :cvar FWE:
    :cvar GAA:
    :cvar GAB:
    :cvar GAC:
    :cvar GAD:
    :cvar GAE:
    :cvar GAF:
    :cvar GAG:
    :cvar GAH:
    :cvar GAI:
    :cvar GAJ:
    :cvar GAK:
    :cvar GAL:
    :cvar GAM:
    :cvar GAN:
    :cvar GAO:
    :cvar GAP:
    :cvar GAQ:
    :cvar GAR:
    :cvar GAS:
    :cvar GAT:
    :cvar GAU:
    :cvar GAW:
    :cvar GAX:
    :cvar GAY:
    :cvar GAZ:
    :cvar GBB:
    :cvar GBD:
    :cvar GBE:
    :cvar GBF:
    :cvar GBG:
    :cvar GBH:
    :cvar GBI:
    :cvar GBJ:
    :cvar GBK:
    :cvar GBL:
    :cvar GBM:
    :cvar GBN:
    :cvar GBO:
    :cvar GBP:
    :cvar GBQ:
    :cvar GBR:
    :cvar GBS:
    :cvar GBU:
    :cvar GBV:
    :cvar GBW:
    :cvar GBX:
    :cvar GBY:
    :cvar GBZ:
    :cvar GCC:
    :cvar GCD:
    :cvar GCE:
    :cvar GCF:
    :cvar GCL:
    :cvar GCN:
    :cvar GCR:
    :cvar GCT:
    :cvar GDA:
    :cvar GDB:
    :cvar GDC:
    :cvar GDD:
    :cvar GDE:
    :cvar GDF:
    :cvar GDG:
    :cvar GDH:
    :cvar GDI:
    :cvar GDJ:
    :cvar GDK:
    :cvar GDL:
    :cvar GDM:
    :cvar GDN:
    :cvar GDO:
    :cvar GDQ:
    :cvar GDR:
    :cvar GDS:
    :cvar GDT:
    :cvar GDU:
    :cvar GDX:
    :cvar GEA:
    :cvar GEB:
    :cvar GEC:
    :cvar GED:
    :cvar GEF:
    :cvar GEG:
    :cvar GEH:
    :cvar GEI:
    :cvar GEJ:
    :cvar GEK:
    :cvar GEL:
    :cvar GEQ:
    :cvar GES:
    :cvar GEV:
    :cvar GEW:
    :cvar GEX:
    :cvar GEY:
    :cvar GEZ:
    :cvar GFK:
    :cvar GFT:
    :cvar GGA:
    :cvar GGB:
    :cvar GGD:
    :cvar GGE:
    :cvar GGG:
    :cvar GGK:
    :cvar GGL:
    :cvar GGT:
    :cvar GGU:
    :cvar GGW:
    :cvar GHA:
    :cvar GHE:
    :cvar GHH:
    :cvar GHK:
    :cvar GHL:
    :cvar GHN:
    :cvar GHO:
    :cvar GHR:
    :cvar GHS:
    :cvar GHT:
    :cvar GIA:
    :cvar GIB:
    :cvar GIC:
    :cvar GID:
    :cvar GIE:
    :cvar GIG:
    :cvar GIH:
    :cvar GII:
    :cvar GIL:
    :cvar GIM:
    :cvar GIN:
    :cvar GIP:
    :cvar GIQ:
    :cvar GIR:
    :cvar GIS:
    :cvar GIT:
    :cvar GIU:
    :cvar GIW:
    :cvar GIX:
    :cvar GIY:
    :cvar GIZ:
    :cvar GJK:
    :cvar GJM:
    :cvar GJN:
    :cvar GJR:
    :cvar GJU:
    :cvar GKA:
    :cvar GKD:
    :cvar GKE:
    :cvar GKN:
    :cvar GKO:
    :cvar GKP:
    :cvar GKU:
    :cvar GLA:
    :cvar GLB:
    :cvar GLC:
    :cvar GLD:
    :cvar GLE:
    :cvar GLG:
    :cvar GLH:
    :cvar GLJ:
    :cvar GLK:
    :cvar GLL:
    :cvar GLO:
    :cvar GLR:
    :cvar GLU:
    :cvar GLV:
    :cvar GLW:
    :cvar GLY:
    :cvar GMA:
    :cvar GMB:
    :cvar GMD:
    :cvar GMG:
    :cvar GMM:
    :cvar GMN:
    :cvar GMR:
    :cvar GMU:
    :cvar GMV:
    :cvar GMX:
    :cvar GMZ:
    :cvar GNA:
    :cvar GNB:
    :cvar GNC:
    :cvar GND:
    :cvar GNE:
    :cvar GNG:
    :cvar GNH:
    :cvar GNI:
    :cvar GNJ:
    :cvar GNK:
    :cvar GNL:
    :cvar GNM:
    :cvar GNN:
    :cvar GNO:
    :cvar GNQ:
    :cvar GNR:
    :cvar GNT:
    :cvar GNU:
    :cvar GNW:
    :cvar GNZ:
    :cvar GOA:
    :cvar GOB:
    :cvar GOC:
    :cvar GOD:
    :cvar GOE:
    :cvar GOF:
    :cvar GOG:
    :cvar GOI:
    :cvar GOJ:
    :cvar GOK:
    :cvar GOL:
    :cvar GOM:
    :cvar GOO:
    :cvar GOP:
    :cvar GOQ:
    :cvar GOR:
    :cvar GOS:
    :cvar GOU:
    :cvar GOV:
    :cvar GOW:
    :cvar GOX:
    :cvar GOY:
    :cvar GOZ:
    :cvar GPA:
    :cvar GPE:
    :cvar GPN:
    :cvar GQA:
    :cvar GQI:
    :cvar GQN:
    :cvar GQR:
    :cvar GQU:
    :cvar GRA:
    :cvar GRC:
    :cvar GRD:
    :cvar GRG:
    :cvar GRH:
    :cvar GRI:
    :cvar GRJ:
    :cvar GRM:
    :cvar GRO:
    :cvar GRQ:
    :cvar GRR:
    :cvar GRS:
    :cvar GRT:
    :cvar GRU:
    :cvar GRV:
    :cvar GRW:
    :cvar GRX:
    :cvar GRY:
    :cvar GRZ:
    :cvar GSE:
    :cvar GSG:
    :cvar GSL:
    :cvar GSM:
    :cvar GSN:
    :cvar GSO:
    :cvar GSP:
    :cvar GSS:
    :cvar GSW:
    :cvar GTA:
    :cvar GTU:
    :cvar GUA:
    :cvar GUB:
    :cvar GUC:
    :cvar GUD:
    :cvar GUE:
    :cvar GUF:
    :cvar GUG:
    :cvar GUH:
    :cvar GUI:
    :cvar GUJ:
    :cvar GUK:
    :cvar GUL:
    :cvar GUM:
    :cvar GUN:
    :cvar GUO:
    :cvar GUP:
    :cvar GUQ:
    :cvar GUR:
    :cvar GUS:
    :cvar GUT:
    :cvar GUU:
    :cvar GUW:
    :cvar GUX:
    :cvar GUZ:
    :cvar GVA:
    :cvar GVC:
    :cvar GVE:
    :cvar GVF:
    :cvar GVJ:
    :cvar GVL:
    :cvar GVM:
    :cvar GVN:
    :cvar GVO:
    :cvar GVP:
    :cvar GVR:
    :cvar GVS:
    :cvar GVY:
    :cvar GWA:
    :cvar GWB:
    :cvar GWC:
    :cvar GWD:
    :cvar GWE:
    :cvar GWF:
    :cvar GWG:
    :cvar GWI:
    :cvar GWJ:
    :cvar GWM:
    :cvar GWN:
    :cvar GWR:
    :cvar GWT:
    :cvar GWU:
    :cvar GWW:
    :cvar GWX:
    :cvar GXX:
    :cvar GYA:
    :cvar GYB:
    :cvar GYD:
    :cvar GYE:
    :cvar GYF:
    :cvar GYG:
    :cvar GYI:
    :cvar GYL:
    :cvar GYM:
    :cvar GYN:
    :cvar GYO:
    :cvar GYR:
    :cvar GYY:
    :cvar GYZ:
    :cvar GZA:
    :cvar GZI:
    :cvar GZN:
    :cvar HAA:
    :cvar HAB:
    :cvar HAC:
    :cvar HAD:
    :cvar HAE:
    :cvar HAF:
    :cvar HAG:
    :cvar HAH:
    :cvar HAJ:
    :cvar HAK:
    :cvar HAL:
    :cvar HAM:
    :cvar HAN:
    :cvar HAO:
    :cvar HAP:
    :cvar HAQ:
    :cvar HAR:
    :cvar HAS:
    :cvar HAT:
    :cvar HAU:
    :cvar HAV:
    :cvar HAW:
    :cvar HAX:
    :cvar HAY:
    :cvar HAZ:
    :cvar HBA:
    :cvar HBB:
    :cvar HBN:
    :cvar HBO:
    :cvar HBU:
    :cvar HCA:
    :cvar HCH:
    :cvar HDN:
    :cvar HDS:
    :cvar HDY:
    :cvar HEA:
    :cvar HEB:
    :cvar HED:
    :cvar HEG:
    :cvar HEH:
    :cvar HEI:
    :cvar HEM:
    :cvar HER:
    :cvar HGM:
    :cvar HGW:
    :cvar HHI:
    :cvar HHR:
    :cvar HHY:
    :cvar HIA:
    :cvar HIB:
    :cvar HID:
    :cvar HIF:
    :cvar HIG:
    :cvar HIH:
    :cvar HII:
    :cvar HIJ:
    :cvar HIK:
    :cvar HIL:
    :cvar HIN:
    :cvar HIO:
    :cvar HIR:
    :cvar HIW:
    :cvar HIX:
    :cvar HJI:
    :cvar HKA:
    :cvar HKE:
    :cvar HKH:
    :cvar HKK:
    :cvar HKN:
    :cvar HKS:
    :cvar HLA:
    :cvar HLB:
    :cvar HLD:
    :cvar HLE:
    :cvar HLT:
    :cvar HMA:
    :cvar HMB:
    :cvar HMC:
    :cvar HMD:
    :cvar HME:
    :cvar HMF:
    :cvar HMG:
    :cvar HMH:
    :cvar HMI:
    :cvar HMJ:
    :cvar HML:
    :cvar HMM:
    :cvar HMO:
    :cvar HMP:
    :cvar HMQ:
    :cvar HMR:
    :cvar HMS:
    :cvar HMT:
    :cvar HMU:
    :cvar HMV:
    :cvar HMW:
    :cvar HMY:
    :cvar HMZ:
    :cvar HNA:
    :cvar HND:
    :cvar HNE:
    :cvar HNG:
    :cvar HNH:
    :cvar HNI:
    :cvar HNJ:
    :cvar HNM:
    :cvar HNN:
    :cvar HNO:
    :cvar HNS:
    :cvar HNU:
    :cvar HOA:
    :cvar HOB:
    :cvar HOC:
    :cvar HOD:
    :cvar HOE:
    :cvar HOH:
    :cvar HOI:
    :cvar HOJ:
    :cvar HOL:
    :cvar HOM:
    :cvar HOO:
    :cvar HOP:
    :cvar HOR:
    :cvar HOS:
    :cvar HOT:
    :cvar HOV:
    :cvar HOW:
    :cvar HOY:
    :cvar HOZ:
    :cvar HPO:
    :cvar HPS:
    :cvar HRA:
    :cvar HRC:
    :cvar HRE:
    :cvar HRK:
    :cvar HRM:
    :cvar HRO:
    :cvar HRP:
    :cvar HRT:
    :cvar HRU:
    :cvar HRV:
    :cvar HRW:
    :cvar HRX:
    :cvar HRZ:
    :cvar HSB:
    :cvar HSH:
    :cvar HSL:
    :cvar HSN:
    :cvar HSS:
    :cvar HTI:
    :cvar HTO:
    :cvar HTS:
    :cvar HTU:
    :cvar HUB:
    :cvar HUC:
    :cvar HUD:
    :cvar HUE:
    :cvar HUF:
    :cvar HUG:
    :cvar HUH:
    :cvar HUI:
    :cvar HUJ:
    :cvar HUK:
    :cvar HUL:
    :cvar HUM:
    :cvar HUN:
    :cvar HUO:
    :cvar HUP:
    :cvar HUQ:
    :cvar HUR:
    :cvar HUS:
    :cvar HUT:
    :cvar HUU:
    :cvar HUV:
    :cvar HUW:
    :cvar HUX:
    :cvar HUY:
    :cvar HUZ:
    :cvar HVC:
    :cvar HVE:
    :cvar HVK:
    :cvar HVN:
    :cvar HVV:
    :cvar HWA:
    :cvar HWC:
    :cvar HWO:
    :cvar HYA:
    :cvar HYE:
    :cvar HYW:
    :cvar IAI:
    :cvar IAN:
    :cvar IAR:
    :cvar IBA:
    :cvar IBB:
    :cvar IBD:
    :cvar IBE:
    :cvar IBG:
    :cvar IBH:
    :cvar IBL:
    :cvar IBM:
    :cvar IBN:
    :cvar IBO:
    :cvar IBR:
    :cvar IBU:
    :cvar IBY:
    :cvar ICA:
    :cvar ICH:
    :cvar ICL:
    :cvar ICR:
    :cvar IDA:
    :cvar IDB:
    :cvar IDC:
    :cvar IDD:
    :cvar IDE:
    :cvar IDI:
    :cvar IDR:
    :cvar IDS:
    :cvar IDT:
    :cvar IDU:
    :cvar IFA:
    :cvar IFB:
    :cvar IFE:
    :cvar IFF:
    :cvar IFK:
    :cvar IFM:
    :cvar IFU:
    :cvar IFY:
    :cvar IGB:
    :cvar IGE:
    :cvar IGG:
    :cvar IGL:
    :cvar IGM:
    :cvar IGN:
    :cvar IGO:
    :cvar IGW:
    :cvar IHB:
    :cvar IHI:
    :cvar IHP:
    :cvar IHW:
    :cvar III:
    :cvar IIN:
    :cvar IJC:
    :cvar IJE:
    :cvar IJJ:
    :cvar IJN:
    :cvar IJS:
    :cvar IKE:
    :cvar IKH:
    :cvar IKI:
    :cvar IKK:
    :cvar IKL:
    :cvar IKO:
    :cvar IKP:
    :cvar IKR:
    :cvar IKS:
    :cvar IKT:
    :cvar IKV:
    :cvar IKW:
    :cvar IKX:
    :cvar IKZ:
    :cvar ILA:
    :cvar ILB:
    :cvar ILG:
    :cvar ILI:
    :cvar ILK:
    :cvar ILM:
    :cvar ILO:
    :cvar ILP:
    :cvar ILS:
    :cvar ILU:
    :cvar ILV:
    :cvar IMA:
    :cvar IMI:
    :cvar IML:
    :cvar IMN:
    :cvar IMO:
    :cvar IMR:
    :cvar IMT:
    :cvar INB:
    :cvar IND:
    :cvar ING:
    :cvar INH:
    :cvar INJ:
    :cvar INL:
    :cvar INN:
    :cvar INO:
    :cvar INP:
    :cvar INS:
    :cvar INT:
    :cvar INZ:
    :cvar IOR:
    :cvar IOU:
    :cvar IOW:
    :cvar IPI:
    :cvar IPO:
    :cvar IQU:
    :cvar IQW:
    :cvar IRE:
    :cvar IRH:
    :cvar IRI:
    :cvar IRK:
    :cvar IRN:
    :cvar IRR:
    :cvar IRU:
    :cvar IRX:
    :cvar IRY:
    :cvar ISA:
    :cvar ISC:
    :cvar ISD:
    :cvar ISE:
    :cvar ISG:
    :cvar ISH:
    :cvar ISI:
    :cvar ISK:
    :cvar ISL:
    :cvar ISM:
    :cvar ISN:
    :cvar ISO:
    :cvar ISR:
    :cvar IST:
    :cvar ISU:
    :cvar ITA:
    :cvar ITB:
    :cvar ITD:
    :cvar ITE:
    :cvar ITI:
    :cvar ITK:
    :cvar ITL:
    :cvar ITM:
    :cvar ITO:
    :cvar ITR:
    :cvar ITS:
    :cvar ITT:
    :cvar ITV:
    :cvar ITW:
    :cvar ITX:
    :cvar ITY:
    :cvar ITZ:
    :cvar IUM:
    :cvar IVB:
    :cvar IVV:
    :cvar IWK:
    :cvar IWM:
    :cvar IWO:
    :cvar IWS:
    :cvar IXC:
    :cvar IXL:
    :cvar IYA:
    :cvar IYO:
    :cvar IYX:
    :cvar IZH:
    :cvar IZM:
    :cvar IZR:
    :cvar IZZ:
    :cvar JAA:
    :cvar JAB:
    :cvar JAC:
    :cvar JAD:
    :cvar JAE:
    :cvar JAF:
    :cvar JAH:
    :cvar JAJ:
    :cvar JAK:
    :cvar JAL:
    :cvar JAM:
    :cvar JAN:
    :cvar JAO:
    :cvar JAQ:
    :cvar JAS:
    :cvar JAT:
    :cvar JAU:
    :cvar JAV:
    :cvar JAX:
    :cvar JAY:
    :cvar JAZ:
    :cvar JBE:
    :cvar JBI:
    :cvar JBJ:
    :cvar JBK:
    :cvar JBM:
    :cvar JBN:
    :cvar JBR:
    :cvar JBT:
    :cvar JBU:
    :cvar JBW:
    :cvar JCS:
    :cvar JCT:
    :cvar JDA:
    :cvar JDG:
    :cvar JDT:
    :cvar JEB:
    :cvar JEE:
    :cvar JEH:
    :cvar JEI:
    :cvar JEK:
    :cvar JEL:
    :cvar JEN:
    :cvar JER:
    :cvar JET:
    :cvar JEU:
    :cvar JGB:
    :cvar JGE:
    :cvar JGK:
    :cvar JGO:
    :cvar JHI:
    :cvar JHS:
    :cvar JIA:
    :cvar JIB:
    :cvar JIC:
    :cvar JID:
    :cvar JIE:
    :cvar JIG:
    :cvar JIH:
    :cvar JII:
    :cvar JIL:
    :cvar JIM:
    :cvar JIO:
    :cvar JIQ:
    :cvar JIT:
    :cvar JIU:
    :cvar JIV:
    :cvar JIY:
    :cvar JJE:
    :cvar JJR:
    :cvar JKA:
    :cvar JKM:
    :cvar JKO:
    :cvar JKP:
    :cvar JKR:
    :cvar JKS:
    :cvar JKU:
    :cvar JLE:
    :cvar JLS:
    :cvar JMA:
    :cvar JMB:
    :cvar JMC:
    :cvar JMD:
    :cvar JMI:
    :cvar JML:
    :cvar JMN:
    :cvar JMR:
    :cvar JMS:
    :cvar JMW:
    :cvar JMX:
    :cvar JNA:
    :cvar JND:
    :cvar JNG:
    :cvar JNI:
    :cvar JNJ:
    :cvar JNL:
    :cvar JNS:
    :cvar JOB:
    :cvar JOD:
    :cvar JOG:
    :cvar JOR:
    :cvar JOS:
    :cvar JOW:
    :cvar JPN:
    :cvar JPR:
    :cvar JQR:
    :cvar JRA:
    :cvar JRR:
    :cvar JRT:
    :cvar JRU:
    :cvar JSL:
    :cvar JUA:
    :cvar JUB:
    :cvar JUC:
    :cvar JUD:
    :cvar JUH:
    :cvar JUI:
    :cvar JUK:
    :cvar JUL:
    :cvar JUM:
    :cvar JUN:
    :cvar JUO:
    :cvar JUP:
    :cvar JUR:
    :cvar JUS:
    :cvar JUU:
    :cvar JUW:
    :cvar JUY:
    :cvar JVD:
    :cvar JVN:
    :cvar JWI:
    :cvar JYA:
    :cvar JYE:
    :cvar JYY:
    :cvar KAA:
    :cvar KAB:
    :cvar KAC:
    :cvar KAD:
    :cvar KAE:
    :cvar KAF:
    :cvar KAG:
    :cvar KAH:
    :cvar KAI:
    :cvar KAJ:
    :cvar KAK:
    :cvar KAL:
    :cvar KAM:
    :cvar KAN:
    :cvar KAO:
    :cvar KAP:
    :cvar KAQ:
    :cvar KAS:
    :cvar KAT:
    :cvar KAV:
    :cvar KAX:
    :cvar KAY:
    :cvar KAZ:
    :cvar KBA:
    :cvar KBB:
    :cvar KBC:
    :cvar KBD:
    :cvar KBE:
    :cvar KBG:
    :cvar KBH:
    :cvar KBI:
    :cvar KBJ:
    :cvar KBK:
    :cvar KBL:
    :cvar KBM:
    :cvar KBN:
    :cvar KBO:
    :cvar KBP:
    :cvar KBQ:
    :cvar KBR:
    :cvar KBS:
    :cvar KBT:
    :cvar KBU:
    :cvar KBV:
    :cvar KBW:
    :cvar KBX:
    :cvar KBY:
    :cvar KBZ:
    :cvar KCA:
    :cvar KCB:
    :cvar KCC:
    :cvar KCD:
    :cvar KCE:
    :cvar KCF:
    :cvar KCG:
    :cvar KCH:
    :cvar KCI:
    :cvar KCJ:
    :cvar KCK:
    :cvar KCL:
    :cvar KCM:
    :cvar KCN:
    :cvar KCO:
    :cvar KCP:
    :cvar KCQ:
    :cvar KCR:
    :cvar KCS:
    :cvar KCT:
    :cvar KCU:
    :cvar KCV:
    :cvar KCW:
    :cvar KCX:
    :cvar KCY:
    :cvar KCZ:
    :cvar KDA:
    :cvar KDC:
    :cvar KDD:
    :cvar KDE:
    :cvar KDF:
    :cvar KDG:
    :cvar KDH:
    :cvar KDI:
    :cvar KDJ:
    :cvar KDK:
    :cvar KDL:
    :cvar KDM:
    :cvar KDN:
    :cvar KDP:
    :cvar KDQ:
    :cvar KDR:
    :cvar KDT:
    :cvar KDU:
    :cvar KDW:
    :cvar KDX:
    :cvar KDY:
    :cvar KDZ:
    :cvar KEA:
    :cvar KEB:
    :cvar KEC:
    :cvar KED:
    :cvar KEE:
    :cvar KEF:
    :cvar KEG:
    :cvar KEH:
    :cvar KEI:
    :cvar KEJ:
    :cvar KEK:
    :cvar KEL:
    :cvar KEM:
    :cvar KEN:
    :cvar KEO:
    :cvar KEP:
    :cvar KEQ:
    :cvar KER:
    :cvar KES:
    :cvar KET:
    :cvar KEU:
    :cvar KEV:
    :cvar KEW:
    :cvar KEX:
    :cvar KEY:
    :cvar KEZ:
    :cvar KFA:
    :cvar KFB:
    :cvar KFC:
    :cvar KFD:
    :cvar KFE:
    :cvar KFF:
    :cvar KFG:
    :cvar KFH:
    :cvar KFI:
    :cvar KFJ:
    :cvar KFK:
    :cvar KFL:
    :cvar KFM:
    :cvar KFN:
    :cvar KFO:
    :cvar KFP:
    :cvar KFQ:
    :cvar KFR:
    :cvar KFS:
    :cvar KFT:
    :cvar KFU:
    :cvar KFV:
    :cvar KFW:
    :cvar KFX:
    :cvar KFY:
    :cvar KFZ:
    :cvar KGA:
    :cvar KGB:
    :cvar KGE:
    :cvar KGF:
    :cvar KGG:
    :cvar KGI:
    :cvar KGJ:
    :cvar KGK:
    :cvar KGL:
    :cvar KGN:
    :cvar KGO:
    :cvar KGP:
    :cvar KGQ:
    :cvar KGR:
    :cvar KGS:
    :cvar KGT:
    :cvar KGU:
    :cvar KGV:
    :cvar KGW:
    :cvar KGX:
    :cvar KGY:
    :cvar KHA:
    :cvar KHB:
    :cvar KHC:
    :cvar KHD:
    :cvar KHE:
    :cvar KHF:
    :cvar KHG:
    :cvar KHH:
    :cvar KHJ:
    :cvar KHK:
    :cvar KHL:
    :cvar KHM:
    :cvar KHN:
    :cvar KHP:
    :cvar KHQ:
    :cvar KHR:
    :cvar KHS:
    :cvar KHT:
    :cvar KHU:
    :cvar KHV:
    :cvar KHW:
    :cvar KHX:
    :cvar KHY:
    :cvar KHZ:
    :cvar KIA:
    :cvar KIB:
    :cvar KIC:
    :cvar KID:
    :cvar KIE:
    :cvar KIF:
    :cvar KIG:
    :cvar KIH:
    :cvar KII:
    :cvar KIJ:
    :cvar KIK:
    :cvar KIL:
    :cvar KIM:
    :cvar KIN:
    :cvar KIO:
    :cvar KIP:
    :cvar KIQ:
    :cvar KIR:
    :cvar KIS:
    :cvar KIT:
    :cvar KIU:
    :cvar KIV:
    :cvar KIW:
    :cvar KIX:
    :cvar KIY:
    :cvar KIZ:
    :cvar KJA:
    :cvar KJB:
    :cvar KJC:
    :cvar KJD:
    :cvar KJE:
    :cvar KJG:
    :cvar KJH:
    :cvar KJI:
    :cvar KJJ:
    :cvar KJK:
    :cvar KJL:
    :cvar KJM:
    :cvar KJN:
    :cvar KJO:
    :cvar KJP:
    :cvar KJQ:
    :cvar KJR:
    :cvar KJS:
    :cvar KJT:
    :cvar KJU:
    :cvar KJX:
    :cvar KJY:
    :cvar KJZ:
    :cvar KKA:
    :cvar KKB:
    :cvar KKC:
    :cvar KKD:
    :cvar KKE:
    :cvar KKF:
    :cvar KKG:
    :cvar KKH:
    :cvar KKI:
    :cvar KKJ:
    :cvar KKK:
    :cvar KKL:
    :cvar KKM:
    :cvar KKN:
    :cvar KKO:
    :cvar KKP:
    :cvar KKQ:
    :cvar KKR:
    :cvar KKS:
    :cvar KKT:
    :cvar KKU:
    :cvar KKV:
    :cvar KKW:
    :cvar KKX:
    :cvar KKY:
    :cvar KKZ:
    :cvar KLA:
    :cvar KLB:
    :cvar KLC:
    :cvar KLD:
    :cvar KLE:
    :cvar KLF:
    :cvar KLG:
    :cvar KLH:
    :cvar KLI:
    :cvar KLJ:
    :cvar KLK:
    :cvar KLL:
    :cvar KLM:
    :cvar KLO:
    :cvar KLP:
    :cvar KLQ:
    :cvar KLR:
    :cvar KLS:
    :cvar KLT:
    :cvar KLU:
    :cvar KLV:
    :cvar KLW:
    :cvar KLX:
    :cvar KLY:
    :cvar KLZ:
    :cvar KMA:
    :cvar KMB:
    :cvar KMC:
    :cvar KMD:
    :cvar KME:
    :cvar KMF:
    :cvar KMG:
    :cvar KMH:
    :cvar KMI:
    :cvar KMJ:
    :cvar KMK:
    :cvar KML:
    :cvar KMM:
    :cvar KMN:
    :cvar KMO:
    :cvar KMP:
    :cvar KMQ:
    :cvar KMR:
    :cvar KMS:
    :cvar KMT:
    :cvar KMU:
    :cvar KMV:
    :cvar KMW:
    :cvar KMX:
    :cvar KMY:
    :cvar KMZ:
    :cvar KNA:
    :cvar KNB:
    :cvar KNC:
    :cvar KND:
    :cvar KNE:
    :cvar KNF:
    :cvar KNG:
    :cvar KNI:
    :cvar KNJ:
    :cvar KNK:
    :cvar KNL:
    :cvar KNM:
    :cvar KNN:
    :cvar KNO:
    :cvar KNP:
    :cvar KNQ:
    :cvar KNR:
    :cvar KNS:
    :cvar KNT:
    :cvar KNU:
    :cvar KNV:
    :cvar KNW:
    :cvar KNX:
    :cvar KNY:
    :cvar KNZ:
    :cvar KOA:
    :cvar KOC:
    :cvar KOD:
    :cvar KOE:
    :cvar KOF:
    :cvar KOG:
    :cvar KOH:
    :cvar KOI:
    :cvar KOL:
    :cvar KOO:
    :cvar KOP:
    :cvar KOQ:
    :cvar KOR:
    :cvar KOS:
    :cvar KOT:
    :cvar KOU:
    :cvar KOV:
    :cvar KOW:
    :cvar KOY:
    :cvar KOZ:
    :cvar KPA:
    :cvar KPB:
    :cvar KPC:
    :cvar KPD:
    :cvar KPF:
    :cvar KPG:
    :cvar KPH:
    :cvar KPI:
    :cvar KPJ:
    :cvar KPK:
    :cvar KPL:
    :cvar KPM:
    :cvar KPN:
    :cvar KPO:
    :cvar KPQ:
    :cvar KPR:
    :cvar KPS:
    :cvar KPT:
    :cvar KPU:
    :cvar KPV:
    :cvar KPW:
    :cvar KPX:
    :cvar KPY:
    :cvar KPZ:
    :cvar KQA:
    :cvar KQB:
    :cvar KQC:
    :cvar KQD:
    :cvar KQE:
    :cvar KQF:
    :cvar KQG:
    :cvar KQH:
    :cvar KQI:
    :cvar KQJ:
    :cvar KQK:
    :cvar KQL:
    :cvar KQM:
    :cvar KQN:
    :cvar KQO:
    :cvar KQP:
    :cvar KQQ:
    :cvar KQR:
    :cvar KQS:
    :cvar KQT:
    :cvar KQU:
    :cvar KQV:
    :cvar KQW:
    :cvar KQX:
    :cvar KQY:
    :cvar KQZ:
    :cvar KRA:
    :cvar KRB:
    :cvar KRC:
    :cvar KRD:
    :cvar KRE:
    :cvar KRF:
    :cvar KRH:
    :cvar KRI:
    :cvar KRJ:
    :cvar KRK:
    :cvar KRL:
    :cvar KRN:
    :cvar KRP:
    :cvar KRR:
    :cvar KRS:
    :cvar KRT:
    :cvar KRU:
    :cvar KRV:
    :cvar KRW:
    :cvar KRX:
    :cvar KRY:
    :cvar KRZ:
    :cvar KSB:
    :cvar KSC:
    :cvar KSD:
    :cvar KSE:
    :cvar KSF:
    :cvar KSG:
    :cvar KSH:
    :cvar KSI:
    :cvar KSJ:
    :cvar KSK:
    :cvar KSL:
    :cvar KSM:
    :cvar KSN:
    :cvar KSO:
    :cvar KSP:
    :cvar KSQ:
    :cvar KSR:
    :cvar KSS:
    :cvar KST:
    :cvar KSU:
    :cvar KSV:
    :cvar KSW:
    :cvar KSX:
    :cvar KSY:
    :cvar KSZ:
    :cvar KTA:
    :cvar KTB:
    :cvar KTC:
    :cvar KTD:
    :cvar KTE:
    :cvar KTF:
    :cvar KTG:
    :cvar KTH:
    :cvar KTI:
    :cvar KTJ:
    :cvar KTK:
    :cvar KTL:
    :cvar KTM:
    :cvar KTN:
    :cvar KTO:
    :cvar KTP:
    :cvar KTS:
    :cvar KTT:
    :cvar KTU:
    :cvar KTV:
    :cvar KTW:
    :cvar KTX:
    :cvar KTY:
    :cvar KTZ:
    :cvar KUA:
    :cvar KUB:
    :cvar KUC:
    :cvar KUD:
    :cvar KUE:
    :cvar KUF:
    :cvar KUG:
    :cvar KUH:
    :cvar KUI:
    :cvar KUJ:
    :cvar KUK:
    :cvar KUL:
    :cvar KUM:
    :cvar KUN:
    :cvar KUO:
    :cvar KUP:
    :cvar KUQ:
    :cvar KUS:
    :cvar KUT:
    :cvar KUU:
    :cvar KUV:
    :cvar KUW:
    :cvar KUX:
    :cvar KUY:
    :cvar KUZ:
    :cvar KVA:
    :cvar KVB:
    :cvar KVC:
    :cvar KVD:
    :cvar KVE:
    :cvar KVF:
    :cvar KVG:
    :cvar KVH:
    :cvar KVI:
    :cvar KVJ:
    :cvar KVK:
    :cvar KVL:
    :cvar KVM:
    :cvar KVN:
    :cvar KVO:
    :cvar KVP:
    :cvar KVQ:
    :cvar KVR:
    :cvar KVT:
    :cvar KVU:
    :cvar KVV:
    :cvar KVW:
    :cvar KVX:
    :cvar KVY:
    :cvar KVZ:
    :cvar KWA:
    :cvar KWB:
    :cvar KWC:
    :cvar KWD:
    :cvar KWE:
    :cvar KWF:
    :cvar KWG:
    :cvar KWH:
    :cvar KWI:
    :cvar KWJ:
    :cvar KWK:
    :cvar KWL:
    :cvar KWM:
    :cvar KWN:
    :cvar KWO:
    :cvar KWP:
    :cvar KWR:
    :cvar KWS:
    :cvar KWT:
    :cvar KWU:
    :cvar KWV:
    :cvar KWW:
    :cvar KWX:
    :cvar KWY:
    :cvar KWZ:
    :cvar KXA:
    :cvar KXB:
    :cvar KXC:
    :cvar KXD:
    :cvar KXF:
    :cvar KXH:
    :cvar KXI:
    :cvar KXJ:
    :cvar KXK:
    :cvar KXM:
    :cvar KXN:
    :cvar KXO:
    :cvar KXP:
    :cvar KXQ:
    :cvar KXR:
    :cvar KXS:
    :cvar KXT:
    :cvar KXV:
    :cvar KXW:
    :cvar KXX:
    :cvar KXY:
    :cvar KXZ:
    :cvar KYA:
    :cvar KYB:
    :cvar KYC:
    :cvar KYD:
    :cvar KYE:
    :cvar KYF:
    :cvar KYG:
    :cvar KYH:
    :cvar KYI:
    :cvar KYJ:
    :cvar KYK:
    :cvar KYL:
    :cvar KYM:
    :cvar KYN:
    :cvar KYO:
    :cvar KYP:
    :cvar KYQ:
    :cvar KYR:
    :cvar KYS:
    :cvar KYT:
    :cvar KYU:
    :cvar KYV:
    :cvar KYW:
    :cvar KYX:
    :cvar KYY:
    :cvar KYZ:
    :cvar KZA:
    :cvar KZB:
    :cvar KZC:
    :cvar KZD:
    :cvar KZE:
    :cvar KZF:
    :cvar KZG:
    :cvar KZI:
    :cvar KZK:
    :cvar KZL:
    :cvar KZM:
    :cvar KZN:
    :cvar KZO:
    :cvar KZP:
    :cvar KZQ:
    :cvar KZR:
    :cvar KZS:
    :cvar KZU:
    :cvar KZV:
    :cvar KZW:
    :cvar KZX:
    :cvar KZY:
    :cvar KZZ:
    :cvar LAA:
    :cvar LAC:
    :cvar LAD:
    :cvar LAE:
    :cvar LAF:
    :cvar LAG:
    :cvar LAI:
    :cvar LAJ:
    :cvar LAL:
    :cvar LAM:
    :cvar LAN:
    :cvar LAO:
    :cvar LAP:
    :cvar LAQ:
    :cvar LAR:
    :cvar LAS:
    :cvar LAT:
    :cvar LAU:
    :cvar LAW:
    :cvar LAX:
    :cvar LAY:
    :cvar LAZ:
    :cvar LBB:
    :cvar LBC:
    :cvar LBE:
    :cvar LBF:
    :cvar LBG:
    :cvar LBI:
    :cvar LBJ:
    :cvar LBK:
    :cvar LBL:
    :cvar LBM:
    :cvar LBN:
    :cvar LBO:
    :cvar LBQ:
    :cvar LBR:
    :cvar LBS:
    :cvar LBT:
    :cvar LBU:
    :cvar LBV:
    :cvar LBW:
    :cvar LBX:
    :cvar LBY:
    :cvar LBZ:
    :cvar LCC:
    :cvar LCD:
    :cvar LCE:
    :cvar LCF:
    :cvar LCH:
    :cvar LCL:
    :cvar LCM:
    :cvar LCP:
    :cvar LCQ:
    :cvar LCS:
    :cvar LDA:
    :cvar LDB:
    :cvar LDD:
    :cvar LDG:
    :cvar LDH:
    :cvar LDI:
    :cvar LDJ:
    :cvar LDK:
    :cvar LDL:
    :cvar LDM:
    :cvar LDO:
    :cvar LDP:
    :cvar LDQ:
    :cvar LEA:
    :cvar LEB:
    :cvar LEC:
    :cvar LED:
    :cvar LEE:
    :cvar LEF:
    :cvar LEH:
    :cvar LEI:
    :cvar LEJ:
    :cvar LEK:
    :cvar LEL:
    :cvar LEM:
    :cvar LEN:
    :cvar LEO:
    :cvar LEP:
    :cvar LEQ:
    :cvar LER:
    :cvar LES:
    :cvar LET:
    :cvar LEU:
    :cvar LEV:
    :cvar LEW:
    :cvar LEX:
    :cvar LEY:
    :cvar LEZ:
    :cvar LFA:
    :cvar LGA:
    :cvar LGB:
    :cvar LGG:
    :cvar LGH:
    :cvar LGI:
    :cvar LGK:
    :cvar LGL:
    :cvar LGM:
    :cvar LGN:
    :cvar LGO:
    :cvar LGQ:
    :cvar LGR:
    :cvar LGS:
    :cvar LGT:
    :cvar LGU:
    :cvar LGZ:
    :cvar LHA:
    :cvar LHH:
    :cvar LHI:
    :cvar LHL:
    :cvar LHM:
    :cvar LHN:
    :cvar LHP:
    :cvar LHS:
    :cvar LHT:
    :cvar LHU:
    :cvar LIA:
    :cvar LIB:
    :cvar LIC:
    :cvar LID:
    :cvar LIE:
    :cvar LIF:
    :cvar LIG:
    :cvar LIH:
    :cvar LIJ:
    :cvar LIK:
    :cvar LIL:
    :cvar LIM:
    :cvar LIN:
    :cvar LIO:
    :cvar LIP:
    :cvar LIQ:
    :cvar LIR:
    :cvar LIS:
    :cvar LIT:
    :cvar LIU:
    :cvar LIV:
    :cvar LIW:
    :cvar LIX:
    :cvar LIY:
    :cvar LIZ:
    :cvar LJA:
    :cvar LJE:
    :cvar LJI:
    :cvar LJL:
    :cvar LJP:
    :cvar LJW:
    :cvar LJX:
    :cvar LKA:
    :cvar LKB:
    :cvar LKC:
    :cvar LKD:
    :cvar LKE:
    :cvar LKH:
    :cvar LKI:
    :cvar LKJ:
    :cvar LKL:
    :cvar LKM:
    :cvar LKN:
    :cvar LKO:
    :cvar LKR:
    :cvar LKS:
    :cvar LKT:
    :cvar LKU:
    :cvar LKY:
    :cvar LLA:
    :cvar LLB:
    :cvar LLC:
    :cvar LLD:
    :cvar LLE:
    :cvar LLF:
    :cvar LLG:
    :cvar LLH:
    :cvar LLI:
    :cvar LLJ:
    :cvar LLK:
    :cvar LLL:
    :cvar LLM:
    :cvar LLN:
    :cvar LLP:
    :cvar LLQ:
    :cvar LLS:
    :cvar LLU:
    :cvar LLX:
    :cvar LMA:
    :cvar LMB:
    :cvar LMC:
    :cvar LMD:
    :cvar LME:
    :cvar LMF:
    :cvar LMG:
    :cvar LMH:
    :cvar LMI:
    :cvar LMJ:
    :cvar LMK:
    :cvar LML:
    :cvar LMN:
    :cvar LMO:
    :cvar LMP:
    :cvar LMQ:
    :cvar LMR:
    :cvar LMU:
    :cvar LMV:
    :cvar LMW:
    :cvar LMX:
    :cvar LMY:
    :cvar LNA:
    :cvar LNB:
    :cvar LND:
    :cvar LNH:
    :cvar LNI:
    :cvar LNJ:
    :cvar LNL:
    :cvar LNM:
    :cvar LNN:
    :cvar LNS:
    :cvar LNU:
    :cvar LNW:
    :cvar LNZ:
    :cvar LOA:
    :cvar LOB:
    :cvar LOC:
    :cvar LOE:
    :cvar LOF:
    :cvar LOG:
    :cvar LOH:
    :cvar LOI:
    :cvar LOJ:
    :cvar LOK:
    :cvar LOL:
    :cvar LOM:
    :cvar LON:
    :cvar LOO:
    :cvar LOP:
    :cvar LOQ:
    :cvar LOR:
    :cvar LOS:
    :cvar LOT:
    :cvar LOU:
    :cvar LOV:
    :cvar LOW:
    :cvar LOX:
    :cvar LOY:
    :cvar LOZ:
    :cvar LPA:
    :cvar LPE:
    :cvar LPN:
    :cvar LPO:
    :cvar LPX:
    :cvar LQR:
    :cvar LRA:
    :cvar LRC:
    :cvar LRE:
    :cvar LRG:
    :cvar LRI:
    :cvar LRK:
    :cvar LRL:
    :cvar LRM:
    :cvar LRN:
    :cvar LRO:
    :cvar LRR:
    :cvar LRT:
    :cvar LRV:
    :cvar LRZ:
    :cvar LSA:
    :cvar LSB:
    :cvar LSC:
    :cvar LSD:
    :cvar LSE:
    :cvar LSH:
    :cvar LSI:
    :cvar LSL:
    :cvar LSM:
    :cvar LSN:
    :cvar LSO:
    :cvar LSP:
    :cvar LSR:
    :cvar LSS:
    :cvar LST:
    :cvar LSV:
    :cvar LSW:
    :cvar LSY:
    :cvar LTG:
    :cvar LTH:
    :cvar LTI:
    :cvar LTN:
    :cvar LTO:
    :cvar LTS:
    :cvar LTU:
    :cvar LTZ:
    :cvar LUA:
    :cvar LUB:
    :cvar LUC:
    :cvar LUD:
    :cvar LUE:
    :cvar LUF:
    :cvar LUG:
    :cvar LUH:
    :cvar LUI:
    :cvar LUJ:
    :cvar LUK:
    :cvar LUL:
    :cvar LUM:
    :cvar LUN:
    :cvar LUO:
    :cvar LUP:
    :cvar LUQ:
    :cvar LUR:
    :cvar LUS:
    :cvar LUT:
    :cvar LUU:
    :cvar LUV:
    :cvar LUW:
    :cvar LUZ:
    :cvar LVA:
    :cvar LVI:
    :cvar LVK:
    :cvar LVL:
    :cvar LVS:
    :cvar LVU:
    :cvar LWA:
    :cvar LWE:
    :cvar LWG:
    :cvar LWH:
    :cvar LWL:
    :cvar LWM:
    :cvar LWO:
    :cvar LWS:
    :cvar LWT:
    :cvar LWU:
    :cvar LWW:
    :cvar LXM:
    :cvar LYA:
    :cvar LYG:
    :cvar LYN:
    :cvar LZH:
    :cvar LZL:
    :cvar LZN:
    :cvar LZZ:
    :cvar MAA:
    :cvar MAB:
    :cvar MAD:
    :cvar MAE:
    :cvar MAF:
    :cvar MAG:
    :cvar MAH:
    :cvar MAI:
    :cvar MAJ:
    :cvar MAK:
    :cvar MAL:
    :cvar MAM:
    :cvar MAQ:
    :cvar MAR:
    :cvar MAS:
    :cvar MAT:
    :cvar MAU:
    :cvar MAV:
    :cvar MAW:
    :cvar MAX:
    :cvar MAZ:
    :cvar MBA:
    :cvar MBB:
    :cvar MBC:
    :cvar MBD:
    :cvar MBE:
    :cvar MBF:
    :cvar MBH:
    :cvar MBI:
    :cvar MBJ:
    :cvar MBK:
    :cvar MBL:
    :cvar MBM:
    :cvar MBN:
    :cvar MBO:
    :cvar MBP:
    :cvar MBQ:
    :cvar MBR:
    :cvar MBS:
    :cvar MBT:
    :cvar MBU:
    :cvar MBV:
    :cvar MBW:
    :cvar MBX:
    :cvar MBY:
    :cvar MBZ:
    :cvar MCA:
    :cvar MCB:
    :cvar MCC:
    :cvar MCD:
    :cvar MCE:
    :cvar MCF:
    :cvar MCG:
    :cvar MCH:
    :cvar MCI:
    :cvar MCJ:
    :cvar MCK:
    :cvar MCL:
    :cvar MCM:
    :cvar MCN:
    :cvar MCO:
    :cvar MCP:
    :cvar MCQ:
    :cvar MCR:
    :cvar MCS:
    :cvar MCT:
    :cvar MCU:
    :cvar MCV:
    :cvar MCW:
    :cvar MCX:
    :cvar MCY:
    :cvar MCZ:
    :cvar MDA:
    :cvar MDB:
    :cvar MDC:
    :cvar MDD:
    :cvar MDE:
    :cvar MDF:
    :cvar MDG:
    :cvar MDH:
    :cvar MDI:
    :cvar MDJ:
    :cvar MDK:
    :cvar MDL:
    :cvar MDM:
    :cvar MDN:
    :cvar MDP:
    :cvar MDQ:
    :cvar MDR:
    :cvar MDS:
    :cvar MDT:
    :cvar MDU:
    :cvar MDV:
    :cvar MDW:
    :cvar MDX:
    :cvar MDY:
    :cvar MDZ:
    :cvar MEA:
    :cvar MEB:
    :cvar MEC:
    :cvar MED:
    :cvar MEE:
    :cvar MEF:
    :cvar MEH:
    :cvar MEI:
    :cvar MEJ:
    :cvar MEK:
    :cvar MEL:
    :cvar MEM:
    :cvar MEN:
    :cvar MEO:
    :cvar MEP:
    :cvar MEQ:
    :cvar MER:
    :cvar MES:
    :cvar MET:
    :cvar MEU:
    :cvar MEV:
    :cvar MEW:
    :cvar MEY:
    :cvar MEZ:
    :cvar MFA:
    :cvar MFB:
    :cvar MFC:
    :cvar MFD:
    :cvar MFE:
    :cvar MFF:
    :cvar MFG:
    :cvar MFH:
    :cvar MFI:
    :cvar MFJ:
    :cvar MFK:
    :cvar MFL:
    :cvar MFM:
    :cvar MFN:
    :cvar MFO:
    :cvar MFP:
    :cvar MFQ:
    :cvar MFR:
    :cvar MFS:
    :cvar MFT:
    :cvar MFU:
    :cvar MFV:
    :cvar MFW:
    :cvar MFX:
    :cvar MFY:
    :cvar MFZ:
    :cvar MGB:
    :cvar MGC:
    :cvar MGD:
    :cvar MGE:
    :cvar MGF:
    :cvar MGG:
    :cvar MGH:
    :cvar MGI:
    :cvar MGJ:
    :cvar MGK:
    :cvar MGL:
    :cvar MGM:
    :cvar MGN:
    :cvar MGO:
    :cvar MGP:
    :cvar MGQ:
    :cvar MGR:
    :cvar MGS:
    :cvar MGT:
    :cvar MGU:
    :cvar MGV:
    :cvar MGW:
    :cvar MGY:
    :cvar MGZ:
    :cvar MHA:
    :cvar MHB:
    :cvar MHC:
    :cvar MHD:
    :cvar MHE:
    :cvar MHF:
    :cvar MHG:
    :cvar MHI:
    :cvar MHJ:
    :cvar MHK:
    :cvar MHL:
    :cvar MHM:
    :cvar MHN:
    :cvar MHO:
    :cvar MHP:
    :cvar MHQ:
    :cvar MHR:
    :cvar MHS:
    :cvar MHT:
    :cvar MHU:
    :cvar MHW:
    :cvar MHX:
    :cvar MHY:
    :cvar MHZ:
    :cvar MIA:
    :cvar MIB:
    :cvar MIC:
    :cvar MID:
    :cvar MIE:
    :cvar MIF:
    :cvar MIG:
    :cvar MIH:
    :cvar MII:
    :cvar MIJ:
    :cvar MIK:
    :cvar MIL:
    :cvar MIM:
    :cvar MIN:
    :cvar MIO:
    :cvar MIP:
    :cvar MIQ:
    :cvar MIR:
    :cvar MIT:
    :cvar MIU:
    :cvar MIW:
    :cvar MIX:
    :cvar MIY:
    :cvar MIZ:
    :cvar MJB:
    :cvar MJC:
    :cvar MJD:
    :cvar MJE:
    :cvar MJG:
    :cvar MJH:
    :cvar MJI:
    :cvar MJJ:
    :cvar MJK:
    :cvar MJL:
    :cvar MJM:
    :cvar MJN:
    :cvar MJO:
    :cvar MJP:
    :cvar MJQ:
    :cvar MJR:
    :cvar MJS:
    :cvar MJT:
    :cvar MJU:
    :cvar MJV:
    :cvar MJW:
    :cvar MJX:
    :cvar MJY:
    :cvar MJZ:
    :cvar MKA:
    :cvar MKB:
    :cvar MKC:
    :cvar MKD:
    :cvar MKE:
    :cvar MKF:
    :cvar MKG:
    :cvar MKI:
    :cvar MKJ:
    :cvar MKK:
    :cvar MKL:
    :cvar MKM:
    :cvar MKN:
    :cvar MKO:
    :cvar MKP:
    :cvar MKQ:
    :cvar MKR:
    :cvar MKS:
    :cvar MKT:
    :cvar MKU:
    :cvar MKV:
    :cvar MKW:
    :cvar MKX:
    :cvar MKY:
    :cvar MKZ:
    :cvar MLA:
    :cvar MLB:
    :cvar MLC:
    :cvar MLE:
    :cvar MLF:
    :cvar MLH:
    :cvar MLI:
    :cvar MLJ:
    :cvar MLK:
    :cvar MLL:
    :cvar MLM:
    :cvar MLN:
    :cvar MLO:
    :cvar MLP:
    :cvar MLQ:
    :cvar MLR:
    :cvar MLS:
    :cvar MLT:
    :cvar MLU:
    :cvar MLV:
    :cvar MLW:
    :cvar MLX:
    :cvar MLZ:
    :cvar MMA:
    :cvar MMB:
    :cvar MMC:
    :cvar MMD:
    :cvar MME:
    :cvar MMF:
    :cvar MMG:
    :cvar MMH:
    :cvar MMI:
    :cvar MMJ:
    :cvar MMK:
    :cvar MML:
    :cvar MMM:
    :cvar MMN:
    :cvar MMO:
    :cvar MMP:
    :cvar MMQ:
    :cvar MMR:
    :cvar MMT:
    :cvar MMU:
    :cvar MMV:
    :cvar MMW:
    :cvar MMX:
    :cvar MMY:
    :cvar MMZ:
    :cvar MNA:
    :cvar MNB:
    :cvar MNC:
    :cvar MND:
    :cvar MNE:
    :cvar MNF:
    :cvar MNG:
    :cvar MNH:
    :cvar MNI:
    :cvar MNJ:
    :cvar MNK:
    :cvar MNL:
    :cvar MNM:
    :cvar MNN:
    :cvar MNP:
    :cvar MNQ:
    :cvar MNR:
    :cvar MNS:
    :cvar MNU:
    :cvar MNV:
    :cvar MNW:
    :cvar MNX:
    :cvar MNY:
    :cvar MNZ:
    :cvar MOA:
    :cvar MOC:
    :cvar MOD:
    :cvar MOE:
    :cvar MOG:
    :cvar MOH:
    :cvar MOI:
    :cvar MOJ:
    :cvar MOK:
    :cvar MOM:
    :cvar MOO:
    :cvar MOP:
    :cvar MOQ:
    :cvar MOR:
    :cvar MOS:
    :cvar MOT:
    :cvar MOU:
    :cvar MOV:
    :cvar MOW:
    :cvar MOX:
    :cvar MOY:
    :cvar MOZ:
    :cvar MPA:
    :cvar MPB:
    :cvar MPC:
    :cvar MPD:
    :cvar MPE:
    :cvar MPG:
    :cvar MPH:
    :cvar MPI:
    :cvar MPJ:
    :cvar MPK:
    :cvar MPL:
    :cvar MPM:
    :cvar MPN:
    :cvar MPO:
    :cvar MPP:
    :cvar MPQ:
    :cvar MPR:
    :cvar MPS:
    :cvar MPT:
    :cvar MPU:
    :cvar MPV:
    :cvar MPW:
    :cvar MPX:
    :cvar MPY:
    :cvar MPZ:
    :cvar MQA:
    :cvar MQB:
    :cvar MQC:
    :cvar MQE:
    :cvar MQF:
    :cvar MQG:
    :cvar MQH:
    :cvar MQI:
    :cvar MQJ:
    :cvar MQK:
    :cvar MQL:
    :cvar MQM:
    :cvar MQN:
    :cvar MQO:
    :cvar MQP:
    :cvar MQQ:
    :cvar MQR:
    :cvar MQS:
    :cvar MQT:
    :cvar MQU:
    :cvar MQV:
    :cvar MQW:
    :cvar MQX:
    :cvar MQY:
    :cvar MQZ:
    :cvar MRA:
    :cvar MRB:
    :cvar MRC:
    :cvar MRD:
    :cvar MRE:
    :cvar MRF:
    :cvar MRG:
    :cvar MRH:
    :cvar MRI:
    :cvar MRJ:
    :cvar MRK:
    :cvar MRL:
    :cvar MRM:
    :cvar MRN:
    :cvar MRO:
    :cvar MRQ:
    :cvar MRR:
    :cvar MRS:
    :cvar MRT:
    :cvar MRU:
    :cvar MRV:
    :cvar MRW:
    :cvar MRX:
    :cvar MRY:
    :cvar MRZ:
    :cvar MSB:
    :cvar MSC:
    :cvar MSD:
    :cvar MSE:
    :cvar MSF:
    :cvar MSG:
    :cvar MSH:
    :cvar MSI:
    :cvar MSJ:
    :cvar MSK:
    :cvar MSL:
    :cvar MSM:
    :cvar MSN:
    :cvar MSO:
    :cvar MSP:
    :cvar MSQ:
    :cvar MSR:
    :cvar MSS:
    :cvar MSU:
    :cvar MSV:
    :cvar MSW:
    :cvar MSX:
    :cvar MSY:
    :cvar MSZ:
    :cvar MTA:
    :cvar MTB:
    :cvar MTC:
    :cvar MTD:
    :cvar MTE:
    :cvar MTF:
    :cvar MTG:
    :cvar MTH:
    :cvar MTI:
    :cvar MTJ:
    :cvar MTK:
    :cvar MTL:
    :cvar MTM:
    :cvar MTN:
    :cvar MTO:
    :cvar MTP:
    :cvar MTQ:
    :cvar MTR:
    :cvar MTS:
    :cvar MTT:
    :cvar MTU:
    :cvar MTV:
    :cvar MTW:
    :cvar MTX:
    :cvar MTY:
    :cvar MUA:
    :cvar MUB:
    :cvar MUC:
    :cvar MUD:
    :cvar MUE:
    :cvar MUG:
    :cvar MUH:
    :cvar MUI:
    :cvar MUJ:
    :cvar MUK:
    :cvar MUM:
    :cvar MUO:
    :cvar MUP:
    :cvar MUQ:
    :cvar MUR:
    :cvar MUS:
    :cvar MUT:
    :cvar MUU:
    :cvar MUV:
    :cvar MUX:
    :cvar MUY:
    :cvar MUZ:
    :cvar MVA:
    :cvar MVB:
    :cvar MVD:
    :cvar MVE:
    :cvar MVF:
    :cvar MVG:
    :cvar MVH:
    :cvar MVI:
    :cvar MVK:
    :cvar MVL:
    :cvar MVN:
    :cvar MVO:
    :cvar MVP:
    :cvar MVQ:
    :cvar MVR:
    :cvar MVS:
    :cvar MVT:
    :cvar MVU:
    :cvar MVV:
    :cvar MVW:
    :cvar MVX:
    :cvar MVY:
    :cvar MVZ:
    :cvar MWA:
    :cvar MWB:
    :cvar MWC:
    :cvar MWE:
    :cvar MWF:
    :cvar MWG:
    :cvar MWH:
    :cvar MWI:
    :cvar MWK:
    :cvar MWL:
    :cvar MWM:
    :cvar MWN:
    :cvar MWO:
    :cvar MWP:
    :cvar MWQ:
    :cvar MWS:
    :cvar MWT:
    :cvar MWU:
    :cvar MWV:
    :cvar MWW:
    :cvar MWZ:
    :cvar MXA:
    :cvar MXB:
    :cvar MXC:
    :cvar MXD:
    :cvar MXE:
    :cvar MXF:
    :cvar MXG:
    :cvar MXH:
    :cvar MXJ:
    :cvar MXK:
    :cvar MXL:
    :cvar MXM:
    :cvar MXN:
    :cvar MXO:
    :cvar MXP:
    :cvar MXQ:
    :cvar MXR:
    :cvar MXS:
    :cvar MXT:
    :cvar MXU:
    :cvar MXV:
    :cvar MXW:
    :cvar MXX:
    :cvar MXY:
    :cvar MXZ:
    :cvar MYA:
    :cvar MYB:
    :cvar MYC:
    :cvar MYE:
    :cvar MYF:
    :cvar MYG:
    :cvar MYH:
    :cvar MYJ:
    :cvar MYK:
    :cvar MYL:
    :cvar MYM:
    :cvar MYO:
    :cvar MYP:
    :cvar MYR:
    :cvar MYS:
    :cvar MYU:
    :cvar MYV:
    :cvar MYW:
    :cvar MYX:
    :cvar MYY:
    :cvar MYZ:
    :cvar MZA:
    :cvar MZB:
    :cvar MZC:
    :cvar MZD:
    :cvar MZE:
    :cvar MZH:
    :cvar MZI:
    :cvar MZJ:
    :cvar MZK:
    :cvar MZL:
    :cvar MZM:
    :cvar MZN:
    :cvar MZO:
    :cvar MZP:
    :cvar MZQ:
    :cvar MZR:
    :cvar MZS:
    :cvar MZT:
    :cvar MZU:
    :cvar MZV:
    :cvar MZW:
    :cvar MZX:
    :cvar MZY:
    :cvar MZZ:
    :cvar NAA:
    :cvar NAB:
    :cvar NAC:
    :cvar NAE:
    :cvar NAF:
    :cvar NAG:
    :cvar NAJ:
    :cvar NAK:
    :cvar NAL:
    :cvar NAM:
    :cvar NAN:
    :cvar NAO:
    :cvar NAP:
    :cvar NAQ:
    :cvar NAR:
    :cvar NAS:
    :cvar NAT:
    :cvar NAU:
    :cvar NAV:
    :cvar NAW:
    :cvar NAX:
    :cvar NAY:
    :cvar NAZ:
    :cvar NBA:
    :cvar NBB:
    :cvar NBC:
    :cvar NBD:
    :cvar NBE:
    :cvar NBG:
    :cvar NBH:
    :cvar NBI:
    :cvar NBJ:
    :cvar NBK:
    :cvar NBL:
    :cvar NBM:
    :cvar NBN:
    :cvar NBO:
    :cvar NBP:
    :cvar NBQ:
    :cvar NBR:
    :cvar NBS:
    :cvar NBT:
    :cvar NBU:
    :cvar NBV:
    :cvar NBW:
    :cvar NBY:
    :cvar NCA:
    :cvar NCB:
    :cvar NCC:
    :cvar NCD:
    :cvar NCE:
    :cvar NCF:
    :cvar NCG:
    :cvar NCH:
    :cvar NCJ:
    :cvar NCK:
    :cvar NCL:
    :cvar NCM:
    :cvar NCN:
    :cvar NCO:
    :cvar NCQ:
    :cvar NCR:
    :cvar NCS:
    :cvar NCT:
    :cvar NCU:
    :cvar NCX:
    :cvar NCZ:
    :cvar NDA:
    :cvar NDB:
    :cvar NDC:
    :cvar NDD:
    :cvar NDE:
    :cvar NDG:
    :cvar NDH:
    :cvar NDI:
    :cvar NDJ:
    :cvar NDK:
    :cvar NDL:
    :cvar NDM:
    :cvar NDN:
    :cvar NDO:
    :cvar NDP:
    :cvar NDQ:
    :cvar NDR:
    :cvar NDS:
    :cvar NDT:
    :cvar NDU:
    :cvar NDV:
    :cvar NDW:
    :cvar NDX:
    :cvar NDY:
    :cvar NDZ:
    :cvar NEA:
    :cvar NEB:
    :cvar NEC:
    :cvar NED:
    :cvar NEE:
    :cvar NEF:
    :cvar NEG:
    :cvar NEH:
    :cvar NEJ:
    :cvar NEK:
    :cvar NEM:
    :cvar NEN:
    :cvar NEO:
    :cvar NEQ:
    :cvar NER:
    :cvar NES:
    :cvar NET:
    :cvar NEV:
    :cvar NEW:
    :cvar NEX:
    :cvar NEY:
    :cvar NEZ:
    :cvar NFA:
    :cvar NFD:
    :cvar NFL:
    :cvar NFR:
    :cvar NFU:
    :cvar NGA:
    :cvar NGB:
    :cvar NGC:
    :cvar NGD:
    :cvar NGE:
    :cvar NGG:
    :cvar NGH:
    :cvar NGI:
    :cvar NGJ:
    :cvar NGK:
    :cvar NGL:
    :cvar NGM:
    :cvar NGN:
    :cvar NGP:
    :cvar NGQ:
    :cvar NGR:
    :cvar NGS:
    :cvar NGT:
    :cvar NGU:
    :cvar NGV:
    :cvar NGW:
    :cvar NGX:
    :cvar NGY:
    :cvar NGZ:
    :cvar NHA:
    :cvar NHB:
    :cvar NHC:
    :cvar NHD:
    :cvar NHE:
    :cvar NHF:
    :cvar NHG:
    :cvar NHH:
    :cvar NHI:
    :cvar NHK:
    :cvar NHM:
    :cvar NHN:
    :cvar NHO:
    :cvar NHP:
    :cvar NHQ:
    :cvar NHR:
    :cvar NHT:
    :cvar NHU:
    :cvar NHV:
    :cvar NHW:
    :cvar NHX:
    :cvar NHY:
    :cvar NHZ:
    :cvar NIA:
    :cvar NIB:
    :cvar NID:
    :cvar NIE:
    :cvar NIF:
    :cvar NIG:
    :cvar NIH:
    :cvar NII:
    :cvar NIJ:
    :cvar NIK:
    :cvar NIL:
    :cvar NIM:
    :cvar NIN:
    :cvar NIO:
    :cvar NIQ:
    :cvar NIR:
    :cvar NIS:
    :cvar NIT:
    :cvar NIU:
    :cvar NIV:
    :cvar NIW:
    :cvar NIX:
    :cvar NIY:
    :cvar NIZ:
    :cvar NJA:
    :cvar NJB:
    :cvar NJD:
    :cvar NJH:
    :cvar NJI:
    :cvar NJJ:
    :cvar NJL:
    :cvar NJM:
    :cvar NJN:
    :cvar NJO:
    :cvar NJR:
    :cvar NJS:
    :cvar NJT:
    :cvar NJU:
    :cvar NJX:
    :cvar NJY:
    :cvar NJZ:
    :cvar NKA:
    :cvar NKB:
    :cvar NKC:
    :cvar NKD:
    :cvar NKE:
    :cvar NKF:
    :cvar NKG:
    :cvar NKH:
    :cvar NKI:
    :cvar NKJ:
    :cvar NKK:
    :cvar NKM:
    :cvar NKN:
    :cvar NKO:
    :cvar NKP:
    :cvar NKQ:
    :cvar NKR:
    :cvar NKS:
    :cvar NKT:
    :cvar NKU:
    :cvar NKV:
    :cvar NKW:
    :cvar NKX:
    :cvar NKZ:
    :cvar NLA:
    :cvar NLC:
    :cvar NLD:
    :cvar NLE:
    :cvar NLG:
    :cvar NLI:
    :cvar NLJ:
    :cvar NLK:
    :cvar NLL:
    :cvar NLM:
    :cvar NLO:
    :cvar NLQ:
    :cvar NLU:
    :cvar NLV:
    :cvar NLW:
    :cvar NLX:
    :cvar NLY:
    :cvar NLZ:
    :cvar NMA:
    :cvar NMB:
    :cvar NMC:
    :cvar NMD:
    :cvar NME:
    :cvar NMF:
    :cvar NMG:
    :cvar NMH:
    :cvar NMI:
    :cvar NMJ:
    :cvar NMK:
    :cvar NML:
    :cvar NMM:
    :cvar NMN:
    :cvar NMO:
    :cvar NMP:
    :cvar NMQ:
    :cvar NMR:
    :cvar NMS:
    :cvar NMT:
    :cvar NMU:
    :cvar NMV:
    :cvar NMW:
    :cvar NMX:
    :cvar NMY:
    :cvar NMZ:
    :cvar NNA:
    :cvar NNB:
    :cvar NNC:
    :cvar NND:
    :cvar NNE:
    :cvar NNF:
    :cvar NNG:
    :cvar NNH:
    :cvar NNI:
    :cvar NNJ:
    :cvar NNK:
    :cvar NNL:
    :cvar NNM:
    :cvar NNN:
    :cvar NNP:
    :cvar NNQ:
    :cvar NNR:
    :cvar NNT:
    :cvar NNU:
    :cvar NNV:
    :cvar NNW:
    :cvar NNY:
    :cvar NNZ:
    :cvar NOA:
    :cvar NOC:
    :cvar NOD:
    :cvar NOE:
    :cvar NOF:
    :cvar NOG:
    :cvar NOH:
    :cvar NOI:
    :cvar NOJ:
    :cvar NOK:
    :cvar NOL:
    :cvar NOP:
    :cvar NOQ:
    :cvar NOR:
    :cvar NOS:
    :cvar NOT:
    :cvar NOU:
    :cvar NOW:
    :cvar NOY:
    :cvar NOZ:
    :cvar NPA:
    :cvar NPB:
    :cvar NPG:
    :cvar NPH:
    :cvar NPI:
    :cvar NPL:
    :cvar NPN:
    :cvar NPO:
    :cvar NPS:
    :cvar NPU:
    :cvar NPX:
    :cvar NPY:
    :cvar NQG:
    :cvar NQK:
    :cvar NQL:
    :cvar NQM:
    :cvar NQN:
    :cvar NQO:
    :cvar NQQ:
    :cvar NQT:
    :cvar NQY:
    :cvar NRA:
    :cvar NRB:
    :cvar NRE:
    :cvar NRF:
    :cvar NRG:
    :cvar NRI:
    :cvar NRK:
    :cvar NRL:
    :cvar NRM:
    :cvar NRN:
    :cvar NRR:
    :cvar NRT:
    :cvar NRU:
    :cvar NRX:
    :cvar NRZ:
    :cvar NSA:
    :cvar NSB:
    :cvar NSD:
    :cvar NSE:
    :cvar NSF:
    :cvar NSG:
    :cvar NSH:
    :cvar NSI:
    :cvar NSK:
    :cvar NSL:
    :cvar NSM:
    :cvar NSN:
    :cvar NSO:
    :cvar NSP:
    :cvar NSQ:
    :cvar NSR:
    :cvar NSS:
    :cvar NST:
    :cvar NSU:
    :cvar NSV:
    :cvar NSW:
    :cvar NSX:
    :cvar NSY:
    :cvar NSZ:
    :cvar NTD:
    :cvar NTG:
    :cvar NTI:
    :cvar NTJ:
    :cvar NTK:
    :cvar NTM:
    :cvar NTO:
    :cvar NTP:
    :cvar NTR:
    :cvar NTU:
    :cvar NTW:
    :cvar NTX:
    :cvar NTY:
    :cvar NTZ:
    :cvar NUA:
    :cvar NUC:
    :cvar NUD:
    :cvar NUE:
    :cvar NUF:
    :cvar NUG:
    :cvar NUH:
    :cvar NUI:
    :cvar NUJ:
    :cvar NUK:
    :cvar NUL:
    :cvar NUM:
    :cvar NUN:
    :cvar NUO:
    :cvar NUP:
    :cvar NUQ:
    :cvar NUR:
    :cvar NUS:
    :cvar NUT:
    :cvar NUU:
    :cvar NUV:
    :cvar NUW:
    :cvar NUX:
    :cvar NUY:
    :cvar NUZ:
    :cvar NVH:
    :cvar NVM:
    :cvar NVO:
    :cvar NWA:
    :cvar NWB:
    :cvar NWE:
    :cvar NWG:
    :cvar NWI:
    :cvar NWM:
    :cvar NWO:
    :cvar NWR:
    :cvar NWW:
    :cvar NWY:
    :cvar NXA:
    :cvar NXD:
    :cvar NXE:
    :cvar NXG:
    :cvar NXI:
    :cvar NXK:
    :cvar NXL:
    :cvar NXN:
    :cvar NXO:
    :cvar NXQ:
    :cvar NXR:
    :cvar NXX:
    :cvar NYA:
    :cvar NYB:
    :cvar NYC:
    :cvar NYD:
    :cvar NYE:
    :cvar NYF:
    :cvar NYG:
    :cvar NYH:
    :cvar NYI:
    :cvar NYJ:
    :cvar NYK:
    :cvar NYL:
    :cvar NYM:
    :cvar NYN:
    :cvar NYO:
    :cvar NYP:
    :cvar NYQ:
    :cvar NYR:
    :cvar NYS:
    :cvar NYT:
    :cvar NYU:
    :cvar NYV:
    :cvar NYW:
    :cvar NYX:
    :cvar NYY:
    :cvar NZA:
    :cvar NZB:
    :cvar NZD:
    :cvar NZI:
    :cvar NZK:
    :cvar NZM:
    :cvar NZR:
    :cvar NZS:
    :cvar NZU:
    :cvar NZY:
    :cvar NZZ:
    :cvar OAA:
    :cvar OAC:
    :cvar OBI:
    :cvar OBK:
    :cvar OBL:
    :cvar OBO:
    :cvar OBU:
    :cvar OCA:
    :cvar OCI:
    :cvar OCU:
    :cvar ODA:
    :cvar ODK:
    :cvar ODU:
    :cvar OFO:
    :cvar OFU:
    :cvar OGB:
    :cvar OGC:
    :cvar OGG:
    :cvar OGO:
    :cvar OGU:
    :cvar OIA:
    :cvar OIE:
    :cvar OIN:
    :cvar OJB:
    :cvar OJC:
    :cvar OJG:
    :cvar OJS:
    :cvar OJV:
    :cvar OJW:
    :cvar OKA:
    :cvar OKB:
    :cvar OKC:
    :cvar OKD:
    :cvar OKE:
    :cvar OKG:
    :cvar OKH:
    :cvar OKI:
    :cvar OKJ:
    :cvar OKK:
    :cvar OKL:
    :cvar OKN:
    :cvar OKR:
    :cvar OKS:
    :cvar OKU:
    :cvar OKV:
    :cvar OKX:
    :cvar OLA:
    :cvar OLD:
    :cvar OLE:
    :cvar OLK:
    :cvar OLM:
    :cvar OLO:
    :cvar OLR:
    :cvar OLU:
    :cvar OMA:
    :cvar OMB:
    :cvar OMC:
    :cvar OMG:
    :cvar OMI:
    :cvar OMK:
    :cvar OML:
    :cvar OMO:
    :cvar OMT:
    :cvar OMU:
    :cvar OMW:
    :cvar ONA:
    :cvar ONB:
    :cvar ONE:
    :cvar ONG:
    :cvar ONI:
    :cvar ONJ:
    :cvar ONK:
    :cvar ONN:
    :cvar ONO:
    :cvar ONP:
    :cvar ONR:
    :cvar ONS:
    :cvar ONT:
    :cvar ONU:
    :cvar ONX:
    :cvar OOD:
    :cvar OOG:
    :cvar OON:
    :cvar OOR:
    :cvar OPA:
    :cvar OPK:
    :cvar OPM:
    :cvar OPO:
    :cvar OPT:
    :cvar OPY:
    :cvar ORA:
    :cvar ORC:
    :cvar ORE:
    :cvar ORG:
    :cvar ORH:
    :cvar ORN:
    :cvar ORO:
    :cvar ORR:
    :cvar ORS:
    :cvar ORT:
    :cvar ORU:
    :cvar ORW:
    :cvar ORX:
    :cvar ORY:
    :cvar ORZ:
    :cvar OSA:
    :cvar OSI:
    :cvar OSO:
    :cvar OSS:
    :cvar OST:
    :cvar OSU:
    :cvar OTD:
    :cvar OTE:
    :cvar OTI:
    :cvar OTL:
    :cvar OTM:
    :cvar OTN:
    :cvar OTQ:
    :cvar OTR:
    :cvar OTS:
    :cvar OTT:
    :cvar OTU:
    :cvar OTW:
    :cvar OTX:
    :cvar OTZ:
    :cvar OUA:
    :cvar OUB:
    :cvar OUE:
    :cvar OUM:
    :cvar OVD:
    :cvar OWI:
    :cvar OYB:
    :cvar OYD:
    :cvar OYM:
    :cvar OYY:
    :cvar OZM:
    :cvar PAB:
    :cvar PAC:
    :cvar PAD:
    :cvar PAE:
    :cvar PAF:
    :cvar PAG:
    :cvar PAH:
    :cvar PAI:
    :cvar PAK:
    :cvar PAM:
    :cvar PAN:
    :cvar PAO:
    :cvar PAP:
    :cvar PAQ:
    :cvar PAR:
    :cvar PAS:
    :cvar PAU:
    :cvar PAV:
    :cvar PAW:
    :cvar PAX:
    :cvar PAY:
    :cvar PAZ:
    :cvar PBB:
    :cvar PBC:
    :cvar PBE:
    :cvar PBF:
    :cvar PBG:
    :cvar PBH:
    :cvar PBI:
    :cvar PBL:
    :cvar PBM:
    :cvar PBN:
    :cvar PBO:
    :cvar PBP:
    :cvar PBR:
    :cvar PBS:
    :cvar PBT:
    :cvar PBU:
    :cvar PBV:
    :cvar PBY:
    :cvar PCA:
    :cvar PCB:
    :cvar PCC:
    :cvar PCD:
    :cvar PCE:
    :cvar PCF:
    :cvar PCG:
    :cvar PCH:
    :cvar PCI:
    :cvar PCJ:
    :cvar PCK:
    :cvar PCL:
    :cvar PCM:
    :cvar PCN:
    :cvar PCP:
    :cvar PCW:
    :cvar PDA:
    :cvar PDC:
    :cvar PDI:
    :cvar PDN:
    :cvar PDO:
    :cvar PDT:
    :cvar PDU:
    :cvar PEA:
    :cvar PEB:
    :cvar PED:
    :cvar PEE:
    :cvar PEF:
    :cvar PEG:
    :cvar PEH:
    :cvar PEI:
    :cvar PEJ:
    :cvar PEK:
    :cvar PEL:
    :cvar PEM:
    :cvar PEP:
    :cvar PEQ:
    :cvar PES:
    :cvar PEV:
    :cvar PEX:
    :cvar PEY:
    :cvar PEZ:
    :cvar PFA:
    :cvar PFE:
    :cvar PFL:
    :cvar PGA:
    :cvar PGG:
    :cvar PGI:
    :cvar PGK:
    :cvar PGS:
    :cvar PGU:
    :cvar PGZ:
    :cvar PHA:
    :cvar PHD:
    :cvar PHG:
    :cvar PHH:
    :cvar PHJ:
    :cvar PHK:
    :cvar PHL:
    :cvar PHM:
    :cvar PHO:
    :cvar PHQ:
    :cvar PHR:
    :cvar PHT:
    :cvar PHU:
    :cvar PHV:
    :cvar PHW:
    :cvar PIA:
    :cvar PIB:
    :cvar PIC:
    :cvar PID:
    :cvar PIE:
    :cvar PIF:
    :cvar PIG:
    :cvar PIH:
    :cvar PIJ:
    :cvar PIL:
    :cvar PIM:
    :cvar PIN:
    :cvar PIO:
    :cvar PIP:
    :cvar PIR:
    :cvar PIS:
    :cvar PIT:
    :cvar PIU:
    :cvar PIV:
    :cvar PIW:
    :cvar PIX:
    :cvar PIY:
    :cvar PIZ:
    :cvar PJT:
    :cvar PKB:
    :cvar PKG:
    :cvar PKH:
    :cvar PKN:
    :cvar PKO:
    :cvar PKP:
    :cvar PKR:
    :cvar PKS:
    :cvar PKT:
    :cvar PKU:
    :cvar PLA:
    :cvar PLB:
    :cvar PLC:
    :cvar PLD:
    :cvar PLE:
    :cvar PLG:
    :cvar PLH:
    :cvar PLI:
    :cvar PLK:
    :cvar PLL:
    :cvar PLN:
    :cvar PLO:
    :cvar PLR:
    :cvar PLS:
    :cvar PLT:
    :cvar PLU:
    :cvar PLV:
    :cvar PLW:
    :cvar PLY:
    :cvar PLZ:
    :cvar PMA:
    :cvar PMB:
    :cvar PMD:
    :cvar PME:
    :cvar PMF:
    :cvar PMI:
    :cvar PMJ:
    :cvar PML:
    :cvar PMM:
    :cvar PMN:
    :cvar PMO:
    :cvar PMQ:
    :cvar PMR:
    :cvar PMS:
    :cvar PMT:
    :cvar PMW:
    :cvar PMX:
    :cvar PMY:
    :cvar PMZ:
    :cvar PNA:
    :cvar PNB:
    :cvar PNC:
    :cvar PND:
    :cvar PNE:
    :cvar PNG:
    :cvar PNH:
    :cvar PNI:
    :cvar PNJ:
    :cvar PNK:
    :cvar PNL:
    :cvar PNM:
    :cvar PNN:
    :cvar PNO:
    :cvar PNP:
    :cvar PNQ:
    :cvar PNR:
    :cvar PNS:
    :cvar PNT:
    :cvar PNU:
    :cvar PNV:
    :cvar PNW:
    :cvar PNX:
    :cvar PNY:
    :cvar PNZ:
    :cvar POC:
    :cvar POE:
    :cvar POF:
    :cvar POG:
    :cvar POH:
    :cvar POI:
    :cvar POK:
    :cvar POL:
    :cvar POM:
    :cvar PON:
    :cvar POO:
    :cvar POP:
    :cvar POQ:
    :cvar POR:
    :cvar POS:
    :cvar POT:
    :cvar POV:
    :cvar POW:
    :cvar POX:
    :cvar POY:
    :cvar PPE:
    :cvar PPI:
    :cvar PPK:
    :cvar PPL:
    :cvar PPM:
    :cvar PPN:
    :cvar PPO:
    :cvar PPP:
    :cvar PPQ:
    :cvar PPS:
    :cvar PPT:
    :cvar PPU:
    :cvar PQA:
    :cvar PQM:
    :cvar PRC:
    :cvar PRD:
    :cvar PRE:
    :cvar PRF:
    :cvar PRG:
    :cvar PRH:
    :cvar PRI:
    :cvar PRK:
    :cvar PRL:
    :cvar PRM:
    :cvar PRN:
    :cvar PRQ:
    :cvar PRR:
    :cvar PRS:
    :cvar PRT:
    :cvar PRU:
    :cvar PRW:
    :cvar PRX:
    :cvar PRZ:
    :cvar PSA:
    :cvar PSC:
    :cvar PSD:
    :cvar PSE:
    :cvar PSG:
    :cvar PSH:
    :cvar PSI:
    :cvar PSL:
    :cvar PSM:
    :cvar PSN:
    :cvar PSO:
    :cvar PSP:
    :cvar PSQ:
    :cvar PSR:
    :cvar PSS:
    :cvar PST:
    :cvar PSW:
    :cvar PSY:
    :cvar PTA:
    :cvar PTH:
    :cvar PTI:
    :cvar PTN:
    :cvar PTO:
    :cvar PTP:
    :cvar PTQ:
    :cvar PTR:
    :cvar PTT:
    :cvar PTU:
    :cvar PTV:
    :cvar PTW:
    :cvar PTY:
    :cvar PUA:
    :cvar PUB:
    :cvar PUC:
    :cvar PUD:
    :cvar PUE:
    :cvar PUF:
    :cvar PUG:
    :cvar PUI:
    :cvar PUJ:
    :cvar PUM:
    :cvar PUO:
    :cvar PUP:
    :cvar PUQ:
    :cvar PUR:
    :cvar PUT:
    :cvar PUU:
    :cvar PUW:
    :cvar PUX:
    :cvar PUY:
    :cvar PWA:
    :cvar PWB:
    :cvar PWG:
    :cvar PWI:
    :cvar PWM:
    :cvar PWN:
    :cvar PWO:
    :cvar PWR:
    :cvar PWW:
    :cvar PXM:
    :cvar PYE:
    :cvar PYM:
    :cvar PYN:
    :cvar PYS:
    :cvar PYU:
    :cvar PYY:
    :cvar PZE:
    :cvar PZH:
    :cvar PZN:
    :cvar QUA:
    :cvar QUB:
    :cvar QUC:
    :cvar QUD:
    :cvar QUF:
    :cvar QUG:
    :cvar QUH:
    :cvar QUI:
    :cvar QUK:
    :cvar QUL:
    :cvar QUM:
    :cvar QUN:
    :cvar QUP:
    :cvar QUQ:
    :cvar QUR:
    :cvar QUS:
    :cvar QUV:
    :cvar QUW:
    :cvar QUX:
    :cvar QUY:
    :cvar QUZ:
    :cvar QVA:
    :cvar QVC:
    :cvar QVE:
    :cvar QVH:
    :cvar QVI:
    :cvar QVJ:
    :cvar QVL:
    :cvar QVM:
    :cvar QVN:
    :cvar QVO:
    :cvar QVP:
    :cvar QVS:
    :cvar QVW:
    :cvar QVY:
    :cvar QVZ:
    :cvar QWA:
    :cvar QWH:
    :cvar QWM:
    :cvar QWS:
    :cvar QWT:
    :cvar QXA:
    :cvar QXC:
    :cvar QXH:
    :cvar QXL:
    :cvar QXN:
    :cvar QXO:
    :cvar QXP:
    :cvar QXQ:
    :cvar QXR:
    :cvar QXS:
    :cvar QXT:
    :cvar QXU:
    :cvar QXW:
    :cvar QYP:
    :cvar RAA:
    :cvar RAB:
    :cvar RAC:
    :cvar RAD:
    :cvar RAF:
    :cvar RAG:
    :cvar RAH:
    :cvar RAI:
    :cvar RAK:
    :cvar RAL:
    :cvar RAM:
    :cvar RAN:
    :cvar RAO:
    :cvar RAP:
    :cvar RAQ:
    :cvar RAR:
    :cvar RAS:
    :cvar RAT:
    :cvar RAU:
    :cvar RAV:
    :cvar RAW:
    :cvar RAX:
    :cvar RAY:
    :cvar RAZ:
    :cvar RBB:
    :cvar RBK:
    :cvar RBL:
    :cvar RBP:
    :cvar RCF:
    :cvar RDB:
    :cvar REA:
    :cvar REB:
    :cvar REE:
    :cvar REG:
    :cvar REI:
    :cvar REJ:
    :cvar REL:
    :cvar REM:
    :cvar REN:
    :cvar RER:
    :cvar RES:
    :cvar RET:
    :cvar REY:
    :cvar RGA:
    :cvar RGE:
    :cvar RGK:
    :cvar RGN:
    :cvar RGR:
    :cvar RGS:
    :cvar RGU:
    :cvar RHG:
    :cvar RHP:
    :cvar RIA:
    :cvar RIB:
    :cvar RIF:
    :cvar RIL:
    :cvar RIM:
    :cvar RIN:
    :cvar RIR:
    :cvar RIT:
    :cvar RIU:
    :cvar RJG:
    :cvar RJI:
    :cvar RJS:
    :cvar RKA:
    :cvar RKB:
    :cvar RKH:
    :cvar RKI:
    :cvar RKM:
    :cvar RKT:
    :cvar RKW:
    :cvar RMA:
    :cvar RMB:
    :cvar RMC:
    :cvar RMD:
    :cvar RME:
    :cvar RMF:
    :cvar RMG:
    :cvar RMH:
    :cvar RMI:
    :cvar RMK:
    :cvar RML:
    :cvar RMM:
    :cvar RMN:
    :cvar RMO:
    :cvar RMP:
    :cvar RMQ:
    :cvar RMS:
    :cvar RMT:
    :cvar RMU:
    :cvar RMW:
    :cvar RMX:
    :cvar RMY:
    :cvar RMZ:
    :cvar RNB:
    :cvar RND:
    :cvar RNG:
    :cvar RNL:
    :cvar RNN:
    :cvar RNP:
    :cvar RNR:
    :cvar RNW:
    :cvar ROB:
    :cvar ROC:
    :cvar ROD:
    :cvar ROE:
    :cvar ROF:
    :cvar ROG:
    :cvar ROH:
    :cvar ROL:
    :cvar RON:
    :cvar ROO:
    :cvar ROP:
    :cvar ROR:
    :cvar ROU:
    :cvar ROW:
    :cvar RPN:
    :cvar RPT:
    :cvar RRI:
    :cvar RRM:
    :cvar RRO:
    :cvar RRT:
    :cvar RSB:
    :cvar RSK:
    :cvar RSL:
    :cvar RSM:
    :cvar RSN:
    :cvar RSW:
    :cvar RTC:
    :cvar RTH:
    :cvar RTM:
    :cvar RTS:
    :cvar RTW:
    :cvar RUB:
    :cvar RUC:
    :cvar RUE:
    :cvar RUF:
    :cvar RUG:
    :cvar RUH:
    :cvar RUK:
    :cvar RUN:
    :cvar RUO:
    :cvar RUP:
    :cvar RUQ:
    :cvar RUS:
    :cvar RUT:
    :cvar RUU:
    :cvar RUY:
    :cvar RUZ:
    :cvar RWA:
    :cvar RWK:
    :cvar RWL:
    :cvar RWM:
    :cvar RWO:
    :cvar RWR:
    :cvar RXD:
    :cvar RXW:
    :cvar RYN:
    :cvar RYS:
    :cvar RYU:
    :cvar RZH:
    :cvar SAA:
    :cvar SAB:
    :cvar SAC:
    :cvar SAD:
    :cvar SAE:
    :cvar SAF:
    :cvar SAG:
    :cvar SAH:
    :cvar SAJ:
    :cvar SAK:
    :cvar SAM:
    :cvar SAN:
    :cvar SAO:
    :cvar SAQ:
    :cvar SAR:
    :cvar SAS:
    :cvar SAT:
    :cvar SAU:
    :cvar SAV:
    :cvar SAW:
    :cvar SAX:
    :cvar SAY:
    :cvar SAZ:
    :cvar SBA:
    :cvar SBB:
    :cvar SBC:
    :cvar SBD:
    :cvar SBE:
    :cvar SBF:
    :cvar SBG:
    :cvar SBH:
    :cvar SBI:
    :cvar SBJ:
    :cvar SBK:
    :cvar SBL:
    :cvar SBM:
    :cvar SBN:
    :cvar SBO:
    :cvar SBP:
    :cvar SBQ:
    :cvar SBR:
    :cvar SBS:
    :cvar SBT:
    :cvar SBU:
    :cvar SBW:
    :cvar SBX:
    :cvar SBY:
    :cvar SBZ:
    :cvar SCB:
    :cvar SCE:
    :cvar SCF:
    :cvar SCG:
    :cvar SCH:
    :cvar SCI:
    :cvar SCK:
    :cvar SCL:
    :cvar SCN:
    :cvar SCO:
    :cvar SCP:
    :cvar SCQ:
    :cvar SCS:
    :cvar SCT:
    :cvar SCU:
    :cvar SCV:
    :cvar SCW:
    :cvar SDA:
    :cvar SDB:
    :cvar SDC:
    :cvar SDE:
    :cvar SDF:
    :cvar SDG:
    :cvar SDH:
    :cvar SDJ:
    :cvar SDK:
    :cvar SDL:
    :cvar SDN:
    :cvar SDO:
    :cvar SDP:
    :cvar SDQ:
    :cvar SDR:
    :cvar SDS:
    :cvar SDT:
    :cvar SDU:
    :cvar SDX:
    :cvar SDZ:
    :cvar SEA:
    :cvar SEB:
    :cvar SEC:
    :cvar SED:
    :cvar SEE:
    :cvar SEF:
    :cvar SEG:
    :cvar SEH:
    :cvar SEI:
    :cvar SEJ:
    :cvar SEK:
    :cvar SEL:
    :cvar SEN:
    :cvar SEO:
    :cvar SEP:
    :cvar SEQ:
    :cvar SER:
    :cvar SES:
    :cvar SET:
    :cvar SEU:
    :cvar SEV:
    :cvar SEW:
    :cvar SEY:
    :cvar SEZ:
    :cvar SFB:
    :cvar SFE:
    :cvar SFM:
    :cvar SFS:
    :cvar SFW:
    :cvar SGB:
    :cvar SGC:
    :cvar SGD:
    :cvar SGE:
    :cvar SGG:
    :cvar SGH:
    :cvar SGI:
    :cvar SGJ:
    :cvar SGK:
    :cvar SGM:
    :cvar SGP:
    :cvar SGR:
    :cvar SGS:
    :cvar SGT:
    :cvar SGU:
    :cvar SGW:
    :cvar SGX:
    :cvar SGY:
    :cvar SGZ:
    :cvar SHA:
    :cvar SHB:
    :cvar SHC:
    :cvar SHD:
    :cvar SHE:
    :cvar SHG:
    :cvar SHH:
    :cvar SHI:
    :cvar SHJ:
    :cvar SHK:
    :cvar SHL:
    :cvar SHM:
    :cvar SHN:
    :cvar SHO:
    :cvar SHP:
    :cvar SHQ:
    :cvar SHR:
    :cvar SHS:
    :cvar SHT:
    :cvar SHU:
    :cvar SHV:
    :cvar SHW:
    :cvar SHX:
    :cvar SHY:
    :cvar SHZ:
    :cvar SIA:
    :cvar SIB:
    :cvar SID:
    :cvar SIE:
    :cvar SIF:
    :cvar SIG:
    :cvar SIH:
    :cvar SII:
    :cvar SIJ:
    :cvar SIK:
    :cvar SIL:
    :cvar SIM:
    :cvar SIN:
    :cvar SIP:
    :cvar SIQ:
    :cvar SIR:
    :cvar SIS:
    :cvar SIU:
    :cvar SIV:
    :cvar SIW:
    :cvar SIX:
    :cvar SIY:
    :cvar SIZ:
    :cvar SJA:
    :cvar SJB:
    :cvar SJC:
    :cvar SJD:
    :cvar SJE:
    :cvar SJG:
    :cvar SJK:
    :cvar SJL:
    :cvar SJM:
    :cvar SJO:
    :cvar SJP:
    :cvar SJR:
    :cvar SJS:
    :cvar SJT:
    :cvar SJU:
    :cvar SJW:
    :cvar SKA:
    :cvar SKB:
    :cvar SKC:
    :cvar SKD:
    :cvar SKE:
    :cvar SKF:
    :cvar SKG:
    :cvar SKH:
    :cvar SKI:
    :cvar SKJ:
    :cvar SKM:
    :cvar SKN:
    :cvar SKO:
    :cvar SKP:
    :cvar SKQ:
    :cvar SKR:
    :cvar SKS:
    :cvar SKT:
    :cvar SKU:
    :cvar SKV:
    :cvar SKW:
    :cvar SKX:
    :cvar SKY:
    :cvar SKZ:
    :cvar SLC:
    :cvar SLD:
    :cvar SLE:
    :cvar SLF:
    :cvar SLG:
    :cvar SLH:
    :cvar SLI:
    :cvar SLJ:
    :cvar SLK:
    :cvar SLL:
    :cvar SLM:
    :cvar SLN:
    :cvar SLP:
    :cvar SLR:
    :cvar SLS:
    :cvar SLT:
    :cvar SLU:
    :cvar SLV:
    :cvar SLW:
    :cvar SLX:
    :cvar SLY:
    :cvar SLZ:
    :cvar SMA:
    :cvar SMB:
    :cvar SMC:
    :cvar SME:
    :cvar SMF:
    :cvar SMG:
    :cvar SMH:
    :cvar SMJ:
    :cvar SMK:
    :cvar SML:
    :cvar SMM:
    :cvar SMN:
    :cvar SMO:
    :cvar SMP:
    :cvar SMQ:
    :cvar SMR:
    :cvar SMS:
    :cvar SMT:
    :cvar SMU:
    :cvar SMV:
    :cvar SMW:
    :cvar SMX:
    :cvar SMY:
    :cvar SMZ:
    :cvar SNA:
    :cvar SNC:
    :cvar SND:
    :cvar SNE:
    :cvar SNF:
    :cvar SNG:
    :cvar SNI:
    :cvar SNJ:
    :cvar SNK:
    :cvar SNL:
    :cvar SNM:
    :cvar SNN:
    :cvar SNO:
    :cvar SNP:
    :cvar SNQ:
    :cvar SNR:
    :cvar SNS:
    :cvar SNU:
    :cvar SNV:
    :cvar SNW:
    :cvar SNX:
    :cvar SNY:
    :cvar SNZ:
    :cvar SOA:
    :cvar SOB:
    :cvar SOC:
    :cvar SOD:
    :cvar SOE:
    :cvar SOH:
    :cvar SOI:
    :cvar SOJ:
    :cvar SOK:
    :cvar SOL:
    :cvar SOM:
    :cvar SOO:
    :cvar SOP:
    :cvar SOQ:
    :cvar SOR:
    :cvar SOS:
    :cvar SOT:
    :cvar SOU:
    :cvar SOV:
    :cvar SOW:
    :cvar SOX:
    :cvar SOY:
    :cvar SOZ:
    :cvar SPA:
    :cvar SPB:
    :cvar SPC:
    :cvar SPD:
    :cvar SPE:
    :cvar SPG:
    :cvar SPI:
    :cvar SPK:
    :cvar SPL:
    :cvar SPM:
    :cvar SPN:
    :cvar SPO:
    :cvar SPP:
    :cvar SPQ:
    :cvar SPR:
    :cvar SPS:
    :cvar SPT:
    :cvar SPU:
    :cvar SPV:
    :cvar SPY:
    :cvar SQA:
    :cvar SQH:
    :cvar SQK:
    :cvar SQM:
    :cvar SQN:
    :cvar SQO:
    :cvar SQQ:
    :cvar SQS:
    :cvar SQT:
    :cvar SQU:
    :cvar SQX:
    :cvar SRA:
    :cvar SRB:
    :cvar SRC:
    :cvar SRE:
    :cvar SRF:
    :cvar SRG:
    :cvar SRH:
    :cvar SRI:
    :cvar SRK:
    :cvar SRL:
    :cvar SRM:
    :cvar SRN:
    :cvar SRO:
    :cvar SRP:
    :cvar SRQ:
    :cvar SRR:
    :cvar SRS:
    :cvar SRT:
    :cvar SRU:
    :cvar SRV:
    :cvar SRW:
    :cvar SRX:
    :cvar SRY:
    :cvar SRZ:
    :cvar SSB:
    :cvar SSC:
    :cvar SSD:
    :cvar SSE:
    :cvar SSF:
    :cvar SSG:
    :cvar SSH:
    :cvar SSI:
    :cvar SSJ:
    :cvar SSK:
    :cvar SSL:
    :cvar SSM:
    :cvar SSN:
    :cvar SSO:
    :cvar SSP:
    :cvar SSQ:
    :cvar SSR:
    :cvar SSS:
    :cvar SST:
    :cvar SSU:
    :cvar SSV:
    :cvar SSW:
    :cvar SSX:
    :cvar SSY:
    :cvar SSZ:
    :cvar STA:
    :cvar STB:
    :cvar STD:
    :cvar STE:
    :cvar STF:
    :cvar STG:
    :cvar STH:
    :cvar STI:
    :cvar STJ:
    :cvar STK:
    :cvar STL:
    :cvar STM:
    :cvar STN:
    :cvar STO:
    :cvar STP:
    :cvar STQ:
    :cvar STR:
    :cvar STS:
    :cvar STT:
    :cvar STU:
    :cvar STV:
    :cvar STW:
    :cvar STY:
    :cvar SUA:
    :cvar SUB:
    :cvar SUC:
    :cvar SUE:
    :cvar SUG:
    :cvar SUI:
    :cvar SUJ:
    :cvar SUK:
    :cvar SUN:
    :cvar SUO:
    :cvar SUQ:
    :cvar SUR:
    :cvar SUS:
    :cvar SUT:
    :cvar SUV:
    :cvar SUW:
    :cvar SUY:
    :cvar SUZ:
    :cvar SVA:
    :cvar SVB:
    :cvar SVC:
    :cvar SVE:
    :cvar SVK:
    :cvar SVM:
    :cvar SVS:
    :cvar SWB:
    :cvar SWC:
    :cvar SWE:
    :cvar SWF:
    :cvar SWG:
    :cvar SWH:
    :cvar SWI:
    :cvar SWJ:
    :cvar SWK:
    :cvar SWL:
    :cvar SWM:
    :cvar SWN:
    :cvar SWO:
    :cvar SWP:
    :cvar SWQ:
    :cvar SWR:
    :cvar SWS:
    :cvar SWT:
    :cvar SWU:
    :cvar SWV:
    :cvar SWW:
    :cvar SWX:
    :cvar SWY:
    :cvar SXB:
    :cvar SXE:
    :cvar SXG:
    :cvar SXK:
    :cvar SXM:
    :cvar SXN:
    :cvar SXR:
    :cvar SXS:
    :cvar SXU:
    :cvar SXW:
    :cvar SYA:
    :cvar SYB:
    :cvar SYC:
    :cvar SYI:
    :cvar SYK:
    :cvar SYL:
    :cvar SYM:
    :cvar SYN:
    :cvar SYO:
    :cvar SYS:
    :cvar SYW:
    :cvar SYX:
    :cvar SYY:
    :cvar SZA:
    :cvar SZB:
    :cvar SZC:
    :cvar SZE:
    :cvar SZG:
    :cvar SZL:
    :cvar SZN:
    :cvar SZP:
    :cvar SZS:
    :cvar SZV:
    :cvar SZW:
    :cvar SZY:
    :cvar TAA:
    :cvar TAB:
    :cvar TAC:
    :cvar TAD:
    :cvar TAE:
    :cvar TAF:
    :cvar TAG:
    :cvar TAH:
    :cvar TAJ:
    :cvar TAK:
    :cvar TAL:
    :cvar TAM:
    :cvar TAN:
    :cvar TAO:
    :cvar TAP:
    :cvar TAQ:
    :cvar TAR:
    :cvar TAS:
    :cvar TAT:
    :cvar TAU:
    :cvar TAV:
    :cvar TAW:
    :cvar TAX:
    :cvar TAY:
    :cvar TAZ:
    :cvar TBA:
    :cvar TBC:
    :cvar TBD:
    :cvar TBE:
    :cvar TBF:
    :cvar TBG:
    :cvar TBH:
    :cvar TBI:
    :cvar TBJ:
    :cvar TBK:
    :cvar TBL:
    :cvar TBM:
    :cvar TBN:
    :cvar TBO:
    :cvar TBP:
    :cvar TBR:
    :cvar TBS:
    :cvar TBT:
    :cvar TBU:
    :cvar TBV:
    :cvar TBW:
    :cvar TBX:
    :cvar TBY:
    :cvar TBZ:
    :cvar TCA:
    :cvar TCB:
    :cvar TCC:
    :cvar TCD:
    :cvar TCE:
    :cvar TCF:
    :cvar TCG:
    :cvar TCH:
    :cvar TCI:
    :cvar TCK:
    :cvar TCL:
    :cvar TCM:
    :cvar TCN:
    :cvar TCO:
    :cvar TCP:
    :cvar TCQ:
    :cvar TCS:
    :cvar TCT:
    :cvar TCU:
    :cvar TCW:
    :cvar TCX:
    :cvar TCY:
    :cvar TCZ:
    :cvar TDA:
    :cvar TDB:
    :cvar TDC:
    :cvar TDD:
    :cvar TDE:
    :cvar TDF:
    :cvar TDG:
    :cvar TDH:
    :cvar TDI:
    :cvar TDJ:
    :cvar TDK:
    :cvar TDL:
    :cvar TDM:
    :cvar TDN:
    :cvar TDO:
    :cvar TDQ:
    :cvar TDR:
    :cvar TDS:
    :cvar TDT:
    :cvar TDV:
    :cvar TDX:
    :cvar TDY:
    :cvar TEA:
    :cvar TEB:
    :cvar TEC:
    :cvar TED:
    :cvar TEE:
    :cvar TEF:
    :cvar TEG:
    :cvar TEH:
    :cvar TEI:
    :cvar TEK:
    :cvar TEL:
    :cvar TEM:
    :cvar TEN:
    :cvar TEO:
    :cvar TEP:
    :cvar TEQ:
    :cvar TER:
    :cvar TES:
    :cvar TET:
    :cvar TEU:
    :cvar TEV:
    :cvar TEW:
    :cvar TEX:
    :cvar TEY:
    :cvar TEZ:
    :cvar TFI:
    :cvar TFN:
    :cvar TFO:
    :cvar TFR:
    :cvar TFT:
    :cvar TGA:
    :cvar TGB:
    :cvar TGC:
    :cvar TGD:
    :cvar TGE:
    :cvar TGF:
    :cvar TGH:
    :cvar TGI:
    :cvar TGJ:
    :cvar TGK:
    :cvar TGL:
    :cvar TGN:
    :cvar TGO:
    :cvar TGP:
    :cvar TGQ:
    :cvar TGR:
    :cvar TGS:
    :cvar TGT:
    :cvar TGU:
    :cvar TGV:
    :cvar TGW:
    :cvar TGX:
    :cvar TGY:
    :cvar TGZ:
    :cvar THA:
    :cvar THD:
    :cvar THE:
    :cvar THF:
    :cvar THH:
    :cvar THI:
    :cvar THK:
    :cvar THL:
    :cvar THM:
    :cvar THN:
    :cvar THP:
    :cvar THQ:
    :cvar THR:
    :cvar THS:
    :cvar THT:
    :cvar THU:
    :cvar THV:
    :cvar THY:
    :cvar THZ:
    :cvar TIA:
    :cvar TIC:
    :cvar TIF:
    :cvar TIG:
    :cvar TIH:
    :cvar TII:
    :cvar TIJ:
    :cvar TIK:
    :cvar TIL:
    :cvar TIM:
    :cvar TIN:
    :cvar TIO:
    :cvar TIP:
    :cvar TIQ:
    :cvar TIR:
    :cvar TIS:
    :cvar TIT:
    :cvar TIU:
    :cvar TIV:
    :cvar TIW:
    :cvar TIX:
    :cvar TIY:
    :cvar TIZ:
    :cvar TJA:
    :cvar TJG:
    :cvar TJI:
    :cvar TJJ:
    :cvar TJL:
    :cvar TJM:
    :cvar TJN:
    :cvar TJO:
    :cvar TJP:
    :cvar TJS:
    :cvar TJU:
    :cvar TJW:
    :cvar TKA:
    :cvar TKB:
    :cvar TKD:
    :cvar TKE:
    :cvar TKF:
    :cvar TKG:
    :cvar TKL:
    :cvar TKM:
    :cvar TKN:
    :cvar TKP:
    :cvar TKQ:
    :cvar TKR:
    :cvar TKS:
    :cvar TKT:
    :cvar TKU:
    :cvar TKV:
    :cvar TKW:
    :cvar TKX:
    :cvar TKZ:
    :cvar TLA:
    :cvar TLB:
    :cvar TLC:
    :cvar TLD:
    :cvar TLF:
    :cvar TLG:
    :cvar TLI:
    :cvar TLJ:
    :cvar TLK:
    :cvar TLL:
    :cvar TLM:
    :cvar TLN:
    :cvar TLO:
    :cvar TLP:
    :cvar TLQ:
    :cvar TLR:
    :cvar TLS:
    :cvar TLT:
    :cvar TLU:
    :cvar TLV:
    :cvar TLX:
    :cvar TLY:
    :cvar TMA:
    :cvar TMB:
    :cvar TMC:
    :cvar TMD:
    :cvar TME:
    :cvar TMF:
    :cvar TMG:
    :cvar TMI:
    :cvar TMJ:
    :cvar TML:
    :cvar TMM:
    :cvar TMN:
    :cvar TMO:
    :cvar TMQ:
    :cvar TMR:
    :cvar TMS:
    :cvar TMT:
    :cvar TMU:
    :cvar TMV:
    :cvar TMW:
    :cvar TMY:
    :cvar TMZ:
    :cvar TNA:
    :cvar TNB:
    :cvar TNC:
    :cvar TND:
    :cvar TNG:
    :cvar TNH:
    :cvar TNI:
    :cvar TNK:
    :cvar TNL:
    :cvar TNM:
    :cvar TNN:
    :cvar TNO:
    :cvar TNP:
    :cvar TNQ:
    :cvar TNR:
    :cvar TNS:
    :cvar TNT:
    :cvar TNU:
    :cvar TNV:
    :cvar TNW:
    :cvar TNX:
    :cvar TNY:
    :cvar TNZ:
    :cvar TOB:
    :cvar TOC:
    :cvar TOD:
    :cvar TOF:
    :cvar TOG:
    :cvar TOH:
    :cvar TOI:
    :cvar TOJ:
    :cvar TOL:
    :cvar TOM:
    :cvar TON:
    :cvar TOO:
    :cvar TOP:
    :cvar TOQ:
    :cvar TOR:
    :cvar TOS:
    :cvar TOU:
    :cvar TOV:
    :cvar TOW:
    :cvar TOX:
    :cvar TOY:
    :cvar TOZ:
    :cvar TPA:
    :cvar TPC:
    :cvar TPE:
    :cvar TPF:
    :cvar TPG:
    :cvar TPI:
    :cvar TPJ:
    :cvar TPK:
    :cvar TPL:
    :cvar TPM:
    :cvar TPN:
    :cvar TPO:
    :cvar TPP:
    :cvar TPQ:
    :cvar TPR:
    :cvar TPT:
    :cvar TPU:
    :cvar TPV:
    :cvar TPX:
    :cvar TPY:
    :cvar TPZ:
    :cvar TQB:
    :cvar TQL:
    :cvar TQM:
    :cvar TQN:
    :cvar TQO:
    :cvar TQP:
    :cvar TQQ:
    :cvar TQR:
    :cvar TQT:
    :cvar TQU:
    :cvar TQW:
    :cvar TRA:
    :cvar TRB:
    :cvar TRC:
    :cvar TRD:
    :cvar TRE:
    :cvar TRF:
    :cvar TRG:
    :cvar TRH:
    :cvar TRI:
    :cvar TRJ:
    :cvar TRL:
    :cvar TRM:
    :cvar TRN:
    :cvar TRO:
    :cvar TRP:
    :cvar TRQ:
    :cvar TRR:
    :cvar TRS:
    :cvar TRT:
    :cvar TRU:
    :cvar TRV:
    :cvar TRW:
    :cvar TRX:
    :cvar TRY:
    :cvar TRZ:
    :cvar TSA:
    :cvar TSB:
    :cvar TSC:
    :cvar TSD:
    :cvar TSE:
    :cvar TSG:
    :cvar TSH:
    :cvar TSI:
    :cvar TSJ:
    :cvar TSK:
    :cvar TSL:
    :cvar TSM:
    :cvar TSN:
    :cvar TSO:
    :cvar TSP:
    :cvar TSQ:
    :cvar TSR:
    :cvar TSS:
    :cvar TST:
    :cvar TSU:
    :cvar TSV:
    :cvar TSW:
    :cvar TSX:
    :cvar TSY:
    :cvar TSZ:
    :cvar TTA:
    :cvar TTB:
    :cvar TTC:
    :cvar TTD:
    :cvar TTE:
    :cvar TTF:
    :cvar TTG:
    :cvar TTH:
    :cvar TTI:
    :cvar TTJ:
    :cvar TTK:
    :cvar TTL:
    :cvar TTM:
    :cvar TTN:
    :cvar TTO:
    :cvar TTP:
    :cvar TTQ:
    :cvar TTR:
    :cvar TTS:
    :cvar TTT:
    :cvar TTU:
    :cvar TTV:
    :cvar TTW:
    :cvar TTY:
    :cvar TTZ:
    :cvar TUA:
    :cvar TUB:
    :cvar TUC:
    :cvar TUD:
    :cvar TUE:
    :cvar TUF:
    :cvar TUG:
    :cvar TUH:
    :cvar TUI:
    :cvar TUJ:
    :cvar TUK:
    :cvar TUL:
    :cvar TUM:
    :cvar TUN:
    :cvar TUO:
    :cvar TUQ:
    :cvar TUR:
    :cvar TUS:
    :cvar TUU:
    :cvar TUV:
    :cvar TUX:
    :cvar TUY:
    :cvar TUZ:
    :cvar TVA:
    :cvar TVD:
    :cvar TVE:
    :cvar TVI:
    :cvar TVK:
    :cvar TVL:
    :cvar TVM:
    :cvar TVN:
    :cvar TVO:
    :cvar TVS:
    :cvar TVT:
    :cvar TVU:
    :cvar TVW:
    :cvar TVX:
    :cvar TVY:
    :cvar TWA:
    :cvar TWB:
    :cvar TWC:
    :cvar TWD:
    :cvar TWE:
    :cvar TWF:
    :cvar TWG:
    :cvar TWH:
    :cvar TWL:
    :cvar TWM:
    :cvar TWN:
    :cvar TWO:
    :cvar TWP:
    :cvar TWQ:
    :cvar TWR:
    :cvar TWT:
    :cvar TWU:
    :cvar TWW:
    :cvar TWX:
    :cvar TWY:
    :cvar TXA:
    :cvar TXC:
    :cvar TXE:
    :cvar TXI:
    :cvar TXJ:
    :cvar TXM:
    :cvar TXN:
    :cvar TXO:
    :cvar TXQ:
    :cvar TXS:
    :cvar TXT:
    :cvar TXU:
    :cvar TXX:
    :cvar TXY:
    :cvar TYA:
    :cvar TYE:
    :cvar TYH:
    :cvar TYI:
    :cvar TYJ:
    :cvar TYL:
    :cvar TYN:
    :cvar TYP:
    :cvar TYR:
    :cvar TYS:
    :cvar TYT:
    :cvar TYU:
    :cvar TYV:
    :cvar TYX:
    :cvar TYY:
    :cvar TYZ:
    :cvar TZA:
    :cvar TZH:
    :cvar TZJ:
    :cvar TZM:
    :cvar TZN:
    :cvar TZO:
    :cvar TZX:
    :cvar UAM:
    :cvar UAN:
    :cvar UAR:
    :cvar UBA:
    :cvar UBI:
    :cvar UBL:
    :cvar UBR:
    :cvar UBU:
    :cvar UBY:
    :cvar UDA:
    :cvar UDE:
    :cvar UDG:
    :cvar UDI:
    :cvar UDJ:
    :cvar UDL:
    :cvar UDM:
    :cvar UDU:
    :cvar UES:
    :cvar UFI:
    :cvar UGB:
    :cvar UGE:
    :cvar UGH:
    :cvar UGN:
    :cvar UGO:
    :cvar UGY:
    :cvar UHA:
    :cvar UHN:
    :cvar UIG:
    :cvar UIS:
    :cvar UIV:
    :cvar UJI:
    :cvar UKA:
    :cvar UKG:
    :cvar UKH:
    :cvar UKI:
    :cvar UKK:
    :cvar UKL:
    :cvar UKP:
    :cvar UKQ:
    :cvar UKR:
    :cvar UKS:
    :cvar UKU:
    :cvar UKV:
    :cvar UKW:
    :cvar UKY:
    :cvar ULA:
    :cvar ULB:
    :cvar ULC:
    :cvar ULE:
    :cvar ULF:
    :cvar ULI:
    :cvar ULK:
    :cvar ULL:
    :cvar ULM:
    :cvar ULN:
    :cvar ULU:
    :cvar ULW:
    :cvar ULY:
    :cvar UMA:
    :cvar UMB:
    :cvar UMD:
    :cvar UMG:
    :cvar UMI:
    :cvar UMM:
    :cvar UMN:
    :cvar UMO:
    :cvar UMP:
    :cvar UMR:
    :cvar UMS:
    :cvar UMU:
    :cvar UNA:
    :cvar UNE:
    :cvar UNG:
    :cvar UNI:
    :cvar UNK:
    :cvar UNM:
    :cvar UNN:
    :cvar UNR:
    :cvar UNU:
    :cvar UNX:
    :cvar UNZ:
    :cvar UON:
    :cvar UPI:
    :cvar UPV:
    :cvar URA:
    :cvar URB:
    :cvar URC:
    :cvar URD:
    :cvar URE:
    :cvar URF:
    :cvar URG:
    :cvar URH:
    :cvar URI:
    :cvar URK:
    :cvar URL:
    :cvar URM:
    :cvar URN:
    :cvar URO:
    :cvar URP:
    :cvar URR:
    :cvar URT:
    :cvar URU:
    :cvar URV:
    :cvar URW:
    :cvar URX:
    :cvar URY:
    :cvar URZ:
    :cvar USA:
    :cvar USH:
    :cvar USI:
    :cvar USK:
    :cvar USP:
    :cvar USS:
    :cvar USU:
    :cvar UTA:
    :cvar UTE:
    :cvar UTH:
    :cvar UTP:
    :cvar UTR:
    :cvar UTU:
    :cvar UUM:
    :cvar UUR:
    :cvar UUU:
    :cvar UVE:
    :cvar UVH:
    :cvar UVL:
    :cvar UWA:
    :cvar UYA:
    :cvar UZN:
    :cvar UZS:
    :cvar VAA:
    :cvar VAE:
    :cvar VAF:
    :cvar VAG:
    :cvar VAH:
    :cvar VAI:
    :cvar VAJ:
    :cvar VAL:
    :cvar VAM:
    :cvar VAN:
    :cvar VAO:
    :cvar VAP:
    :cvar VAR:
    :cvar VAS:
    :cvar VAU:
    :cvar VAV:
    :cvar VAY:
    :cvar VBB:
    :cvar VBK:
    :cvar VEC:
    :cvar VED:
    :cvar VEL:
    :cvar VEM:
    :cvar VEN:
    :cvar VEO:
    :cvar VEP:
    :cvar VER:
    :cvar VGR:
    :cvar VGT:
    :cvar VIC:
    :cvar VID:
    :cvar VIE:
    :cvar VIF:
    :cvar VIG:
    :cvar VIL:
    :cvar VIS:
    :cvar VIT:
    :cvar VIV:
    :cvar VJK:
    :cvar VKA:
    :cvar VKJ:
    :cvar VKK:
    :cvar VKL:
    :cvar VKM:
    :cvar VKN:
    :cvar VKO:
    :cvar VKP:
    :cvar VKT:
    :cvar VKU:
    :cvar VKZ:
    :cvar VLP:
    :cvar VLS:
    :cvar VMA:
    :cvar VMB:
    :cvar VMC:
    :cvar VMD:
    :cvar VME:
    :cvar VMF:
    :cvar VMG:
    :cvar VMH:
    :cvar VMI:
    :cvar VMJ:
    :cvar VMK:
    :cvar VML:
    :cvar VMM:
    :cvar VMP:
    :cvar VMQ:
    :cvar VMR:
    :cvar VMS:
    :cvar VMU:
    :cvar VMV:
    :cvar VMW:
    :cvar VMX:
    :cvar VMY:
    :cvar VMZ:
    :cvar VNK:
    :cvar VNM:
    :cvar VNP:
    :cvar VOR:
    :cvar VOT:
    :cvar VRA:
    :cvar VRO:
    :cvar VRS:
    :cvar VRT:
    :cvar VSI:
    :cvar VSL:
    :cvar VSV:
    :cvar VTO:
    :cvar VUM:
    :cvar VUN:
    :cvar VUT:
    :cvar VWA:
    :cvar WAA:
    :cvar WAB:
    :cvar WAC:
    :cvar WAD:
    :cvar WAE:
    :cvar WAF:
    :cvar WAG:
    :cvar WAH:
    :cvar WAI:
    :cvar WAJ:
    :cvar WAL:
    :cvar WAM:
    :cvar WAN:
    :cvar WAO:
    :cvar WAP:
    :cvar WAQ:
    :cvar WAR:
    :cvar WAS:
    :cvar WAT:
    :cvar WAU:
    :cvar WAV:
    :cvar WAW:
    :cvar WAX:
    :cvar WAY:
    :cvar WAZ:
    :cvar WBA:
    :cvar WBB:
    :cvar WBE:
    :cvar WBF:
    :cvar WBH:
    :cvar WBI:
    :cvar WBJ:
    :cvar WBK:
    :cvar WBL:
    :cvar WBM:
    :cvar WBP:
    :cvar WBQ:
    :cvar WBR:
    :cvar WBS:
    :cvar WBT:
    :cvar WBV:
    :cvar WBW:
    :cvar WCA:
    :cvar WCI:
    :cvar WDD:
    :cvar WDG:
    :cvar WDJ:
    :cvar WDK:
    :cvar WDT:
    :cvar WDU:
    :cvar WDY:
    :cvar WEA:
    :cvar WEC:
    :cvar WED:
    :cvar WEG:
    :cvar WEH:
    :cvar WEI:
    :cvar WEM:
    :cvar WEO:
    :cvar WEP:
    :cvar WER:
    :cvar WES:
    :cvar WET:
    :cvar WEU:
    :cvar WEW:
    :cvar WFG:
    :cvar WGA:
    :cvar WGB:
    :cvar WGG:
    :cvar WGI:
    :cvar WGO:
    :cvar WGU:
    :cvar WGY:
    :cvar WHA:
    :cvar WHG:
    :cvar WHK:
    :cvar WHU:
    :cvar WIB:
    :cvar WIC:
    :cvar WIE:
    :cvar WIF:
    :cvar WIG:
    :cvar WIH:
    :cvar WII:
    :cvar WIJ:
    :cvar WIK:
    :cvar WIL:
    :cvar WIM:
    :cvar WIN:
    :cvar WIR:
    :cvar WIU:
    :cvar WIV:
    :cvar WIY:
    :cvar WJA:
    :cvar WJI:
    :cvar WKA:
    :cvar WKB:
    :cvar WKD:
    :cvar WKL:
    :cvar WKR:
    :cvar WKU:
    :cvar WKW:
    :cvar WKY:
    :cvar WLA:
    :cvar WLC:
    :cvar WLE:
    :cvar WLG:
    :cvar WLH:
    :cvar WLI:
    :cvar WLK:
    :cvar WLL:
    :cvar WLN:
    :cvar WLO:
    :cvar WLR:
    :cvar WLS:
    :cvar WLU:
    :cvar WLV:
    :cvar WLW:
    :cvar WLX:
    :cvar WMB:
    :cvar WMC:
    :cvar WMD:
    :cvar WME:
    :cvar WMG:
    :cvar WMH:
    :cvar WMI:
    :cvar WMM:
    :cvar WMN:
    :cvar WMO:
    :cvar WMS:
    :cvar WMT:
    :cvar WMW:
    :cvar WMX:
    :cvar WNB:
    :cvar WNC:
    :cvar WND:
    :cvar WNE:
    :cvar WNG:
    :cvar WNI:
    :cvar WNK:
    :cvar WNM:
    :cvar WNN:
    :cvar WNO:
    :cvar WNP:
    :cvar WNU:
    :cvar WNW:
    :cvar WNY:
    :cvar WOA:
    :cvar WOB:
    :cvar WOC:
    :cvar WOD:
    :cvar WOE:
    :cvar WOF:
    :cvar WOG:
    :cvar WOI:
    :cvar WOK:
    :cvar WOL:
    :cvar WOM:
    :cvar WON:
    :cvar WOO:
    :cvar WOR:
    :cvar WOS:
    :cvar WOW:
    :cvar WOY:
    :cvar WPC:
    :cvar WRB:
    :cvar WRG:
    :cvar WRH:
    :cvar WRI:
    :cvar WRK:
    :cvar WRL:
    :cvar WRM:
    :cvar WRN:
    :cvar WRO:
    :cvar WRP:
    :cvar WRR:
    :cvar WRS:
    :cvar WRU:
    :cvar WRV:
    :cvar WRW:
    :cvar WRX:
    :cvar WRY:
    :cvar WRZ:
    :cvar WSA:
    :cvar WSG:
    :cvar WSI:
    :cvar WSK:
    :cvar WSR:
    :cvar WSS:
    :cvar WSU:
    :cvar WSV:
    :cvar WTB:
    :cvar WTF:
    :cvar WTH:
    :cvar WTI:
    :cvar WTK:
    :cvar WTM:
    :cvar WTW:
    :cvar WUA:
    :cvar WUB:
    :cvar WUD:
    :cvar WUH:
    :cvar WUL:
    :cvar WUM:
    :cvar WUN:
    :cvar WUT:
    :cvar WUU:
    :cvar WUV:
    :cvar WUX:
    :cvar WUY:
    :cvar WWA:
    :cvar WWB:
    :cvar WWO:
    :cvar WWR:
    :cvar WWW:
    :cvar WXA:
    :cvar WXW:
    :cvar WYB:
    :cvar WYI:
    :cvar WYM:
    :cvar WYN:
    :cvar WYR:
    :cvar WYY:
    :cvar XAB:
    :cvar XAC:
    :cvar XAD:
    :cvar XAI:
    :cvar XAJ:
    :cvar XAK:
    :cvar XAL:
    :cvar XAM:
    :cvar XAN:
    :cvar XAO:
    :cvar XAP:
    :cvar XAR:
    :cvar XAS:
    :cvar XAT:
    :cvar XAU:
    :cvar XAV:
    :cvar XAW:
    :cvar XAY:
    :cvar XBB:
    :cvar XBD:
    :cvar XBE:
    :cvar XBG:
    :cvar XBI:
    :cvar XBJ:
    :cvar XBN:
    :cvar XBP:
    :cvar XBR:
    :cvar XBW:
    :cvar XBY:
    :cvar XCH:
    :cvar XCM:
    :cvar XCN:
    :cvar XCV:
    :cvar XCW:
    :cvar XCY:
    :cvar XDA:
    :cvar XDK:
    :cvar XDO:
    :cvar XDQ:
    :cvar XDY:
    :cvar XED:
    :cvar XEG:
    :cvar XEL:
    :cvar XEM:
    :cvar XER:
    :cvar XES:
    :cvar XET:
    :cvar XEU:
    :cvar XGB:
    :cvar XGD:
    :cvar XGF:
    :cvar XGG:
    :cvar XGI:
    :cvar XGM:
    :cvar XGR:
    :cvar XGU:
    :cvar XGW:
    :cvar XHE:
    :cvar XHO:
    :cvar XHV:
    :cvar XII:
    :cvar XIN:
    :cvar XIR:
    :cvar XIS:
    :cvar XIY:
    :cvar XJB:
    :cvar XJT:
    :cvar XKA:
    :cvar XKB:
    :cvar XKC:
    :cvar XKD:
    :cvar XKE:
    :cvar XKF:
    :cvar XKG:
    :cvar XKI:
    :cvar XKJ:
    :cvar XKK:
    :cvar XKL:
    :cvar XKN:
    :cvar XKO:
    :cvar XKP:
    :cvar XKQ:
    :cvar XKR:
    :cvar XKS:
    :cvar XKT:
    :cvar XKU:
    :cvar XKV:
    :cvar XKW:
    :cvar XKX:
    :cvar XKY:
    :cvar XKZ:
    :cvar XLA:
    :cvar XLB:
    :cvar XLO:
    :cvar XMA:
    :cvar XMB:
    :cvar XMC:
    :cvar XMD:
    :cvar XMF:
    :cvar XMG:
    :cvar XMH:
    :cvar XMJ:
    :cvar XML:
    :cvar XMM:
    :cvar XMO:
    :cvar XMP:
    :cvar XMQ:
    :cvar XMS:
    :cvar XMT:
    :cvar XMU:
    :cvar XMV:
    :cvar XMW:
    :cvar XMX:
    :cvar XMY:
    :cvar XMZ:
    :cvar XNB:
    :cvar XNH:
    :cvar XNI:
    :cvar XNJ:
    :cvar XNK:
    :cvar XNM:
    :cvar XNN:
    :cvar XNQ:
    :cvar XNR:
    :cvar XNS:
    :cvar XNT:
    :cvar XNU:
    :cvar XNY:
    :cvar XNZ:
    :cvar XOC:
    :cvar XOD:
    :cvar XOG:
    :cvar XOI:
    :cvar XOK:
    :cvar XOM:
    :cvar XON:
    :cvar XOO:
    :cvar XOP:
    :cvar XOR:
    :cvar XOW:
    :cvar XPA:
    :cvar XPB:
    :cvar XPD:
    :cvar XPE:
    :cvar XPF:
    :cvar XPH:
    :cvar XPJ:
    :cvar XPK:
    :cvar XPL:
    :cvar XPM:
    :cvar XPN:
    :cvar XPO:
    :cvar XPQ:
    :cvar XPT:
    :cvar XPV:
    :cvar XPW:
    :cvar XPX:
    :cvar XPZ:
    :cvar XRA:
    :cvar XRB:
    :cvar XRD:
    :cvar XRE:
    :cvar XRG:
    :cvar XRI:
    :cvar XRN:
    :cvar XRT:
    :cvar XRU:
    :cvar XRW:
    :cvar XSB:
    :cvar XSE:
    :cvar XSH:
    :cvar XSI:
    :cvar XSJ:
    :cvar XSL:
    :cvar XSM:
    :cvar XSN:
    :cvar XSO:
    :cvar XSP:
    :cvar XSQ:
    :cvar XSR:
    :cvar XSU:
    :cvar XSV:
    :cvar XSY:
    :cvar XTA:
    :cvar XTB:
    :cvar XTC:
    :cvar XTD:
    :cvar XTE:
    :cvar XTH:
    :cvar XTI:
    :cvar XTJ:
    :cvar XTL:
    :cvar XTM:
    :cvar XTN:
    :cvar XTP:
    :cvar XTS:
    :cvar XTT:
    :cvar XTU:
    :cvar XTV:
    :cvar XTW:
    :cvar XTY:
    :cvar XUA:
    :cvar XUB:
    :cvar XUD:
    :cvar XUG:
    :cvar XUJ:
    :cvar XUL:
    :cvar XUN:
    :cvar XUO:
    :cvar XUP:
    :cvar XUT:
    :cvar XUU:
    :cvar XVI:
    :cvar XWA:
    :cvar XWC:
    :cvar XWD:
    :cvar XWE:
    :cvar XWG:
    :cvar XWJ:
    :cvar XWK:
    :cvar XWL:
    :cvar XWR:
    :cvar XWT:
    :cvar XWW:
    :cvar XXB:
    :cvar XXK:
    :cvar XXM:
    :cvar XXR:
    :cvar XXT:
    :cvar XYA:
    :cvar XYB:
    :cvar XYJ:
    :cvar XYK:
    :cvar XYL:
    :cvar XYT:
    :cvar XYY:
    :cvar XZM:
    :cvar YAA:
    :cvar YAB:
    :cvar YAC:
    :cvar YAD:
    :cvar YAE:
    :cvar YAF:
    :cvar YAG:
    :cvar YAH:
    :cvar YAI:
    :cvar YAJ:
    :cvar YAK:
    :cvar YAL:
    :cvar YAM:
    :cvar YAN:
    :cvar YAO:
    :cvar YAP:
    :cvar YAQ:
    :cvar YAR:
    :cvar YAS:
    :cvar YAT:
    :cvar YAU:
    :cvar YAV:
    :cvar YAW:
    :cvar YAX:
    :cvar YAY:
    :cvar YAZ:
    :cvar YBA:
    :cvar YBB:
    :cvar YBE:
    :cvar YBH:
    :cvar YBI:
    :cvar YBJ:
    :cvar YBK:
    :cvar YBL:
    :cvar YBM:
    :cvar YBN:
    :cvar YBO:
    :cvar YBX:
    :cvar YBY:
    :cvar YCH:
    :cvar YCL:
    :cvar YCN:
    :cvar YCP:
    :cvar YCR:
    :cvar YDA:
    :cvar YDD:
    :cvar YDE:
    :cvar YDG:
    :cvar YDK:
    :cvar YEA:
    :cvar YEC:
    :cvar YEE:
    :cvar YEI:
    :cvar YEJ:
    :cvar YER:
    :cvar YES:
    :cvar YET:
    :cvar YEU:
    :cvar YEV:
    :cvar YEY:
    :cvar YGA:
    :cvar YGI:
    :cvar YGL:
    :cvar YGM:
    :cvar YGP:
    :cvar YGR:
    :cvar YGS:
    :cvar YGU:
    :cvar YGW:
    :cvar YHA:
    :cvar YHD:
    :cvar YHL:
    :cvar YHS:
    :cvar YIA:
    :cvar YIF:
    :cvar YIG:
    :cvar YIH:
    :cvar YII:
    :cvar YIJ:
    :cvar YIK:
    :cvar YIL:
    :cvar YIM:
    :cvar YIN:
    :cvar YIP:
    :cvar YIQ:
    :cvar YIR:
    :cvar YIS:
    :cvar YIT:
    :cvar YIU:
    :cvar YIV:
    :cvar YIX:
    :cvar YIZ:
    :cvar YKA:
    :cvar YKG:
    :cvar YKH:
    :cvar YKI:
    :cvar YKK:
    :cvar YKL:
    :cvar YKM:
    :cvar YKN:
    :cvar YKO:
    :cvar YKR:
    :cvar YKT:
    :cvar YKU:
    :cvar YKY:
    :cvar YLA:
    :cvar YLB:
    :cvar YLE:
    :cvar YLG:
    :cvar YLI:
    :cvar YLL:
    :cvar YLM:
    :cvar YLN:
    :cvar YLO:
    :cvar YLR:
    :cvar YLU:
    :cvar YLY:
    :cvar YMB:
    :cvar YMC:
    :cvar YMD:
    :cvar YME:
    :cvar YMG:
    :cvar YMH:
    :cvar YMI:
    :cvar YMK:
    :cvar YML:
    :cvar YMM:
    :cvar YMN:
    :cvar YMO:
    :cvar YMP:
    :cvar YMQ:
    :cvar YMR:
    :cvar YMX:
    :cvar YMZ:
    :cvar YNA:
    :cvar YNB:
    :cvar YND:
    :cvar YNE:
    :cvar YNG:
    :cvar YNK:
    :cvar YNL:
    :cvar YNN:
    :cvar YNO:
    :cvar YNQ:
    :cvar YNS:
    :cvar YNU:
    :cvar YOB:
    :cvar YOG:
    :cvar YOI:
    :cvar YOK:
    :cvar YOL:
    :cvar YOM:
    :cvar YON:
    :cvar YOR:
    :cvar YOT:
    :cvar YOX:
    :cvar YOY:
    :cvar YPA:
    :cvar YPB:
    :cvar YPG:
    :cvar YPH:
    :cvar YPM:
    :cvar YPN:
    :cvar YPO:
    :cvar YPP:
    :cvar YPZ:
    :cvar YRA:
    :cvar YRB:
    :cvar YRE:
    :cvar YRK:
    :cvar YRL:
    :cvar YRM:
    :cvar YRN:
    :cvar YRO:
    :cvar YRS:
    :cvar YRW:
    :cvar YRY:
    :cvar YSC:
    :cvar YSD:
    :cvar YSG:
    :cvar YSL:
    :cvar YSM:
    :cvar YSN:
    :cvar YSO:
    :cvar YSP:
    :cvar YSR:
    :cvar YSS:
    :cvar YSY:
    :cvar YTA:
    :cvar YTL:
    :cvar YTP:
    :cvar YTW:
    :cvar YTY:
    :cvar YUA:
    :cvar YUB:
    :cvar YUC:
    :cvar YUD:
    :cvar YUE:
    :cvar YUF:
    :cvar YUG:
    :cvar YUI:
    :cvar YUJ:
    :cvar YUK:
    :cvar YUL:
    :cvar YUM:
    :cvar YUN:
    :cvar YUP:
    :cvar YUQ:
    :cvar YUR:
    :cvar YUT:
    :cvar YUW:
    :cvar YUX:
    :cvar YUY:
    :cvar YUZ:
    :cvar YVA:
    :cvar YVT:
    :cvar YWA:
    :cvar YWG:
    :cvar YWL:
    :cvar YWN:
    :cvar YWQ:
    :cvar YWR:
    :cvar YWT:
    :cvar YWU:
    :cvar YWW:
    :cvar YXA:
    :cvar YXG:
    :cvar YXL:
    :cvar YXM:
    :cvar YXU:
    :cvar YXY:
    :cvar YYR:
    :cvar YYU:
    :cvar YYZ:
    :cvar YZG:
    :cvar YZK:
    :cvar ZAA:
    :cvar ZAB:
    :cvar ZAC:
    :cvar ZAD:
    :cvar ZAE:
    :cvar ZAF:
    :cvar ZAG:
    :cvar ZAH:
    :cvar ZAI:
    :cvar ZAJ:
    :cvar ZAK:
    :cvar ZAL:
    :cvar ZAM:
    :cvar ZAO:
    :cvar ZAQ:
    :cvar ZAR:
    :cvar ZAS:
    :cvar ZAT:
    :cvar ZAU:
    :cvar ZAV:
    :cvar ZAW:
    :cvar ZAX:
    :cvar ZAY:
    :cvar ZAZ:
    :cvar ZBC:
    :cvar ZBE:
    :cvar ZBT:
    :cvar ZBU:
    :cvar ZBW:
    :cvar ZCA:
    :cvar ZCD:
    :cvar ZCH:
    :cvar ZDJ:
    :cvar ZEA:
    :cvar ZEG:
    :cvar ZEH:
    :cvar ZEM:
    :cvar ZEN:
    :cvar ZGA:
    :cvar ZGB:
    :cvar ZGH:
    :cvar ZGM:
    :cvar ZGN:
    :cvar ZGR:
    :cvar ZHB:
    :cvar ZHD:
    :cvar ZHI:
    :cvar ZHN:
    :cvar ZHW:
    :cvar ZIA:
    :cvar ZIB:
    :cvar ZIK:
    :cvar ZIL:
    :cvar ZIM:
    :cvar ZIN:
    :cvar ZIW:
    :cvar ZIZ:
    :cvar ZKA:
    :cvar ZKD:
    :cvar ZKK:
    :cvar ZKN:
    :cvar ZKO:
    :cvar ZKP:
    :cvar ZKR:
    :cvar ZKU:
    :cvar ZKV:
    :cvar ZLA:
    :cvar ZLJ:
    :cvar ZLM:
    :cvar ZLN:
    :cvar ZLQ:
    :cvar ZLU:
    :cvar ZMA:
    :cvar ZMB:
    :cvar ZMC:
    :cvar ZMD:
    :cvar ZME:
    :cvar ZMF:
    :cvar ZMG:
    :cvar ZMH:
    :cvar ZMI:
    :cvar ZMJ:
    :cvar ZMK:
    :cvar ZML:
    :cvar ZMM:
    :cvar ZMN:
    :cvar ZMO:
    :cvar ZMP:
    :cvar ZMQ:
    :cvar ZMR:
    :cvar ZMS:
    :cvar ZMT:
    :cvar ZMU:
    :cvar ZMV:
    :cvar ZMW:
    :cvar ZMX:
    :cvar ZMY:
    :cvar ZMZ:
    :cvar ZNA:
    :cvar ZNE:
    :cvar ZNG:
    :cvar ZNK:
    :cvar ZNS:
    :cvar ZOC:
    :cvar ZOH:
    :cvar ZOM:
    :cvar ZOO:
    :cvar ZOQ:
    :cvar ZOR:
    :cvar ZOS:
    :cvar ZPA:
    :cvar ZPB:
    :cvar ZPC:
    :cvar ZPD:
    :cvar ZPE:
    :cvar ZPF:
    :cvar ZPG:
    :cvar ZPH:
    :cvar ZPI:
    :cvar ZPJ:
    :cvar ZPK:
    :cvar ZPL:
    :cvar ZPM:
    :cvar ZPN:
    :cvar ZPO:
    :cvar ZPP:
    :cvar ZPQ:
    :cvar ZPR:
    :cvar ZPS:
    :cvar ZPT:
    :cvar ZPU:
    :cvar ZPV:
    :cvar ZPW:
    :cvar ZPX:
    :cvar ZPY:
    :cvar ZPZ:
    :cvar ZQE:
    :cvar ZRG:
    :cvar ZRN:
    :cvar ZRO:
    :cvar ZRS:
    :cvar ZSA:
    :cvar ZSL:
    :cvar ZSM:
    :cvar ZSR:
    :cvar ZSU:
    :cvar ZTE:
    :cvar ZTG:
    :cvar ZTL:
    :cvar ZTM:
    :cvar ZTN:
    :cvar ZTP:
    :cvar ZTQ:
    :cvar ZTS:
    :cvar ZTT:
    :cvar ZTU:
    :cvar ZTX:
    :cvar ZTY:
    :cvar ZUH:
    :cvar ZUL:
    :cvar ZUM:
    :cvar ZUN:
    :cvar ZUY:
    :cvar ZWA:
    :cvar ZYB:
    :cvar ZYG:
    :cvar ZYJ:
    :cvar ZYN:
    :cvar ZYP:
    :cvar ZZJ:
    :cvar KUR:
    :cvar PAT:
    :cvar EWA:
    :cvar NOT_AVAILABLE:
    """
    AAA = "aaa"
    AAB = "aab"
    AAC = "aac"
    AAD = "aad"
    AAE = "aae"
    AAF = "aaf"
    AAG = "aag"
    AAH = "aah"
    AAI = "aai"
    AAK = "aak"
    AAL = "aal"
    AAN = "aan"
    AAO = "aao"
    AAP = "aap"
    AAQ = "aaq"
    AAR = "aar"
    AAS = "aas"
    ALB = "alb"
    SQI = "sqi"
    AAT = "aat"
    AAU = "aau"
    AAW = "aaw"
    AAX = "aax"
    GER = "ger"
    AAZ = "aaz"
    ABA = "aba"
    ABB = "abb"
    ABC = "abc"
    ABD = "abd"
    ABE = "abe"
    ABF = "abf"
    ABG = "abg"
    ABH = "abh"
    ABI = "abi"
    ABJ = "abj"
    ABK = "abk"
    ABL = "abl"
    ABM = "abm"
    ABN = "abn"
    ABO = "abo"
    ABP = "abp"
    ABQ = "abq"
    ABR = "abr"
    ABS = "abs"
    ABT = "abt"
    ABU = "abu"
    ABV = "abv"
    ABW = "abw"
    ABX = "abx"
    ABY = "aby"
    ABZ = "abz"
    ACA = "aca"
    ACB = "acb"
    ACD = "acd"
    ACE = "ace"
    ACF = "acf"
    ACH = "ach"
    ACI = "aci"
    ACK = "ack"
    ACL = "acl"
    ACM = "acm"
    ACN = "acn"
    ACP = "acp"
    ACQ = "acq"
    ACR = "acr"
    ACS = "acs"
    ACT = "act"
    ACU = "acu"
    ACV = "acv"
    ACW = "acw"
    ACX = "acx"
    ACY = "acy"
    ACZ = "acz"
    ADA = "ada"
    ADB = "adb"
    ADD = "add"
    ADE = "ade"
    ADF = "adf"
    ADG = "adg"
    ADH = "adh"
    ADI = "adi"
    ADJ = "adj"
    ADL = "adl"
    ADN = "adn"
    ADO = "ado"
    ADQ = "adq"
    ADR = "adr"
    ADS = "ads"
    ADT = "adt"
    ADU = "adu"
    ADW = "adw"
    ADX = "adx"
    ADY = "ady"
    ADZ = "adz"
    AEA = "aea"
    AEB = "aeb"
    AEC = "aec"
    AED = "aed"
    AEE = "aee"
    AEK = "aek"
    AEL = "ael"
    AEM = "aem"
    AEN = "aen"
    AEQ = "aeq"
    AER = "aer"
    AES = "aes"
    AEU = "aeu"
    AEW = "aew"
    AEY = "aey"
    AEZ = "aez"
    AFB = "afb"
    AFD = "afd"
    AFE = "afe"
    AFG = "afg"
    AFI = "afi"
    AFK = "afk"
    AFN = "afn"
    AFO = "afo"
    AFP = "afp"
    AFR = "afr"
    AFS = "afs"
    AFT = "aft"
    AFU = "afu"
    AFZ = "afz"
    AGA = "aga"
    AGB = "agb"
    AGC = "agc"
    AGD = "agd"
    AGE = "age"
    AGF = "agf"
    AGG = "agg"
    AGH = "agh"
    AGI = "agi"
    AGJ = "agj"
    AGK = "agk"
    AGL = "agl"
    AGM = "agm"
    AGN = "agn"
    AGO = "ago"
    AGQ = "agq"
    AGR = "agr"
    AGS = "ags"
    AGT = "agt"
    AGU = "agu"
    AGV = "agv"
    AGW = "agw"
    AGX = "agx"
    AGY = "agy"
    AGZ = "agz"
    AHA = "aha"
    AHB = "ahb"
    AHG = "ahg"
    AHH = "ahh"
    AHI = "ahi"
    AHK = "ahk"
    AHL = "ahl"
    AHM = "ahm"
    AHN = "ahn"
    AHO = "aho"
    AHP = "ahp"
    AHR = "ahr"
    AHS = "ahs"
    AHT = "aht"
    AIA = "aia"
    AIB = "aib"
    AIC = "aic"
    AID = "aid"
    AIE = "aie"
    AIF = "aif"
    AIG = "aig"
    AIH = "aih"
    AII = "aii"
    AIJ = "aij"
    AIK = "aik"
    AIL = "ail"
    AIM = "aim"
    AIN = "ain"
    AIO = "aio"
    AIP = "aip"
    AIQ = "aiq"
    AIR = "air"
    AIT = "ait"
    AIW = "aiw"
    AIX = "aix"
    AIY = "aiy"
    AJA = "aja"
    AJG = "ajg"
    AJI = "aji"
    AJN = "ajn"
    AJS = "ajs"
    AJU = "aju"
    AJW = "ajw"
    AJZ = "ajz"
    AKA = "aka"
    AKB = "akb"
    AKC = "akc"
    AKD = "akd"
    AKE = "ake"
    AKF = "akf"
    AKG = "akg"
    AKH = "akh"
    AKI = "aki"
    AKJ = "akj"
    AKL = "akl"
    AKM = "akm"
    AKO = "ako"
    AKP = "akp"
    AKQ = "akq"
    AKR = "akr"
    AKS = "aks"
    AKT = "akt"
    AKU = "aku"
    AKV = "akv"
    AKW = "akw"
    AKX = "akx"
    AKY = "aky"
    AKZ = "akz"
    ALA = "ala"
    ALC = "alc"
    ALD = "ald"
    ALE = "ale"
    ALF = "alf"
    ALH = "alh"
    ALI = "ali"
    ALJ = "alj"
    ALK = "alk"
    ALL = "all"
    ALM = "alm"
    ALN = "aln"
    ALO = "alo"
    ALP = "alp"
    ALQ = "alq"
    ALR = "alr"
    ALS = "als"
    ALT = "alt"
    ALU = "alu"
    ALW = "alw"
    ALX = "alx"
    ALY = "aly"
    ALZ = "alz"
    AMA = "ama"
    AMB = "amb"
    AMC = "amc"
    AME = "ame"
    AMF = "amf"
    AMG = "amg"
    AMH = "amh"
    AMI = "ami"
    AMJ = "amj"
    AMK = "amk"
    AML = "aml"
    AMM = "amm"
    AMN = "amn"
    AMO = "amo"
    AMP = "amp"
    AMQ = "amq"
    AMR = "amr"
    AMS = "ams"
    AMT = "amt"
    AMU = "amu"
    AMV = "amv"
    AMW = "amw"
    AMX = "amx"
    AMY = "amy"
    AMZ = "amz"
    ANA = "ana"
    ANB = "anb"
    ANC = "anc"
    AND = "and"
    ANE = "ane"
    ANF = "anf"
    ANH = "anh"
    ANI = "ani"
    ANJ = "anj"
    ANK = "ank"
    ANL = "anl"
    ANM = "anm"
    ANN = "ann"
    ANO = "ano"
    ANP = "anp"
    ANQ = "anq"
    ANR = "anr"
    ANS = "ans"
    ANT = "ant"
    ANU = "anu"
    ANV = "anv"
    ANW = "anw"
    ANX = "anx"
    ANY = "any"
    ANZ = "anz"
    AOA = "aoa"
    AOB = "aob"
    AOC = "aoc"
    AOD = "aod"
    AOE = "aoe"
    AOF = "aof"
    AOG = "aog"
    AOI = "aoi"
    AOJ = "aoj"
    AOK = "aok"
    AOL = "aol"
    AOM = "aom"
    AON = "aon"
    AOR = "aor"
    AOS = "aos"
    AOT = "aot"
    AOU = "aou"
    AOX = "aox"
    AOZ = "aoz"
    APB = "apb"
    APC = "apc"
    APD = "apd"
    APE = "ape"
    APF = "apf"
    APG = "apg"
    APH = "aph"
    API = "api"
    APJ = "apj"
    APK = "apk"
    APL = "apl"
    APM = "apm"
    APN = "apn"
    APO = "apo"
    APP = "app"
    APQ = "apq"
    APR = "apr"
    APS = "aps"
    APT = "apt"
    APU = "apu"
    APV = "apv"
    APW = "apw"
    APX = "apx"
    APY = "apy"
    APZ = "apz"
    AQC = "aqc"
    AQD = "aqd"
    AQG = "aqg"
    AQK = "aqk"
    AQM = "aqm"
    AQN = "aqn"
    AQP = "aqp"
    AQR = "aqr"
    AQT = "aqt"
    AQZ = "aqz"
    ARB = "arb"
    ARD = "ard"
    ARE = "are"
    ARG = "arg"
    ARH = "arh"
    ARI = "ari"
    ARJ = "arj"
    ARK = "ark"
    ARL = "arl"
    ARN = "arn"
    ARO = "aro"
    ARP = "arp"
    ARQ = "arq"
    ARR = "arr"
    ARS = "ars"
    ARU = "aru"
    ARV = "arv"
    ARW = "arw"
    ARX = "arx"
    ARY = "ary"
    ARZ = "arz"
    ASA = "asa"
    ASB = "asb"
    ASC = "asc"
    ASE = "ase"
    ASF = "asf"
    ASG = "asg"
    ASH = "ash"
    ASI = "asi"
    ASJ = "asj"
    ASK = "ask"
    ASL = "asl"
    ASM = "asm"
    ASN = "asn"
    ASO = "aso"
    ASP = "asp"
    ASQ = "asq"
    ASR = "asr"
    ASS = "ass"
    AST = "ast"
    ASU = "asu"
    ASV = "asv"
    ASW = "asw"
    ASX = "asx"
    ASY = "asy"
    ASZ = "asz"
    ATA = "ata"
    ATB = "atb"
    ATC = "atc"
    ATD = "atd"
    ATE = "ate"
    ATG = "atg"
    ATI = "ati"
    ATJ = "atj"
    ATK = "atk"
    ATL = "atl"
    ATM = "atm"
    ATN = "atn"
    ATO = "ato"
    ATP = "atp"
    ATQ = "atq"
    ATR = "atr"
    ATS = "ats"
    ATT = "att"
    ATU = "atu"
    ATV = "atv"
    ATW = "atw"
    ATX = "atx"
    ATY = "aty"
    ATZ = "atz"
    AUA = "aua"
    AUB = "aub"
    AUC = "auc"
    AUD = "aud"
    AUG = "aug"
    AUH = "auh"
    AUI = "aui"
    AUJ = "auj"
    AUK = "auk"
    AUL = "aul"
    AUM = "aum"
    AUN = "aun"
    AUO = "auo"
    AUP = "aup"
    AUQ = "auq"
    AUR = "aur"
    AUT = "aut"
    AUU = "auu"
    AUW = "auw"
    AUX = "aux"
    AUY = "auy"
    AUZ = "auz"
    AVA = "ava"
    AVB = "avb"
    AVD = "avd"
    AVE = "ave"
    AVI = "avi"
    AVL = "avl"
    AVM = "avm"
    AVN = "avn"
    AVO = "avo"
    AVS = "avs"
    AVT = "avt"
    AVU = "avu"
    AVV = "avv"
    AWA = "awa"
    AWB = "awb"
    AWC = "awc"
    AWE = "awe"
    AWG = "awg"
    AWH = "awh"
    AWI = "awi"
    AWK = "awk"
    AWM = "awm"
    AWN = "awn"
    AWO = "awo"
    AWR = "awr"
    AWS = "aws"
    AWT = "awt"
    AWU = "awu"
    AWV = "awv"
    AWW = "aww"
    AWX = "awx"
    AWY = "awy"
    AXB = "axb"
    AXE = "axe"
    AXG = "axg"
    AXK = "axk"
    AXL = "axl"
    AXX = "axx"
    AYA = "aya"
    AYB = "ayb"
    AYC = "ayc"
    AYD = "ayd"
    AYE = "aye"
    AYG = "ayg"
    AYH = "ayh"
    AYI = "ayi"
    AYK = "ayk"
    AYL = "ayl"
    AYN = "ayn"
    AYO = "ayo"
    AYP = "ayp"
    AYQ = "ayq"
    AYR = "ayr"
    AYS = "ays"
    AYT = "ayt"
    AYU = "ayu"
    AYZ = "ayz"
    AZA = "aza"
    AZB = "azb"
    AZD = "azd"
    AZG = "azg"
    AZJ = "azj"
    AZM = "azm"
    AZN = "azn"
    AZO = "azo"
    AZT = "azt"
    AZZ = "azz"
    BAA = "baa"
    BAB = "bab"
    BAC = "bac"
    BAE = "bae"
    BAF = "baf"
    BAG = "bag"
    BAH = "bah"
    BAJ = "baj"
    BAK = "bak"
    BAM = "bam"
    BAN = "ban"
    BAO = "bao"
    BAP = "bap"
    BAR = "bar"
    BAS = "bas"
    BAU = "bau"
    BAV = "bav"
    BAW = "baw"
    BAX = "bax"
    BAY = "bay"
    BBA = "bba"
    BBB = "bbb"
    BBC = "bbc"
    BBD = "bbd"
    BBE = "bbe"
    BBF = "bbf"
    BBG = "bbg"
    BBH = "bbh"
    BBI = "bbi"
    BBJ = "bbj"
    BBK = "bbk"
    BBL = "bbl"
    BBM = "bbm"
    BBN = "bbn"
    BBO = "bbo"
    BBP = "bbp"
    BBQ = "bbq"
    BBR = "bbr"
    BBS = "bbs"
    BBT = "bbt"
    BBU = "bbu"
    BBV = "bbv"
    BBW = "bbw"
    BBX = "bbx"
    BBY = "bby"
    BCA = "bca"
    BCB = "bcb"
    BCC = "bcc"
    BCD = "bcd"
    BCE = "bce"
    BCF = "bcf"
    BCG = "bcg"
    BCH = "bch"
    BCI = "bci"
    BCJ = "bcj"
    BCK = "bck"
    BCL = "bcl"
    BCM = "bcm"
    BCN = "bcn"
    BCO = "bco"
    BCP = "bcp"
    BCQ = "bcq"
    BCR = "bcr"
    BCS = "bcs"
    BCT = "bct"
    BCU = "bcu"
    BCV = "bcv"
    BCW = "bcw"
    BCY = "bcy"
    BCZ = "bcz"
    BDA = "bda"
    BDB = "bdb"
    BDC = "bdc"
    BDD = "bdd"
    BDE = "bde"
    BDF = "bdf"
    BDG = "bdg"
    BDH = "bdh"
    BDI = "bdi"
    BDJ = "bdj"
    BDK = "bdk"
    BDL = "bdl"
    BDM = "bdm"
    BDN = "bdn"
    BDO = "bdo"
    BDP = "bdp"
    BDQ = "bdq"
    BDR = "bdr"
    BDS = "bds"
    BDT = "bdt"
    BDU = "bdu"
    BDV = "bdv"
    BDW = "bdw"
    BDX = "bdx"
    BDY = "bdy"
    BDZ = "bdz"
    BEA = "bea"
    BEB = "beb"
    BEC = "bec"
    BED = "bed"
    BEE = "bee"
    BEF = "bef"
    BEG = "beg"
    BEH = "beh"
    BEI = "bei"
    BEJ = "bej"
    BEK = "bek"
    BEL = "bel"
    BEM = "bem"
    BEN = "ben"
    BEO = "beo"
    BEP = "bep"
    BEQ = "beq"
    BES = "bes"
    BET = "bet"
    BEU = "beu"
    BEV = "bev"
    BEW = "bew"
    BEX = "bex"
    BEY = "bey"
    BEZ = "bez"
    BFA = "bfa"
    BFB = "bfb"
    BFC = "bfc"
    BFD = "bfd"
    BFE = "bfe"
    BFF = "bff"
    BFG = "bfg"
    BFH = "bfh"
    BFI = "bfi"
    BFJ = "bfj"
    BFK = "bfk"
    BFL = "bfl"
    BFM = "bfm"
    BFN = "bfn"
    BFO = "bfo"
    BFP = "bfp"
    BFQ = "bfq"
    BFR = "bfr"
    BFS = "bfs"
    BFT = "bft"
    BFU = "bfu"
    BFW = "bfw"
    BFX = "bfx"
    BFY = "bfy"
    BFZ = "bfz"
    BGA = "bga"
    BGB = "bgb"
    BGC = "bgc"
    BGD = "bgd"
    BGE = "bge"
    BGF = "bgf"
    BGG = "bgg"
    BGI = "bgi"
    BGJ = "bgj"
    BGK = "bgk"
    BGL = "bgl"
    BGN = "bgn"
    BGO = "bgo"
    BGP = "bgp"
    BGQ = "bgq"
    BGR = "bgr"
    BGS = "bgs"
    BGT = "bgt"
    BGU = "bgu"
    BGV = "bgv"
    BGW = "bgw"
    BGX = "bgx"
    BGY = "bgy"
    BGZ = "bgz"
    BHA = "bha"
    BHB = "bhb"
    BHC = "bhc"
    BHD = "bhd"
    BHE = "bhe"
    BHF = "bhf"
    BHG = "bhg"
    BHH = "bhh"
    BHI = "bhi"
    BHJ = "bhj"
    BHL = "bhl"
    BHM = "bhm"
    BHN = "bhn"
    BHO = "bho"
    BHP = "bhp"
    BHQ = "bhq"
    BHR = "bhr"
    BHS = "bhs"
    BHT = "bht"
    BHU = "bhu"
    BHV = "bhv"
    BHW = "bhw"
    BHX = "bhx"
    BHY = "bhy"
    BHZ = "bhz"
    BIA = "bia"
    BIB = "bib"
    BID = "bid"
    BIE = "bie"
    BIF = "bif"
    BIG = "big"
    BIL = "bil"
    BIM = "bim"
    BIN = "bin"
    BIO = "bio"
    BIP = "bip"
    BIQ = "biq"
    BIR = "bir"
    BIS = "bis"
    BIT = "bit"
    BIU = "biu"
    BIV = "biv"
    BIW = "biw"
    BIX = "bix"
    BIY = "biy"
    BIZ = "biz"
    BJA = "bja"
    BJB = "bjb"
    BJC = "bjc"
    BJE = "bje"
    BJF = "bjf"
    BJG = "bjg"
    BJH = "bjh"
    BJI = "bji"
    BJJ = "bjj"
    BJK = "bjk"
    BJL = "bjl"
    BJM = "bjm"
    BJN = "bjn"
    BJO = "bjo"
    BJP = "bjp"
    BJR = "bjr"
    BJS = "bjs"
    BJT = "bjt"
    BJU = "bju"
    BJV = "bjv"
    BJW = "bjw"
    BJX = "bjx"
    BJY = "bjy"
    BJZ = "bjz"
    BKA = "bka"
    BKC = "bkc"
    BKD = "bkd"
    BKF = "bkf"
    BKG = "bkg"
    BKH = "bkh"
    BKI = "bki"
    BKJ = "bkj"
    BKK = "bkk"
    BKL = "bkl"
    BKM = "bkm"
    BKN = "bkn"
    BKO = "bko"
    BKP = "bkp"
    BKQ = "bkq"
    BKR = "bkr"
    BKS = "bks"
    BKT = "bkt"
    BKU = "bku"
    BKV = "bkv"
    BKW = "bkw"
    BKX = "bkx"
    BKY = "bky"
    BKZ = "bkz"
    BLA = "bla"
    BLB = "blb"
    BLC = "blc"
    BLD = "bld"
    BLE = "ble"
    BLF = "blf"
    BLH = "blh"
    BLI = "bli"
    BLJ = "blj"
    BLK = "blk"
    BLL = "bll"
    BLM = "blm"
    BLN = "bln"
    BLO = "blo"
    BLP = "blp"
    BLQ = "blq"
    BLR = "blr"
    BLS = "bls"
    BLT = "blt"
    BLV = "blv"
    BLW = "blw"
    BLX = "blx"
    BLY = "bly"
    BLZ = "blz"
    BMA = "bma"
    BMB = "bmb"
    BMC = "bmc"
    BMD = "bmd"
    BME = "bme"
    BMF = "bmf"
    BMG = "bmg"
    BMH = "bmh"
    BMI = "bmi"
    BMJ = "bmj"
    BMK = "bmk"
    BML = "bml"
    BMM = "bmm"
    BMN = "bmn"
    BMO = "bmo"
    BMP = "bmp"
    BMQ = "bmq"
    BMR = "bmr"
    BMS = "bms"
    BMT = "bmt"
    BMU = "bmu"
    BMV = "bmv"
    BMW = "bmw"
    BMX = "bmx"
    BMZ = "bmz"
    BNA = "bna"
    BNB = "bnb"
    BND = "bnd"
    BNE = "bne"
    BNF = "bnf"
    BNG = "bng"
    BNI = "bni"
    BNJ = "bnj"
    BNK = "bnk"
    BNL = "bnl"
    BNM = "bnm"
    BNN = "bnn"
    BNO = "bno"
    BNP = "bnp"
    BNQ = "bnq"
    BNR = "bnr"
    BNS = "bns"
    BNU = "bnu"
    BNV = "bnv"
    BNW = "bnw"
    BNX = "bnx"
    BNY = "bny"
    BNZ = "bnz"
    BOA = "boa"
    BOB = "bob"
    BOD = "bod"
    BOE = "boe"
    BOF = "bof"
    BOG = "bog"
    BOH = "boh"
    BOI = "boi"
    BOJ = "boj"
    BOK = "bok"
    BOL = "bol"
    BOM = "bom"
    BON = "bon"
    BOO = "boo"
    BOP = "bop"
    BOQ = "boq"
    BOR = "bor"
    BOS = "bos"
    BOT = "bot"
    BOU = "bou"
    BOV = "bov"
    BOW = "bow"
    BOX = "box"
    BOY = "boy"
    BOZ = "boz"
    BPA = "bpa"
    BPC = "bpc"
    BPD = "bpd"
    BPE = "bpe"
    BPG = "bpg"
    BPH = "bph"
    BPI = "bpi"
    BPJ = "bpj"
    BPK = "bpk"
    BPL = "bpl"
    BPM = "bpm"
    BPN = "bpn"
    BPO = "bpo"
    BPP = "bpp"
    BPQ = "bpq"
    BPR = "bpr"
    BPS = "bps"
    BPT = "bpt"
    BPU = "bpu"
    BPV = "bpv"
    BPW = "bpw"
    BPX = "bpx"
    BPY = "bpy"
    BPZ = "bpz"
    BQA = "bqa"
    BQB = "bqb"
    BQC = "bqc"
    BQD = "bqd"
    BQF = "bqf"
    BQG = "bqg"
    BQH = "bqh"
    BQI = "bqi"
    BQJ = "bqj"
    BQK = "bqk"
    BQL = "bql"
    BQM = "bqm"
    BQN = "bqn"
    BQO = "bqo"
    BQP = "bqp"
    BQQ = "bqq"
    BQR = "bqr"
    BQS = "bqs"
    BQT = "bqt"
    BQU = "bqu"
    BQV = "bqv"
    BQW = "bqw"
    BQX = "bqx"
    BQY = "bqy"
    BQZ = "bqz"
    BRA = "bra"
    BRB = "brb"
    BRC = "brc"
    BRD = "brd"
    BRE = "bre"
    BRF = "brf"
    BRG = "brg"
    BRH = "brh"
    BRI = "bri"
    BRJ = "brj"
    BRK = "brk"
    BRL = "brl"
    BRM = "brm"
    BRN = "brn"
    BRO = "bro"
    BRP = "brp"
    BRQ = "brq"
    BRR = "brr"
    BRS = "brs"
    BRT = "brt"
    BRU = "bru"
    BRV = "brv"
    BRW = "brw"
    BRX = "brx"
    BRY = "bry"
    BRZ = "brz"
    BSA = "bsa"
    BSB = "bsb"
    BSC = "bsc"
    BSE = "bse"
    BSF = "bsf"
    BSG = "bsg"
    BSH = "bsh"
    BSI = "bsi"
    BSJ = "bsj"
    BSK = "bsk"
    BSL = "bsl"
    BSM = "bsm"
    BSN = "bsn"
    BSO = "bso"
    BSP = "bsp"
    BSQ = "bsq"
    BSR = "bsr"
    BSS = "bss"
    BST = "bst"
    BSU = "bsu"
    BSV = "bsv"
    BSW = "bsw"
    BSX = "bsx"
    BSY = "bsy"
    BTA = "bta"
    BTC = "btc"
    BTD = "btd"
    BTE = "bte"
    BTF = "btf"
    BTG = "btg"
    BTH = "bth"
    BTI = "bti"
    BTJ = "btj"
    BTM = "btm"
    BTN = "btn"
    BTO = "bto"
    BTP = "btp"
    BTQ = "btq"
    BTR = "btr"
    BTS = "bts"
    BTT = "btt"
    BTU = "btu"
    BTV = "btv"
    BTW = "btw"
    BTX = "btx"
    BTY = "bty"
    BTZ = "btz"
    BUB = "bub"
    BUC = "buc"
    BUD = "bud"
    BUE = "bue"
    BUF = "buf"
    BUG = "bug"
    BUH = "buh"
    BUI = "bui"
    BUJ = "buj"
    BUK = "buk"
    BUL = "bul"
    BUM = "bum"
    BUN = "bun"
    BUO = "buo"
    BUP = "bup"
    BUQ = "buq"
    BUS = "bus"
    BUT = "but"
    BUU = "buu"
    BUV = "buv"
    BUW = "buw"
    BUX = "bux"
    BUY = "buy"
    BUZ = "buz"
    BVA = "bva"
    BVB = "bvb"
    BVC = "bvc"
    BVD = "bvd"
    BVE = "bve"
    BVF = "bvf"
    BVG = "bvg"
    BVH = "bvh"
    BVI = "bvi"
    BVJ = "bvj"
    BVK = "bvk"
    BVL = "bvl"
    BVM = "bvm"
    BVN = "bvn"
    BVO = "bvo"
    BVP = "bvp"
    BVQ = "bvq"
    BVR = "bvr"
    BVT = "bvt"
    BVU = "bvu"
    BVV = "bvv"
    BVW = "bvw"
    BVX = "bvx"
    BVY = "bvy"
    BVZ = "bvz"
    BWA = "bwa"
    BWB = "bwb"
    BWC = "bwc"
    BWD = "bwd"
    BWE = "bwe"
    BWF = "bwf"
    BWG = "bwg"
    BWH = "bwh"
    BWI = "bwi"
    BWJ = "bwj"
    BWK = "bwk"
    BWL = "bwl"
    BWM = "bwm"
    BWN = "bwn"
    BWO = "bwo"
    BWP = "bwp"
    BWQ = "bwq"
    BWR = "bwr"
    BWS = "bws"
    BWT = "bwt"
    BWU = "bwu"
    BWW = "bww"
    BWX = "bwx"
    BWY = "bwy"
    BWZ = "bwz"
    BXA = "bxa"
    BXB = "bxb"
    BXC = "bxc"
    BXD = "bxd"
    BXE = "bxe"
    BXF = "bxf"
    BXG = "bxg"
    BXH = "bxh"
    BXI = "bxi"
    BXJ = "bxj"
    BXK = "bxk"
    BXL = "bxl"
    BXM = "bxm"
    BXN = "bxn"
    BXO = "bxo"
    BXP = "bxp"
    BXQ = "bxq"
    BXR = "bxr"
    BXS = "bxs"
    BXU = "bxu"
    BXV = "bxv"
    BXW = "bxw"
    BXZ = "bxz"
    BYA = "bya"
    BYB = "byb"
    BYC = "byc"
    BYD = "byd"
    BYE = "bye"
    BYF = "byf"
    BYG = "byg"
    BYH = "byh"
    BYI = "byi"
    BYJ = "byj"
    BYK = "byk"
    BYL = "byl"
    BYM = "bym"
    BYN = "byn"
    BYO = "byo"
    BYP = "byp"
    BYQ = "byq"
    BYR = "byr"
    BYS = "bys"
    BYT = "byt"
    BYV = "byv"
    BYW = "byw"
    BYX = "byx"
    BYZ = "byz"
    BZA = "bza"
    BZB = "bzb"
    BZC = "bzc"
    BZD = "bzd"
    BZE = "bze"
    BZF = "bzf"
    BZG = "bzg"
    BZH = "bzh"
    BZI = "bzi"
    BZJ = "bzj"
    BZK = "bzk"
    BZL = "bzl"
    BZM = "bzm"
    BZN = "bzn"
    BZO = "bzo"
    BZP = "bzp"
    BZQ = "bzq"
    BZR = "bzr"
    BZS = "bzs"
    BZU = "bzu"
    BZV = "bzv"
    BZW = "bzw"
    BZX = "bzx"
    BZY = "bzy"
    BZZ = "bzz"
    CAA = "caa"
    CAB = "cab"
    CAC = "cac"
    CAD = "cad"
    CAE = "cae"
    CAF = "caf"
    CAG = "cag"
    CAH = "cah"
    CAJ = "caj"
    CAK = "cak"
    CAL = "cal"
    CAM = "cam"
    CAN = "can"
    CAO = "cao"
    CAP = "cap"
    CAQ = "caq"
    CAR = "car"
    CAS = "cas"
    CAT = "cat"
    CAV = "cav"
    CAW = "caw"
    CAX = "cax"
    CAY = "cay"
    CAZ = "caz"
    CBB = "cbb"
    CBC = "cbc"
    CBD = "cbd"
    CBG = "cbg"
    CBI = "cbi"
    CBJ = "cbj"
    CBK = "cbk"
    CBL = "cbl"
    CBN = "cbn"
    CBO = "cbo"
    CBQ = "cbq"
    CBR = "cbr"
    CBS = "cbs"
    CBT = "cbt"
    CBU = "cbu"
    CBV = "cbv"
    CBW = "cbw"
    CBY = "cby"
    CCC = "ccc"
    CCD = "ccd"
    CCE = "cce"
    CCG = "ccg"
    CCH = "cch"
    CCJ = "ccj"
    CCL = "ccl"
    CCM = "ccm"
    CCO = "cco"
    CCP = "ccp"
    CCR = "ccr"
    CDA = "cda"
    CDE = "cde"
    CDF = "cdf"
    CDH = "cdh"
    CDI = "cdi"
    CDJ = "cdj"
    CDM = "cdm"
    CDN = "cdn"
    CDO = "cdo"
    CDR = "cdr"
    CDS = "cds"
    CDY = "cdy"
    CDZ = "cdz"
    CEA = "cea"
    CEB = "ceb"
    CEG = "ceg"
    CEK = "cek"
    CEN = "cen"
    CES = "ces"
    CET = "cet"
    CEY = "cey"
    CFA = "cfa"
    CFD = "cfd"
    CFG = "cfg"
    CFM = "cfm"
    CGA = "cga"
    CGC = "cgc"
    CGG = "cgg"
    CGK = "cgk"
    CHA = "cha"
    CHB = "chb"
    CHC = "chc"
    CHD = "chd"
    CHE = "che"
    CHF = "chf"
    CHG = "chg"
    CHH = "chh"
    CHI = "chi"
    CHJ = "chj"
    CHK = "chk"
    CHL = "chl"
    CHN = "chn"
    CHO = "cho"
    CHP = "chp"
    CHQ = "chq"
    CHR = "chr"
    CHT = "cht"
    CHU = "chu"
    CHV = "chv"
    CHW = "chw"
    CHX = "chx"
    CHY = "chy"
    CHZ = "chz"
    CIA = "cia"
    CIB = "cib"
    CIC = "cic"
    CID = "cid"
    CIE = "cie"
    CIH = "cih"
    CIK = "cik"
    CIM = "cim"
    CIN = "cin"
    CIP = "cip"
    CIR = "cir"
    CIW = "ciw"
    CIY = "ciy"
    CJA = "cja"
    CJE = "cje"
    CJH = "cjh"
    CJI = "cji"
    CJK = "cjk"
    CJM = "cjm"
    CJN = "cjn"
    CJO = "cjo"
    CJP = "cjp"
    CJS = "cjs"
    CJV = "cjv"
    CJY = "cjy"
    CKB = "ckb"
    CKH = "ckh"
    CKL = "ckl"
    CKM = "ckm"
    CKN = "ckn"
    CKO = "cko"
    CKQ = "ckq"
    CKR = "ckr"
    CKS = "cks"
    CKT = "ckt"
    CKU = "cku"
    CKV = "ckv"
    CKX = "ckx"
    CKY = "cky"
    CKZ = "ckz"
    CLA = "cla"
    CLC = "clc"
    CLD = "cld"
    CLE = "cle"
    CLH = "clh"
    CLI = "cli"
    CLJ = "clj"
    CLK = "clk"
    CLL = "cll"
    CLM = "clm"
    CLO = "clo"
    CLT = "clt"
    CLU = "clu"
    CLW = "clw"
    CLY = "cly"
    CMA = "cma"
    CME = "cme"
    CMI = "cmi"
    CML = "cml"
    CMM = "cmm"
    CMN = "cmn"
    CMO = "cmo"
    CMR = "cmr"
    CMT = "cmt"
    CNA = "cna"
    CNB = "cnb"
    CNC = "cnc"
    CNG = "cng"
    CNH = "cnh"
    CNI = "cni"
    CNK = "cnk"
    CNL = "cnl"
    CNO = "cno"
    CNP = "cnp"
    CNQ = "cnq"
    CNR = "cnr"
    CNS = "cns"
    CNT = "cnt"
    CNU = "cnu"
    CNW = "cnw"
    COA = "coa"
    COB = "cob"
    COC = "coc"
    COD = "cod"
    COE = "coe"
    COF = "cof"
    COG = "cog"
    COH = "coh"
    COJ = "coj"
    COK = "cok"
    COL = "col"
    COM = "com"
    CON = "con"
    COO = "coo"
    COP = "cop"
    COQ = "coq"
    COR = "cor"
    COS = "cos"
    COT = "cot"
    COU = "cou"
    COV = "cov"
    COW = "cow"
    COX = "cox"
    COZ = "coz"
    CPA = "cpa"
    CPB = "cpb"
    CPC = "cpc"
    CPG = "cpg"
    CPI = "cpi"
    CPN = "cpn"
    CPO = "cpo"
    CPS = "cps"
    CPU = "cpu"
    CPX = "cpx"
    CPY = "cpy"
    CQD = "cqd"
    CRA = "cra"
    CRB = "crb"
    CRC = "crc"
    CRD = "crd"
    CRF = "crf"
    CRG = "crg"
    CRH = "crh"
    CRI = "cri"
    CRJ = "crj"
    CRK = "crk"
    CRL = "crl"
    CRM = "crm"
    CRN = "crn"
    CRO = "cro"
    CRQ = "crq"
    CRR = "crr"
    CRS = "crs"
    CRT = "crt"
    CRV = "crv"
    CRW = "crw"
    CRX = "crx"
    CRY = "cry"
    CRZ = "crz"
    CSA = "csa"
    CSB = "csb"
    CSC = "csc"
    CSD = "csd"
    CSE = "cse"
    CSF = "csf"
    CSG = "csg"
    CSH = "csh"
    CSI = "csi"
    CSJ = "csj"
    CSK = "csk"
    CSL = "csl"
    CSM = "csm"
    CSN = "csn"
    CSO = "cso"
    CSP = "csp"
    CSQ = "csq"
    CSR = "csr"
    CSS = "css"
    CST = "cst"
    CSV = "csv"
    CSW = "csw"
    CSX = "csx"
    CSY = "csy"
    CSZ = "csz"
    CTA = "cta"
    CTC = "ctc"
    CTD = "ctd"
    CTE = "cte"
    CTG = "ctg"
    CTH = "cth"
    CTL = "ctl"
    CTM = "ctm"
    CTN = "ctn"
    CTO = "cto"
    CTP = "ctp"
    CTS = "cts"
    CTT = "ctt"
    CTU = "ctu"
    CTY = "cty"
    CTZ = "ctz"
    CUA = "cua"
    CUB = "cub"
    CUC = "cuc"
    CUH = "cuh"
    CUI = "cui"
    CUJ = "cuj"
    CUK = "cuk"
    CUL = "cul"
    CUO = "cuo"
    CUP = "cup"
    CUQ = "cuq"
    CUR = "cur"
    CUT = "cut"
    CUU = "cuu"
    CUV = "cuv"
    CUW = "cuw"
    CUX = "cux"
    CUY = "cuy"
    CVG = "cvg"
    CVN = "cvn"
    CWA = "cwa"
    CWB = "cwb"
    CWD = "cwd"
    CWE = "cwe"
    CWG = "cwg"
    CWT = "cwt"
    CXH = "cxh"
    CYA = "cya"
    CYB = "cyb"
    CYM = "cym"
    CYO = "cyo"
    CZH = "czh"
    CZK = "czk"
    CZN = "czn"
    CZO = "czo"
    CZT = "czt"
    DAA = "daa"
    DAC = "dac"
    DAD = "dad"
    DAE = "dae"
    DAG = "dag"
    DAH = "dah"
    DAI = "dai"
    DAJ = "daj"
    DAK = "dak"
    DAL = "dal"
    DAM = "dam"
    DAN = "dan"
    DAO = "dao"
    DAQ = "daq"
    DAR = "dar"
    DAS = "das"
    DAU = "dau"
    DAV = "dav"
    DAW = "daw"
    DAX = "dax"
    DAZ = "daz"
    DBA = "dba"
    DBB = "dbb"
    DBD = "dbd"
    DBE = "dbe"
    DBF = "dbf"
    DBG = "dbg"
    DBI = "dbi"
    DBJ = "dbj"
    DBL = "dbl"
    DBM = "dbm"
    DBN = "dbn"
    DBO = "dbo"
    DBP = "dbp"
    DBQ = "dbq"
    DBR = "dbr"
    DBT = "dbt"
    DBU = "dbu"
    DBV = "dbv"
    DBW = "dbw"
    DBY = "dby"
    DCC = "dcc"
    DCR = "dcr"
    DDA = "dda"
    DDD = "ddd"
    DDE = "dde"
    DDG = "ddg"
    DDI = "ddi"
    DDJ = "ddj"
    DDN = "ddn"
    DDO = "ddo"
    DDR = "ddr"
    DDS = "dds"
    DDW = "ddw"
    DEC = "dec"
    DED = "ded"
    DEE = "dee"
    DEF = "def"
    DEG = "deg"
    DEH = "deh"
    DEI = "dei"
    DEM = "dem"
    DEP = "dep"
    DEQ = "deq"
    DER = "der"
    DES = "des"
    DEU = "deu"
    DEV = "dev"
    DEZ = "dez"
    DGA = "dga"
    DGB = "dgb"
    DGC = "dgc"
    DGD = "dgd"
    DGE = "dge"
    DGG = "dgg"
    DGH = "dgh"
    DGI = "dgi"
    DGK = "dgk"
    DGL = "dgl"
    DGN = "dgn"
    DGO = "dgo"
    DGR = "dgr"
    DGS = "dgs"
    DGT = "dgt"
    DGW = "dgw"
    DGX = "dgx"
    DGZ = "dgz"
    DHD = "dhd"
    DHG = "dhg"
    DHI = "dhi"
    DHL = "dhl"
    DHM = "dhm"
    DHN = "dhn"
    DHO = "dho"
    DHR = "dhr"
    DHS = "dhs"
    DHU = "dhu"
    DHV = "dhv"
    DHW = "dhw"
    DHX = "dhx"
    DIA = "dia"
    DIB = "dib"
    DIC = "dic"
    DID = "did"
    DIF = "dif"
    DIG = "dig"
    DIH = "dih"
    DII = "dii"
    DIJ = "dij"
    DIK = "dik"
    DIL = "dil"
    DIM = "dim"
    DIO = "dio"
    DIP = "dip"
    DIQ = "diq"
    DIR = "dir"
    DIS = "dis"
    DIU = "diu"
    DIV = "div"
    DIW = "diw"
    DIX = "dix"
    DIY = "diy"
    DIZ = "diz"
    DJA = "dja"
    DJB = "djb"
    DJC = "djc"
    DJD = "djd"
    DJE = "dje"
    DJF = "djf"
    DJI = "dji"
    DJJ = "djj"
    DJK = "djk"
    DJM = "djm"
    DJN = "djn"
    DJO = "djo"
    DJR = "djr"
    DJU = "dju"
    DJW = "djw"
    DKA = "dka"
    DKG = "dkg"
    DKK = "dkk"
    DKR = "dkr"
    DKS = "dks"
    DKX = "dkx"
    DLG = "dlg"
    DLK = "dlk"
    DLM = "dlm"
    DLN = "dln"
    DMA = "dma"
    DMB = "dmb"
    DMC = "dmc"
    DMD = "dmd"
    DME = "dme"
    DMG = "dmg"
    DMK = "dmk"
    DML = "dml"
    DMM = "dmm"
    DMO = "dmo"
    DMR = "dmr"
    DMS = "dms"
    DMU = "dmu"
    DMV = "dmv"
    DMW = "dmw"
    DMX = "dmx"
    DMY = "dmy"
    DNA = "dna"
    DND = "dnd"
    DNE = "dne"
    DNG = "dng"
    DNI = "dni"
    DNJ = "dnj"
    DNK = "dnk"
    DNN = "dnn"
    DNO = "dno"
    DNR = "dnr"
    DNT = "dnt"
    DNU = "dnu"
    DNV = "dnv"
    DNW = "dnw"
    DNY = "dny"
    DOA = "doa"
    DOB = "dob"
    DOC = "doc"
    DOE = "doe"
    DOF = "dof"
    DOH = "doh"
    DOK = "dok"
    DOL = "dol"
    DON = "don"
    DOO = "doo"
    DOP = "dop"
    DOQ = "doq"
    DOR = "dor"
    DOS = "dos"
    DOT = "dot"
    DOV = "dov"
    DOW = "dow"
    DOX = "dox"
    DOY = "doy"
    DOZ = "doz"
    DPP = "dpp"
    DRB = "drb"
    DRC = "drc"
    DRD = "drd"
    DRE = "dre"
    DRG = "drg"
    DRI = "dri"
    DRL = "drl"
    DRN = "drn"
    DRO = "dro"
    DRQ = "drq"
    DRS = "drs"
    DRT = "drt"
    DRU = "dru"
    DRY = "dry"
    DSB = "dsb"
    DSE = "dse"
    DSH = "dsh"
    DSI = "dsi"
    DSK = "dsk"
    DSL = "dsl"
    DSN = "dsn"
    DSO = "dso"
    DSQ = "dsq"
    DSZ = "dsz"
    DTA = "dta"
    DTB = "dtb"
    DTD = "dtd"
    DTH = "dth"
    DTI = "dti"
    DTK = "dtk"
    DTM = "dtm"
    DTN = "dtn"
    DTO = "dto"
    DTP = "dtp"
    DTR = "dtr"
    DTS = "dts"
    DTT = "dtt"
    DTU = "dtu"
    DTY = "dty"
    DUA = "dua"
    DUB = "dub"
    DUC = "duc"
    DUE = "due"
    DUF = "duf"
    DUG = "dug"
    DUH = "duh"
    DUI = "dui"
    DUK = "duk"
    DUL = "dul"
    DUN = "dun"
    DUO = "duo"
    DUP = "dup"
    DUQ = "duq"
    DUR = "dur"
    DUS = "dus"
    DUU = "duu"
    DUV = "duv"
    DUW = "duw"
    DUX = "dux"
    DUY = "duy"
    DUZ = "duz"
    DVA = "dva"
    DWA = "dwa"
    DWK = "dwk"
    DWR = "dwr"
    DWU = "dwu"
    DWW = "dww"
    DWY = "dwy"
    DWZ = "dwz"
    DYA = "dya"
    DYB = "dyb"
    DYD = "dyd"
    DYG = "dyg"
    DYI = "dyi"
    DYM = "dym"
    DYN = "dyn"
    DYO = "dyo"
    DYR = "dyr"
    DYU = "dyu"
    DYY = "dyy"
    DZA = "dza"
    DZD = "dzd"
    DZE = "dze"
    DZG = "dzg"
    DZL = "dzl"
    DZN = "dzn"
    DZO = "dzo"
    EAA = "eaa"
    EBC = "ebc"
    EBG = "ebg"
    EBK = "ebk"
    EBO = "ebo"
    EBR = "ebr"
    EBU = "ebu"
    ECS = "ecs"
    EEE = "eee"
    EFA = "efa"
    EFE = "efe"
    EFI = "efi"
    EGA = "ega"
    EGL = "egl"
    EGM = "egm"
    EGO = "ego"
    EHS = "ehs"
    EHU = "ehu"
    EIP = "eip"
    EIT = "eit"
    EIV = "eiv"
    EJA = "eja"
    EKA = "eka"
    EKE = "eke"
    EKG = "ekg"
    EKI = "eki"
    EKK = "ekk"
    EKL = "ekl"
    EKM = "ekm"
    EKO = "eko"
    EKP = "ekp"
    EKR = "ekr"
    EKY = "eky"
    ELE = "ele"
    ELH = "elh"
    ELI = "eli"
    ELK = "elk"
    ELL = "ell"
    ELM = "elm"
    ELO = "elo"
    ELU = "elu"
    EMA = "ema"
    EMB = "emb"
    EME = "eme"
    EMG = "emg"
    EMI = "emi"
    EMK = "emk"
    EMM = "emm"
    EMN = "emn"
    EMP = "emp"
    EMQ = "emq"
    EMS = "ems"
    EMU = "emu"
    EMW = "emw"
    EMX = "emx"
    EMZ = "emz"
    ENA = "ena"
    ENB = "enb"
    ENC = "enc"
    END = "end"
    ENF = "enf"
    ENG = "eng"
    ENH = "enh"
    ENL = "enl"
    ENN = "enn"
    ENO = "eno"
    ENQ = "enq"
    ENR = "enr"
    ENU = "enu"
    ENV = "env"
    ENW = "enw"
    ENX = "enx"
    EOT = "eot"
    EPI = "epi"
    EPO = "epo"
    ERA = "era"
    ERG = "erg"
    ERH = "erh"
    ERI = "eri"
    ERK = "erk"
    ERO = "ero"
    ERR = "err"
    ERS = "ers"
    ERT = "ert"
    ERW = "erw"
    ESE = "ese"
    ESG = "esg"
    ESH = "esh"
    ESI = "esi"
    ESK = "esk"
    ESL = "esl"
    ESM = "esm"
    ESN = "esn"
    ESO = "eso"
    ESQ = "esq"
    ESS = "ess"
    ESU = "esu"
    ESY = "esy"
    ETB = "etb"
    ETC = "etc"
    ETH = "eth"
    ETN = "etn"
    ETO = "eto"
    ETR = "etr"
    ETS = "ets"
    ETU = "etu"
    ETX = "etx"
    ETZ = "etz"
    EUD = "eud"
    EUS = "eus"
    EVE = "eve"
    EVH = "evh"
    EVN = "evn"
    EWE = "ewe"
    EWO = "ewo"
    EXT = "ext"
    EYA = "eya"
    EYO = "eyo"
    EZA = "eza"
    EZE = "eze"
    FAA = "faa"
    FAB = "fab"
    FAD = "fad"
    FAF = "faf"
    FAG = "fag"
    FAH = "fah"
    FAI = "fai"
    FAJ = "faj"
    FAK = "fak"
    FAL = "fal"
    FAM = "fam"
    FAN = "fan"
    FAO = "fao"
    FAP = "fap"
    FAR = "far"
    FAU = "fau"
    FAX = "fax"
    FAY = "fay"
    FBL = "fbl"
    FCS = "fcs"
    FER = "fer"
    FFI = "ffi"
    FFM = "ffm"
    FGR = "fgr"
    FIA = "fia"
    FIE = "fie"
    FIF = "fif"
    FIJ = "fij"
    FIL = "fil"
    FIN = "fin"
    FIP = "fip"
    FIR = "fir"
    FIT = "fit"
    FIW = "fiw"
    FKK = "fkk"
    FKV = "fkv"
    FLA = "fla"
    FLH = "flh"
    FLI = "fli"
    FLL = "fll"
    FLN = "fln"
    FLR = "flr"
    FLY = "fly"
    FMP = "fmp"
    FMU = "fmu"
    FNB = "fnb"
    FNG = "fng"
    FNI = "fni"
    FOD = "fod"
    FOI = "foi"
    FOM = "fom"
    FON = "fon"
    FOR = "for"
    FOS = "fos"
    FPE = "fpe"
    FQS = "fqs"
    FRA = "fra"
    FRC = "frc"
    FRD = "frd"
    FRP = "frp"
    FRQ = "frq"
    FRR = "frr"
    FRS = "frs"
    FRT = "frt"
    FRY = "fry"
    FSE = "fse"
    FSL = "fsl"
    FSS = "fss"
    FUB = "fub"
    FUC = "fuc"
    FUD = "fud"
    FUE = "fue"
    FUF = "fuf"
    FUH = "fuh"
    FUI = "fui"
    FUJ = "fuj"
    FUM = "fum"
    FUN = "fun"
    FUQ = "fuq"
    FUR = "fur"
    FUT = "fut"
    FUU = "fuu"
    FUV = "fuv"
    FUY = "fuy"
    FVR = "fvr"
    FWA = "fwa"
    FWE = "fwe"
    GAA = "gaa"
    GAB = "gab"
    GAC = "gac"
    GAD = "gad"
    GAE = "gae"
    GAF = "gaf"
    GAG = "gag"
    GAH = "gah"
    GAI = "gai"
    GAJ = "gaj"
    GAK = "gak"
    GAL = "gal"
    GAM = "gam"
    GAN = "gan"
    GAO = "gao"
    GAP = "gap"
    GAQ = "gaq"
    GAR = "gar"
    GAS = "gas"
    GAT = "gat"
    GAU = "gau"
    GAW = "gaw"
    GAX = "gax"
    GAY = "gay"
    GAZ = "gaz"
    GBB = "gbb"
    GBD = "gbd"
    GBE = "gbe"
    GBF = "gbf"
    GBG = "gbg"
    GBH = "gbh"
    GBI = "gbi"
    GBJ = "gbj"
    GBK = "gbk"
    GBL = "gbl"
    GBM = "gbm"
    GBN = "gbn"
    GBO = "gbo"
    GBP = "gbp"
    GBQ = "gbq"
    GBR = "gbr"
    GBS = "gbs"
    GBU = "gbu"
    GBV = "gbv"
    GBW = "gbw"
    GBX = "gbx"
    GBY = "gby"
    GBZ = "gbz"
    GCC = "gcc"
    GCD = "gcd"
    GCE = "gce"
    GCF = "gcf"
    GCL = "gcl"
    GCN = "gcn"
    GCR = "gcr"
    GCT = "gct"
    GDA = "gda"
    GDB = "gdb"
    GDC = "gdc"
    GDD = "gdd"
    GDE = "gde"
    GDF = "gdf"
    GDG = "gdg"
    GDH = "gdh"
    GDI = "gdi"
    GDJ = "gdj"
    GDK = "gdk"
    GDL = "gdl"
    GDM = "gdm"
    GDN = "gdn"
    GDO = "gdo"
    GDQ = "gdq"
    GDR = "gdr"
    GDS = "gds"
    GDT = "gdt"
    GDU = "gdu"
    GDX = "gdx"
    GEA = "gea"
    GEB = "geb"
    GEC = "gec"
    GED = "ged"
    GEF = "gef"
    GEG = "geg"
    GEH = "geh"
    GEI = "gei"
    GEJ = "gej"
    GEK = "gek"
    GEL = "gel"
    GEQ = "geq"
    GES = "ges"
    GEV = "gev"
    GEW = "gew"
    GEX = "gex"
    GEY = "gey"
    GEZ = "gez"
    GFK = "gfk"
    GFT = "gft"
    GGA = "gga"
    GGB = "ggb"
    GGD = "ggd"
    GGE = "gge"
    GGG = "ggg"
    GGK = "ggk"
    GGL = "ggl"
    GGT = "ggt"
    GGU = "ggu"
    GGW = "ggw"
    GHA = "gha"
    GHE = "ghe"
    GHH = "ghh"
    GHK = "ghk"
    GHL = "ghl"
    GHN = "ghn"
    GHO = "gho"
    GHR = "ghr"
    GHS = "ghs"
    GHT = "ght"
    GIA = "gia"
    GIB = "gib"
    GIC = "gic"
    GID = "gid"
    GIE = "gie"
    GIG = "gig"
    GIH = "gih"
    GII = "gii"
    GIL = "gil"
    GIM = "gim"
    GIN = "gin"
    GIP = "gip"
    GIQ = "giq"
    GIR = "gir"
    GIS = "gis"
    GIT = "git"
    GIU = "giu"
    GIW = "giw"
    GIX = "gix"
    GIY = "giy"
    GIZ = "giz"
    GJK = "gjk"
    GJM = "gjm"
    GJN = "gjn"
    GJR = "gjr"
    GJU = "gju"
    GKA = "gka"
    GKD = "gkd"
    GKE = "gke"
    GKN = "gkn"
    GKO = "gko"
    GKP = "gkp"
    GKU = "gku"
    GLA = "gla"
    GLB = "glb"
    GLC = "glc"
    GLD = "gld"
    GLE = "gle"
    GLG = "glg"
    GLH = "glh"
    GLJ = "glj"
    GLK = "glk"
    GLL = "gll"
    GLO = "glo"
    GLR = "glr"
    GLU = "glu"
    GLV = "glv"
    GLW = "glw"
    GLY = "gly"
    GMA = "gma"
    GMB = "gmb"
    GMD = "gmd"
    GMG = "gmg"
    GMM = "gmm"
    GMN = "gmn"
    GMR = "gmr"
    GMU = "gmu"
    GMV = "gmv"
    GMX = "gmx"
    GMZ = "gmz"
    GNA = "gna"
    GNB = "gnb"
    GNC = "gnc"
    GND = "gnd"
    GNE = "gne"
    GNG = "gng"
    GNH = "gnh"
    GNI = "gni"
    GNJ = "gnj"
    GNK = "gnk"
    GNL = "gnl"
    GNM = "gnm"
    GNN = "gnn"
    GNO = "gno"
    GNQ = "gnq"
    GNR = "gnr"
    GNT = "gnt"
    GNU = "gnu"
    GNW = "gnw"
    GNZ = "gnz"
    GOA = "goa"
    GOB = "gob"
    GOC = "goc"
    GOD = "god"
    GOE = "goe"
    GOF = "gof"
    GOG = "gog"
    GOI = "goi"
    GOJ = "goj"
    GOK = "gok"
    GOL = "gol"
    GOM = "gom"
    GOO = "goo"
    GOP = "gop"
    GOQ = "goq"
    GOR = "gor"
    GOS = "gos"
    GOU = "gou"
    GOV = "gov"
    GOW = "gow"
    GOX = "gox"
    GOY = "goy"
    GOZ = "goz"
    GPA = "gpa"
    GPE = "gpe"
    GPN = "gpn"
    GQA = "gqa"
    GQI = "gqi"
    GQN = "gqn"
    GQR = "gqr"
    GQU = "gqu"
    GRA = "gra"
    GRC = "grc"
    GRD = "grd"
    GRG = "grg"
    GRH = "grh"
    GRI = "gri"
    GRJ = "grj"
    GRM = "grm"
    GRO = "gro"
    GRQ = "grq"
    GRR = "grr"
    GRS = "grs"
    GRT = "grt"
    GRU = "gru"
    GRV = "grv"
    GRW = "grw"
    GRX = "grx"
    GRY = "gry"
    GRZ = "grz"
    GSE = "gse"
    GSG = "gsg"
    GSL = "gsl"
    GSM = "gsm"
    GSN = "gsn"
    GSO = "gso"
    GSP = "gsp"
    GSS = "gss"
    GSW = "gsw"
    GTA = "gta"
    GTU = "gtu"
    GUA = "gua"
    GUB = "gub"
    GUC = "guc"
    GUD = "gud"
    GUE = "gue"
    GUF = "guf"
    GUG = "gug"
    GUH = "guh"
    GUI = "gui"
    GUJ = "guj"
    GUK = "guk"
    GUL = "gul"
    GUM = "gum"
    GUN = "gun"
    GUO = "guo"
    GUP = "gup"
    GUQ = "guq"
    GUR = "gur"
    GUS = "gus"
    GUT = "gut"
    GUU = "guu"
    GUW = "guw"
    GUX = "gux"
    GUZ = "guz"
    GVA = "gva"
    GVC = "gvc"
    GVE = "gve"
    GVF = "gvf"
    GVJ = "gvj"
    GVL = "gvl"
    GVM = "gvm"
    GVN = "gvn"
    GVO = "gvo"
    GVP = "gvp"
    GVR = "gvr"
    GVS = "gvs"
    GVY = "gvy"
    GWA = "gwa"
    GWB = "gwb"
    GWC = "gwc"
    GWD = "gwd"
    GWE = "gwe"
    GWF = "gwf"
    GWG = "gwg"
    GWI = "gwi"
    GWJ = "gwj"
    GWM = "gwm"
    GWN = "gwn"
    GWR = "gwr"
    GWT = "gwt"
    GWU = "gwu"
    GWW = "gww"
    GWX = "gwx"
    GXX = "gxx"
    GYA = "gya"
    GYB = "gyb"
    GYD = "gyd"
    GYE = "gye"
    GYF = "gyf"
    GYG = "gyg"
    GYI = "gyi"
    GYL = "gyl"
    GYM = "gym"
    GYN = "gyn"
    GYO = "gyo"
    GYR = "gyr"
    GYY = "gyy"
    GYZ = "gyz"
    GZA = "gza"
    GZI = "gzi"
    GZN = "gzn"
    HAA = "haa"
    HAB = "hab"
    HAC = "hac"
    HAD = "had"
    HAE = "hae"
    HAF = "haf"
    HAG = "hag"
    HAH = "hah"
    HAJ = "haj"
    HAK = "hak"
    HAL = "hal"
    HAM = "ham"
    HAN = "han"
    HAO = "hao"
    HAP = "hap"
    HAQ = "haq"
    HAR = "har"
    HAS = "has"
    HAT = "hat"
    HAU = "hau"
    HAV = "hav"
    HAW = "haw"
    HAX = "hax"
    HAY = "hay"
    HAZ = "haz"
    HBA = "hba"
    HBB = "hbb"
    HBN = "hbn"
    HBO = "hbo"
    HBU = "hbu"
    HCA = "hca"
    HCH = "hch"
    HDN = "hdn"
    HDS = "hds"
    HDY = "hdy"
    HEA = "hea"
    HEB = "heb"
    HED = "hed"
    HEG = "heg"
    HEH = "heh"
    HEI = "hei"
    HEM = "hem"
    HER = "her"
    HGM = "hgm"
    HGW = "hgw"
    HHI = "hhi"
    HHR = "hhr"
    HHY = "hhy"
    HIA = "hia"
    HIB = "hib"
    HID = "hid"
    HIF = "hif"
    HIG = "hig"
    HIH = "hih"
    HII = "hii"
    HIJ = "hij"
    HIK = "hik"
    HIL = "hil"
    HIN = "hin"
    HIO = "hio"
    HIR = "hir"
    HIW = "hiw"
    HIX = "hix"
    HJI = "hji"
    HKA = "hka"
    HKE = "hke"
    HKH = "hkh"
    HKK = "hkk"
    HKN = "hkn"
    HKS = "hks"
    HLA = "hla"
    HLB = "hlb"
    HLD = "hld"
    HLE = "hle"
    HLT = "hlt"
    HMA = "hma"
    HMB = "hmb"
    HMC = "hmc"
    HMD = "hmd"
    HME = "hme"
    HMF = "hmf"
    HMG = "hmg"
    HMH = "hmh"
    HMI = "hmi"
    HMJ = "hmj"
    HML = "hml"
    HMM = "hmm"
    HMO = "hmo"
    HMP = "hmp"
    HMQ = "hmq"
    HMR = "hmr"
    HMS = "hms"
    HMT = "hmt"
    HMU = "hmu"
    HMV = "hmv"
    HMW = "hmw"
    HMY = "hmy"
    HMZ = "hmz"
    HNA = "hna"
    HND = "hnd"
    HNE = "hne"
    HNG = "hng"
    HNH = "hnh"
    HNI = "hni"
    HNJ = "hnj"
    HNM = "hnm"
    HNN = "hnn"
    HNO = "hno"
    HNS = "hns"
    HNU = "hnu"
    HOA = "hoa"
    HOB = "hob"
    HOC = "hoc"
    HOD = "hod"
    HOE = "hoe"
    HOH = "hoh"
    HOI = "hoi"
    HOJ = "hoj"
    HOL = "hol"
    HOM = "hom"
    HOO = "hoo"
    HOP = "hop"
    HOR = "hor"
    HOS = "hos"
    HOT = "hot"
    HOV = "hov"
    HOW = "how"
    HOY = "hoy"
    HOZ = "hoz"
    HPO = "hpo"
    HPS = "hps"
    HRA = "hra"
    HRC = "hrc"
    HRE = "hre"
    HRK = "hrk"
    HRM = "hrm"
    HRO = "hro"
    HRP = "hrp"
    HRT = "hrt"
    HRU = "hru"
    HRV = "hrv"
    HRW = "hrw"
    HRX = "hrx"
    HRZ = "hrz"
    HSB = "hsb"
    HSH = "hsh"
    HSL = "hsl"
    HSN = "hsn"
    HSS = "hss"
    HTI = "hti"
    HTO = "hto"
    HTS = "hts"
    HTU = "htu"
    HUB = "hub"
    HUC = "huc"
    HUD = "hud"
    HUE = "hue"
    HUF = "huf"
    HUG = "hug"
    HUH = "huh"
    HUI = "hui"
    HUJ = "huj"
    HUK = "huk"
    HUL = "hul"
    HUM = "hum"
    HUN = "hun"
    HUO = "huo"
    HUP = "hup"
    HUQ = "huq"
    HUR = "hur"
    HUS = "hus"
    HUT = "hut"
    HUU = "huu"
    HUV = "huv"
    HUW = "huw"
    HUX = "hux"
    HUY = "huy"
    HUZ = "huz"
    HVC = "hvc"
    HVE = "hve"
    HVK = "hvk"
    HVN = "hvn"
    HVV = "hvv"
    HWA = "hwa"
    HWC = "hwc"
    HWO = "hwo"
    HYA = "hya"
    HYE = "hye"
    HYW = "hyw"
    IAI = "iai"
    IAN = "ian"
    IAR = "iar"
    IBA = "iba"
    IBB = "ibb"
    IBD = "ibd"
    IBE = "ibe"
    IBG = "ibg"
    IBH = "ibh"
    IBL = "ibl"
    IBM = "ibm"
    IBN = "ibn"
    IBO = "ibo"
    IBR = "ibr"
    IBU = "ibu"
    IBY = "iby"
    ICA = "ica"
    ICH = "ich"
    ICL = "icl"
    ICR = "icr"
    IDA = "ida"
    IDB = "idb"
    IDC = "idc"
    IDD = "idd"
    IDE = "ide"
    IDI = "idi"
    IDR = "idr"
    IDS = "ids"
    IDT = "idt"
    IDU = "idu"
    IFA = "ifa"
    IFB = "ifb"
    IFE = "ife"
    IFF = "iff"
    IFK = "ifk"
    IFM = "ifm"
    IFU = "ifu"
    IFY = "ify"
    IGB = "igb"
    IGE = "ige"
    IGG = "igg"
    IGL = "igl"
    IGM = "igm"
    IGN = "ign"
    IGO = "igo"
    IGW = "igw"
    IHB = "ihb"
    IHI = "ihi"
    IHP = "ihp"
    IHW = "ihw"
    III = "iii"
    IIN = "iin"
    IJC = "ijc"
    IJE = "ije"
    IJJ = "ijj"
    IJN = "ijn"
    IJS = "ijs"
    IKE = "ike"
    IKH = "ikh"
    IKI = "iki"
    IKK = "ikk"
    IKL = "ikl"
    IKO = "iko"
    IKP = "ikp"
    IKR = "ikr"
    IKS = "iks"
    IKT = "ikt"
    IKV = "ikv"
    IKW = "ikw"
    IKX = "ikx"
    IKZ = "ikz"
    ILA = "ila"
    ILB = "ilb"
    ILG = "ilg"
    ILI = "ili"
    ILK = "ilk"
    ILM = "ilm"
    ILO = "ilo"
    ILP = "ilp"
    ILS = "ils"
    ILU = "ilu"
    ILV = "ilv"
    IMA = "ima"
    IMI = "imi"
    IML = "iml"
    IMN = "imn"
    IMO = "imo"
    IMR = "imr"
    IMT = "imt"
    INB = "inb"
    IND = "ind"
    ING = "ing"
    INH = "inh"
    INJ = "inj"
    INL = "inl"
    INN = "inn"
    INO = "ino"
    INP = "inp"
    INS = "ins"
    INT = "int"
    INZ = "inz"
    IOR = "ior"
    IOU = "iou"
    IOW = "iow"
    IPI = "ipi"
    IPO = "ipo"
    IQU = "iqu"
    IQW = "iqw"
    IRE = "ire"
    IRH = "irh"
    IRI = "iri"
    IRK = "irk"
    IRN = "irn"
    IRR = "irr"
    IRU = "iru"
    IRX = "irx"
    IRY = "iry"
    ISA = "isa"
    ISC = "isc"
    ISD = "isd"
    ISE = "ise"
    ISG = "isg"
    ISH = "ish"
    ISI = "isi"
    ISK = "isk"
    ISL = "isl"
    ISM = "ism"
    ISN = "isn"
    ISO = "iso"
    ISR = "isr"
    IST = "ist"
    ISU = "isu"
    ITA = "ita"
    ITB = "itb"
    ITD = "itd"
    ITE = "ite"
    ITI = "iti"
    ITK = "itk"
    ITL = "itl"
    ITM = "itm"
    ITO = "ito"
    ITR = "itr"
    ITS = "its"
    ITT = "itt"
    ITV = "itv"
    ITW = "itw"
    ITX = "itx"
    ITY = "ity"
    ITZ = "itz"
    IUM = "ium"
    IVB = "ivb"
    IVV = "ivv"
    IWK = "iwk"
    IWM = "iwm"
    IWO = "iwo"
    IWS = "iws"
    IXC = "ixc"
    IXL = "ixl"
    IYA = "iya"
    IYO = "iyo"
    IYX = "iyx"
    IZH = "izh"
    IZM = "izm"
    IZR = "izr"
    IZZ = "izz"
    JAA = "jaa"
    JAB = "jab"
    JAC = "jac"
    JAD = "jad"
    JAE = "jae"
    JAF = "jaf"
    JAH = "jah"
    JAJ = "jaj"
    JAK = "jak"
    JAL = "jal"
    JAM = "jam"
    JAN = "jan"
    JAO = "jao"
    JAQ = "jaq"
    JAS = "jas"
    JAT = "jat"
    JAU = "jau"
    JAV = "jav"
    JAX = "jax"
    JAY = "jay"
    JAZ = "jaz"
    JBE = "jbe"
    JBI = "jbi"
    JBJ = "jbj"
    JBK = "jbk"
    JBM = "jbm"
    JBN = "jbn"
    JBR = "jbr"
    JBT = "jbt"
    JBU = "jbu"
    JBW = "jbw"
    JCS = "jcs"
    JCT = "jct"
    JDA = "jda"
    JDG = "jdg"
    JDT = "jdt"
    JEB = "jeb"
    JEE = "jee"
    JEH = "jeh"
    JEI = "jei"
    JEK = "jek"
    JEL = "jel"
    JEN = "jen"
    JER = "jer"
    JET = "jet"
    JEU = "jeu"
    JGB = "jgb"
    JGE = "jge"
    JGK = "jgk"
    JGO = "jgo"
    JHI = "jhi"
    JHS = "jhs"
    JIA = "jia"
    JIB = "jib"
    JIC = "jic"
    JID = "jid"
    JIE = "jie"
    JIG = "jig"
    JIH = "jih"
    JII = "jii"
    JIL = "jil"
    JIM = "jim"
    JIO = "jio"
    JIQ = "jiq"
    JIT = "jit"
    JIU = "jiu"
    JIV = "jiv"
    JIY = "jiy"
    JJE = "jje"
    JJR = "jjr"
    JKA = "jka"
    JKM = "jkm"
    JKO = "jko"
    JKP = "jkp"
    JKR = "jkr"
    JKS = "jks"
    JKU = "jku"
    JLE = "jle"
    JLS = "jls"
    JMA = "jma"
    JMB = "jmb"
    JMC = "jmc"
    JMD = "jmd"
    JMI = "jmi"
    JML = "jml"
    JMN = "jmn"
    JMR = "jmr"
    JMS = "jms"
    JMW = "jmw"
    JMX = "jmx"
    JNA = "jna"
    JND = "jnd"
    JNG = "jng"
    JNI = "jni"
    JNJ = "jnj"
    JNL = "jnl"
    JNS = "jns"
    JOB = "job"
    JOD = "jod"
    JOG = "jog"
    JOR = "jor"
    JOS = "jos"
    JOW = "jow"
    JPN = "jpn"
    JPR = "jpr"
    JQR = "jqr"
    JRA = "jra"
    JRR = "jrr"
    JRT = "jrt"
    JRU = "jru"
    JSL = "jsl"
    JUA = "jua"
    JUB = "jub"
    JUC = "juc"
    JUD = "jud"
    JUH = "juh"
    JUI = "jui"
    JUK = "juk"
    JUL = "jul"
    JUM = "jum"
    JUN = "jun"
    JUO = "juo"
    JUP = "jup"
    JUR = "jur"
    JUS = "jus"
    JUU = "juu"
    JUW = "juw"
    JUY = "juy"
    JVD = "jvd"
    JVN = "jvn"
    JWI = "jwi"
    JYA = "jya"
    JYE = "jye"
    JYY = "jyy"
    KAA = "kaa"
    KAB = "kab"
    KAC = "kac"
    KAD = "kad"
    KAE = "kae"
    KAF = "kaf"
    KAG = "kag"
    KAH = "kah"
    KAI = "kai"
    KAJ = "kaj"
    KAK = "kak"
    KAL = "kal"
    KAM = "kam"
    KAN = "kan"
    KAO = "kao"
    KAP = "kap"
    KAQ = "kaq"
    KAS = "kas"
    KAT = "kat"
    KAV = "kav"
    KAX = "kax"
    KAY = "kay"
    KAZ = "kaz"
    KBA = "kba"
    KBB = "kbb"
    KBC = "kbc"
    KBD = "kbd"
    KBE = "kbe"
    KBG = "kbg"
    KBH = "kbh"
    KBI = "kbi"
    KBJ = "kbj"
    KBK = "kbk"
    KBL = "kbl"
    KBM = "kbm"
    KBN = "kbn"
    KBO = "kbo"
    KBP = "kbp"
    KBQ = "kbq"
    KBR = "kbr"
    KBS = "kbs"
    KBT = "kbt"
    KBU = "kbu"
    KBV = "kbv"
    KBW = "kbw"
    KBX = "kbx"
    KBY = "kby"
    KBZ = "kbz"
    KCA = "kca"
    KCB = "kcb"
    KCC = "kcc"
    KCD = "kcd"
    KCE = "kce"
    KCF = "kcf"
    KCG = "kcg"
    KCH = "kch"
    KCI = "kci"
    KCJ = "kcj"
    KCK = "kck"
    KCL = "kcl"
    KCM = "kcm"
    KCN = "kcn"
    KCO = "kco"
    KCP = "kcp"
    KCQ = "kcq"
    KCR = "kcr"
    KCS = "kcs"
    KCT = "kct"
    KCU = "kcu"
    KCV = "kcv"
    KCW = "kcw"
    KCX = "kcx"
    KCY = "kcy"
    KCZ = "kcz"
    KDA = "kda"
    KDC = "kdc"
    KDD = "kdd"
    KDE = "kde"
    KDF = "kdf"
    KDG = "kdg"
    KDH = "kdh"
    KDI = "kdi"
    KDJ = "kdj"
    KDK = "kdk"
    KDL = "kdl"
    KDM = "kdm"
    KDN = "kdn"
    KDP = "kdp"
    KDQ = "kdq"
    KDR = "kdr"
    KDT = "kdt"
    KDU = "kdu"
    KDW = "kdw"
    KDX = "kdx"
    KDY = "kdy"
    KDZ = "kdz"
    KEA = "kea"
    KEB = "keb"
    KEC = "kec"
    KED = "ked"
    KEE = "kee"
    KEF = "kef"
    KEG = "keg"
    KEH = "keh"
    KEI = "kei"
    KEJ = "kej"
    KEK = "kek"
    KEL = "kel"
    KEM = "kem"
    KEN = "ken"
    KEO = "keo"
    KEP = "kep"
    KEQ = "keq"
    KER = "ker"
    KES = "kes"
    KET = "ket"
    KEU = "keu"
    KEV = "kev"
    KEW = "kew"
    KEX = "kex"
    KEY = "key"
    KEZ = "kez"
    KFA = "kfa"
    KFB = "kfb"
    KFC = "kfc"
    KFD = "kfd"
    KFE = "kfe"
    KFF = "kff"
    KFG = "kfg"
    KFH = "kfh"
    KFI = "kfi"
    KFJ = "kfj"
    KFK = "kfk"
    KFL = "kfl"
    KFM = "kfm"
    KFN = "kfn"
    KFO = "kfo"
    KFP = "kfp"
    KFQ = "kfq"
    KFR = "kfr"
    KFS = "kfs"
    KFT = "kft"
    KFU = "kfu"
    KFV = "kfv"
    KFW = "kfw"
    KFX = "kfx"
    KFY = "kfy"
    KFZ = "kfz"
    KGA = "kga"
    KGB = "kgb"
    KGE = "kge"
    KGF = "kgf"
    KGG = "kgg"
    KGI = "kgi"
    KGJ = "kgj"
    KGK = "kgk"
    KGL = "kgl"
    KGN = "kgn"
    KGO = "kgo"
    KGP = "kgp"
    KGQ = "kgq"
    KGR = "kgr"
    KGS = "kgs"
    KGT = "kgt"
    KGU = "kgu"
    KGV = "kgv"
    KGW = "kgw"
    KGX = "kgx"
    KGY = "kgy"
    KHA = "kha"
    KHB = "khb"
    KHC = "khc"
    KHD = "khd"
    KHE = "khe"
    KHF = "khf"
    KHG = "khg"
    KHH = "khh"
    KHJ = "khj"
    KHK = "khk"
    KHL = "khl"
    KHM = "khm"
    KHN = "khn"
    KHP = "khp"
    KHQ = "khq"
    KHR = "khr"
    KHS = "khs"
    KHT = "kht"
    KHU = "khu"
    KHV = "khv"
    KHW = "khw"
    KHX = "khx"
    KHY = "khy"
    KHZ = "khz"
    KIA = "kia"
    KIB = "kib"
    KIC = "kic"
    KID = "kid"
    KIE = "kie"
    KIF = "kif"
    KIG = "kig"
    KIH = "kih"
    KII = "kii"
    KIJ = "kij"
    KIK = "kik"
    KIL = "kil"
    KIM = "kim"
    KIN = "kin"
    KIO = "kio"
    KIP = "kip"
    KIQ = "kiq"
    KIR = "kir"
    KIS = "kis"
    KIT = "kit"
    KIU = "kiu"
    KIV = "kiv"
    KIW = "kiw"
    KIX = "kix"
    KIY = "kiy"
    KIZ = "kiz"
    KJA = "kja"
    KJB = "kjb"
    KJC = "kjc"
    KJD = "kjd"
    KJE = "kje"
    KJG = "kjg"
    KJH = "kjh"
    KJI = "kji"
    KJJ = "kjj"
    KJK = "kjk"
    KJL = "kjl"
    KJM = "kjm"
    KJN = "kjn"
    KJO = "kjo"
    KJP = "kjp"
    KJQ = "kjq"
    KJR = "kjr"
    KJS = "kjs"
    KJT = "kjt"
    KJU = "kju"
    KJX = "kjx"
    KJY = "kjy"
    KJZ = "kjz"
    KKA = "kka"
    KKB = "kkb"
    KKC = "kkc"
    KKD = "kkd"
    KKE = "kke"
    KKF = "kkf"
    KKG = "kkg"
    KKH = "kkh"
    KKI = "kki"
    KKJ = "kkj"
    KKK = "kkk"
    KKL = "kkl"
    KKM = "kkm"
    KKN = "kkn"
    KKO = "kko"
    KKP = "kkp"
    KKQ = "kkq"
    KKR = "kkr"
    KKS = "kks"
    KKT = "kkt"
    KKU = "kku"
    KKV = "kkv"
    KKW = "kkw"
    KKX = "kkx"
    KKY = "kky"
    KKZ = "kkz"
    KLA = "kla"
    KLB = "klb"
    KLC = "klc"
    KLD = "kld"
    KLE = "kle"
    KLF = "klf"
    KLG = "klg"
    KLH = "klh"
    KLI = "kli"
    KLJ = "klj"
    KLK = "klk"
    KLL = "kll"
    KLM = "klm"
    KLO = "klo"
    KLP = "klp"
    KLQ = "klq"
    KLR = "klr"
    KLS = "kls"
    KLT = "klt"
    KLU = "klu"
    KLV = "klv"
    KLW = "klw"
    KLX = "klx"
    KLY = "kly"
    KLZ = "klz"
    KMA = "kma"
    KMB = "kmb"
    KMC = "kmc"
    KMD = "kmd"
    KME = "kme"
    KMF = "kmf"
    KMG = "kmg"
    KMH = "kmh"
    KMI = "kmi"
    KMJ = "kmj"
    KMK = "kmk"
    KML = "kml"
    KMM = "kmm"
    KMN = "kmn"
    KMO = "kmo"
    KMP = "kmp"
    KMQ = "kmq"
    KMR = "kmr"
    KMS = "kms"
    KMT = "kmt"
    KMU = "kmu"
    KMV = "kmv"
    KMW = "kmw"
    KMX = "kmx"
    KMY = "kmy"
    KMZ = "kmz"
    KNA = "kna"
    KNB = "knb"
    KNC = "knc"
    KND = "knd"
    KNE = "kne"
    KNF = "knf"
    KNG = "kng"
    KNI = "kni"
    KNJ = "knj"
    KNK = "knk"
    KNL = "knl"
    KNM = "knm"
    KNN = "knn"
    KNO = "kno"
    KNP = "knp"
    KNQ = "knq"
    KNR = "knr"
    KNS = "kns"
    KNT = "knt"
    KNU = "knu"
    KNV = "knv"
    KNW = "knw"
    KNX = "knx"
    KNY = "kny"
    KNZ = "knz"
    KOA = "koa"
    KOC = "koc"
    KOD = "kod"
    KOE = "koe"
    KOF = "kof"
    KOG = "kog"
    KOH = "koh"
    KOI = "koi"
    KOL = "kol"
    KOO = "koo"
    KOP = "kop"
    KOQ = "koq"
    KOR = "kor"
    KOS = "kos"
    KOT = "kot"
    KOU = "kou"
    KOV = "kov"
    KOW = "kow"
    KOY = "koy"
    KOZ = "koz"
    KPA = "kpa"
    KPB = "kpb"
    KPC = "kpc"
    KPD = "kpd"
    KPF = "kpf"
    KPG = "kpg"
    KPH = "kph"
    KPI = "kpi"
    KPJ = "kpj"
    KPK = "kpk"
    KPL = "kpl"
    KPM = "kpm"
    KPN = "kpn"
    KPO = "kpo"
    KPQ = "kpq"
    KPR = "kpr"
    KPS = "kps"
    KPT = "kpt"
    KPU = "kpu"
    KPV = "kpv"
    KPW = "kpw"
    KPX = "kpx"
    KPY = "kpy"
    KPZ = "kpz"
    KQA = "kqa"
    KQB = "kqb"
    KQC = "kqc"
    KQD = "kqd"
    KQE = "kqe"
    KQF = "kqf"
    KQG = "kqg"
    KQH = "kqh"
    KQI = "kqi"
    KQJ = "kqj"
    KQK = "kqk"
    KQL = "kql"
    KQM = "kqm"
    KQN = "kqn"
    KQO = "kqo"
    KQP = "kqp"
    KQQ = "kqq"
    KQR = "kqr"
    KQS = "kqs"
    KQT = "kqt"
    KQU = "kqu"
    KQV = "kqv"
    KQW = "kqw"
    KQX = "kqx"
    KQY = "kqy"
    KQZ = "kqz"
    KRA = "kra"
    KRB = "krb"
    KRC = "krc"
    KRD = "krd"
    KRE = "kre"
    KRF = "krf"
    KRH = "krh"
    KRI = "kri"
    KRJ = "krj"
    KRK = "krk"
    KRL = "krl"
    KRN = "krn"
    KRP = "krp"
    KRR = "krr"
    KRS = "krs"
    KRT = "krt"
    KRU = "kru"
    KRV = "krv"
    KRW = "krw"
    KRX = "krx"
    KRY = "kry"
    KRZ = "krz"
    KSB = "ksb"
    KSC = "ksc"
    KSD = "ksd"
    KSE = "kse"
    KSF = "ksf"
    KSG = "ksg"
    KSH = "ksh"
    KSI = "ksi"
    KSJ = "ksj"
    KSK = "ksk"
    KSL = "ksl"
    KSM = "ksm"
    KSN = "ksn"
    KSO = "kso"
    KSP = "ksp"
    KSQ = "ksq"
    KSR = "ksr"
    KSS = "kss"
    KST = "kst"
    KSU = "ksu"
    KSV = "ksv"
    KSW = "ksw"
    KSX = "ksx"
    KSY = "ksy"
    KSZ = "ksz"
    KTA = "kta"
    KTB = "ktb"
    KTC = "ktc"
    KTD = "ktd"
    KTE = "kte"
    KTF = "ktf"
    KTG = "ktg"
    KTH = "kth"
    KTI = "kti"
    KTJ = "ktj"
    KTK = "ktk"
    KTL = "ktl"
    KTM = "ktm"
    KTN = "ktn"
    KTO = "kto"
    KTP = "ktp"
    KTS = "kts"
    KTT = "ktt"
    KTU = "ktu"
    KTV = "ktv"
    KTW = "ktw"
    KTX = "ktx"
    KTY = "kty"
    KTZ = "ktz"
    KUA = "kua"
    KUB = "kub"
    KUC = "kuc"
    KUD = "kud"
    KUE = "kue"
    KUF = "kuf"
    KUG = "kug"
    KUH = "kuh"
    KUI = "kui"
    KUJ = "kuj"
    KUK = "kuk"
    KUL = "kul"
    KUM = "kum"
    KUN = "kun"
    KUO = "kuo"
    KUP = "kup"
    KUQ = "kuq"
    KUS = "kus"
    KUT = "kut"
    KUU = "kuu"
    KUV = "kuv"
    KUW = "kuw"
    KUX = "kux"
    KUY = "kuy"
    KUZ = "kuz"
    KVA = "kva"
    KVB = "kvb"
    KVC = "kvc"
    KVD = "kvd"
    KVE = "kve"
    KVF = "kvf"
    KVG = "kvg"
    KVH = "kvh"
    KVI = "kvi"
    KVJ = "kvj"
    KVK = "kvk"
    KVL = "kvl"
    KVM = "kvm"
    KVN = "kvn"
    KVO = "kvo"
    KVP = "kvp"
    KVQ = "kvq"
    KVR = "kvr"
    KVT = "kvt"
    KVU = "kvu"
    KVV = "kvv"
    KVW = "kvw"
    KVX = "kvx"
    KVY = "kvy"
    KVZ = "kvz"
    KWA = "kwa"
    KWB = "kwb"
    KWC = "kwc"
    KWD = "kwd"
    KWE = "kwe"
    KWF = "kwf"
    KWG = "kwg"
    KWH = "kwh"
    KWI = "kwi"
    KWJ = "kwj"
    KWK = "kwk"
    KWL = "kwl"
    KWM = "kwm"
    KWN = "kwn"
    KWO = "kwo"
    KWP = "kwp"
    KWR = "kwr"
    KWS = "kws"
    KWT = "kwt"
    KWU = "kwu"
    KWV = "kwv"
    KWW = "kww"
    KWX = "kwx"
    KWY = "kwy"
    KWZ = "kwz"
    KXA = "kxa"
    KXB = "kxb"
    KXC = "kxc"
    KXD = "kxd"
    KXF = "kxf"
    KXH = "kxh"
    KXI = "kxi"
    KXJ = "kxj"
    KXK = "kxk"
    KXM = "kxm"
    KXN = "kxn"
    KXO = "kxo"
    KXP = "kxp"
    KXQ = "kxq"
    KXR = "kxr"
    KXS = "kxs"
    KXT = "kxt"
    KXV = "kxv"
    KXW = "kxw"
    KXX = "kxx"
    KXY = "kxy"
    KXZ = "kxz"
    KYA = "kya"
    KYB = "kyb"
    KYC = "kyc"
    KYD = "kyd"
    KYE = "kye"
    KYF = "kyf"
    KYG = "kyg"
    KYH = "kyh"
    KYI = "kyi"
    KYJ = "kyj"
    KYK = "kyk"
    KYL = "kyl"
    KYM = "kym"
    KYN = "kyn"
    KYO = "kyo"
    KYP = "kyp"
    KYQ = "kyq"
    KYR = "kyr"
    KYS = "kys"
    KYT = "kyt"
    KYU = "kyu"
    KYV = "kyv"
    KYW = "kyw"
    KYX = "kyx"
    KYY = "kyy"
    KYZ = "kyz"
    KZA = "kza"
    KZB = "kzb"
    KZC = "kzc"
    KZD = "kzd"
    KZE = "kze"
    KZF = "kzf"
    KZG = "kzg"
    KZI = "kzi"
    KZK = "kzk"
    KZL = "kzl"
    KZM = "kzm"
    KZN = "kzn"
    KZO = "kzo"
    KZP = "kzp"
    KZQ = "kzq"
    KZR = "kzr"
    KZS = "kzs"
    KZU = "kzu"
    KZV = "kzv"
    KZW = "kzw"
    KZX = "kzx"
    KZY = "kzy"
    KZZ = "kzz"
    LAA = "laa"
    LAC = "lac"
    LAD = "lad"
    LAE = "lae"
    LAF = "laf"
    LAG = "lag"
    LAI = "lai"
    LAJ = "laj"
    LAL = "lal"
    LAM = "lam"
    LAN = "lan"
    LAO = "lao"
    LAP = "lap"
    LAQ = "laq"
    LAR = "lar"
    LAS = "las"
    LAT = "lat"
    LAU = "lau"
    LAW = "law"
    LAX = "lax"
    LAY = "lay"
    LAZ = "laz"
    LBB = "lbb"
    LBC = "lbc"
    LBE = "lbe"
    LBF = "lbf"
    LBG = "lbg"
    LBI = "lbi"
    LBJ = "lbj"
    LBK = "lbk"
    LBL = "lbl"
    LBM = "lbm"
    LBN = "lbn"
    LBO = "lbo"
    LBQ = "lbq"
    LBR = "lbr"
    LBS = "lbs"
    LBT = "lbt"
    LBU = "lbu"
    LBV = "lbv"
    LBW = "lbw"
    LBX = "lbx"
    LBY = "lby"
    LBZ = "lbz"
    LCC = "lcc"
    LCD = "lcd"
    LCE = "lce"
    LCF = "lcf"
    LCH = "lch"
    LCL = "lcl"
    LCM = "lcm"
    LCP = "lcp"
    LCQ = "lcq"
    LCS = "lcs"
    LDA = "lda"
    LDB = "ldb"
    LDD = "ldd"
    LDG = "ldg"
    LDH = "ldh"
    LDI = "ldi"
    LDJ = "ldj"
    LDK = "ldk"
    LDL = "ldl"
    LDM = "ldm"
    LDO = "ldo"
    LDP = "ldp"
    LDQ = "ldq"
    LEA = "lea"
    LEB = "leb"
    LEC = "lec"
    LED = "led"
    LEE = "lee"
    LEF = "lef"
    LEH = "leh"
    LEI = "lei"
    LEJ = "lej"
    LEK = "lek"
    LEL = "lel"
    LEM = "lem"
    LEN = "len"
    LEO = "leo"
    LEP = "lep"
    LEQ = "leq"
    LER = "ler"
    LES = "les"
    LET = "let"
    LEU = "leu"
    LEV = "lev"
    LEW = "lew"
    LEX = "lex"
    LEY = "ley"
    LEZ = "lez"
    LFA = "lfa"
    LGA = "lga"
    LGB = "lgb"
    LGG = "lgg"
    LGH = "lgh"
    LGI = "lgi"
    LGK = "lgk"
    LGL = "lgl"
    LGM = "lgm"
    LGN = "lgn"
    LGO = "lgo"
    LGQ = "lgq"
    LGR = "lgr"
    LGS = "lgs"
    LGT = "lgt"
    LGU = "lgu"
    LGZ = "lgz"
    LHA = "lha"
    LHH = "lhh"
    LHI = "lhi"
    LHL = "lhl"
    LHM = "lhm"
    LHN = "lhn"
    LHP = "lhp"
    LHS = "lhs"
    LHT = "lht"
    LHU = "lhu"
    LIA = "lia"
    LIB = "lib"
    LIC = "lic"
    LID = "lid"
    LIE = "lie"
    LIF = "lif"
    LIG = "lig"
    LIH = "lih"
    LIJ = "lij"
    LIK = "lik"
    LIL = "lil"
    LIM = "lim"
    LIN = "lin"
    LIO = "lio"
    LIP = "lip"
    LIQ = "liq"
    LIR = "lir"
    LIS = "lis"
    LIT = "lit"
    LIU = "liu"
    LIV = "liv"
    LIW = "liw"
    LIX = "lix"
    LIY = "liy"
    LIZ = "liz"
    LJA = "lja"
    LJE = "lje"
    LJI = "lji"
    LJL = "ljl"
    LJP = "ljp"
    LJW = "ljw"
    LJX = "ljx"
    LKA = "lka"
    LKB = "lkb"
    LKC = "lkc"
    LKD = "lkd"
    LKE = "lke"
    LKH = "lkh"
    LKI = "lki"
    LKJ = "lkj"
    LKL = "lkl"
    LKM = "lkm"
    LKN = "lkn"
    LKO = "lko"
    LKR = "lkr"
    LKS = "lks"
    LKT = "lkt"
    LKU = "lku"
    LKY = "lky"
    LLA = "lla"
    LLB = "llb"
    LLC = "llc"
    LLD = "lld"
    LLE = "lle"
    LLF = "llf"
    LLG = "llg"
    LLH = "llh"
    LLI = "lli"
    LLJ = "llj"
    LLK = "llk"
    LLL = "lll"
    LLM = "llm"
    LLN = "lln"
    LLP = "llp"
    LLQ = "llq"
    LLS = "lls"
    LLU = "llu"
    LLX = "llx"
    LMA = "lma"
    LMB = "lmb"
    LMC = "lmc"
    LMD = "lmd"
    LME = "lme"
    LMF = "lmf"
    LMG = "lmg"
    LMH = "lmh"
    LMI = "lmi"
    LMJ = "lmj"
    LMK = "lmk"
    LML = "lml"
    LMN = "lmn"
    LMO = "lmo"
    LMP = "lmp"
    LMQ = "lmq"
    LMR = "lmr"
    LMU = "lmu"
    LMV = "lmv"
    LMW = "lmw"
    LMX = "lmx"
    LMY = "lmy"
    LNA = "lna"
    LNB = "lnb"
    LND = "lnd"
    LNH = "lnh"
    LNI = "lni"
    LNJ = "lnj"
    LNL = "lnl"
    LNM = "lnm"
    LNN = "lnn"
    LNS = "lns"
    LNU = "lnu"
    LNW = "lnw"
    LNZ = "lnz"
    LOA = "loa"
    LOB = "lob"
    LOC = "loc"
    LOE = "loe"
    LOF = "lof"
    LOG = "log"
    LOH = "loh"
    LOI = "loi"
    LOJ = "loj"
    LOK = "lok"
    LOL = "lol"
    LOM = "lom"
    LON = "lon"
    LOO = "loo"
    LOP = "lop"
    LOQ = "loq"
    LOR = "lor"
    LOS = "los"
    LOT = "lot"
    LOU = "lou"
    LOV = "lov"
    LOW = "low"
    LOX = "lox"
    LOY = "loy"
    LOZ = "loz"
    LPA = "lpa"
    LPE = "lpe"
    LPN = "lpn"
    LPO = "lpo"
    LPX = "lpx"
    LQR = "lqr"
    LRA = "lra"
    LRC = "lrc"
    LRE = "lre"
    LRG = "lrg"
    LRI = "lri"
    LRK = "lrk"
    LRL = "lrl"
    LRM = "lrm"
    LRN = "lrn"
    LRO = "lro"
    LRR = "lrr"
    LRT = "lrt"
    LRV = "lrv"
    LRZ = "lrz"
    LSA = "lsa"
    LSB = "lsb"
    LSC = "lsc"
    LSD = "lsd"
    LSE = "lse"
    LSH = "lsh"
    LSI = "lsi"
    LSL = "lsl"
    LSM = "lsm"
    LSN = "lsn"
    LSO = "lso"
    LSP = "lsp"
    LSR = "lsr"
    LSS = "lss"
    LST = "lst"
    LSV = "lsv"
    LSW = "lsw"
    LSY = "lsy"
    LTG = "ltg"
    LTH = "lth"
    LTI = "lti"
    LTN = "ltn"
    LTO = "lto"
    LTS = "lts"
    LTU = "ltu"
    LTZ = "ltz"
    LUA = "lua"
    LUB = "lub"
    LUC = "luc"
    LUD = "lud"
    LUE = "lue"
    LUF = "luf"
    LUG = "lug"
    LUH = "luh"
    LUI = "lui"
    LUJ = "luj"
    LUK = "luk"
    LUL = "lul"
    LUM = "lum"
    LUN = "lun"
    LUO = "luo"
    LUP = "lup"
    LUQ = "luq"
    LUR = "lur"
    LUS = "lus"
    LUT = "lut"
    LUU = "luu"
    LUV = "luv"
    LUW = "luw"
    LUZ = "luz"
    LVA = "lva"
    LVI = "lvi"
    LVK = "lvk"
    LVL = "lvl"
    LVS = "lvs"
    LVU = "lvu"
    LWA = "lwa"
    LWE = "lwe"
    LWG = "lwg"
    LWH = "lwh"
    LWL = "lwl"
    LWM = "lwm"
    LWO = "lwo"
    LWS = "lws"
    LWT = "lwt"
    LWU = "lwu"
    LWW = "lww"
    LXM = "lxm"
    LYA = "lya"
    LYG = "lyg"
    LYN = "lyn"
    LZH = "lzh"
    LZL = "lzl"
    LZN = "lzn"
    LZZ = "lzz"
    MAA = "maa"
    MAB = "mab"
    MAD = "mad"
    MAE = "mae"
    MAF = "maf"
    MAG = "mag"
    MAH = "mah"
    MAI = "mai"
    MAJ = "maj"
    MAK = "mak"
    MAL = "mal"
    MAM = "mam"
    MAQ = "maq"
    MAR = "mar"
    MAS = "mas"
    MAT = "mat"
    MAU = "mau"
    MAV = "mav"
    MAW = "maw"
    MAX = "max"
    MAZ = "maz"
    MBA = "mba"
    MBB = "mbb"
    MBC = "mbc"
    MBD = "mbd"
    MBE = "mbe"
    MBF = "mbf"
    MBH = "mbh"
    MBI = "mbi"
    MBJ = "mbj"
    MBK = "mbk"
    MBL = "mbl"
    MBM = "mbm"
    MBN = "mbn"
    MBO = "mbo"
    MBP = "mbp"
    MBQ = "mbq"
    MBR = "mbr"
    MBS = "mbs"
    MBT = "mbt"
    MBU = "mbu"
    MBV = "mbv"
    MBW = "mbw"
    MBX = "mbx"
    MBY = "mby"
    MBZ = "mbz"
    MCA = "mca"
    MCB = "mcb"
    MCC = "mcc"
    MCD = "mcd"
    MCE = "mce"
    MCF = "mcf"
    MCG = "mcg"
    MCH = "mch"
    MCI = "mci"
    MCJ = "mcj"
    MCK = "mck"
    MCL = "mcl"
    MCM = "mcm"
    MCN = "mcn"
    MCO = "mco"
    MCP = "mcp"
    MCQ = "mcq"
    MCR = "mcr"
    MCS = "mcs"
    MCT = "mct"
    MCU = "mcu"
    MCV = "mcv"
    MCW = "mcw"
    MCX = "mcx"
    MCY = "mcy"
    MCZ = "mcz"
    MDA = "mda"
    MDB = "mdb"
    MDC = "mdc"
    MDD = "mdd"
    MDE = "mde"
    MDF = "mdf"
    MDG = "mdg"
    MDH = "mdh"
    MDI = "mdi"
    MDJ = "mdj"
    MDK = "mdk"
    MDL = "mdl"
    MDM = "mdm"
    MDN = "mdn"
    MDP = "mdp"
    MDQ = "mdq"
    MDR = "mdr"
    MDS = "mds"
    MDT = "mdt"
    MDU = "mdu"
    MDV = "mdv"
    MDW = "mdw"
    MDX = "mdx"
    MDY = "mdy"
    MDZ = "mdz"
    MEA = "mea"
    MEB = "meb"
    MEC = "mec"
    MED = "med"
    MEE = "mee"
    MEF = "mef"
    MEH = "meh"
    MEI = "mei"
    MEJ = "mej"
    MEK = "mek"
    MEL = "mel"
    MEM = "mem"
    MEN = "men"
    MEO = "meo"
    MEP = "mep"
    MEQ = "meq"
    MER = "mer"
    MES = "mes"
    MET = "met"
    MEU = "meu"
    MEV = "mev"
    MEW = "mew"
    MEY = "mey"
    MEZ = "mez"
    MFA = "mfa"
    MFB = "mfb"
    MFC = "mfc"
    MFD = "mfd"
    MFE = "mfe"
    MFF = "mff"
    MFG = "mfg"
    MFH = "mfh"
    MFI = "mfi"
    MFJ = "mfj"
    MFK = "mfk"
    MFL = "mfl"
    MFM = "mfm"
    MFN = "mfn"
    MFO = "mfo"
    MFP = "mfp"
    MFQ = "mfq"
    MFR = "mfr"
    MFS = "mfs"
    MFT = "mft"
    MFU = "mfu"
    MFV = "mfv"
    MFW = "mfw"
    MFX = "mfx"
    MFY = "mfy"
    MFZ = "mfz"
    MGB = "mgb"
    MGC = "mgc"
    MGD = "mgd"
    MGE = "mge"
    MGF = "mgf"
    MGG = "mgg"
    MGH = "mgh"
    MGI = "mgi"
    MGJ = "mgj"
    MGK = "mgk"
    MGL = "mgl"
    MGM = "mgm"
    MGN = "mgn"
    MGO = "mgo"
    MGP = "mgp"
    MGQ = "mgq"
    MGR = "mgr"
    MGS = "mgs"
    MGT = "mgt"
    MGU = "mgu"
    MGV = "mgv"
    MGW = "mgw"
    MGY = "mgy"
    MGZ = "mgz"
    MHA = "mha"
    MHB = "mhb"
    MHC = "mhc"
    MHD = "mhd"
    MHE = "mhe"
    MHF = "mhf"
    MHG = "mhg"
    MHI = "mhi"
    MHJ = "mhj"
    MHK = "mhk"
    MHL = "mhl"
    MHM = "mhm"
    MHN = "mhn"
    MHO = "mho"
    MHP = "mhp"
    MHQ = "mhq"
    MHR = "mhr"
    MHS = "mhs"
    MHT = "mht"
    MHU = "mhu"
    MHW = "mhw"
    MHX = "mhx"
    MHY = "mhy"
    MHZ = "mhz"
    MIA = "mia"
    MIB = "mib"
    MIC = "mic"
    MID = "mid"
    MIE = "mie"
    MIF = "mif"
    MIG = "mig"
    MIH = "mih"
    MII = "mii"
    MIJ = "mij"
    MIK = "mik"
    MIL = "mil"
    MIM = "mim"
    MIN = "min"
    MIO = "mio"
    MIP = "mip"
    MIQ = "miq"
    MIR = "mir"
    MIT = "mit"
    MIU = "miu"
    MIW = "miw"
    MIX = "mix"
    MIY = "miy"
    MIZ = "miz"
    MJB = "mjb"
    MJC = "mjc"
    MJD = "mjd"
    MJE = "mje"
    MJG = "mjg"
    MJH = "mjh"
    MJI = "mji"
    MJJ = "mjj"
    MJK = "mjk"
    MJL = "mjl"
    MJM = "mjm"
    MJN = "mjn"
    MJO = "mjo"
    MJP = "mjp"
    MJQ = "mjq"
    MJR = "mjr"
    MJS = "mjs"
    MJT = "mjt"
    MJU = "mju"
    MJV = "mjv"
    MJW = "mjw"
    MJX = "mjx"
    MJY = "mjy"
    MJZ = "mjz"
    MKA = "mka"
    MKB = "mkb"
    MKC = "mkc"
    MKD = "mkd"
    MKE = "mke"
    MKF = "mkf"
    MKG = "mkg"
    MKI = "mki"
    MKJ = "mkj"
    MKK = "mkk"
    MKL = "mkl"
    MKM = "mkm"
    MKN = "mkn"
    MKO = "mko"
    MKP = "mkp"
    MKQ = "mkq"
    MKR = "mkr"
    MKS = "mks"
    MKT = "mkt"
    MKU = "mku"
    MKV = "mkv"
    MKW = "mkw"
    MKX = "mkx"
    MKY = "mky"
    MKZ = "mkz"
    MLA = "mla"
    MLB = "mlb"
    MLC = "mlc"
    MLE = "mle"
    MLF = "mlf"
    MLH = "mlh"
    MLI = "mli"
    MLJ = "mlj"
    MLK = "mlk"
    MLL = "mll"
    MLM = "mlm"
    MLN = "mln"
    MLO = "mlo"
    MLP = "mlp"
    MLQ = "mlq"
    MLR = "mlr"
    MLS = "mls"
    MLT = "mlt"
    MLU = "mlu"
    MLV = "mlv"
    MLW = "mlw"
    MLX = "mlx"
    MLZ = "mlz"
    MMA = "mma"
    MMB = "mmb"
    MMC = "mmc"
    MMD = "mmd"
    MME = "mme"
    MMF = "mmf"
    MMG = "mmg"
    MMH = "mmh"
    MMI = "mmi"
    MMJ = "mmj"
    MMK = "mmk"
    MML = "mml"
    MMM = "mmm"
    MMN = "mmn"
    MMO = "mmo"
    MMP = "mmp"
    MMQ = "mmq"
    MMR = "mmr"
    MMT = "mmt"
    MMU = "mmu"
    MMV = "mmv"
    MMW = "mmw"
    MMX = "mmx"
    MMY = "mmy"
    MMZ = "mmz"
    MNA = "mna"
    MNB = "mnb"
    MNC = "mnc"
    MND = "mnd"
    MNE = "mne"
    MNF = "mnf"
    MNG = "mng"
    MNH = "mnh"
    MNI = "mni"
    MNJ = "mnj"
    MNK = "mnk"
    MNL = "mnl"
    MNM = "mnm"
    MNN = "mnn"
    MNP = "mnp"
    MNQ = "mnq"
    MNR = "mnr"
    MNS = "mns"
    MNU = "mnu"
    MNV = "mnv"
    MNW = "mnw"
    MNX = "mnx"
    MNY = "mny"
    MNZ = "mnz"
    MOA = "moa"
    MOC = "moc"
    MOD = "mod"
    MOE = "moe"
    MOG = "mog"
    MOH = "moh"
    MOI = "moi"
    MOJ = "moj"
    MOK = "mok"
    MOM = "mom"
    MOO = "moo"
    MOP = "mop"
    MOQ = "moq"
    MOR = "mor"
    MOS = "mos"
    MOT = "mot"
    MOU = "mou"
    MOV = "mov"
    MOW = "mow"
    MOX = "mox"
    MOY = "moy"
    MOZ = "moz"
    MPA = "mpa"
    MPB = "mpb"
    MPC = "mpc"
    MPD = "mpd"
    MPE = "mpe"
    MPG = "mpg"
    MPH = "mph"
    MPI = "mpi"
    MPJ = "mpj"
    MPK = "mpk"
    MPL = "mpl"
    MPM = "mpm"
    MPN = "mpn"
    MPO = "mpo"
    MPP = "mpp"
    MPQ = "mpq"
    MPR = "mpr"
    MPS = "mps"
    MPT = "mpt"
    MPU = "mpu"
    MPV = "mpv"
    MPW = "mpw"
    MPX = "mpx"
    MPY = "mpy"
    MPZ = "mpz"
    MQA = "mqa"
    MQB = "mqb"
    MQC = "mqc"
    MQE = "mqe"
    MQF = "mqf"
    MQG = "mqg"
    MQH = "mqh"
    MQI = "mqi"
    MQJ = "mqj"
    MQK = "mqk"
    MQL = "mql"
    MQM = "mqm"
    MQN = "mqn"
    MQO = "mqo"
    MQP = "mqp"
    MQQ = "mqq"
    MQR = "mqr"
    MQS = "mqs"
    MQT = "mqt"
    MQU = "mqu"
    MQV = "mqv"
    MQW = "mqw"
    MQX = "mqx"
    MQY = "mqy"
    MQZ = "mqz"
    MRA = "mra"
    MRB = "mrb"
    MRC = "mrc"
    MRD = "mrd"
    MRE = "mre"
    MRF = "mrf"
    MRG = "mrg"
    MRH = "mrh"
    MRI = "mri"
    MRJ = "mrj"
    MRK = "mrk"
    MRL = "mrl"
    MRM = "mrm"
    MRN = "mrn"
    MRO = "mro"
    MRQ = "mrq"
    MRR = "mrr"
    MRS = "mrs"
    MRT = "mrt"
    MRU = "mru"
    MRV = "mrv"
    MRW = "mrw"
    MRX = "mrx"
    MRY = "mry"
    MRZ = "mrz"
    MSB = "msb"
    MSC = "msc"
    MSD = "msd"
    MSE = "mse"
    MSF = "msf"
    MSG = "msg"
    MSH = "msh"
    MSI = "msi"
    MSJ = "msj"
    MSK = "msk"
    MSL = "msl"
    MSM = "msm"
    MSN = "msn"
    MSO = "mso"
    MSP = "msp"
    MSQ = "msq"
    MSR = "msr"
    MSS = "mss"
    MSU = "msu"
    MSV = "msv"
    MSW = "msw"
    MSX = "msx"
    MSY = "msy"
    MSZ = "msz"
    MTA = "mta"
    MTB = "mtb"
    MTC = "mtc"
    MTD = "mtd"
    MTE = "mte"
    MTF = "mtf"
    MTG = "mtg"
    MTH = "mth"
    MTI = "mti"
    MTJ = "mtj"
    MTK = "mtk"
    MTL = "mtl"
    MTM = "mtm"
    MTN = "mtn"
    MTO = "mto"
    MTP = "mtp"
    MTQ = "mtq"
    MTR = "mtr"
    MTS = "mts"
    MTT = "mtt"
    MTU = "mtu"
    MTV = "mtv"
    MTW = "mtw"
    MTX = "mtx"
    MTY = "mty"
    MUA = "mua"
    MUB = "mub"
    MUC = "muc"
    MUD = "mud"
    MUE = "mue"
    MUG = "mug"
    MUH = "muh"
    MUI = "mui"
    MUJ = "muj"
    MUK = "muk"
    MUM = "mum"
    MUO = "muo"
    MUP = "mup"
    MUQ = "muq"
    MUR = "mur"
    MUS = "mus"
    MUT = "mut"
    MUU = "muu"
    MUV = "muv"
    MUX = "mux"
    MUY = "muy"
    MUZ = "muz"
    MVA = "mva"
    MVB = "mvb"
    MVD = "mvd"
    MVE = "mve"
    MVF = "mvf"
    MVG = "mvg"
    MVH = "mvh"
    MVI = "mvi"
    MVK = "mvk"
    MVL = "mvl"
    MVN = "mvn"
    MVO = "mvo"
    MVP = "mvp"
    MVQ = "mvq"
    MVR = "mvr"
    MVS = "mvs"
    MVT = "mvt"
    MVU = "mvu"
    MVV = "mvv"
    MVW = "mvw"
    MVX = "mvx"
    MVY = "mvy"
    MVZ = "mvz"
    MWA = "mwa"
    MWB = "mwb"
    MWC = "mwc"
    MWE = "mwe"
    MWF = "mwf"
    MWG = "mwg"
    MWH = "mwh"
    MWI = "mwi"
    MWK = "mwk"
    MWL = "mwl"
    MWM = "mwm"
    MWN = "mwn"
    MWO = "mwo"
    MWP = "mwp"
    MWQ = "mwq"
    MWS = "mws"
    MWT = "mwt"
    MWU = "mwu"
    MWV = "mwv"
    MWW = "mww"
    MWZ = "mwz"
    MXA = "mxa"
    MXB = "mxb"
    MXC = "mxc"
    MXD = "mxd"
    MXE = "mxe"
    MXF = "mxf"
    MXG = "mxg"
    MXH = "mxh"
    MXJ = "mxj"
    MXK = "mxk"
    MXL = "mxl"
    MXM = "mxm"
    MXN = "mxn"
    MXO = "mxo"
    MXP = "mxp"
    MXQ = "mxq"
    MXR = "mxr"
    MXS = "mxs"
    MXT = "mxt"
    MXU = "mxu"
    MXV = "mxv"
    MXW = "mxw"
    MXX = "mxx"
    MXY = "mxy"
    MXZ = "mxz"
    MYA = "mya"
    MYB = "myb"
    MYC = "myc"
    MYE = "mye"
    MYF = "myf"
    MYG = "myg"
    MYH = "myh"
    MYJ = "myj"
    MYK = "myk"
    MYL = "myl"
    MYM = "mym"
    MYO = "myo"
    MYP = "myp"
    MYR = "myr"
    MYS = "mys"
    MYU = "myu"
    MYV = "myv"
    MYW = "myw"
    MYX = "myx"
    MYY = "myy"
    MYZ = "myz"
    MZA = "mza"
    MZB = "mzb"
    MZC = "mzc"
    MZD = "mzd"
    MZE = "mze"
    MZH = "mzh"
    MZI = "mzi"
    MZJ = "mzj"
    MZK = "mzk"
    MZL = "mzl"
    MZM = "mzm"
    MZN = "mzn"
    MZO = "mzo"
    MZP = "mzp"
    MZQ = "mzq"
    MZR = "mzr"
    MZS = "mzs"
    MZT = "mzt"
    MZU = "mzu"
    MZV = "mzv"
    MZW = "mzw"
    MZX = "mzx"
    MZY = "mzy"
    MZZ = "mzz"
    NAA = "naa"
    NAB = "nab"
    NAC = "nac"
    NAE = "nae"
    NAF = "naf"
    NAG = "nag"
    NAJ = "naj"
    NAK = "nak"
    NAL = "nal"
    NAM = "nam"
    NAN = "nan"
    NAO = "nao"
    NAP = "nap"
    NAQ = "naq"
    NAR = "nar"
    NAS = "nas"
    NAT = "nat"
    NAU = "nau"
    NAV = "nav"
    NAW = "naw"
    NAX = "nax"
    NAY = "nay"
    NAZ = "naz"
    NBA = "nba"
    NBB = "nbb"
    NBC = "nbc"
    NBD = "nbd"
    NBE = "nbe"
    NBG = "nbg"
    NBH = "nbh"
    NBI = "nbi"
    NBJ = "nbj"
    NBK = "nbk"
    NBL = "nbl"
    NBM = "nbm"
    NBN = "nbn"
    NBO = "nbo"
    NBP = "nbp"
    NBQ = "nbq"
    NBR = "nbr"
    NBS = "nbs"
    NBT = "nbt"
    NBU = "nbu"
    NBV = "nbv"
    NBW = "nbw"
    NBY = "nby"
    NCA = "nca"
    NCB = "ncb"
    NCC = "ncc"
    NCD = "ncd"
    NCE = "nce"
    NCF = "ncf"
    NCG = "ncg"
    NCH = "nch"
    NCJ = "ncj"
    NCK = "nck"
    NCL = "ncl"
    NCM = "ncm"
    NCN = "ncn"
    NCO = "nco"
    NCQ = "ncq"
    NCR = "ncr"
    NCS = "ncs"
    NCT = "nct"
    NCU = "ncu"
    NCX = "ncx"
    NCZ = "ncz"
    NDA = "nda"
    NDB = "ndb"
    NDC = "ndc"
    NDD = "ndd"
    NDE = "nde"
    NDG = "ndg"
    NDH = "ndh"
    NDI = "ndi"
    NDJ = "ndj"
    NDK = "ndk"
    NDL = "ndl"
    NDM = "ndm"
    NDN = "ndn"
    NDO = "ndo"
    NDP = "ndp"
    NDQ = "ndq"
    NDR = "ndr"
    NDS = "nds"
    NDT = "ndt"
    NDU = "ndu"
    NDV = "ndv"
    NDW = "ndw"
    NDX = "ndx"
    NDY = "ndy"
    NDZ = "ndz"
    NEA = "nea"
    NEB = "neb"
    NEC = "nec"
    NED = "ned"
    NEE = "nee"
    NEF = "nef"
    NEG = "neg"
    NEH = "neh"
    NEJ = "nej"
    NEK = "nek"
    NEM = "nem"
    NEN = "nen"
    NEO = "neo"
    NEQ = "neq"
    NER = "ner"
    NES = "nes"
    NET = "net"
    NEV = "nev"
    NEW = "new"
    NEX = "nex"
    NEY = "ney"
    NEZ = "nez"
    NFA = "nfa"
    NFD = "nfd"
    NFL = "nfl"
    NFR = "nfr"
    NFU = "nfu"
    NGA = "nga"
    NGB = "ngb"
    NGC = "ngc"
    NGD = "ngd"
    NGE = "nge"
    NGG = "ngg"
    NGH = "ngh"
    NGI = "ngi"
    NGJ = "ngj"
    NGK = "ngk"
    NGL = "ngl"
    NGM = "ngm"
    NGN = "ngn"
    NGP = "ngp"
    NGQ = "ngq"
    NGR = "ngr"
    NGS = "ngs"
    NGT = "ngt"
    NGU = "ngu"
    NGV = "ngv"
    NGW = "ngw"
    NGX = "ngx"
    NGY = "ngy"
    NGZ = "ngz"
    NHA = "nha"
    NHB = "nhb"
    NHC = "nhc"
    NHD = "nhd"
    NHE = "nhe"
    NHF = "nhf"
    NHG = "nhg"
    NHH = "nhh"
    NHI = "nhi"
    NHK = "nhk"
    NHM = "nhm"
    NHN = "nhn"
    NHO = "nho"
    NHP = "nhp"
    NHQ = "nhq"
    NHR = "nhr"
    NHT = "nht"
    NHU = "nhu"
    NHV = "nhv"
    NHW = "nhw"
    NHX = "nhx"
    NHY = "nhy"
    NHZ = "nhz"
    NIA = "nia"
    NIB = "nib"
    NID = "nid"
    NIE = "nie"
    NIF = "nif"
    NIG = "nig"
    NIH = "nih"
    NII = "nii"
    NIJ = "nij"
    NIK = "nik"
    NIL = "nil"
    NIM = "nim"
    NIN = "nin"
    NIO = "nio"
    NIQ = "niq"
    NIR = "nir"
    NIS = "nis"
    NIT = "nit"
    NIU = "niu"
    NIV = "niv"
    NIW = "niw"
    NIX = "nix"
    NIY = "niy"
    NIZ = "niz"
    NJA = "nja"
    NJB = "njb"
    NJD = "njd"
    NJH = "njh"
    NJI = "nji"
    NJJ = "njj"
    NJL = "njl"
    NJM = "njm"
    NJN = "njn"
    NJO = "njo"
    NJR = "njr"
    NJS = "njs"
    NJT = "njt"
    NJU = "nju"
    NJX = "njx"
    NJY = "njy"
    NJZ = "njz"
    NKA = "nka"
    NKB = "nkb"
    NKC = "nkc"
    NKD = "nkd"
    NKE = "nke"
    NKF = "nkf"
    NKG = "nkg"
    NKH = "nkh"
    NKI = "nki"
    NKJ = "nkj"
    NKK = "nkk"
    NKM = "nkm"
    NKN = "nkn"
    NKO = "nko"
    NKP = "nkp"
    NKQ = "nkq"
    NKR = "nkr"
    NKS = "nks"
    NKT = "nkt"
    NKU = "nku"
    NKV = "nkv"
    NKW = "nkw"
    NKX = "nkx"
    NKZ = "nkz"
    NLA = "nla"
    NLC = "nlc"
    NLD = "nld"
    NLE = "nle"
    NLG = "nlg"
    NLI = "nli"
    NLJ = "nlj"
    NLK = "nlk"
    NLL = "nll"
    NLM = "nlm"
    NLO = "nlo"
    NLQ = "nlq"
    NLU = "nlu"
    NLV = "nlv"
    NLW = "nlw"
    NLX = "nlx"
    NLY = "nly"
    NLZ = "nlz"
    NMA = "nma"
    NMB = "nmb"
    NMC = "nmc"
    NMD = "nmd"
    NME = "nme"
    NMF = "nmf"
    NMG = "nmg"
    NMH = "nmh"
    NMI = "nmi"
    NMJ = "nmj"
    NMK = "nmk"
    NML = "nml"
    NMM = "nmm"
    NMN = "nmn"
    NMO = "nmo"
    NMP = "nmp"
    NMQ = "nmq"
    NMR = "nmr"
    NMS = "nms"
    NMT = "nmt"
    NMU = "nmu"
    NMV = "nmv"
    NMW = "nmw"
    NMX = "nmx"
    NMY = "nmy"
    NMZ = "nmz"
    NNA = "nna"
    NNB = "nnb"
    NNC = "nnc"
    NND = "nnd"
    NNE = "nne"
    NNF = "nnf"
    NNG = "nng"
    NNH = "nnh"
    NNI = "nni"
    NNJ = "nnj"
    NNK = "nnk"
    NNL = "nnl"
    NNM = "nnm"
    NNN = "nnn"
    NNP = "nnp"
    NNQ = "nnq"
    NNR = "nnr"
    NNT = "nnt"
    NNU = "nnu"
    NNV = "nnv"
    NNW = "nnw"
    NNY = "nny"
    NNZ = "nnz"
    NOA = "noa"
    NOC = "noc"
    NOD = "nod"
    NOE = "noe"
    NOF = "nof"
    NOG = "nog"
    NOH = "noh"
    NOI = "noi"
    NOJ = "noj"
    NOK = "nok"
    NOL = "nol"
    NOP = "nop"
    NOQ = "noq"
    NOR = "nor"
    NOS = "nos"
    NOT = "not"
    NOU = "nou"
    NOW = "now"
    NOY = "noy"
    NOZ = "noz"
    NPA = "npa"
    NPB = "npb"
    NPG = "npg"
    NPH = "nph"
    NPI = "npi"
    NPL = "npl"
    NPN = "npn"
    NPO = "npo"
    NPS = "nps"
    NPU = "npu"
    NPX = "npx"
    NPY = "npy"
    NQG = "nqg"
    NQK = "nqk"
    NQL = "nql"
    NQM = "nqm"
    NQN = "nqn"
    NQO = "nqo"
    NQQ = "nqq"
    NQT = "nqt"
    NQY = "nqy"
    NRA = "nra"
    NRB = "nrb"
    NRE = "nre"
    NRF = "nrf"
    NRG = "nrg"
    NRI = "nri"
    NRK = "nrk"
    NRL = "nrl"
    NRM = "nrm"
    NRN = "nrn"
    NRR = "nrr"
    NRT = "nrt"
    NRU = "nru"
    NRX = "nrx"
    NRZ = "nrz"
    NSA = "nsa"
    NSB = "nsb"
    NSD = "nsd"
    NSE = "nse"
    NSF = "nsf"
    NSG = "nsg"
    NSH = "nsh"
    NSI = "nsi"
    NSK = "nsk"
    NSL = "nsl"
    NSM = "nsm"
    NSN = "nsn"
    NSO = "nso"
    NSP = "nsp"
    NSQ = "nsq"
    NSR = "nsr"
    NSS = "nss"
    NST = "nst"
    NSU = "nsu"
    NSV = "nsv"
    NSW = "nsw"
    NSX = "nsx"
    NSY = "nsy"
    NSZ = "nsz"
    NTD = "ntd"
    NTG = "ntg"
    NTI = "nti"
    NTJ = "ntj"
    NTK = "ntk"
    NTM = "ntm"
    NTO = "nto"
    NTP = "ntp"
    NTR = "ntr"
    NTU = "ntu"
    NTW = "ntw"
    NTX = "ntx"
    NTY = "nty"
    NTZ = "ntz"
    NUA = "nua"
    NUC = "nuc"
    NUD = "nud"
    NUE = "nue"
    NUF = "nuf"
    NUG = "nug"
    NUH = "nuh"
    NUI = "nui"
    NUJ = "nuj"
    NUK = "nuk"
    NUL = "nul"
    NUM = "num"
    NUN = "nun"
    NUO = "nuo"
    NUP = "nup"
    NUQ = "nuq"
    NUR = "nur"
    NUS = "nus"
    NUT = "nut"
    NUU = "nuu"
    NUV = "nuv"
    NUW = "nuw"
    NUX = "nux"
    NUY = "nuy"
    NUZ = "nuz"
    NVH = "nvh"
    NVM = "nvm"
    NVO = "nvo"
    NWA = "nwa"
    NWB = "nwb"
    NWE = "nwe"
    NWG = "nwg"
    NWI = "nwi"
    NWM = "nwm"
    NWO = "nwo"
    NWR = "nwr"
    NWW = "nww"
    NWY = "nwy"
    NXA = "nxa"
    NXD = "nxd"
    NXE = "nxe"
    NXG = "nxg"
    NXI = "nxi"
    NXK = "nxk"
    NXL = "nxl"
    NXN = "nxn"
    NXO = "nxo"
    NXQ = "nxq"
    NXR = "nxr"
    NXX = "nxx"
    NYA = "nya"
    NYB = "nyb"
    NYC = "nyc"
    NYD = "nyd"
    NYE = "nye"
    NYF = "nyf"
    NYG = "nyg"
    NYH = "nyh"
    NYI = "nyi"
    NYJ = "nyj"
    NYK = "nyk"
    NYL = "nyl"
    NYM = "nym"
    NYN = "nyn"
    NYO = "nyo"
    NYP = "nyp"
    NYQ = "nyq"
    NYR = "nyr"
    NYS = "nys"
    NYT = "nyt"
    NYU = "nyu"
    NYV = "nyv"
    NYW = "nyw"
    NYX = "nyx"
    NYY = "nyy"
    NZA = "nza"
    NZB = "nzb"
    NZD = "nzd"
    NZI = "nzi"
    NZK = "nzk"
    NZM = "nzm"
    NZR = "nzr"
    NZS = "nzs"
    NZU = "nzu"
    NZY = "nzy"
    NZZ = "nzz"
    OAA = "oaa"
    OAC = "oac"
    OBI = "obi"
    OBK = "obk"
    OBL = "obl"
    OBO = "obo"
    OBU = "obu"
    OCA = "oca"
    OCI = "oci"
    OCU = "ocu"
    ODA = "oda"
    ODK = "odk"
    ODU = "odu"
    OFO = "ofo"
    OFU = "ofu"
    OGB = "ogb"
    OGC = "ogc"
    OGG = "ogg"
    OGO = "ogo"
    OGU = "ogu"
    OIA = "oia"
    OIE = "oie"
    OIN = "oin"
    OJB = "ojb"
    OJC = "ojc"
    OJG = "ojg"
    OJS = "ojs"
    OJV = "ojv"
    OJW = "ojw"
    OKA = "oka"
    OKB = "okb"
    OKC = "okc"
    OKD = "okd"
    OKE = "oke"
    OKG = "okg"
    OKH = "okh"
    OKI = "oki"
    OKJ = "okj"
    OKK = "okk"
    OKL = "okl"
    OKN = "okn"
    OKR = "okr"
    OKS = "oks"
    OKU = "oku"
    OKV = "okv"
    OKX = "okx"
    OLA = "ola"
    OLD = "old"
    OLE = "ole"
    OLK = "olk"
    OLM = "olm"
    OLO = "olo"
    OLR = "olr"
    OLU = "olu"
    OMA = "oma"
    OMB = "omb"
    OMC = "omc"
    OMG = "omg"
    OMI = "omi"
    OMK = "omk"
    OML = "oml"
    OMO = "omo"
    OMT = "omt"
    OMU = "omu"
    OMW = "omw"
    ONA = "ona"
    ONB = "onb"
    ONE = "one"
    ONG = "ong"
    ONI = "oni"
    ONJ = "onj"
    ONK = "onk"
    ONN = "onn"
    ONO = "ono"
    ONP = "onp"
    ONR = "onr"
    ONS = "ons"
    ONT = "ont"
    ONU = "onu"
    ONX = "onx"
    OOD = "ood"
    OOG = "oog"
    OON = "oon"
    OOR = "oor"
    OPA = "opa"
    OPK = "opk"
    OPM = "opm"
    OPO = "opo"
    OPT = "opt"
    OPY = "opy"
    ORA = "ora"
    ORC = "orc"
    ORE = "ore"
    ORG = "org"
    ORH = "orh"
    ORN = "orn"
    ORO = "oro"
    ORR = "orr"
    ORS = "ors"
    ORT = "ort"
    ORU = "oru"
    ORW = "orw"
    ORX = "orx"
    ORY = "ory"
    ORZ = "orz"
    OSA = "osa"
    OSI = "osi"
    OSO = "oso"
    OSS = "oss"
    OST = "ost"
    OSU = "osu"
    OTD = "otd"
    OTE = "ote"
    OTI = "oti"
    OTL = "otl"
    OTM = "otm"
    OTN = "otn"
    OTQ = "otq"
    OTR = "otr"
    OTS = "ots"
    OTT = "ott"
    OTU = "otu"
    OTW = "otw"
    OTX = "otx"
    OTZ = "otz"
    OUA = "oua"
    OUB = "oub"
    OUE = "oue"
    OUM = "oum"
    OVD = "ovd"
    OWI = "owi"
    OYB = "oyb"
    OYD = "oyd"
    OYM = "oym"
    OYY = "oyy"
    OZM = "ozm"
    PAB = "pab"
    PAC = "pac"
    PAD = "pad"
    PAE = "pae"
    PAF = "paf"
    PAG = "pag"
    PAH = "pah"
    PAI = "pai"
    PAK = "pak"
    PAM = "pam"
    PAN = "pan"
    PAO = "pao"
    PAP = "pap"
    PAQ = "paq"
    PAR = "par"
    PAS = "pas"
    PAU = "pau"
    PAV = "pav"
    PAW = "paw"
    PAX = "pax"
    PAY = "pay"
    PAZ = "paz"
    PBB = "pbb"
    PBC = "pbc"
    PBE = "pbe"
    PBF = "pbf"
    PBG = "pbg"
    PBH = "pbh"
    PBI = "pbi"
    PBL = "pbl"
    PBM = "pbm"
    PBN = "pbn"
    PBO = "pbo"
    PBP = "pbp"
    PBR = "pbr"
    PBS = "pbs"
    PBT = "pbt"
    PBU = "pbu"
    PBV = "pbv"
    PBY = "pby"
    PCA = "pca"
    PCB = "pcb"
    PCC = "pcc"
    PCD = "pcd"
    PCE = "pce"
    PCF = "pcf"
    PCG = "pcg"
    PCH = "pch"
    PCI = "pci"
    PCJ = "pcj"
    PCK = "pck"
    PCL = "pcl"
    PCM = "pcm"
    PCN = "pcn"
    PCP = "pcp"
    PCW = "pcw"
    PDA = "pda"
    PDC = "pdc"
    PDI = "pdi"
    PDN = "pdn"
    PDO = "pdo"
    PDT = "pdt"
    PDU = "pdu"
    PEA = "pea"
    PEB = "peb"
    PED = "ped"
    PEE = "pee"
    PEF = "pef"
    PEG = "peg"
    PEH = "peh"
    PEI = "pei"
    PEJ = "pej"
    PEK = "pek"
    PEL = "pel"
    PEM = "pem"
    PEP = "pep"
    PEQ = "peq"
    PES = "pes"
    PEV = "pev"
    PEX = "pex"
    PEY = "pey"
    PEZ = "pez"
    PFA = "pfa"
    PFE = "pfe"
    PFL = "pfl"
    PGA = "pga"
    PGG = "pgg"
    PGI = "pgi"
    PGK = "pgk"
    PGS = "pgs"
    PGU = "pgu"
    PGZ = "pgz"
    PHA = "pha"
    PHD = "phd"
    PHG = "phg"
    PHH = "phh"
    PHJ = "phj"
    PHK = "phk"
    PHL = "phl"
    PHM = "phm"
    PHO = "pho"
    PHQ = "phq"
    PHR = "phr"
    PHT = "pht"
    PHU = "phu"
    PHV = "phv"
    PHW = "phw"
    PIA = "pia"
    PIB = "pib"
    PIC = "pic"
    PID = "pid"
    PIE = "pie"
    PIF = "pif"
    PIG = "pig"
    PIH = "pih"
    PIJ = "pij"
    PIL = "pil"
    PIM = "pim"
    PIN = "pin"
    PIO = "pio"
    PIP = "pip"
    PIR = "pir"
    PIS = "pis"
    PIT = "pit"
    PIU = "piu"
    PIV = "piv"
    PIW = "piw"
    PIX = "pix"
    PIY = "piy"
    PIZ = "piz"
    PJT = "pjt"
    PKB = "pkb"
    PKG = "pkg"
    PKH = "pkh"
    PKN = "pkn"
    PKO = "pko"
    PKP = "pkp"
    PKR = "pkr"
    PKS = "pks"
    PKT = "pkt"
    PKU = "pku"
    PLA = "pla"
    PLB = "plb"
    PLC = "plc"
    PLD = "pld"
    PLE = "ple"
    PLG = "plg"
    PLH = "plh"
    PLI = "pli"
    PLK = "plk"
    PLL = "pll"
    PLN = "pln"
    PLO = "plo"
    PLR = "plr"
    PLS = "pls"
    PLT = "plt"
    PLU = "plu"
    PLV = "plv"
    PLW = "plw"
    PLY = "ply"
    PLZ = "plz"
    PMA = "pma"
    PMB = "pmb"
    PMD = "pmd"
    PME = "pme"
    PMF = "pmf"
    PMI = "pmi"
    PMJ = "pmj"
    PML = "pml"
    PMM = "pmm"
    PMN = "pmn"
    PMO = "pmo"
    PMQ = "pmq"
    PMR = "pmr"
    PMS = "pms"
    PMT = "pmt"
    PMW = "pmw"
    PMX = "pmx"
    PMY = "pmy"
    PMZ = "pmz"
    PNA = "pna"
    PNB = "pnb"
    PNC = "pnc"
    PND = "pnd"
    PNE = "pne"
    PNG = "png"
    PNH = "pnh"
    PNI = "pni"
    PNJ = "pnj"
    PNK = "pnk"
    PNL = "pnl"
    PNM = "pnm"
    PNN = "pnn"
    PNO = "pno"
    PNP = "pnp"
    PNQ = "pnq"
    PNR = "pnr"
    PNS = "pns"
    PNT = "pnt"
    PNU = "pnu"
    PNV = "pnv"
    PNW = "pnw"
    PNX = "pnx"
    PNY = "pny"
    PNZ = "pnz"
    POC = "poc"
    POE = "poe"
    POF = "pof"
    POG = "pog"
    POH = "poh"
    POI = "poi"
    POK = "pok"
    POL = "pol"
    POM = "pom"
    PON = "pon"
    POO = "poo"
    POP = "pop"
    POQ = "poq"
    POR = "por"
    POS = "pos"
    POT = "pot"
    POV = "pov"
    POW = "pow"
    POX = "pox"
    POY = "poy"
    PPE = "ppe"
    PPI = "ppi"
    PPK = "ppk"
    PPL = "ppl"
    PPM = "ppm"
    PPN = "ppn"
    PPO = "ppo"
    PPP = "ppp"
    PPQ = "ppq"
    PPS = "pps"
    PPT = "ppt"
    PPU = "ppu"
    PQA = "pqa"
    PQM = "pqm"
    PRC = "prc"
    PRD = "prd"
    PRE = "pre"
    PRF = "prf"
    PRG = "prg"
    PRH = "prh"
    PRI = "pri"
    PRK = "prk"
    PRL = "prl"
    PRM = "prm"
    PRN = "prn"
    PRQ = "prq"
    PRR = "prr"
    PRS = "prs"
    PRT = "prt"
    PRU = "pru"
    PRW = "prw"
    PRX = "prx"
    PRZ = "prz"
    PSA = "psa"
    PSC = "psc"
    PSD = "psd"
    PSE = "pse"
    PSG = "psg"
    PSH = "psh"
    PSI = "psi"
    PSL = "psl"
    PSM = "psm"
    PSN = "psn"
    PSO = "pso"
    PSP = "psp"
    PSQ = "psq"
    PSR = "psr"
    PSS = "pss"
    PST = "pst"
    PSW = "psw"
    PSY = "psy"
    PTA = "pta"
    PTH = "pth"
    PTI = "pti"
    PTN = "ptn"
    PTO = "pto"
    PTP = "ptp"
    PTQ = "ptq"
    PTR = "ptr"
    PTT = "ptt"
    PTU = "ptu"
    PTV = "ptv"
    PTW = "ptw"
    PTY = "pty"
    PUA = "pua"
    PUB = "pub"
    PUC = "puc"
    PUD = "pud"
    PUE = "pue"
    PUF = "puf"
    PUG = "pug"
    PUI = "pui"
    PUJ = "puj"
    PUM = "pum"
    PUO = "puo"
    PUP = "pup"
    PUQ = "puq"
    PUR = "pur"
    PUT = "put"
    PUU = "puu"
    PUW = "puw"
    PUX = "pux"
    PUY = "puy"
    PWA = "pwa"
    PWB = "pwb"
    PWG = "pwg"
    PWI = "pwi"
    PWM = "pwm"
    PWN = "pwn"
    PWO = "pwo"
    PWR = "pwr"
    PWW = "pww"
    PXM = "pxm"
    PYE = "pye"
    PYM = "pym"
    PYN = "pyn"
    PYS = "pys"
    PYU = "pyu"
    PYY = "pyy"
    PZE = "pze"
    PZH = "pzh"
    PZN = "pzn"
    QUA = "qua"
    QUB = "qub"
    QUC = "quc"
    QUD = "qud"
    QUF = "quf"
    QUG = "qug"
    QUH = "quh"
    QUI = "qui"
    QUK = "quk"
    QUL = "qul"
    QUM = "qum"
    QUN = "qun"
    QUP = "qup"
    QUQ = "quq"
    QUR = "qur"
    QUS = "qus"
    QUV = "quv"
    QUW = "quw"
    QUX = "qux"
    QUY = "quy"
    QUZ = "quz"
    QVA = "qva"
    QVC = "qvc"
    QVE = "qve"
    QVH = "qvh"
    QVI = "qvi"
    QVJ = "qvj"
    QVL = "qvl"
    QVM = "qvm"
    QVN = "qvn"
    QVO = "qvo"
    QVP = "qvp"
    QVS = "qvs"
    QVW = "qvw"
    QVY = "qvy"
    QVZ = "qvz"
    QWA = "qwa"
    QWH = "qwh"
    QWM = "qwm"
    QWS = "qws"
    QWT = "qwt"
    QXA = "qxa"
    QXC = "qxc"
    QXH = "qxh"
    QXL = "qxl"
    QXN = "qxn"
    QXO = "qxo"
    QXP = "qxp"
    QXQ = "qxq"
    QXR = "qxr"
    QXS = "qxs"
    QXT = "qxt"
    QXU = "qxu"
    QXW = "qxw"
    QYP = "qyp"
    RAA = "raa"
    RAB = "rab"
    RAC = "rac"
    RAD = "rad"
    RAF = "raf"
    RAG = "rag"
    RAH = "rah"
    RAI = "rai"
    RAK = "rak"
    RAL = "ral"
    RAM = "ram"
    RAN = "ran"
    RAO = "rao"
    RAP = "rap"
    RAQ = "raq"
    RAR = "rar"
    RAS = "ras"
    RAT = "rat"
    RAU = "rau"
    RAV = "rav"
    RAW = "raw"
    RAX = "rax"
    RAY = "ray"
    RAZ = "raz"
    RBB = "rbb"
    RBK = "rbk"
    RBL = "rbl"
    RBP = "rbp"
    RCF = "rcf"
    RDB = "rdb"
    REA = "rea"
    REB = "reb"
    REE = "ree"
    REG = "reg"
    REI = "rei"
    REJ = "rej"
    REL = "rel"
    REM = "rem"
    REN = "ren"
    RER = "rer"
    RES = "res"
    RET = "ret"
    REY = "rey"
    RGA = "rga"
    RGE = "rge"
    RGK = "rgk"
    RGN = "rgn"
    RGR = "rgr"
    RGS = "rgs"
    RGU = "rgu"
    RHG = "rhg"
    RHP = "rhp"
    RIA = "ria"
    RIB = "rib"
    RIF = "rif"
    RIL = "ril"
    RIM = "rim"
    RIN = "rin"
    RIR = "rir"
    RIT = "rit"
    RIU = "riu"
    RJG = "rjg"
    RJI = "rji"
    RJS = "rjs"
    RKA = "rka"
    RKB = "rkb"
    RKH = "rkh"
    RKI = "rki"
    RKM = "rkm"
    RKT = "rkt"
    RKW = "rkw"
    RMA = "rma"
    RMB = "rmb"
    RMC = "rmc"
    RMD = "rmd"
    RME = "rme"
    RMF = "rmf"
    RMG = "rmg"
    RMH = "rmh"
    RMI = "rmi"
    RMK = "rmk"
    RML = "rml"
    RMM = "rmm"
    RMN = "rmn"
    RMO = "rmo"
    RMP = "rmp"
    RMQ = "rmq"
    RMS = "rms"
    RMT = "rmt"
    RMU = "rmu"
    RMW = "rmw"
    RMX = "rmx"
    RMY = "rmy"
    RMZ = "rmz"
    RNB = "rnb"
    RND = "rnd"
    RNG = "rng"
    RNL = "rnl"
    RNN = "rnn"
    RNP = "rnp"
    RNR = "rnr"
    RNW = "rnw"
    ROB = "rob"
    ROC = "roc"
    ROD = "rod"
    ROE = "roe"
    ROF = "rof"
    ROG = "rog"
    ROH = "roh"
    ROL = "rol"
    RON = "ron"
    ROO = "roo"
    ROP = "rop"
    ROR = "ror"
    ROU = "rou"
    ROW = "row"
    RPN = "rpn"
    RPT = "rpt"
    RRI = "rri"
    RRM = "rrm"
    RRO = "rro"
    RRT = "rrt"
    RSB = "rsb"
    RSK = "rsk"
    RSL = "rsl"
    RSM = "rsm"
    RSN = "rsn"
    RSW = "rsw"
    RTC = "rtc"
    RTH = "rth"
    RTM = "rtm"
    RTS = "rts"
    RTW = "rtw"
    RUB = "rub"
    RUC = "ruc"
    RUE = "rue"
    RUF = "ruf"
    RUG = "rug"
    RUH = "ruh"
    RUK = "ruk"
    RUN = "run"
    RUO = "ruo"
    RUP = "rup"
    RUQ = "ruq"
    RUS = "rus"
    RUT = "rut"
    RUU = "ruu"
    RUY = "ruy"
    RUZ = "ruz"
    RWA = "rwa"
    RWK = "rwk"
    RWL = "rwl"
    RWM = "rwm"
    RWO = "rwo"
    RWR = "rwr"
    RXD = "rxd"
    RXW = "rxw"
    RYN = "ryn"
    RYS = "rys"
    RYU = "ryu"
    RZH = "rzh"
    SAA = "saa"
    SAB = "sab"
    SAC = "sac"
    SAD = "sad"
    SAE = "sae"
    SAF = "saf"
    SAG = "sag"
    SAH = "sah"
    SAJ = "saj"
    SAK = "sak"
    SAM = "sam"
    SAN = "san"
    SAO = "sao"
    SAQ = "saq"
    SAR = "sar"
    SAS = "sas"
    SAT = "sat"
    SAU = "sau"
    SAV = "sav"
    SAW = "saw"
    SAX = "sax"
    SAY = "say"
    SAZ = "saz"
    SBA = "sba"
    SBB = "sbb"
    SBC = "sbc"
    SBD = "sbd"
    SBE = "sbe"
    SBF = "sbf"
    SBG = "sbg"
    SBH = "sbh"
    SBI = "sbi"
    SBJ = "sbj"
    SBK = "sbk"
    SBL = "sbl"
    SBM = "sbm"
    SBN = "sbn"
    SBO = "sbo"
    SBP = "sbp"
    SBQ = "sbq"
    SBR = "sbr"
    SBS = "sbs"
    SBT = "sbt"
    SBU = "sbu"
    SBW = "sbw"
    SBX = "sbx"
    SBY = "sby"
    SBZ = "sbz"
    SCB = "scb"
    SCE = "sce"
    SCF = "scf"
    SCG = "scg"
    SCH = "sch"
    SCI = "sci"
    SCK = "sck"
    SCL = "scl"
    SCN = "scn"
    SCO = "sco"
    SCP = "scp"
    SCQ = "scq"
    SCS = "scs"
    SCT = "sct"
    SCU = "scu"
    SCV = "scv"
    SCW = "scw"
    SDA = "sda"
    SDB = "sdb"
    SDC = "sdc"
    SDE = "sde"
    SDF = "sdf"
    SDG = "sdg"
    SDH = "sdh"
    SDJ = "sdj"
    SDK = "sdk"
    SDL = "sdl"
    SDN = "sdn"
    SDO = "sdo"
    SDP = "sdp"
    SDQ = "sdq"
    SDR = "sdr"
    SDS = "sds"
    SDT = "sdt"
    SDU = "sdu"
    SDX = "sdx"
    SDZ = "sdz"
    SEA = "sea"
    SEB = "seb"
    SEC = "sec"
    SED = "sed"
    SEE = "see"
    SEF = "sef"
    SEG = "seg"
    SEH = "seh"
    SEI = "sei"
    SEJ = "sej"
    SEK = "sek"
    SEL = "sel"
    SEN = "sen"
    SEO = "seo"
    SEP = "sep"
    SEQ = "seq"
    SER = "ser"
    SES = "ses"
    SET = "set"
    SEU = "seu"
    SEV = "sev"
    SEW = "sew"
    SEY = "sey"
    SEZ = "sez"
    SFB = "sfb"
    SFE = "sfe"
    SFM = "sfm"
    SFS = "sfs"
    SFW = "sfw"
    SGB = "sgb"
    SGC = "sgc"
    SGD = "sgd"
    SGE = "sge"
    SGG = "sgg"
    SGH = "sgh"
    SGI = "sgi"
    SGJ = "sgj"
    SGK = "sgk"
    SGM = "sgm"
    SGP = "sgp"
    SGR = "sgr"
    SGS = "sgs"
    SGT = "sgt"
    SGU = "sgu"
    SGW = "sgw"
    SGX = "sgx"
    SGY = "sgy"
    SGZ = "sgz"
    SHA = "sha"
    SHB = "shb"
    SHC = "shc"
    SHD = "shd"
    SHE = "she"
    SHG = "shg"
    SHH = "shh"
    SHI = "shi"
    SHJ = "shj"
    SHK = "shk"
    SHL = "shl"
    SHM = "shm"
    SHN = "shn"
    SHO = "sho"
    SHP = "shp"
    SHQ = "shq"
    SHR = "shr"
    SHS = "shs"
    SHT = "sht"
    SHU = "shu"
    SHV = "shv"
    SHW = "shw"
    SHX = "shx"
    SHY = "shy"
    SHZ = "shz"
    SIA = "sia"
    SIB = "sib"
    SID = "sid"
    SIE = "sie"
    SIF = "sif"
    SIG = "sig"
    SIH = "sih"
    SII = "sii"
    SIJ = "sij"
    SIK = "sik"
    SIL = "sil"
    SIM = "sim"
    SIN = "sin"
    SIP = "sip"
    SIQ = "siq"
    SIR = "sir"
    SIS = "sis"
    SIU = "siu"
    SIV = "siv"
    SIW = "siw"
    SIX = "six"
    SIY = "siy"
    SIZ = "siz"
    SJA = "sja"
    SJB = "sjb"
    SJC = "sjc"
    SJD = "sjd"
    SJE = "sje"
    SJG = "sjg"
    SJK = "sjk"
    SJL = "sjl"
    SJM = "sjm"
    SJO = "sjo"
    SJP = "sjp"
    SJR = "sjr"
    SJS = "sjs"
    SJT = "sjt"
    SJU = "sju"
    SJW = "sjw"
    SKA = "ska"
    SKB = "skb"
    SKC = "skc"
    SKD = "skd"
    SKE = "ske"
    SKF = "skf"
    SKG = "skg"
    SKH = "skh"
    SKI = "ski"
    SKJ = "skj"
    SKM = "skm"
    SKN = "skn"
    SKO = "sko"
    SKP = "skp"
    SKQ = "skq"
    SKR = "skr"
    SKS = "sks"
    SKT = "skt"
    SKU = "sku"
    SKV = "skv"
    SKW = "skw"
    SKX = "skx"
    SKY = "sky"
    SKZ = "skz"
    SLC = "slc"
    SLD = "sld"
    SLE = "sle"
    SLF = "slf"
    SLG = "slg"
    SLH = "slh"
    SLI = "sli"
    SLJ = "slj"
    SLK = "slk"
    SLL = "sll"
    SLM = "slm"
    SLN = "sln"
    SLP = "slp"
    SLR = "slr"
    SLS = "sls"
    SLT = "slt"
    SLU = "slu"
    SLV = "slv"
    SLW = "slw"
    SLX = "slx"
    SLY = "sly"
    SLZ = "slz"
    SMA = "sma"
    SMB = "smb"
    SMC = "smc"
    SME = "sme"
    SMF = "smf"
    SMG = "smg"
    SMH = "smh"
    SMJ = "smj"
    SMK = "smk"
    SML = "sml"
    SMM = "smm"
    SMN = "smn"
    SMO = "smo"
    SMP = "smp"
    SMQ = "smq"
    SMR = "smr"
    SMS = "sms"
    SMT = "smt"
    SMU = "smu"
    SMV = "smv"
    SMW = "smw"
    SMX = "smx"
    SMY = "smy"
    SMZ = "smz"
    SNA = "sna"
    SNC = "snc"
    SND = "snd"
    SNE = "sne"
    SNF = "snf"
    SNG = "sng"
    SNI = "sni"
    SNJ = "snj"
    SNK = "snk"
    SNL = "snl"
    SNM = "snm"
    SNN = "snn"
    SNO = "sno"
    SNP = "snp"
    SNQ = "snq"
    SNR = "snr"
    SNS = "sns"
    SNU = "snu"
    SNV = "snv"
    SNW = "snw"
    SNX = "snx"
    SNY = "sny"
    SNZ = "snz"
    SOA = "soa"
    SOB = "sob"
    SOC = "soc"
    SOD = "sod"
    SOE = "soe"
    SOH = "soh"
    SOI = "soi"
    SOJ = "soj"
    SOK = "sok"
    SOL = "sol"
    SOM = "som"
    SOO = "soo"
    SOP = "sop"
    SOQ = "soq"
    SOR = "sor"
    SOS = "sos"
    SOT = "sot"
    SOU = "sou"
    SOV = "sov"
    SOW = "sow"
    SOX = "sox"
    SOY = "soy"
    SOZ = "soz"
    SPA = "spa"
    SPB = "spb"
    SPC = "spc"
    SPD = "spd"
    SPE = "spe"
    SPG = "spg"
    SPI = "spi"
    SPK = "spk"
    SPL = "spl"
    SPM = "spm"
    SPN = "spn"
    SPO = "spo"
    SPP = "spp"
    SPQ = "spq"
    SPR = "spr"
    SPS = "sps"
    SPT = "spt"
    SPU = "spu"
    SPV = "spv"
    SPY = "spy"
    SQA = "sqa"
    SQH = "sqh"
    SQK = "sqk"
    SQM = "sqm"
    SQN = "sqn"
    SQO = "sqo"
    SQQ = "sqq"
    SQS = "sqs"
    SQT = "sqt"
    SQU = "squ"
    SQX = "sqx"
    SRA = "sra"
    SRB = "srb"
    SRC = "src"
    SRE = "sre"
    SRF = "srf"
    SRG = "srg"
    SRH = "srh"
    SRI = "sri"
    SRK = "srk"
    SRL = "srl"
    SRM = "srm"
    SRN = "srn"
    SRO = "sro"
    SRP = "srp"
    SRQ = "srq"
    SRR = "srr"
    SRS = "srs"
    SRT = "srt"
    SRU = "sru"
    SRV = "srv"
    SRW = "srw"
    SRX = "srx"
    SRY = "sry"
    SRZ = "srz"
    SSB = "ssb"
    SSC = "ssc"
    SSD = "ssd"
    SSE = "sse"
    SSF = "ssf"
    SSG = "ssg"
    SSH = "ssh"
    SSI = "ssi"
    SSJ = "ssj"
    SSK = "ssk"
    SSL = "ssl"
    SSM = "ssm"
    SSN = "ssn"
    SSO = "sso"
    SSP = "ssp"
    SSQ = "ssq"
    SSR = "ssr"
    SSS = "sss"
    SST = "sst"
    SSU = "ssu"
    SSV = "ssv"
    SSW = "ssw"
    SSX = "ssx"
    SSY = "ssy"
    SSZ = "ssz"
    STA = "sta"
    STB = "stb"
    STD = "std"
    STE = "ste"
    STF = "stf"
    STG = "stg"
    STH = "sth"
    STI = "sti"
    STJ = "stj"
    STK = "stk"
    STL = "stl"
    STM = "stm"
    STN = "stn"
    STO = "sto"
    STP = "stp"
    STQ = "stq"
    STR = "str"
    STS = "sts"
    STT = "stt"
    STU = "stu"
    STV = "stv"
    STW = "stw"
    STY = "sty"
    SUA = "sua"
    SUB = "sub"
    SUC = "suc"
    SUE = "sue"
    SUG = "sug"
    SUI = "sui"
    SUJ = "suj"
    SUK = "suk"
    SUN = "sun"
    SUO = "suo"
    SUQ = "suq"
    SUR = "sur"
    SUS = "sus"
    SUT = "sut"
    SUV = "suv"
    SUW = "suw"
    SUY = "suy"
    SUZ = "suz"
    SVA = "sva"
    SVB = "svb"
    SVC = "svc"
    SVE = "sve"
    SVK = "svk"
    SVM = "svm"
    SVS = "svs"
    SWB = "swb"
    SWC = "swc"
    SWE = "swe"
    SWF = "swf"
    SWG = "swg"
    SWH = "swh"
    SWI = "swi"
    SWJ = "swj"
    SWK = "swk"
    SWL = "swl"
    SWM = "swm"
    SWN = "swn"
    SWO = "swo"
    SWP = "swp"
    SWQ = "swq"
    SWR = "swr"
    SWS = "sws"
    SWT = "swt"
    SWU = "swu"
    SWV = "swv"
    SWW = "sww"
    SWX = "swx"
    SWY = "swy"
    SXB = "sxb"
    SXE = "sxe"
    SXG = "sxg"
    SXK = "sxk"
    SXM = "sxm"
    SXN = "sxn"
    SXR = "sxr"
    SXS = "sxs"
    SXU = "sxu"
    SXW = "sxw"
    SYA = "sya"
    SYB = "syb"
    SYC = "syc"
    SYI = "syi"
    SYK = "syk"
    SYL = "syl"
    SYM = "sym"
    SYN = "syn"
    SYO = "syo"
    SYS = "sys"
    SYW = "syw"
    SYX = "syx"
    SYY = "syy"
    SZA = "sza"
    SZB = "szb"
    SZC = "szc"
    SZE = "sze"
    SZG = "szg"
    SZL = "szl"
    SZN = "szn"
    SZP = "szp"
    SZS = "szs"
    SZV = "szv"
    SZW = "szw"
    SZY = "szy"
    TAA = "taa"
    TAB = "tab"
    TAC = "tac"
    TAD = "tad"
    TAE = "tae"
    TAF = "taf"
    TAG = "tag"
    TAH = "tah"
    TAJ = "taj"
    TAK = "tak"
    TAL = "tal"
    TAM = "tam"
    TAN = "tan"
    TAO = "tao"
    TAP = "tap"
    TAQ = "taq"
    TAR = "tar"
    TAS = "tas"
    TAT = "tat"
    TAU = "tau"
    TAV = "tav"
    TAW = "taw"
    TAX = "tax"
    TAY = "tay"
    TAZ = "taz"
    TBA = "tba"
    TBC = "tbc"
    TBD = "tbd"
    TBE = "tbe"
    TBF = "tbf"
    TBG = "tbg"
    TBH = "tbh"
    TBI = "tbi"
    TBJ = "tbj"
    TBK = "tbk"
    TBL = "tbl"
    TBM = "tbm"
    TBN = "tbn"
    TBO = "tbo"
    TBP = "tbp"
    TBR = "tbr"
    TBS = "tbs"
    TBT = "tbt"
    TBU = "tbu"
    TBV = "tbv"
    TBW = "tbw"
    TBX = "tbx"
    TBY = "tby"
    TBZ = "tbz"
    TCA = "tca"
    TCB = "tcb"
    TCC = "tcc"
    TCD = "tcd"
    TCE = "tce"
    TCF = "tcf"
    TCG = "tcg"
    TCH = "tch"
    TCI = "tci"
    TCK = "tck"
    TCL = "tcl"
    TCM = "tcm"
    TCN = "tcn"
    TCO = "tco"
    TCP = "tcp"
    TCQ = "tcq"
    TCS = "tcs"
    TCT = "tct"
    TCU = "tcu"
    TCW = "tcw"
    TCX = "tcx"
    TCY = "tcy"
    TCZ = "tcz"
    TDA = "tda"
    TDB = "tdb"
    TDC = "tdc"
    TDD = "tdd"
    TDE = "tde"
    TDF = "tdf"
    TDG = "tdg"
    TDH = "tdh"
    TDI = "tdi"
    TDJ = "tdj"
    TDK = "tdk"
    TDL = "tdl"
    TDM = "tdm"
    TDN = "tdn"
    TDO = "tdo"
    TDQ = "tdq"
    TDR = "tdr"
    TDS = "tds"
    TDT = "tdt"
    TDV = "tdv"
    TDX = "tdx"
    TDY = "tdy"
    TEA = "tea"
    TEB = "teb"
    TEC = "tec"
    TED = "ted"
    TEE = "tee"
    TEF = "tef"
    TEG = "teg"
    TEH = "teh"
    TEI = "tei"
    TEK = "tek"
    TEL = "tel"
    TEM = "tem"
    TEN = "ten"
    TEO = "teo"
    TEP = "tep"
    TEQ = "teq"
    TER = "ter"
    TES = "tes"
    TET = "tet"
    TEU = "teu"
    TEV = "tev"
    TEW = "tew"
    TEX = "tex"
    TEY = "tey"
    TEZ = "tez"
    TFI = "tfi"
    TFN = "tfn"
    TFO = "tfo"
    TFR = "tfr"
    TFT = "tft"
    TGA = "tga"
    TGB = "tgb"
    TGC = "tgc"
    TGD = "tgd"
    TGE = "tge"
    TGF = "tgf"
    TGH = "tgh"
    TGI = "tgi"
    TGJ = "tgj"
    TGK = "tgk"
    TGL = "tgl"
    TGN = "tgn"
    TGO = "tgo"
    TGP = "tgp"
    TGQ = "tgq"
    TGR = "tgr"
    TGS = "tgs"
    TGT = "tgt"
    TGU = "tgu"
    TGV = "tgv"
    TGW = "tgw"
    TGX = "tgx"
    TGY = "tgy"
    TGZ = "tgz"
    THA = "tha"
    THD = "thd"
    THE = "the"
    THF = "thf"
    THH = "thh"
    THI = "thi"
    THK = "thk"
    THL = "thl"
    THM = "thm"
    THN = "thn"
    THP = "thp"
    THQ = "thq"
    THR = "thr"
    THS = "ths"
    THT = "tht"
    THU = "thu"
    THV = "thv"
    THY = "thy"
    THZ = "thz"
    TIA = "tia"
    TIC = "tic"
    TIF = "tif"
    TIG = "tig"
    TIH = "tih"
    TII = "tii"
    TIJ = "tij"
    TIK = "tik"
    TIL = "til"
    TIM = "tim"
    TIN = "tin"
    TIO = "tio"
    TIP = "tip"
    TIQ = "tiq"
    TIR = "tir"
    TIS = "tis"
    TIT = "tit"
    TIU = "tiu"
    TIV = "tiv"
    TIW = "tiw"
    TIX = "tix"
    TIY = "tiy"
    TIZ = "tiz"
    TJA = "tja"
    TJG = "tjg"
    TJI = "tji"
    TJJ = "tjj"
    TJL = "tjl"
    TJM = "tjm"
    TJN = "tjn"
    TJO = "tjo"
    TJP = "tjp"
    TJS = "tjs"
    TJU = "tju"
    TJW = "tjw"
    TKA = "tka"
    TKB = "tkb"
    TKD = "tkd"
    TKE = "tke"
    TKF = "tkf"
    TKG = "tkg"
    TKL = "tkl"
    TKM = "tkm"
    TKN = "tkn"
    TKP = "tkp"
    TKQ = "tkq"
    TKR = "tkr"
    TKS = "tks"
    TKT = "tkt"
    TKU = "tku"
    TKV = "tkv"
    TKW = "tkw"
    TKX = "tkx"
    TKZ = "tkz"
    TLA = "tla"
    TLB = "tlb"
    TLC = "tlc"
    TLD = "tld"
    TLF = "tlf"
    TLG = "tlg"
    TLI = "tli"
    TLJ = "tlj"
    TLK = "tlk"
    TLL = "tll"
    TLM = "tlm"
    TLN = "tln"
    TLO = "tlo"
    TLP = "tlp"
    TLQ = "tlq"
    TLR = "tlr"
    TLS = "tls"
    TLT = "tlt"
    TLU = "tlu"
    TLV = "tlv"
    TLX = "tlx"
    TLY = "tly"
    TMA = "tma"
    TMB = "tmb"
    TMC = "tmc"
    TMD = "tmd"
    TME = "tme"
    TMF = "tmf"
    TMG = "tmg"
    TMI = "tmi"
    TMJ = "tmj"
    TML = "tml"
    TMM = "tmm"
    TMN = "tmn"
    TMO = "tmo"
    TMQ = "tmq"
    TMR = "tmr"
    TMS = "tms"
    TMT = "tmt"
    TMU = "tmu"
    TMV = "tmv"
    TMW = "tmw"
    TMY = "tmy"
    TMZ = "tmz"
    TNA = "tna"
    TNB = "tnb"
    TNC = "tnc"
    TND = "tnd"
    TNG = "tng"
    TNH = "tnh"
    TNI = "tni"
    TNK = "tnk"
    TNL = "tnl"
    TNM = "tnm"
    TNN = "tnn"
    TNO = "tno"
    TNP = "tnp"
    TNQ = "tnq"
    TNR = "tnr"
    TNS = "tns"
    TNT = "tnt"
    TNU = "tnu"
    TNV = "tnv"
    TNW = "tnw"
    TNX = "tnx"
    TNY = "tny"
    TNZ = "tnz"
    TOB = "tob"
    TOC = "toc"
    TOD = "tod"
    TOF = "tof"
    TOG = "tog"
    TOH = "toh"
    TOI = "toi"
    TOJ = "toj"
    TOL = "tol"
    TOM = "tom"
    TON = "ton"
    TOO = "too"
    TOP = "top"
    TOQ = "toq"
    TOR = "tor"
    TOS = "tos"
    TOU = "tou"
    TOV = "tov"
    TOW = "tow"
    TOX = "tox"
    TOY = "toy"
    TOZ = "toz"
    TPA = "tpa"
    TPC = "tpc"
    TPE = "tpe"
    TPF = "tpf"
    TPG = "tpg"
    TPI = "tpi"
    TPJ = "tpj"
    TPK = "tpk"
    TPL = "tpl"
    TPM = "tpm"
    TPN = "tpn"
    TPO = "tpo"
    TPP = "tpp"
    TPQ = "tpq"
    TPR = "tpr"
    TPT = "tpt"
    TPU = "tpu"
    TPV = "tpv"
    TPX = "tpx"
    TPY = "tpy"
    TPZ = "tpz"
    TQB = "tqb"
    TQL = "tql"
    TQM = "tqm"
    TQN = "tqn"
    TQO = "tqo"
    TQP = "tqp"
    TQQ = "tqq"
    TQR = "tqr"
    TQT = "tqt"
    TQU = "tqu"
    TQW = "tqw"
    TRA = "tra"
    TRB = "trb"
    TRC = "trc"
    TRD = "trd"
    TRE = "tre"
    TRF = "trf"
    TRG = "trg"
    TRH = "trh"
    TRI = "tri"
    TRJ = "trj"
    TRL = "trl"
    TRM = "trm"
    TRN = "trn"
    TRO = "tro"
    TRP = "trp"
    TRQ = "trq"
    TRR = "trr"
    TRS = "trs"
    TRT = "trt"
    TRU = "tru"
    TRV = "trv"
    TRW = "trw"
    TRX = "trx"
    TRY = "try"
    TRZ = "trz"
    TSA = "tsa"
    TSB = "tsb"
    TSC = "tsc"
    TSD = "tsd"
    TSE = "tse"
    TSG = "tsg"
    TSH = "tsh"
    TSI = "tsi"
    TSJ = "tsj"
    TSK = "tsk"
    TSL = "tsl"
    TSM = "tsm"
    TSN = "tsn"
    TSO = "tso"
    TSP = "tsp"
    TSQ = "tsq"
    TSR = "tsr"
    TSS = "tss"
    TST = "tst"
    TSU = "tsu"
    TSV = "tsv"
    TSW = "tsw"
    TSX = "tsx"
    TSY = "tsy"
    TSZ = "tsz"
    TTA = "tta"
    TTB = "ttb"
    TTC = "ttc"
    TTD = "ttd"
    TTE = "tte"
    TTF = "ttf"
    TTG = "ttg"
    TTH = "tth"
    TTI = "tti"
    TTJ = "ttj"
    TTK = "ttk"
    TTL = "ttl"
    TTM = "ttm"
    TTN = "ttn"
    TTO = "tto"
    TTP = "ttp"
    TTQ = "ttq"
    TTR = "ttr"
    TTS = "tts"
    TTT = "ttt"
    TTU = "ttu"
    TTV = "ttv"
    TTW = "ttw"
    TTY = "tty"
    TTZ = "ttz"
    TUA = "tua"
    TUB = "tub"
    TUC = "tuc"
    TUD = "tud"
    TUE = "tue"
    TUF = "tuf"
    TUG = "tug"
    TUH = "tuh"
    TUI = "tui"
    TUJ = "tuj"
    TUK = "tuk"
    TUL = "tul"
    TUM = "tum"
    TUN = "tun"
    TUO = "tuo"
    TUQ = "tuq"
    TUR = "tur"
    TUS = "tus"
    TUU = "tuu"
    TUV = "tuv"
    TUX = "tux"
    TUY = "tuy"
    TUZ = "tuz"
    TVA = "tva"
    TVD = "tvd"
    TVE = "tve"
    TVI = "tvi"
    TVK = "tvk"
    TVL = "tvl"
    TVM = "tvm"
    TVN = "tvn"
    TVO = "tvo"
    TVS = "tvs"
    TVT = "tvt"
    TVU = "tvu"
    TVW = "tvw"
    TVX = "tvx"
    TVY = "tvy"
    TWA = "twa"
    TWB = "twb"
    TWC = "twc"
    TWD = "twd"
    TWE = "twe"
    TWF = "twf"
    TWG = "twg"
    TWH = "twh"
    TWL = "twl"
    TWM = "twm"
    TWN = "twn"
    TWO = "two"
    TWP = "twp"
    TWQ = "twq"
    TWR = "twr"
    TWT = "twt"
    TWU = "twu"
    TWW = "tww"
    TWX = "twx"
    TWY = "twy"
    TXA = "txa"
    TXC = "txc"
    TXE = "txe"
    TXI = "txi"
    TXJ = "txj"
    TXM = "txm"
    TXN = "txn"
    TXO = "txo"
    TXQ = "txq"
    TXS = "txs"
    TXT = "txt"
    TXU = "txu"
    TXX = "txx"
    TXY = "txy"
    TYA = "tya"
    TYE = "tye"
    TYH = "tyh"
    TYI = "tyi"
    TYJ = "tyj"
    TYL = "tyl"
    TYN = "tyn"
    TYP = "typ"
    TYR = "tyr"
    TYS = "tys"
    TYT = "tyt"
    TYU = "tyu"
    TYV = "tyv"
    TYX = "tyx"
    TYY = "tyy"
    TYZ = "tyz"
    TZA = "tza"
    TZH = "tzh"
    TZJ = "tzj"
    TZM = "tzm"
    TZN = "tzn"
    TZO = "tzo"
    TZX = "tzx"
    UAM = "uam"
    UAN = "uan"
    UAR = "uar"
    UBA = "uba"
    UBI = "ubi"
    UBL = "ubl"
    UBR = "ubr"
    UBU = "ubu"
    UBY = "uby"
    UDA = "uda"
    UDE = "ude"
    UDG = "udg"
    UDI = "udi"
    UDJ = "udj"
    UDL = "udl"
    UDM = "udm"
    UDU = "udu"
    UES = "ues"
    UFI = "ufi"
    UGB = "ugb"
    UGE = "uge"
    UGH = "ugh"
    UGN = "ugn"
    UGO = "ugo"
    UGY = "ugy"
    UHA = "uha"
    UHN = "uhn"
    UIG = "uig"
    UIS = "uis"
    UIV = "uiv"
    UJI = "uji"
    UKA = "uka"
    UKG = "ukg"
    UKH = "ukh"
    UKI = "uki"
    UKK = "ukk"
    UKL = "ukl"
    UKP = "ukp"
    UKQ = "ukq"
    UKR = "ukr"
    UKS = "uks"
    UKU = "uku"
    UKV = "ukv"
    UKW = "ukw"
    UKY = "uky"
    ULA = "ula"
    ULB = "ulb"
    ULC = "ulc"
    ULE = "ule"
    ULF = "ulf"
    ULI = "uli"
    ULK = "ulk"
    ULL = "ull"
    ULM = "ulm"
    ULN = "uln"
    ULU = "ulu"
    ULW = "ulw"
    ULY = "uly"
    UMA = "uma"
    UMB = "umb"
    UMD = "umd"
    UMG = "umg"
    UMI = "umi"
    UMM = "umm"
    UMN = "umn"
    UMO = "umo"
    UMP = "ump"
    UMR = "umr"
    UMS = "ums"
    UMU = "umu"
    UNA = "una"
    UNE = "une"
    UNG = "ung"
    UNI = "uni"
    UNK = "unk"
    UNM = "unm"
    UNN = "unn"
    UNR = "unr"
    UNU = "unu"
    UNX = "unx"
    UNZ = "unz"
    UON = "uon"
    UPI = "upi"
    UPV = "upv"
    URA = "ura"
    URB = "urb"
    URC = "urc"
    URD = "urd"
    URE = "ure"
    URF = "urf"
    URG = "urg"
    URH = "urh"
    URI = "uri"
    URK = "urk"
    URL = "url"
    URM = "urm"
    URN = "urn"
    URO = "uro"
    URP = "urp"
    URR = "urr"
    URT = "urt"
    URU = "uru"
    URV = "urv"
    URW = "urw"
    URX = "urx"
    URY = "ury"
    URZ = "urz"
    USA = "usa"
    USH = "ush"
    USI = "usi"
    USK = "usk"
    USP = "usp"
    USS = "uss"
    USU = "usu"
    UTA = "uta"
    UTE = "ute"
    UTH = "uth"
    UTP = "utp"
    UTR = "utr"
    UTU = "utu"
    UUM = "uum"
    UUR = "uur"
    UUU = "uuu"
    UVE = "uve"
    UVH = "uvh"
    UVL = "uvl"
    UWA = "uwa"
    UYA = "uya"
    UZN = "uzn"
    UZS = "uzs"
    VAA = "vaa"
    VAE = "vae"
    VAF = "vaf"
    VAG = "vag"
    VAH = "vah"
    VAI = "vai"
    VAJ = "vaj"
    VAL = "val"
    VAM = "vam"
    VAN = "van"
    VAO = "vao"
    VAP = "vap"
    VAR = "var"
    VAS = "vas"
    VAU = "vau"
    VAV = "vav"
    VAY = "vay"
    VBB = "vbb"
    VBK = "vbk"
    VEC = "vec"
    VED = "ved"
    VEL = "vel"
    VEM = "vem"
    VEN = "ven"
    VEO = "veo"
    VEP = "vep"
    VER = "ver"
    VGR = "vgr"
    VGT = "vgt"
    VIC = "vic"
    VID = "vid"
    VIE = "vie"
    VIF = "vif"
    VIG = "vig"
    VIL = "vil"
    VIS = "vis"
    VIT = "vit"
    VIV = "viv"
    VJK = "vjk"
    VKA = "vka"
    VKJ = "vkj"
    VKK = "vkk"
    VKL = "vkl"
    VKM = "vkm"
    VKN = "vkn"
    VKO = "vko"
    VKP = "vkp"
    VKT = "vkt"
    VKU = "vku"
    VKZ = "vkz"
    VLP = "vlp"
    VLS = "vls"
    VMA = "vma"
    VMB = "vmb"
    VMC = "vmc"
    VMD = "vmd"
    VME = "vme"
    VMF = "vmf"
    VMG = "vmg"
    VMH = "vmh"
    VMI = "vmi"
    VMJ = "vmj"
    VMK = "vmk"
    VML = "vml"
    VMM = "vmm"
    VMP = "vmp"
    VMQ = "vmq"
    VMR = "vmr"
    VMS = "vms"
    VMU = "vmu"
    VMV = "vmv"
    VMW = "vmw"
    VMX = "vmx"
    VMY = "vmy"
    VMZ = "vmz"
    VNK = "vnk"
    VNM = "vnm"
    VNP = "vnp"
    VOR = "vor"
    VOT = "vot"
    VRA = "vra"
    VRO = "vro"
    VRS = "vrs"
    VRT = "vrt"
    VSI = "vsi"
    VSL = "vsl"
    VSV = "vsv"
    VTO = "vto"
    VUM = "vum"
    VUN = "vun"
    VUT = "vut"
    VWA = "vwa"
    WAA = "waa"
    WAB = "wab"
    WAC = "wac"
    WAD = "wad"
    WAE = "wae"
    WAF = "waf"
    WAG = "wag"
    WAH = "wah"
    WAI = "wai"
    WAJ = "waj"
    WAL = "wal"
    WAM = "wam"
    WAN = "wan"
    WAO = "wao"
    WAP = "wap"
    WAQ = "waq"
    WAR = "war"
    WAS = "was"
    WAT = "wat"
    WAU = "wau"
    WAV = "wav"
    WAW = "waw"
    WAX = "wax"
    WAY = "way"
    WAZ = "waz"
    WBA = "wba"
    WBB = "wbb"
    WBE = "wbe"
    WBF = "wbf"
    WBH = "wbh"
    WBI = "wbi"
    WBJ = "wbj"
    WBK = "wbk"
    WBL = "wbl"
    WBM = "wbm"
    WBP = "wbp"
    WBQ = "wbq"
    WBR = "wbr"
    WBS = "wbs"
    WBT = "wbt"
    WBV = "wbv"
    WBW = "wbw"
    WCA = "wca"
    WCI = "wci"
    WDD = "wdd"
    WDG = "wdg"
    WDJ = "wdj"
    WDK = "wdk"
    WDT = "wdt"
    WDU = "wdu"
    WDY = "wdy"
    WEA = "wea"
    WEC = "wec"
    WED = "wed"
    WEG = "weg"
    WEH = "weh"
    WEI = "wei"
    WEM = "wem"
    WEO = "weo"
    WEP = "wep"
    WER = "wer"
    WES = "wes"
    WET = "wet"
    WEU = "weu"
    WEW = "wew"
    WFG = "wfg"
    WGA = "wga"
    WGB = "wgb"
    WGG = "wgg"
    WGI = "wgi"
    WGO = "wgo"
    WGU = "wgu"
    WGY = "wgy"
    WHA = "wha"
    WHG = "whg"
    WHK = "whk"
    WHU = "whu"
    WIB = "wib"
    WIC = "wic"
    WIE = "wie"
    WIF = "wif"
    WIG = "wig"
    WIH = "wih"
    WII = "wii"
    WIJ = "wij"
    WIK = "wik"
    WIL = "wil"
    WIM = "wim"
    WIN = "win"
    WIR = "wir"
    WIU = "wiu"
    WIV = "wiv"
    WIY = "wiy"
    WJA = "wja"
    WJI = "wji"
    WKA = "wka"
    WKB = "wkb"
    WKD = "wkd"
    WKL = "wkl"
    WKR = "wkr"
    WKU = "wku"
    WKW = "wkw"
    WKY = "wky"
    WLA = "wla"
    WLC = "wlc"
    WLE = "wle"
    WLG = "wlg"
    WLH = "wlh"
    WLI = "wli"
    WLK = "wlk"
    WLL = "wll"
    WLN = "wln"
    WLO = "wlo"
    WLR = "wlr"
    WLS = "wls"
    WLU = "wlu"
    WLV = "wlv"
    WLW = "wlw"
    WLX = "wlx"
    WMB = "wmb"
    WMC = "wmc"
    WMD = "wmd"
    WME = "wme"
    WMG = "wmg"
    WMH = "wmh"
    WMI = "wmi"
    WMM = "wmm"
    WMN = "wmn"
    WMO = "wmo"
    WMS = "wms"
    WMT = "wmt"
    WMW = "wmw"
    WMX = "wmx"
    WNB = "wnb"
    WNC = "wnc"
    WND = "wnd"
    WNE = "wne"
    WNG = "wng"
    WNI = "wni"
    WNK = "wnk"
    WNM = "wnm"
    WNN = "wnn"
    WNO = "wno"
    WNP = "wnp"
    WNU = "wnu"
    WNW = "wnw"
    WNY = "wny"
    WOA = "woa"
    WOB = "wob"
    WOC = "woc"
    WOD = "wod"
    WOE = "woe"
    WOF = "wof"
    WOG = "wog"
    WOI = "woi"
    WOK = "wok"
    WOL = "wol"
    WOM = "wom"
    WON = "won"
    WOO = "woo"
    WOR = "wor"
    WOS = "wos"
    WOW = "wow"
    WOY = "woy"
    WPC = "wpc"
    WRB = "wrb"
    WRG = "wrg"
    WRH = "wrh"
    WRI = "wri"
    WRK = "wrk"
    WRL = "wrl"
    WRM = "wrm"
    WRN = "wrn"
    WRO = "wro"
    WRP = "wrp"
    WRR = "wrr"
    WRS = "wrs"
    WRU = "wru"
    WRV = "wrv"
    WRW = "wrw"
    WRX = "wrx"
    WRY = "wry"
    WRZ = "wrz"
    WSA = "wsa"
    WSG = "wsg"
    WSI = "wsi"
    WSK = "wsk"
    WSR = "wsr"
    WSS = "wss"
    WSU = "wsu"
    WSV = "wsv"
    WTB = "wtb"
    WTF = "wtf"
    WTH = "wth"
    WTI = "wti"
    WTK = "wtk"
    WTM = "wtm"
    WTW = "wtw"
    WUA = "wua"
    WUB = "wub"
    WUD = "wud"
    WUH = "wuh"
    WUL = "wul"
    WUM = "wum"
    WUN = "wun"
    WUT = "wut"
    WUU = "wuu"
    WUV = "wuv"
    WUX = "wux"
    WUY = "wuy"
    WWA = "wwa"
    WWB = "wwb"
    WWO = "wwo"
    WWR = "wwr"
    WWW = "www"
    WXA = "wxa"
    WXW = "wxw"
    WYB = "wyb"
    WYI = "wyi"
    WYM = "wym"
    WYN = "wyn"
    WYR = "wyr"
    WYY = "wyy"
    XAB = "xab"
    XAC = "xac"
    XAD = "xad"
    XAI = "xai"
    XAJ = "xaj"
    XAK = "xak"
    XAL = "xal"
    XAM = "xam"
    XAN = "xan"
    XAO = "xao"
    XAP = "xap"
    XAR = "xar"
    XAS = "xas"
    XAT = "xat"
    XAU = "xau"
    XAV = "xav"
    XAW = "xaw"
    XAY = "xay"
    XBB = "xbb"
    XBD = "xbd"
    XBE = "xbe"
    XBG = "xbg"
    XBI = "xbi"
    XBJ = "xbj"
    XBN = "xbn"
    XBP = "xbp"
    XBR = "xbr"
    XBW = "xbw"
    XBY = "xby"
    XCH = "xch"
    XCM = "xcm"
    XCN = "xcn"
    XCV = "xcv"
    XCW = "xcw"
    XCY = "xcy"
    XDA = "xda"
    XDK = "xdk"
    XDO = "xdo"
    XDQ = "xdq"
    XDY = "xdy"
    XED = "xed"
    XEG = "xeg"
    XEL = "xel"
    XEM = "xem"
    XER = "xer"
    XES = "xes"
    XET = "xet"
    XEU = "xeu"
    XGB = "xgb"
    XGD = "xgd"
    XGF = "xgf"
    XGG = "xgg"
    XGI = "xgi"
    XGM = "xgm"
    XGR = "xgr"
    XGU = "xgu"
    XGW = "xgw"
    XHE = "xhe"
    XHO = "xho"
    XHV = "xhv"
    XII = "xii"
    XIN = "xin"
    XIR = "xir"
    XIS = "xis"
    XIY = "xiy"
    XJB = "xjb"
    XJT = "xjt"
    XKA = "xka"
    XKB = "xkb"
    XKC = "xkc"
    XKD = "xkd"
    XKE = "xke"
    XKF = "xkf"
    XKG = "xkg"
    XKI = "xki"
    XKJ = "xkj"
    XKK = "xkk"
    XKL = "xkl"
    XKN = "xkn"
    XKO = "xko"
    XKP = "xkp"
    XKQ = "xkq"
    XKR = "xkr"
    XKS = "xks"
    XKT = "xkt"
    XKU = "xku"
    XKV = "xkv"
    XKW = "xkw"
    XKX = "xkx"
    XKY = "xky"
    XKZ = "xkz"
    XLA = "xla"
    XLB = "xlb"
    XLO = "xlo"
    XMA = "xma"
    XMB = "xmb"
    XMC = "xmc"
    XMD = "xmd"
    XMF = "xmf"
    XMG = "xmg"
    XMH = "xmh"
    XMJ = "xmj"
    XML = "xml"
    XMM = "xmm"
    XMO = "xmo"
    XMP = "xmp"
    XMQ = "xmq"
    XMS = "xms"
    XMT = "xmt"
    XMU = "xmu"
    XMV = "xmv"
    XMW = "xmw"
    XMX = "xmx"
    XMY = "xmy"
    XMZ = "xmz"
    XNB = "xnb"
    XNH = "xnh"
    XNI = "xni"
    XNJ = "xnj"
    XNK = "xnk"
    XNM = "xnm"
    XNN = "xnn"
    XNQ = "xnq"
    XNR = "xnr"
    XNS = "xns"
    XNT = "xnt"
    XNU = "xnu"
    XNY = "xny"
    XNZ = "xnz"
    XOC = "xoc"
    XOD = "xod"
    XOG = "xog"
    XOI = "xoi"
    XOK = "xok"
    XOM = "xom"
    XON = "xon"
    XOO = "xoo"
    XOP = "xop"
    XOR = "xor"
    XOW = "xow"
    XPA = "xpa"
    XPB = "xpb"
    XPD = "xpd"
    XPE = "xpe"
    XPF = "xpf"
    XPH = "xph"
    XPJ = "xpj"
    XPK = "xpk"
    XPL = "xpl"
    XPM = "xpm"
    XPN = "xpn"
    XPO = "xpo"
    XPQ = "xpq"
    XPT = "xpt"
    XPV = "xpv"
    XPW = "xpw"
    XPX = "xpx"
    XPZ = "xpz"
    XRA = "xra"
    XRB = "xrb"
    XRD = "xrd"
    XRE = "xre"
    XRG = "xrg"
    XRI = "xri"
    XRN = "xrn"
    XRT = "xrt"
    XRU = "xru"
    XRW = "xrw"
    XSB = "xsb"
    XSE = "xse"
    XSH = "xsh"
    XSI = "xsi"
    XSJ = "xsj"
    XSL = "xsl"
    XSM = "xsm"
    XSN = "xsn"
    XSO = "xso"
    XSP = "xsp"
    XSQ = "xsq"
    XSR = "xsr"
    XSU = "xsu"
    XSV = "xsv"
    XSY = "xsy"
    XTA = "xta"
    XTB = "xtb"
    XTC = "xtc"
    XTD = "xtd"
    XTE = "xte"
    XTH = "xth"
    XTI = "xti"
    XTJ = "xtj"
    XTL = "xtl"
    XTM = "xtm"
    XTN = "xtn"
    XTP = "xtp"
    XTS = "xts"
    XTT = "xtt"
    XTU = "xtu"
    XTV = "xtv"
    XTW = "xtw"
    XTY = "xty"
    XUA = "xua"
    XUB = "xub"
    XUD = "xud"
    XUG = "xug"
    XUJ = "xuj"
    XUL = "xul"
    XUN = "xun"
    XUO = "xuo"
    XUP = "xup"
    XUT = "xut"
    XUU = "xuu"
    XVI = "xvi"
    XWA = "xwa"
    XWC = "xwc"
    XWD = "xwd"
    XWE = "xwe"
    XWG = "xwg"
    XWJ = "xwj"
    XWK = "xwk"
    XWL = "xwl"
    XWR = "xwr"
    XWT = "xwt"
    XWW = "xww"
    XXB = "xxb"
    XXK = "xxk"
    XXM = "xxm"
    XXR = "xxr"
    XXT = "xxt"
    XYA = "xya"
    XYB = "xyb"
    XYJ = "xyj"
    XYK = "xyk"
    XYL = "xyl"
    XYT = "xyt"
    XYY = "xyy"
    XZM = "xzm"
    YAA = "yaa"
    YAB = "yab"
    YAC = "yac"
    YAD = "yad"
    YAE = "yae"
    YAF = "yaf"
    YAG = "yag"
    YAH = "yah"
    YAI = "yai"
    YAJ = "yaj"
    YAK = "yak"
    YAL = "yal"
    YAM = "yam"
    YAN = "yan"
    YAO = "yao"
    YAP = "yap"
    YAQ = "yaq"
    YAR = "yar"
    YAS = "yas"
    YAT = "yat"
    YAU = "yau"
    YAV = "yav"
    YAW = "yaw"
    YAX = "yax"
    YAY = "yay"
    YAZ = "yaz"
    YBA = "yba"
    YBB = "ybb"
    YBE = "ybe"
    YBH = "ybh"
    YBI = "ybi"
    YBJ = "ybj"
    YBK = "ybk"
    YBL = "ybl"
    YBM = "ybm"
    YBN = "ybn"
    YBO = "ybo"
    YBX = "ybx"
    YBY = "yby"
    YCH = "ych"
    YCL = "ycl"
    YCN = "ycn"
    YCP = "ycp"
    YCR = "ycr"
    YDA = "yda"
    YDD = "ydd"
    YDE = "yde"
    YDG = "ydg"
    YDK = "ydk"
    YEA = "yea"
    YEC = "yec"
    YEE = "yee"
    YEI = "yei"
    YEJ = "yej"
    YER = "yer"
    YES = "yes"
    YET = "yet"
    YEU = "yeu"
    YEV = "yev"
    YEY = "yey"
    YGA = "yga"
    YGI = "ygi"
    YGL = "ygl"
    YGM = "ygm"
    YGP = "ygp"
    YGR = "ygr"
    YGS = "ygs"
    YGU = "ygu"
    YGW = "ygw"
    YHA = "yha"
    YHD = "yhd"
    YHL = "yhl"
    YHS = "yhs"
    YIA = "yia"
    YIF = "yif"
    YIG = "yig"
    YIH = "yih"
    YII = "yii"
    YIJ = "yij"
    YIK = "yik"
    YIL = "yil"
    YIM = "yim"
    YIN = "yin"
    YIP = "yip"
    YIQ = "yiq"
    YIR = "yir"
    YIS = "yis"
    YIT = "yit"
    YIU = "yiu"
    YIV = "yiv"
    YIX = "yix"
    YIZ = "yiz"
    YKA = "yka"
    YKG = "ykg"
    YKH = "ykh"
    YKI = "yki"
    YKK = "ykk"
    YKL = "ykl"
    YKM = "ykm"
    YKN = "ykn"
    YKO = "yko"
    YKR = "ykr"
    YKT = "ykt"
    YKU = "yku"
    YKY = "yky"
    YLA = "yla"
    YLB = "ylb"
    YLE = "yle"
    YLG = "ylg"
    YLI = "yli"
    YLL = "yll"
    YLM = "ylm"
    YLN = "yln"
    YLO = "ylo"
    YLR = "ylr"
    YLU = "ylu"
    YLY = "yly"
    YMB = "ymb"
    YMC = "ymc"
    YMD = "ymd"
    YME = "yme"
    YMG = "ymg"
    YMH = "ymh"
    YMI = "ymi"
    YMK = "ymk"
    YML = "yml"
    YMM = "ymm"
    YMN = "ymn"
    YMO = "ymo"
    YMP = "ymp"
    YMQ = "ymq"
    YMR = "ymr"
    YMX = "ymx"
    YMZ = "ymz"
    YNA = "yna"
    YNB = "ynb"
    YND = "ynd"
    YNE = "yne"
    YNG = "yng"
    YNK = "ynk"
    YNL = "ynl"
    YNN = "ynn"
    YNO = "yno"
    YNQ = "ynq"
    YNS = "yns"
    YNU = "ynu"
    YOB = "yob"
    YOG = "yog"
    YOI = "yoi"
    YOK = "yok"
    YOL = "yol"
    YOM = "yom"
    YON = "yon"
    YOR = "yor"
    YOT = "yot"
    YOX = "yox"
    YOY = "yoy"
    YPA = "ypa"
    YPB = "ypb"
    YPG = "ypg"
    YPH = "yph"
    YPM = "ypm"
    YPN = "ypn"
    YPO = "ypo"
    YPP = "ypp"
    YPZ = "ypz"
    YRA = "yra"
    YRB = "yrb"
    YRE = "yre"
    YRK = "yrk"
    YRL = "yrl"
    YRM = "yrm"
    YRN = "yrn"
    YRO = "yro"
    YRS = "yrs"
    YRW = "yrw"
    YRY = "yry"
    YSC = "ysc"
    YSD = "ysd"
    YSG = "ysg"
    YSL = "ysl"
    YSM = "ysm"
    YSN = "ysn"
    YSO = "yso"
    YSP = "ysp"
    YSR = "ysr"
    YSS = "yss"
    YSY = "ysy"
    YTA = "yta"
    YTL = "ytl"
    YTP = "ytp"
    YTW = "ytw"
    YTY = "yty"
    YUA = "yua"
    YUB = "yub"
    YUC = "yuc"
    YUD = "yud"
    YUE = "yue"
    YUF = "yuf"
    YUG = "yug"
    YUI = "yui"
    YUJ = "yuj"
    YUK = "yuk"
    YUL = "yul"
    YUM = "yum"
    YUN = "yun"
    YUP = "yup"
    YUQ = "yuq"
    YUR = "yur"
    YUT = "yut"
    YUW = "yuw"
    YUX = "yux"
    YUY = "yuy"
    YUZ = "yuz"
    YVA = "yva"
    YVT = "yvt"
    YWA = "ywa"
    YWG = "ywg"
    YWL = "ywl"
    YWN = "ywn"
    YWQ = "ywq"
    YWR = "ywr"
    YWT = "ywt"
    YWU = "ywu"
    YWW = "yww"
    YXA = "yxa"
    YXG = "yxg"
    YXL = "yxl"
    YXM = "yxm"
    YXU = "yxu"
    YXY = "yxy"
    YYR = "yyr"
    YYU = "yyu"
    YYZ = "yyz"
    YZG = "yzg"
    YZK = "yzk"
    ZAA = "zaa"
    ZAB = "zab"
    ZAC = "zac"
    ZAD = "zad"
    ZAE = "zae"
    ZAF = "zaf"
    ZAG = "zag"
    ZAH = "zah"
    ZAI = "zai"
    ZAJ = "zaj"
    ZAK = "zak"
    ZAL = "zal"
    ZAM = "zam"
    ZAO = "zao"
    ZAQ = "zaq"
    ZAR = "zar"
    ZAS = "zas"
    ZAT = "zat"
    ZAU = "zau"
    ZAV = "zav"
    ZAW = "zaw"
    ZAX = "zax"
    ZAY = "zay"
    ZAZ = "zaz"
    ZBC = "zbc"
    ZBE = "zbe"
    ZBT = "zbt"
    ZBU = "zbu"
    ZBW = "zbw"
    ZCA = "zca"
    ZCD = "zcd"
    ZCH = "zch"
    ZDJ = "zdj"
    ZEA = "zea"
    ZEG = "zeg"
    ZEH = "zeh"
    ZEM = "zem"
    ZEN = "zen"
    ZGA = "zga"
    ZGB = "zgb"
    ZGH = "zgh"
    ZGM = "zgm"
    ZGN = "zgn"
    ZGR = "zgr"
    ZHB = "zhb"
    ZHD = "zhd"
    ZHI = "zhi"
    ZHN = "zhn"
    ZHW = "zhw"
    ZIA = "zia"
    ZIB = "zib"
    ZIK = "zik"
    ZIL = "zil"
    ZIM = "zim"
    ZIN = "zin"
    ZIW = "ziw"
    ZIZ = "ziz"
    ZKA = "zka"
    ZKD = "zkd"
    ZKK = "zkk"
    ZKN = "zkn"
    ZKO = "zko"
    ZKP = "zkp"
    ZKR = "zkr"
    ZKU = "zku"
    ZKV = "zkv"
    ZLA = "zla"
    ZLJ = "zlj"
    ZLM = "zlm"
    ZLN = "zln"
    ZLQ = "zlq"
    ZLU = "zlu"
    ZMA = "zma"
    ZMB = "zmb"
    ZMC = "zmc"
    ZMD = "zmd"
    ZME = "zme"
    ZMF = "zmf"
    ZMG = "zmg"
    ZMH = "zmh"
    ZMI = "zmi"
    ZMJ = "zmj"
    ZMK = "zmk"
    ZML = "zml"
    ZMM = "zmm"
    ZMN = "zmn"
    ZMO = "zmo"
    ZMP = "zmp"
    ZMQ = "zmq"
    ZMR = "zmr"
    ZMS = "zms"
    ZMT = "zmt"
    ZMU = "zmu"
    ZMV = "zmv"
    ZMW = "zmw"
    ZMX = "zmx"
    ZMY = "zmy"
    ZMZ = "zmz"
    ZNA = "zna"
    ZNE = "zne"
    ZNG = "zng"
    ZNK = "znk"
    ZNS = "zns"
    ZOC = "zoc"
    ZOH = "zoh"
    ZOM = "zom"
    ZOO = "zoo"
    ZOQ = "zoq"
    ZOR = "zor"
    ZOS = "zos"
    ZPA = "zpa"
    ZPB = "zpb"
    ZPC = "zpc"
    ZPD = "zpd"
    ZPE = "zpe"
    ZPF = "zpf"
    ZPG = "zpg"
    ZPH = "zph"
    ZPI = "zpi"
    ZPJ = "zpj"
    ZPK = "zpk"
    ZPL = "zpl"
    ZPM = "zpm"
    ZPN = "zpn"
    ZPO = "zpo"
    ZPP = "zpp"
    ZPQ = "zpq"
    ZPR = "zpr"
    ZPS = "zps"
    ZPT = "zpt"
    ZPU = "zpu"
    ZPV = "zpv"
    ZPW = "zpw"
    ZPX = "zpx"
    ZPY = "zpy"
    ZPZ = "zpz"
    ZQE = "zqe"
    ZRG = "zrg"
    ZRN = "zrn"
    ZRO = "zro"
    ZRS = "zrs"
    ZSA = "zsa"
    ZSL = "zsl"
    ZSM = "zsm"
    ZSR = "zsr"
    ZSU = "zsu"
    ZTE = "zte"
    ZTG = "ztg"
    ZTL = "ztl"
    ZTM = "ztm"
    ZTN = "ztn"
    ZTP = "ztp"
    ZTQ = "ztq"
    ZTS = "zts"
    ZTT = "ztt"
    ZTU = "ztu"
    ZTX = "ztx"
    ZTY = "zty"
    ZUH = "zuh"
    ZUL = "zul"
    ZUM = "zum"
    ZUN = "zun"
    ZUY = "zuy"
    ZWA = "zwa"
    ZYB = "zyb"
    ZYG = "zyg"
    ZYJ = "zyj"
    ZYN = "zyn"
    ZYP = "zyp"
    ZZJ = "zzj"
    KUR = "kur"
    PAT = "pat"
    EWA = "ewa"
    NOT_AVAILABLE = "notAvailable"

class CoarseCefrLevel(Enum):
    """A list of coarse CEFR LEVELS .

    The A1 and A2 are merged. The same goes for the B and C levels.
    """
    A = "A"
    B = "B"
    C = "C"
    NOT_AVAILABLE = "notAvailable"


class CorpusAvailabilityType(Enum):
    """
    A list of license types by which a corpus may be available, if at all.

    :cvar VALUE_01: closed
    :cvar VALUE_02: restricted
    :cvar VALUE_02_1: special case
    :cvar VALUE_03: open; all CC-licenses
    :cvar NOT_AVAILABLE: information is not available
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_02_1 = "02!"
    VALUE_03 = "03!"
    NOT_AVAILABLE = "notAvailable"


class CorpusGroup(Enum):
    CDLK = "CDLK"
    KIEZ_DEUTSCH_KORPUS = "KiezDeutsch-Korpus"
    DISKO = "DISKO"
    EURAC_KORPORA = "EURAC-Korpora"
    FALKO = "Falko"
    FD_LEX = "FD-Lex"
    HA_MA_TA_C = "HaMaTaC"
    HA_MO_TI_C = "HaMoTiC"
    NOT_APPLICABLE = "notApplicable"


class CountryTypeOrNa(Enum):
    """
    A country specified as COUNTRY_TYPE or a string indicating that no value is
    available.
    """
    NOT_AVAILABLE = "notAvailable"
    AFG = "AFG"
    ALA = "ALA"
    ALB = "ALB"
    DZA = "DZA"
    ASM = "ASM"
    AND = "AND"
    AGO = "AGO"
    AIA = "AIA"
    ATA = "ATA"
    ATG = "ATG"
    ARG = "ARG"
    ARM = "ARM"
    ABW = "ABW"
    AUS = "AUS"
    AUT = "AUT"
    AZE = "AZE"
    BHS = "BHS"
    BHR = "BHR"
    BGD = "BGD"
    BRB = "BRB"
    BLR = "BLR"
    BEL = "BEL"
    BLZ = "BLZ"
    BEN = "BEN"
    BMU = "BMU"
    BTN = "BTN"
    BOL = "BOL"
    BES = "BES"
    BIH = "BIH"
    BWA = "BWA"
    BVT = "BVT"
    BRA = "BRA"
    IOT = "IOT"
    BRN = "BRN"
    BGR = "BGR"
    BFA = "BFA"
    BDI = "BDI"
    CPV = "CPV"
    KHM = "KHM"
    CMR = "CMR"
    CAN = "CAN"
    CYM = "CYM"
    CAF = "CAF"
    TCD = "TCD"
    CHL = "CHL"
    CHN = "CHN"
    CXR = "CXR"
    CCK = "CCK"
    COL = "COL"
    COM = "COM"
    COG = "COG"
    COD = "COD"
    COK = "COK"
    CRI = "CRI"
    CIV = "CIV"
    HRV = "HRV"
    CUB = "CUB"
    CUW = "CUW"
    CYP = "CYP"
    CZE = "CZE"
    DNK = "DNK"
    DJI = "DJI"
    DMA = "DMA"
    DOM = "DOM"
    ECU = "ECU"
    EGY = "EGY"
    SLV = "SLV"
    GNQ = "GNQ"
    ERI = "ERI"
    EST = "EST"
    SWZ = "SWZ"
    ETH = "ETH"
    FLK = "FLK"
    FRO = "FRO"
    FJI = "FJI"
    FIN = "FIN"
    FRA = "FRA"
    GUF = "GUF"
    PYF = "PYF"
    ATF = "ATF"
    GAB = "GAB"
    GMB = "GMB"
    GEO = "GEO"
    DEU = "DEU"
    GHA = "GHA"
    GIB = "GIB"
    GRC = "GRC"
    GRL = "GRL"
    GRD = "GRD"
    GLP = "GLP"
    GUM = "GUM"
    GTM = "GTM"
    GGY = "GGY"
    GIN = "GIN"
    GNB = "GNB"
    GUY = "GUY"
    HTI = "HTI"
    HMD = "HMD"
    VAT = "VAT"
    HND = "HND"
    HKG = "HKG"
    HUN = "HUN"
    ISL = "ISL"
    IND = "IND"
    IDN = "IDN"
    IRN = "IRN"
    IRQ = "IRQ"
    IRL = "IRL"
    IMN = "IMN"
    ISR = "ISR"
    ITA = "ITA"
    JAM = "JAM"
    JPN = "JPN"
    JEY = "JEY"
    JOR = "JOR"
    KAZ = "KAZ"
    KEN = "KEN"
    KIR = "KIR"
    PRK = "PRK"
    KOR = "KOR"
    KWT = "KWT"
    KGZ = "KGZ"
    LAO = "LAO"
    LVA = "LVA"
    LBN = "LBN"
    LSO = "LSO"
    LBR = "LBR"
    LBY = "LBY"
    LIE = "LIE"
    LTU = "LTU"
    LUX = "LUX"
    MAC = "MAC"
    MDG = "MDG"
    MWI = "MWI"
    MYS = "MYS"
    MDV = "MDV"
    MLI = "MLI"
    MLT = "MLT"
    MHL = "MHL"
    MTQ = "MTQ"
    MRT = "MRT"
    MUS = "MUS"
    MYT = "MYT"
    MEX = "MEX"
    FSM = "FSM"
    MDA = "MDA"
    MCO = "MCO"
    MNG = "MNG"
    MNE = "MNE"
    MSR = "MSR"
    MAR = "MAR"
    MOZ = "MOZ"
    MMR = "MMR"
    NAM = "NAM"
    NRU = "NRU"
    NPL = "NPL"
    NLD = "NLD"
    NCL = "NCL"
    NZL = "NZL"
    NIC = "NIC"
    NER = "NER"
    NGA = "NGA"
    NIU = "NIU"
    NFK = "NFK"
    MKD = "MKD"
    MNP = "MNP"
    NOR = "NOR"
    OMN = "OMN"
    PAK = "PAK"
    PLW = "PLW"
    PSE = "PSE"
    PAN = "PAN"
    PNG = "PNG"
    PRY = "PRY"
    PER = "PER"
    PHL = "PHL"
    PCN = "PCN"
    POL = "POL"
    PRT = "PRT"
    PRI = "PRI"
    QAT = "QAT"
    REU = "REU"
    ROU = "ROU"
    RUS = "RUS"
    RWA = "RWA"
    BLM = "BLM"
    SHN = "SHN"
    KNA = "KNA"
    LCA = "LCA"
    MAF = "MAF"
    SPM = "SPM"
    VCT = "VCT"
    WSM = "WSM"
    SMR = "SMR"
    STP = "STP"
    SAU = "SAU"
    SEN = "SEN"
    SRB = "SRB"
    SYC = "SYC"
    SLE = "SLE"
    SGP = "SGP"
    SXM = "SXM"
    SVK = "SVK"
    SVN = "SVN"
    SLB = "SLB"
    SOM = "SOM"
    ZAF = "ZAF"
    SGS = "SGS"
    SSD = "SSD"
    ESP = "ESP"
    LKA = "LKA"
    SDN = "SDN"
    SUR = "SUR"
    SJM = "SJM"
    SWE = "SWE"
    CHE = "CHE"
    SYR = "SYR"
    TWN = "TWN"
    TJK = "TJK"
    TZA = "TZA"
    THA = "THA"
    TLS = "TLS"
    TGO = "TGO"
    TKL = "TKL"
    TON = "TON"
    TTO = "TTO"
    TUN = "TUN"
    TUR = "TUR"
    TKM = "TKM"
    TCA = "TCA"
    TUV = "TUV"
    UGA = "UGA"
    UKR = "UKR"
    ARE = "ARE"
    GBR = "GBR"
    USA = "USA"
    UMI = "UMI"
    URY = "URY"
    UZB = "UZB"
    VUT = "VUT"
    VEN = "VEN"
    VNM = "VNM"
    VGB = "VGB"
    VIR = "VIR"
    WLF = "WLF"
    ESH = "ESH"
    YEM = "YEM"
    ZMB = "ZMB"
    ZWE = "ZWE"
    NOT_APPLICABLE = "notApplicable"


class DakodaProjectDuration(Enum):
    VALUE_2022_2025 = "2022-2025"


class DataProductionSetting(Enum):
    """
    :cvar EDUCATIONAL_SETTING:
    :cvar NATURALISTIC:
    :cvar OFFICIAL_LANGUAGE_TEST: Official language testing refers to a
        situation where language testing is performed by an approved
        language assessment body.
    :cvar RESEARCH_PROJECT:
    :cvar LANGUAGE_COURSE:
    :cvar NOT_AVAILABLE:
    """
    EDUCATIONAL_SETTING = "educational setting"
    NATURALISTIC = "naturalistic"
    OFFICIAL_LANGUAGE_TEST = "officialLanguageTest"
    RESEARCH_PROJECT = "research project"
    LANGUAGE_COURSE = "language course"
    NOT_AVAILABLE = "notAvailable"


class DataProductionSettingConceptualMode(Enum):
    """
    A list of possible ceonceptual modes in which the corpus data was produced.
    """
    SPOKEN = "spoken"
    WRITTEN = "written"
    NOT_AVAILABLE = "notAvailable"


class DataProductionSettingMode(Enum):
    """
    A list of possible modes in which the corpus data was produced.
    """
    SPOKEN = "spoken"
    WRITTEN = "written"
    NOT_AVAILABLE = "notAvailable"


class DkdContributor(Enum):
    """
    A person working for the Dakoda project.
    """
    JAMILA_BL_SING = "Jamila Bläsing"
    LUISE_B_TTCHER = "Luise Böttcher"
    SHANNY_DRUKER = "Shanny Druker"
    LISA_LENORT = "Lisa Lenort"
    ANNETTE_PORTMANN = "Annette Portmann"
    CHRISTINE_RENKER = "Christine Renker"
    JOSEF_RUPPENHOFER = "Josef Ruppenhofer"
    MATTHIAS_SCHWENDEMANN = "Matthias Schwendemann"
    IULIA_SUCUTARDEAN = "Iulia Sucutardean"
    KATRIN_WISNIEWSKI = "Katrin Wisniewski"
    TORSTEN_ZESCH = "Torsten Zesch"


class DkdInstitution(Enum):
    UNIVERSIT_T_LEIPZIG = "Universität Leipzig"
    FERN_UNIVERSIT_T_IN_HAGEN = "FernUniversität in Hagen"


class DkdProjectHead(Enum):
    """
    A principal investigator of the Dakoda project.
    """
    KATRIN_WISNIEWSKI = "Katrin Wisniewski"
    TORSTEN_ZESCH = "Torsten Zesch"


class DkdProjectName(Enum):
    """
    Vollständiger Name des DAKODA-Projekts.
    """
    DATENKOMPETENZEN_IN_DA_F_DA_Z_EXPLORATION_SPRACHTECHNOLOGISCHER_ANS_TZE_ZUR_ANALYSE_VON_L2_ERWERBSSTUFEN_IN_LERNERKORPORA_DES_DEUTSCHEN = "Datenkompetenzen in DaF/DaZ: Exploration sprachtechnologischer Ansätze zur Analyse von L2-Erwerbsstufen in Lernerkorpora des Deutschen"


class DkdProjectType(Enum):
    """
    The type of funding that supported the DADKOA project.
    """
    BUNDESMINISTERIUM_F_R_BILDUNG_UND_FORSCHUNG_BMBF = "Bundesministerium für Bildung und Forschung (BMBF)"


class DkdTrgLang(Enum):
    ARC = "arc"
    KUR = "kur"
    PES = "pes"
    AZE = "aze"
    BEN = "ben"
    EUS = "eus"
    HIN = "hin"
    JPN = "jpn"
    KAT = "kat"
    KOR = "kor"
    NEP = "nep"
    TAM = "tam"
    TAT = "tat"
    TGK = "tgk"
    TUR = "tur"
    URD = "urd"
    UZB = "uzb"
    PAN = "pan"
    FAS = "fas"
    DEU = "deu"
    HUN = "hun"
    NLD = "nld"
    BOS = "bos"
    SCC = "scc"
    HRV = "hrv"
    HEB = "heb"
    ZHO = "zho"
    BUL = "bul"
    CAT = "cat"
    CES = "ces"
    DAN = "dan"
    ENG = "eng"
    EWE = "ewe"
    FIN = "fin"
    FRA = "fra"
    GAA = "gaa"
    IND = "ind"
    ISL = "isl"
    ITA = "ita"
    KIK = "kik"
    LAV = "lav"
    LIT = "lit"
    LUB = "lub"
    NOR = "nor"
    POL = "pol"
    POR = "por"
    RON = "ron"
    RUS = "rus"
    SLV = "slv"
    SME = "sme"
    SNA = "sna"
    SPA = "spa"
    SQI = "sqi"
    ALB = "alb"
    SWA = "swa"
    SWE = "swe"
    THA = "tha"
    UKR = "ukr"
    VIE = "vie"
    XHO = "xho"
    YOR = "yor"
    YUE = "yue"
    MKD = "mkd"
    HBS = "hbs"
    CMN = "cmn"
    ELL = "ell"
    GRE = "gre"
    AFR = "afr"
    ALQ = "alq"
    ANG = "ang"
    BAK = "bak"
    BEW = "bew"
    BFI = "bfi"
    CMA = "cma"
    EBU = "ebu"
    GLG = "glg"
    GRC = "grc"
    HBO = "hbo"
    III = "iii"
    KAZ = "kaz"
    KIR = "kir"
    KUA = "kua"
    LAT = "lat"
    LUY = "luy"
    MAI = "mai"
    MON = "mon"
    BAI = "bai"
    NAP = "nap"
    NON = "non"
    NYF = "nyf"
    ROH = "roh"
    SLK = "slk"
    SVE = "sve"
    TWI = "twi"
    TZM = "tzm"
    YID = "yid"
    EPO = "epo"
    KYE = "kye"
    LTZ = "ltz"
    GER = "ger"
    JBE = "jbe"
    ARA = "ara"
    HYE = "hye"
    MLY = "mly"
    KAL = "kal"
    NDE = "nde"
    PST = "pst"
    PRS = "prs"
    BEL = "bel"
    CYM = "cym"
    GLE = "gle"
    ARB = "arb"
    PRD = "prd"
    NAN = "nan"
    PAT = "pat"
    EWA = "ewa"
    ROU = "rou"


class EducationalStage(Enum):
    """
    The education stage the learner is in at the time of data collection.
    """
    EARLY_CHILDHOOD = "early childhood"
    PRIMARY = "primary"
    LOWER_SECONDARY = "lower secondary"
    UPPER_SECONDARY = "upper secondary"
    POST_SECONDARY_NON_TERTIARY = "post-secondary non-tertiary"
    SHORT_CYCLE_TERTIARY = "short-cycle tertiary"
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DOCTORATE = "Doctorate"
    NOT_AVAILABLE = "notAvailable"


class FormalityType(Enum):
    """
    Formality level of the task.
    """
    INFORMAL = "informal"
    UNMARKED_TO_INFORMAL = "unmarked to informal"
    UNMARKED = "unmarked"
    UNMARKED_TO_FORMAL = "unmarked to formal"
    FORMAL = "formal"
    NOT_AVAILABLE = "notAvailable"


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    NON_BINARY = "non-binary"
    NOT_AVAILABLE = "notAvailable"


class InteractionTypes(Enum):
    """
    A specification of the language combinations used .

    :cvar GERMAN_L1: Only L1-German speakers are part in the
        interaction.
    :cvar GERMAN_L2: Only L2-German speakers part of the interaction.
    :cvar GERMAN_L1_L2: A mix of L1- and L2-German speakers is part of
        the interaction.
    :cvar NOT_AVAILABLE:
    :cvar NOT_APPLICABLE:
    """
    GERMAN_L1 = "German-L1"
    GERMAN_L2 = "German-L2"
    GERMAN_L1_L2 = "German-L1_L2"
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class L1Constellation(Enum):
    MONO = "mono"
    MULTI = "multi"


class LangStatus(Enum):
    L1 = "L1"
    L2 = "L2"
    TARGET_LANGUAGE = "Target language"
    NOT_AVAILABLE = "notAvailable"


class LearnerAgeRange(Enum):
    """
    A predefined set of age ranges that are associated with different types of
    language acquisition processes.
    """
    VALUE_0_BIS_3_ERSTSPRACHERWERB = "0 bis 3, Erstspracherwerb"
    VALUE_4_BIS_6_FR_HER_KINDLICHER_ZWEITSPRACHERWERB = "4 bis 6, Früher (kindlicher) Zweitspracherwerb"
    VALUE_7_BIS_8_SP_TER_KINDLICHER_ZWEITSPRACHERWERB_FREMDSPRACHERWERB = "7 bis 8,(Später kindlicher) Zweitspracherwerb / Fremdspracherwerb"
    VALUE_9_BIS_12_SP_TER_KINDLICHER_ZWEITSPRACHERWERB_FREMDSPRACHERWERB = "9 bis 12, (später kindlicher) Zweitspracherwerb / Fremdspracherwerb"
    VALUE_12_BIS_18_ZWEITSPRACHERWERB_FREMDSPRACHERWERB_VON_JUGENDLICHEN_UND_ERWACHSENEN = "12 bis 18, Zweitspracherwerb / Fremdspracherwerb (von Jugendlichen und Erwachsenen)"
    VALUE_19_BIS_35_ZWEITSPRACHERWERB_FREMDSPRACHERWERB_VON_JUGENDLICHEN_UND_ERWACHSENEN = "19 bis 35, Zweitspracherwerb / Fremdspracherwerb (von Jugendlichen und Erwachsenen)"
    LTER_ALS_35_ZWEITSPRACHERWERB_FREMDSPRACHERWERB_VON_JUGENDLICHEN_UND_ERWACHSENEN = "älter als 35, Zweitspracherwerb / Fremdspracherwerb (von Jugendlichen und Erwachsenen)"
    UNKLAR_BZW_SONSTIGE = "unklar bzw. sonstige"
    NOT_AVAILABLE = "notAvailable"


class LearnerTaskType(Enum):
    """
    Type of task used in collecting the data.
    """
    BOOK_REVIEW = "book review"
    CONSULTATION = "consultation"
    CONVERSATION = "conversation"
    DESCRIPTION = "description"
    ESSAY = "essay"
    INSTRUCTION = "instruction"
    INTERVIEW = "interview"
    LETTER = "letter"
    MAP_TASK = "map task"
    NARROW_ELICITATION_TASK = "narrow elicitation task"
    POST_IN_A_FORUM = "post in a forum"
    PROBLEM_SOVLING = "problem sovling"
    REPORT = "report"
    STORY = "story"
    SUMMARY = "summary"
    TRANSLATION = "translation"
    NOT_AVAILABLE = "notAvailable"


class NaString(Enum):
    """
    A string indicating that no value is available for a metadatum or that the
    metadatum is not applicable.
    """
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class PossibilitiesForComparisons(Enum):
    """
    Possibilities for comparing tasks and time points.
    """
    ONE_TASK_ONE_TIME = "one task one-time"
    ONE_TASK_REPEATED = "one task repeated"
    SEVERAL_TASKS_REPEATED = "several tasks repeated"
    SEVERAL_TASKS_EACH_ONE_TIME = "several tasks each one-time"
    NOT_AVAILABLE = "notAvailable"


class ProficiencyAssessmentMethod(Enum):
    """
    A type of proficiency assessment.
    """
    INDEPENDENT_INSTRUMENT = "independent instrument"
    TOTAL_TEST_SCORE = "total test score"
    OTHER = "other"
    NOT_AVAILABLE = "notAvailable"


class ProficiencyAssignmentMethod(Enum):
    LEARNER_CENTRED = "learner-centred"
    TEXT_CENTRED = "text-centred"
    AUTOMATIC = "automatic"
    NONE = "none"
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class ProficiencyAssignmentMethodType(Enum):
    """
    Method used for proficiency assessment.
    """
    SCORE_ON_TEXT = "score on text"
    TEACHER_S_EVALUATION = "teacher's evaluation"
    POST_HOC_ASSIGNMENT = "post-hoc assignment"
    NOT_AVAILABLE = "notAvailable"


class ProficiencyLevel(Enum):
    """A list of possible coarse proficiency levels specified as CEFR levels or
    ranges.

    Including value "notAvailable"
    """
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    C1 = "C1"
    C2 = "C2"
    NOT_AVAILABLE = "notAvailable"


class RhetoricalFunctions(Enum):
    APPLYING = "applying"
    ARGUING = "arguing"
    ASKING_FOR_HELP = "asking for help"
    ASKING_FOR_INFORMATION = "asking for information"
    BUILD_A_SENTENCE = "build a sentence"
    COMPARING = "comparing"
    COMPLAINING = "complaining"
    DESCRIBING = "describing"
    EXPRESS_CONGRATULATIONS = "express congratulations"
    GIVING_ADVICE = "giving advice"
    INFORMING = "informing"
    INSTRUCTING = "instructing"
    NARRATING = "narrating"
    OFFERING_SOMETHING = "offering something"
    ORGANISE_MEETING = "organise meeting"
    QUESTION_AND_ANSWER = "question and answer"
    READING_ALOUD = "reading aloud"
    REPORTING = "reporting"
    SUMMARISING = "summarising"
    TRANSLATING = "translating"
    NOT_AVAILABLE = "notAvailable"


class StorageUnit(Enum):
    KB = "KB"
    MB = "MB"
    GB = "GB"
    TB = "TB"
    PB = "PB"


class StudyDesign(Enum):
    """
    The study design under which the corpus data was produced.
    """
    LONGITUDINAL = "longitudinal"
    PSEUDO_LONGITUDINAL = "pseudo-longitudinal"
    CROSS_SECTIONAL = "cross-sectional"


class TaskStimulusType(Enum):
    """
    Type of stimulus for the task.
    """
    ADVERTISEMENT = "advertisement"
    ARTICLE = "article"
    ARTICLES = "articles"
    BOOK = "book"
    COMIC = "comic"
    DESCRIPTION_OF_A_SITUATION = "description of a situation"
    DIAGRAM = "diagram"
    ESSAY = "essay"
    EXTRACT_FROM_A_DOCTORAL_DISSERTATION = "extract from a doctoral dissertation"
    EXTRACT_FROM_A_DOCTORAL_ARTICLES = "extract from a doctoral articles"
    FIGURE = "figure"
    TEXT_EDITED_FOR_TEACHING = "text edited for teaching"
    FORM = "form"
    INTERVIEW = "interview"
    JOB_ADVERTISEMENT = "job advertisement"
    LETTER = "letter"
    LIST_OF_WORDS_OR_EXPRESSIONS = "list of words or expressions"
    MAP = "map"
    ORAL_INSTRUCTIONS = "oral instructions"
    PICTURE_S = "picture(s)"
    QUESTIONNAIRE = "questionnaire"
    QUOTE = "quote"
    SCENE_ACTED_OUT = "scene acted out"
    TALKS = "talks"
    VIDEO = "video"
    WRITTEN_INSTRUCTION = "written instruction"
    NOT_AVAILABLE = "notAvailable"
    NOT_APPLICABLE = "notApplicable"


class TopicType(Enum):
    """
    A list of topic types that may be assigned to texts.
    """
    DOMESTIC = "domestic"
    DAILY_ACTIVITIES = "daily activities"
    BUSINESS_WORK_PLACE = "business/work place"
    SCIENCE = "science"
    EDUCATION_ACADEMIC = "education / academic"
    GOVERNMENT_LEGAL_POLITICS = "government / legal / politics"
    RELIGION = "religion"
    SPORTS = "sports"
    ART_ENTERTAINEMENT = "art / entertainement"
    OTHER = "other"
    NOT_AVAILABLE = "notAvailable"


class TrgLangInputType(Enum):
    """
    Dominant word order type according to WALS.
    """
    MAINLY_WITHOUT_CONTROLLED_TEACHING_PROCESSES = "mainly without controlled teaching processes"
    MAINLY_IN_CONTROLLED_TEACHING_CONTEXTS = "mainly in controlled teaching contexts"
    HYBRID = "hybrid"
    NOT_AVAILABLE = "notAvailable"


class WordOrderType(Enum):
    """
    Dominant word order type according to WALS.
    """
    SOV = "SOV"
    SVO = "SVO"
    VSO = "VSO"
    SVO_VSO = "SVO ; VSO"
    SOV_SVO = "SOV; SVO"
    NO_DOMINANT_ORDER = "no dominant order"
    UNCLEAR = "unclear"
    NOT_AVAILABLE = "notAvailable"


@dataclass
class Annotation:
    """
    :ivar annotation_automatic: Was the annotation process fully
        automatic? An equivalent field in LC-meta is
        `annotation_automatic`.
    :ivar annotation_corrected: Was the automatic annotation subject to
        further correction?  An equivalent field in LC-meta is
        `annotation_corrected`.
    :ivar annotation_documentation: Plain text description of annotation
        or link to documentation An equivalent field in LC-meta is
        `annotation_documentation`.
    :ivar annotation_evaluation: Was the annotation evaluated? An
        equivalent field in LC-meta is `annotation_evaluation`.
    :ivar annotation_tool: Name of tool used for annotation An
        equivalent field in LC-meta is `annotation_tool`.
    :ivar annotation_tool_version: Version of tool used for annotation
        An equivalent field in LC-meta is `annotation_tool_version`.
    :ivar annotation_model_version: Version of a trained statistical
        model or parameter set for use with the annotation tool. LC-meta
        has no related field.
    :ivar annotation_type: Specification of an annotation type(s) such
        as lemma , POS, etc. that are provided by the tool in question.
        An equivalent field in LC-meta is `annotation_type`.
    """
    annotation_automatic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotation_corrected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotation_documentation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    annotation_evaluation: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotation_tool: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotation_tool_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "annotation_toolVersion",
            "type": "Element",
            "required": True,
        }
    )
    annotation_model_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "annotation_modelVersion",
            "type": "Element",
            "required": True,
        }
    )
    annotation_type: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class CorpusAdministrative:
    """
    :ivar corpus_admin_acronym: Corpus acronym. An equivalent field in
        LC-meta is `corpus_acronym`.
    :ivar corpus_admin_name: The fully disabbreviated title of the
        corpus. Can occur multiple times for corpora with official names
        in multiple languages. An equivalent field in LC-meta is
        `corpus_name`.
    :ivar corpus_admin_author: Corpus creator. An equivalent field in
        LC-meta is  `corpus_author`.
    :ivar corpus_admin_availability: Licensing terms and conditions for
        corpus. An equivalent field in LC-meta is `corpus_availability`
    :ivar corpus_admin_citation_document: Information on how excerpts of
        the corpus should be referenced. This field has no counterpart
        in LC-meta .
    :ivar corpus_admin_cite_as: Corpus citation. An equivalent field in
        LC-meta is `corpus_cite_as`.
    :ivar corpus_admin_contact_mail: Contact e-mail address . An
        equivalent field in LC-meta is `corpus_contact_mail`.
    :ivar corpus_admin_contributor_dkd: Contributor (DAKODA version).
        LC-meta has the comparable field `corpus_contributor`.
    :ivar corpus_admin_contributor_orig: Contributor (original version).
        LC-meta has the comparable field `corpus_contributor`.
    :ivar corpus_admin_date_of_publication: Publication year of the
        source version of the corpus. An comparable field name in LC-
        meta is `corpus_date_of_publication`.
    :ivar corpus_admin_documentation: Link to more extensive corpus
        documentation. Usually a corpus manual covering , for instance,
        the trancription and/or annotation guidelines. An equivalent
        field in LC-meta is  `corpus_documentation`.
    :ivar corpus_admin_file_format: File format (DAKODA-Version). An
        equivalent field in LC-meta is `corpus_file_format`.
    :ivar corpus_admin_licence: Licence name (DAKODA version).  An
        equivalent field in LC-meta is `corpus_licence`.
    :ivar corpus_admin_licence_fulltext: Licence text (DAKODA version).
        There is no equivalent field in LC-meta.
    :ivar corpus_admin_licence_url: Link to licence text. An equivalent
        field in LC-meta is `corpus_licence_url`.
    :ivar corpus_admin_other_versions: Associated version of the corpus.
        This will often be an earlier release of the corpus. An
        equivalent field in LC-meta is `corpus_other_versions`.
    :ivar corpus_admin_pid_dkd: Persistent identifier (DAKODA version).
        An equivalent field in LC-meta is `corpus_pid`. <xs:appinfo
        xmlns:xs="http://www.w3.org/2001/XMLSchema"><displayname
        xmlns="">PID (DAKODA-Version)</displayname></xs:appinfo>
    :ivar corpus_admin_pid_orig: Persistent Identifier (original
        version). An equivalent field in LC-meta is  `corpus_pid`.
    :ivar corpus_admin_ref_article: Reference article. Such articles
        typically contain an extensive verbal description of the corpus
        and its design. An equivalent field in LC-meta is
        `corpus_ref_article`.
    :ivar corpus_admin_references_other: Further important publications
        or links to the corpus . LC-meta has related metadata field
        `corpus_ref_article`.
    :ivar corpus_admin_research_paper: Further publications (original
        version). An equivalent field in LC-meta is
        corpus_ref_article`.
    :ivar corpus_admin_url_download: Link to corpus download (original
        version). There is no equivalent field in LC-meta.
    :ivar corpus_admin_urlquery: Link to corpus query (original
        version).
    :ivar corpus_admin_version_orig: Data version on which the DAKODA
        version is based: Version number, PID or download link with
        date. An equivalent field in LC-meta is `corpus_version`.
    """
    class Meta:
        name = "Corpus_Administrative"

    corpus_admin_acronym: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    corpus_admin_name: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_admin_author: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_admin_availability: Optional[CorpusAvailabilityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_admin_citation_document: str = field(
        default="notAvailable",
        metadata={
            "name": "corpus_admin_citationDocument",
            "type": "Element",
            "required": True,
        }
    )
    corpus_admin_cite_as: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_admin_citeAs",
            "type": "Element",
            "required": True,
            "min_length": 1,
        }
    )
    corpus_admin_contact_mail: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_contactMail",
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"([^@]+@[^\.]+\..+)|(notAvailable)",
        }
    )
    corpus_admin_contributor_dkd: List[DkdContributor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 11,
            "max_occurs": 11,
        }
    )
    corpus_admin_contributor_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    corpus_admin_date_of_publication: Optional[Union[XmlPeriod, XmlDate, str, NaString]] = field(
        default=None,
        metadata={
            "name": "corpus_admin_dateOfPublication",
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{2}",
        }
    )
    corpus_admin_documentation: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_admin_file_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_fileFormat",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_admin_licence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_admin_licence_fulltext: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_admin_licenceFulltext",
            "type": "Element",
        }
    )
    corpus_admin_licence_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_admin_licenceUrl",
            "type": "Element",
            "required": True,
        }
    )
    corpus_admin_other_versions: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_otherVersions",
            "type": "Element",
        }
    )
    corpus_admin_pid_dkd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_admin_pid_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_admin_ref_article: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_refArticle",
            "type": "Element",
        }
    )
    corpus_admin_references_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_referencesOther",
            "type": "Element",
        }
    )
    corpus_admin_research_paper: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_researchPaper",
            "type": "Element",
        }
    )
    corpus_admin_url_download: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_URL_download",
            "type": "Element",
        }
    )
    corpus_admin_urlquery: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_admin_URLquery",
            "type": "Element",
        }
    )
    corpus_admin_version_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CorpusDesign:
    """
    :ivar corpus_design_description: A short description of the corpus.
        An equivalent field in LC-meta is `corpus_description` in LC-
        meta.
    :ivar corpus_design_design_type: Design of data collection/study
        design. An equivalent field in LC-meta `corpus_longitudinal`.
    :ivar corpus_design_group: Affiliation of the corpus to a corpus
        group. An equivalent field in LC-meta is `corpus_related`.
    :ivar corpus_design_is_comparable_data_included: Does the corpus
        include comparison data? An equivalent field in LC-meta is
        `corpus_comparable_data_included`.
    :ivar corpus_design_l1_language: L1 language(s). An equivalent field
        in LC-meta is `corpus_L1_language`.
    :ivar corpus_design_l1_type: L1 constellation. If all participants
        share one L1: mono; if there are multiple L1s: multi . There is
        no eqivalent field in LC-meta.
    :ivar corpus_design_size: Storage requirement in KB, MB, GB, TB or
        PB. An equivalent field in LC-meta is  `corpus_size`.
    :ivar corpus_design_target_language: Target languages of the
        complete corpus. An equivalent field in LC-meta is
        `corpus_target_language`.
    :ivar corpus_design_target_language_type: Target languages of the
        complete corpus. If only German is the target language, this is
        coded as mono. When there are other target languages in addition
        to German , this is coded as multi.
    :ivar corpus_design_time_of_data_collection: The year or span of
        years during which the corpus was created. An equivalent field
        in LC-meta is `corpus_time_of_data_collection`.
    """
    class Meta:
        name = "Corpus_Design"

    corpus_design_description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
        }
    )
    corpus_design_design_type: Optional[StudyDesign] = field(
        default=None,
        metadata={
            "name": "corpus_design_designType",
            "type": "Element",
            "required": True,
        }
    )
    corpus_design_group: Optional[CorpusGroup] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    corpus_design_is_comparable_data_included: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "name": "corpus_design_isComparableDataIncluded",
            "type": "Element",
            "required": True,
        }
    )
    corpus_design_l1_language: List[LanguageNameDe] = field(
        default_factory=list,
        metadata={
            "name": "corpus_design_l1Language",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_design_l1_type: List[L1Constellation] = field(
        default_factory=list,
        metadata={
            "name": "corpus_design_l1Type",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_design_size: Optional["CorpusDesign.CorpusDesignSize"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_design_target_language: List[DkdTrgLang] = field(
        default_factory=list,
        metadata={
            "name": "corpus_design_targetLanguage",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_design_target_language_type: List[L1Constellation] = field(
        default_factory=list,
        metadata={
            "name": "corpus_design_targetLanguageType",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_design_time_of_data_collection: Optional[Union[XmlPeriod, str, NaString]] = field(
        default=None,
        metadata={
            "name": "corpus_design_timeOfDataCollection",
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{4}",
        }
    )

    @dataclass
    class CorpusDesignSize:
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "required": True,
            }
        )
        unit: Optional[StorageUnit] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class CorpusProficiency:
    """
    :ivar corpus_proficiency_assignment_method: The method of
        proficiency level assignment used for the corpus . An equivalent
        field in LC-meta is `corpus_proficiency_assignment_method`.
    :ivar corpus_proficiency_is_assignment_available: specification of
        whether the corpus contains proficiency scores for individual
        learner/L1 speakers or texts. A related field in LC-meta is
        `corpus_proficiency_assignment_available`.
    :ivar corpus_proficiency_learner_assignment_instrument: Name of test
        instrument used to evaluate learners’ proficiency. CMSCL has
        matching field
        `corpus_learner_proficiency_assignment_instrument`.
    :ivar corpus_proficiency_level_max: proficiency levels; if only
        approximately known, enter the maximum value here. A related
        field in LC-meta is `corpus_proficiency_level`.
    :ivar corpus_proficiency_level_min: proficiency levels; if only
        approximately known, enter the minimum value here. An equivalent
        field in LC-meta is `corpus_proficiency_level`.
    :ivar corpus_proficiency_text_assignment_instrument: Name of
        instrument used to evaluate texts’ proficiency. A related field
        in LC-meta is `corpus_text_proficiency_assignment_instrument`.
    :ivar corpus_proficiency_text_automatic_assignment_instrument:
        Specification of the automatic instrument used to assess the
        profiency of a text. A related field in LC-meta is
        `corpus_text_proficiency_assignment_instrument`.
    """
    class Meta:
        name = "Corpus_Proficiency"

    corpus_proficiency_assignment_method: ProficiencyAssignmentMethod = field(
        default=ProficiencyAssignmentMethod.NONE,
        metadata={
            "name": "corpus_proficiency_assignmentMethod",
            "type": "Element",
            "required": True,
        }
    )
    corpus_proficiency_is_assignment_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "corpus_proficiency_isAssignmentAvailable",
            "type": "Element",
            "required": True,
        }
    )
    corpus_proficiency_learner_assignment_instrument: List[str] = field(
        default_factory=list,
        metadata={
            "name": "corpus_proficiency_learner_AssignmentInstrument",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_proficiency_level_max: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "name": "corpus_proficiency_levelMax",
            "type": "Element",
            "required": True,
        }
    )
    corpus_proficiency_level_min: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "name": "corpus_proficiency_levelMin",
            "type": "Element",
            "required": True,
        }
    )
    corpus_proficiency_text_assignment_instrument: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_proficiency_textAssignmentInstrument",
            "type": "Element",
            "required": True,
        }
    )
    corpus_proficiency_text_automatic_assignment_instrument: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_proficiency_textAutomaticAssignmentInstrument",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CorpusProject:
    """
    :ivar corpus_project_contact_orig: Contact e-mail address of the
        source project (original version). LC-meta has a matching field
        `corpus_contact_mail`.
    :ivar corpus_project_duration_dkd: Duration of the project (DAKODA)
    :ivar corpus_project_duration_orig: Duration of the project
        (original version)
    :ivar corpus_project_head_dkd: One of the PIs of the Dakoda project.
    :ivar corpus_project_head_orig: Head(s) of the creation project
        (original version).
    :ivar corpus_project_institution_dkd: One of the institutions
        responsible for creating the DAKODA version of the corpus. A
        comparable field in LC-meta is `corpus_publisher`. <xs:appinfo
        xmlns:xs="http://www.w3.org/2001/XMLSchema"><displayname
        xmlns="">Einrichtungen von DAKODA</displayname></xs:appinfo>
    :ivar corpus_project_institution_orig: Institutions responsible for
        creating the source version of the corpus. If corpus resulted
        from Phd or other thesis, the relevant institution is the
        degree-conferring one. A comparable field in LC-meta is
        `corpus_publisher`.
    :ivar corpus_project_name_dkd: Name of the project (DAKODA version)
    :ivar corpus_project_name_orig: Name of related research project.
    :ivar corpus_project_type_dkd: Type of project (DAKODA)
    :ivar corpus_project_type_orig: Type of project: Funding type and
        project number of the funding organisation (original version)
    :ivar corpus_project_url_dkd: Link to related research project. A
        related variable in LC-meta is
        `corpus_related_research_project_URL`
    :ivar corpus_project_url_orig: Link to related research project. A
        related variable in LC-meta is
        `corpus_related_research_project_URL`
    """
    class Meta:
        name = "Corpus_Project"

    corpus_project_contact_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "pattern": r"([^@]+@[^\.]+\..+)|(notAvailable)",
        }
    )
    corpus_project_duration_dkd: Optional[DakodaProjectDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_project_duration_orig: Optional[Union[XmlPeriod, str, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{4}",
        }
    )
    corpus_project_head_dkd: List[DkdProjectHead] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )
    corpus_project_head_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    corpus_project_institution_dkd: List[DkdInstitution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_project_institution_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    corpus_project_name_dkd: Optional[DkdProjectName] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_project_name_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    corpus_project_type_dkd: DkdProjectType = field(
        init=False,
        default=DkdProjectType.BUNDESMINISTERIUM_F_R_BILDUNG_UND_FORSCHUNG_BMBF,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_project_type_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_project_url_dkd: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_project_URL_dkd",
            "type": "Element",
        }
    )
    corpus_project_url_orig: Optional[str] = field(
        default=None,
        metadata={
            "name": "corpus_project_URL_orig",
            "type": "Element",
        }
    )


@dataclass
class CorpusSubcorpus:
    """
    :ivar corpus_subcorpus_signet: Identifier of the (sub)corpus in the
        DAKODA repository.
    :ivar corpus_subcorpus_size_learners: The number of learners
        represented in the subcorpus. An equivalent field in LC-meta is
        `corpus_size_learners`.
    :ivar corpus_subcorpus_size_texts: The number of texts in the
        subcorpus. A related field in LC-meta is `corpus_size_texts`.
    :ivar corpus_subcorpus_size_tokens: The number of tokens in the
        subcorpus. A related field in LC-meta is `corpus_size_tokens`.
    :ivar corpus_subcorpus_target_language: Specification of the target
        language in a subcorpus as a value followig ISO 639-3. A related
        field in LC-meta is `corpus_target_language`.
    """
    class Meta:
        name = "Corpus_Subcorpus"

    corpus_subcorpus_signet: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    corpus_subcorpus_size_learners: Optional[int] = field(
        default=None,
        metadata={
            "name": "corpus_subcorpus_sizeLearners",
            "type": "Element",
            "required": True,
        }
    )
    corpus_subcorpus_size_texts: Optional[int] = field(
        default=None,
        metadata={
            "name": "corpus_subcorpus_sizeTexts",
            "type": "Element",
            "required": True,
        }
    )
    corpus_subcorpus_size_tokens: Optional[int] = field(
        default=None,
        metadata={
            "name": "corpus_subcorpus_sizeTokens",
            "type": "Element",
            "required": True,
        }
    )
    corpus_subcorpus_target_language: List[DkdTrgLang] = field(
        default_factory=list,
        metadata={
            "name": "corpus_subcorpus_targetLanguage",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class InteractionBlock:
    """
    :ivar task_interaction_conceptual_mode: Conceptual orality
        (immediacy) or conceptual literacy (distance) according to Koch
        and Oesterreicher's model of "Nähe und Distanz" . An equivalent
        field in LC-meta is `situation_medium`.
    :ivar task_interaction_expected_rhetorical_functions: The
        communicative purpose. An equivalent field in LC-meta is
        `XXX`.`situation_purpose`.
    :ivar task_interaction_formality: Formality level of the task.
        Related fields in LC-meta are  `situation_mode` and
        `corpus_mode`.
    :ivar task_interaction_mode: Corpus modality. Related fields in LC-
        meta are `corpus_mode` and `situation_mode`.
    :ivar task_interaction_participants_l1_l2_interaction: Type of
        interaction. There is no related field in LC-meta.
    :ivar task_interaction_participants: Number of speakers. An
        equivalent field in LC-meta is `corpus_single_or_multi_author`.
    :ivar task_interaction_type: Register. An equivalent field in LC-
        meta is `situation_register`.
    """
    class Meta:
        name = "Interaction_Block"

    task_interaction_conceptual_mode: List[DataProductionSettingConceptualMode] = field(
        default_factory=list,
        metadata={
            "name": "task_interaction_conceptualMode",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    task_interaction_expected_rhetorical_functions: List[RhetoricalFunctions] = field(
        default_factory=list,
        metadata={
            "name": "task_interaction_ExpectedRhetoricalFunctions",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    task_interaction_formality: FormalityType = field(
        default=FormalityType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_interaction_mode: Optional[DataProductionSettingMode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_interaction_participants_l1_l2_interaction: Optional[InteractionTypes] = field(
        default=None,
        metadata={
            "name": "task_interaction_participantsL1L2-interaction",
            "type": "Element",
        }
    )
    task_interaction_participants: List[Union[int, str, NaString]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "pattern": r"\d{1,2}-\d{1,2}",
        }
    )
    task_interaction_type: LearnerTaskType = field(
        default=LearnerTaskType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LanguageExposure:
    """
    :ivar learner_language_exposure_onset: Age of Onset. Related field
        in CMSCL are `learner_target_language_onset` and
        `learner_L"_language_onset`.
    :ivar learner_language_exposure_onset_group: Age bracket within
        which the start of acquisition for the language in question
        falls. There is no related field in CMSCL.
    :ivar learner_language_exposure_duration_of_instruction: Number of
        years of instruction of a foreign or second language. Not
        applicable to L1-instruction. A related field in CMSCL is
        `learner_target_language_learning_context` .
    :ivar learner_language_exposure_duration_of_use: Number of years in
        which learner used German (any form of learning or contact
        time). In cases, where the language in question is an L1, this
        value can be equated to the person's age at the time of text
        producton. A related field in CMSCL is
        `learner_target_language_learning_context` .
    :ivar learner_language_exposure_input: Type of input through which
        the learner came into contact with the language. A related field
        in CMSCL is `learner_target_language_learning_context`.
    :ivar learner_language_exposure_institution: Type of institution in
        which the learner learnt the language . There is a related field
        `months_spent_target_language_environment` in CMSCL.
    :ivar learner_language_exposure_months_spent_environment: Cumulative
        time (in months) spent in an environment where the L2 is spoken.
        A related field in CMSCL are
        `learner_L2_months_spent_L2_environment` and
        `months_spent_target_language_environment` .
    :ivar learner_language_exposure_learning_context: Learning context
        of target language from onset to current age. There is no
        related field in LC-meta.
    :ivar learner_language_exposure_place_acquisition: Place where
        learner mainly has learnt German (specified as a country or
        territory according to ISO 3166-ALPHA-3). A related field in
        CMSCL is `learner_target_language_learning_context`.
    :ivar learner_language_exposure_was_in_environment: Was the
        learner/L1 speaker in a country/region where the target language
        is spoken at the time of data collection? A related field in
        CMSCL is `learner_target_language_environment`.
    :ivar learner_language_was_instructed: Was the learner/L1 speaker in
        an instructed learning context at the time of data collection? A
        related field in CMSCL is `learner_target_language_instructed`.
    """
    class Meta:
        name = "Language_Exposure"

    learner_language_exposure_onset: Optional[Union[int, float, NaString]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        }
    )
    learner_language_exposure_onset_group: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_language_exposure_duration_of_instruction: Optional[Union[int, float, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_exposure_durationOfInstruction",
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        }
    )
    learner_language_exposure_duration_of_use: Optional[Union[int, float, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_exposure_durationOfUse",
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        }
    )
    learner_language_exposure_input: Optional[TrgLangInputType] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_language_exposure_institution: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    learner_language_exposure_months_spent_environment: Optional[Union[int, float, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_exposure_monthsSpentEnvironment",
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        }
    )
    learner_language_exposure_learning_context: Optional[str] = field(
        default=None,
        metadata={
            "name": "learner_language_exposure_learningContext",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_exposure_place_acquisition: Optional[CountryTypeOrNa] = field(
        default=None,
        metadata={
            "name": "learner_language_exposure_placeAcquisition",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_exposure_was_in_environment: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_exposure_WasInEnvironment",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_was_instructed: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_WasInstructed",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LearnerLanguageProficiency:
    """
    :ivar learner_language_proficiency_score: learner/L1 speaker
        proficiency (not harmonised across DAKODA corpora) A related
        field in LC-meta is `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_cefr: Learners' language
        proficiency (CEFR). An equivalent field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_c_test_cefr: Level of CEFR-
        related c-tests. An equivalent field in LC-meta is
        `learner_target_language_proficiency_CEFR_conversion`.
    :ivar learner_language_proficiency_c_test_level_detail: Detailed
        c-test level. An equivalent field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_c_test_percent: c-test result in
        per cent. A related field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_c_test_type: Name of the c-test .
        An equivalent field in LC-meta is
        `corpus_learner_proficiency_assignment_instrument`.
    :ivar learner_language_proficiency_estimate_min: Approximate
        indication of the speaker's language competence; if possible,
        based on GeR-related text assessment; if not, based on C-test
        result or duration of use (0-2 years = A2, 2-5 years = B2, &gt;5
        years = C2. If the level cannot be specified precisely, the
        lower limit of the estimated competence is given here. .A
        related field in LC-meta is
        `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_estimate_max: Approximate
        indication of the speaker's language competence; if possible,
        based on GeR-related text assessment; if not, based on C-test
        result or duration of use (0-2 years = A2, 2-5 years = B2, &gt;5
        years = C2. If the level cannot be specified precisely, the
        upper limit of the estimated competence is given here. A related
        field in LC-meta is `learner_target_language_proficiency`.
    :ivar learner_language_proficiency_self_assessment: Self-assessment
        of language skills. An equivalent field in LC-meta is
        `learner_L2_language_proficiency`.
    :ivar learner_language_proficiency_assignment_instrument: Name of
        instrument used to evaluate learners’ proficiency. An equivalent
        field in LC-meta is
        `corpus_learner_proficiency_assignment_instrument`.
    :ivar learner_language_proficiency_assignment_method: How was the
        proficiency of the learner evaluated?  An equivalent field in
        LC-meta is `corpus_learner_proficiency_assignment_method`.
    :ivar learner_language_proficiency_documentation: Link to relevant
        documentation on how learners were evaluated. An equivalent
        field in LC-meta is `corpus_learner_proficiency_documentation`.
    """
    class Meta:
        name = "Learner_Language_Proficiency"

    learner_language_proficiency_score: Optional[Union[int, Decimal, str]] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_cefr: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_c_test_cefr: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_cTestCefr",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_c_test_level_detail: Optional[str] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_cTestLevelDetail",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_c_test_percent: Optional[Union[Decimal, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_cTestPercent",
            "type": "Element",
            "required": True,
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
        }
    )
    learner_language_proficiency_c_test_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_cTestType",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_estimate_min: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_estimateMin",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_estimate_max: Optional[ProficiencyLevel] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_estimateMax",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_self_assessment: Optional[str] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_selfAssessment",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_assignment_instrument: Optional[str] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_assignmentInstrument",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_assignment_method: Optional[ProficiencyAssessmentMethod] = field(
        default=None,
        metadata={
            "name": "learner_language_proficiency_assignmentMethod",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_proficiency_documentation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Lingua:
    name_de: Optional[LanguageNameDe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name_en: Optional[LanguageNameEn] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    iso_code_639_3: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    group: Optional[LanguageGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ProductionSetting:
    """
    :ivar production_setting_school_grade: School year in which the
        productions were collected. There is no related field in LC-
        meta.
    :ivar production_setting_educational_stage: Level of education the
        learners are currently in and have not yet completed. An
        equivalent field in LC-meta is `learner_educational_background`.
    :ivar production_setting_language_test: If the texts were collected
        as part of an official language test, this represents the full
        name of the language test taken. LC-meta has a related field
        `corpus_language_testing_setting`.
    :ivar production_setting_language_course_level: Level of the
        language course currently attended. LC-meta has no equivalent
        field.
    :ivar production_setting_naturalistic: Specification of the
        elicitation context if outside institutional contexts. Possible
        values include e.g. work, family, friends, leisure. A related
        field in LC-meta is `situation_setting`.
    :ivar production_setting_collected_in_research_project: Was the data
        collected as part of a research project?
    :ivar production_setting_setting: Language production setting. An
        equivalent field in LC-meta is `corpus_production_setting`.
    """
    class Meta:
        name = "Production_Setting"

    production_setting_school_grade: Optional[Union[int, NaString]] = field(
        default=None,
        metadata={
            "name": "production_setting_schoolGrade",
            "type": "Element",
        }
    )
    production_setting_educational_stage: List[EducationalStage] = field(
        default_factory=list,
        metadata={
            "name": "productionSetting_educationalStage",
            "type": "Element",
        }
    )
    production_setting_language_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "productionSetting_languageTest",
            "type": "Element",
            "required": True,
        }
    )
    production_setting_language_course_level: str = field(
        default="notApplicable",
        metadata={
            "name": "productionSetting_languageCourseLevel",
            "type": "Element",
            "required": True,
        }
    )
    production_setting_naturalistic: Optional[str] = field(
        default=None,
        metadata={
            "name": "productionSetting_naturalistic",
            "type": "Element",
            "required": True,
        }
    )
    production_setting_collected_in_research_project: Optional[bool] = field(
        default=None,
        metadata={
            "name": "productionSetting_collectedInResearchProject",
            "type": "Element",
            "required": True,
        }
    )
    production_setting_setting: List[DataProductionSetting] = field(
        default_factory=list,
        metadata={
            "name": "productionSetting_setting",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Sociodemographics:
    """
    :ivar learner_socio_birthplace: Place of birth of the speaker. This
        is coded as country or territory. There is no related field in
        CMSCL.
    :ivar learner_socio_country: Country in which the learner spent most
        of his/her childhood. There is a related field in CMSCL,
        `learner_country`.
    :ivar learner_socio_educational_background: Highest level of
        education attained by the learner. There is a related field in
        LC-meta called `learner_educational_background`.
    :ivar learner_socio_gender: Learner/L1 speaker gender. An equivalent
        field in LC-meta is `learner_gender`.
    :ivar learner_socio_major_subject: (Major) subject at university.
        There is no related field in LC-meta .
    :ivar learner_socio_profession: Occupation. An equivalent field in
        LC-meta is `learner_socioeconomic_status`.
    :ivar learner_socio_school_grade: School year in which the text was
        collected. There is no related field in LC-meta .
    """
    learner_socio_birthplace: CountryType = field(
        default=CountryType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_socio_country: CountryType = field(
        default=CountryType.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_socio_educational_background: EducationalStage = field(
        default=EducationalStage.NOT_AVAILABLE,
        metadata={
            "name": "learner_socio_educationalBackground",
            "type": "Element",
            "required": True,
        }
    )
    learner_socio_gender: Gender = field(
        default=Gender.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_socio_major_subject: List[str] = field(
        default_factory=list,
        metadata={
            "name": "learner_socio_majorSubject",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    learner_socio_profession: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    learner_socio_school_grade: Optional[Union[int, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_socio_schoolGrade",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TargetHypothesis:
    """
    :ivar target_hypotheses_automatic: Was the th generation done fully
        automatically? A related field in LC-meta is
        `annotation_automatic`.
    :ivar target_hypotheses_corrected: Were the automatically generated
        ths subject to further correction?  A related field in LC-meta
        is `annotation_corrected`.
    :ivar target_hypotheses_documentation: Plain text description of TH
        generation process or link to documentation A related field in
        LC-meta is `annotation_documentation`.
    :ivar target_hypotheses_evaluation: Were the automatically generated
        THs evaluated? A related field in LC-meta is
        `annotation_evaluation`.
    :ivar target_hypotheses_tool: Name of tool used for generation of
        THs. A related field in LC-meta is `annotation_tool`.
    :ivar target_hypotheses_tool_version: Version of tool used for
        generating THs. A related field in LC-meta is
        `annotation_tool_version`.
    """
    class Meta:
        name = "Target_Hypothesis"

    target_hypotheses_automatic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "targetHypotheses_automatic",
            "type": "Element",
            "required": True,
        }
    )
    target_hypotheses_corrected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "targetHypotheses_corrected",
            "type": "Element",
            "required": True,
        }
    )
    target_hypotheses_documentation: Optional[object] = field(
        default=None,
        metadata={
            "name": "targetHypotheses_documentation",
            "type": "Element",
        }
    )
    target_hypotheses_evaluation: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "name": "targetHypotheses_evaluation",
            "type": "Element",
            "required": True,
        }
    )
    target_hypotheses_tool: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetHypotheses_tool",
            "type": "Element",
            "required": True,
        }
    )
    target_hypotheses_tool_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetHypotheses_toolVersion",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TextAnnotation:
    """
    :ivar text_annotation_borrowed_orig: Does the text contain
        annotations for structures taken from the task prompt? There is
        no related field in LC-meta .
    :ivar text_annotation_has_error_annotation_orig: Is the text error-
        annotated? There is no related field in LC-meta .
    :ivar text_annotation_has_target_hypotheses: Does the text have a
        target hypothesis or other type of normalisation? There is no
        related field in LC-meta.
    """
    class Meta:
        name = "Text_Annotation"

    text_annotation_borrowed_orig: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text_annotation_has_error_annotation_orig: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "text_annotation_hasErrorAnnotation_orig",
            "type": "Element",
            "required": True,
        }
    )
    text_annotation_has_target_hypotheses: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "text_annotation_hasTargetHypotheses",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TextLearner:
    """
    :ivar text_learner_age_production: Age at time of text production.
        An equivalent field in LC-meta is `learner_age`.
    :ivar text_learner_age_production_aggregated: Rough age range at the
        time of the data collection . A related field in LC-meta is
        `learner_age`.
    :ivar text_learner_role: Role of the person in this event . There is
        no related field in LC-meta .
    """
    class Meta:
        name = "Text_Learner"

    text_learner_age_production: Union[int, float, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "text_learner_ageProduction",
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        }
    )
    text_learner_age_production_aggregated: LearnerAgeRange = field(
        default=LearnerAgeRange.NOT_AVAILABLE,
        metadata={
            "name": "text_learner_ageProductionAggregated",
            "type": "Element",
            "required": True,
        }
    )
    text_learner_role: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TextProficiency:
    """
    :ivar text_proficiency_assignment_instrument: Name of instrument
        used to evaluate a text's proficiency. An equivalent field in
        LC-meta is `corpus_text_proficiency_assignment_instrument`.
    :ivar text_proficiency_assignment_method: How were the texts
        evaluated? An equivalent field in LC-meta is
        `corpus_text_proficiency_assignment_method .
    :ivar text_proficiency_cefr: Conversion of text proficiency score to
        CEFR. An equivalent field in LC-meta is
        `text_proficiency_CEFR_conversion`.
    :ivar text_proficiency_cefr_autom_max: Automatically generated rough
        level A, B or C based on CEFR; maximum value of the result. A
        related field in LC-meta is `text_proficiency`.
    :ivar text_proficiency_cefr_autom_min: Automatically generated rough
        level A, B or C based on CEFR; minimum value of the result. A
        related field in LC-meta is `text_proficiency`.
    :ivar text_proficiency_documentation: Link to relevant documentation
        on how texts were evaluated (descriptors, rubric, etc.).An
        equivalent field in LC-meta is
        `corpus_text_proficiency_documentation`.
    :ivar text_proficiency_official_language_testing_score: Results of
        the official language test (score for the text; not global score
        which should be recorded at the level of the learner/L1 speaker
        metadata). An equivalent field in LC-meta is
        `text_official_language_testing_score`.
    :ivar text_proficiency_score: Proficiency score or level for the
        text (not harmonised across DAKODA corpora). An equivalent field
        in LC-meta is `text_proficiency`.
    """
    class Meta:
        name = "Text_Proficiency"

    text_proficiency_assignment_instrument: str = field(
        default="notAvailable",
        metadata={
            "name": "text_proficiency_assignmentInstrument",
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_assignment_method: ProficiencyAssignmentMethodType = field(
        default=ProficiencyAssignmentMethodType.NOT_AVAILABLE,
        metadata={
            "name": "text_proficiency_assignmentMethod",
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_cefr: CoarseCefrLevel = field(
        default=CoarseCefrLevel.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_cefr_autom_max: CoarseCefrLevel = field(
        default=CoarseCefrLevel.NOT_AVAILABLE,
        metadata={
            "name": "text_proficiency_cefrAutomMax",
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_cefr_autom_min: CoarseCefrLevel = field(
        default=CoarseCefrLevel.NOT_AVAILABLE,
        metadata={
            "name": "text_proficiency_cefrAutomMin",
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_documentation: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_official_language_testing_score: str = field(
        default="notAvailable",
        metadata={
            "name": "text_proficiency_official_languageTestingScore",
            "type": "Element",
            "required": True,
        }
    )
    text_proficiency_score: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Annotator:
    """
    :ivar annotator_id: Unique identifier for manual annotator A related
        field in LC-meta is `annotator_id`.
    :ivar annotator_l1: Annotator L1.  An equivalent field in LC-meta is
        `annotator_L1`.
    :ivar annotator_l2: Annotator L2.  An equivalent field in LC-meta is
        `annotator_L2`.
    :ivar annotator_note: Any comments regarding the annotator. An
        equivalent field in LC-meta is `annotator_note`.
    :ivar annotator_target_language_competence: Annotator target
        language competence . An equivalent field in LC-meta is
        `annotator_target_language_competence`.
    :ivar annotator_type: Annotator experience. An equivalent field in
        LC-meta is `annotator_type`.
    """
    annotator_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotator_l1: Optional[Lingua] = field(
        default=None,
        metadata={
            "name": "annotator_L1",
            "type": "Element",
            "required": True,
        }
    )
    annotator_l2: Optional[Lingua] = field(
        default=None,
        metadata={
            "name": "annotator_L2",
            "type": "Element",
            "required": True,
        }
    )
    annotator_note: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotator_target_language_competence: Optional[str] = field(
        default=None,
        metadata={
            "name": "annotator_targetLanguageCompetence",
            "type": "Element",
            "required": True,
        }
    )
    annotator_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Corpus:
    """
    :ivar administrative: Administrative information about the corpus.
    :ivar design: Information about the corpus design.
    :ivar proficiency: Information about the corpus proficiency.
    :ivar project: Information about the project from which the corpus
        originated.
    :ivar subcorpus: Information about a subcorpus of the corpus.
    """
    administrative: Optional[CorpusAdministrative] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    design: Optional[CorpusDesign] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    proficiency: Optional[CorpusProficiency] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    project: Optional[CorpusProject] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    subcorpus: Optional[CorpusSubcorpus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LanguageOfSpeaker:
    """
    :ivar learner_language_iso639_3: Depending on the context, this
        represents information about the Learner's L1, their L2 and/or
        the target language.
    :ivar learner_language_status: What status does the language have
        for the learner? There is no single equivalent field in LC-meta.
    :ivar learner_language_is_target: Is there a text for the language
        in the corpus?
    :ivar learner_language_dominant_word_order: Word order types of L2
        according to WALS
    :ivar learner_language_group: language genus according to WALS
    :ivar learner_language_is_spoken_home: Is the language(s) spoken at
        home
    :ivar learner_language_is_spoken_school: Is the language(s) spoken
        in school
    :ivar learner_language_parent_l1: Parent L1(s)
    :ivar exposure:
    :ivar proficiency:
    """
    class Meta:
        name = "Language_Of_Speaker"

    learner_language_iso639_3: Optional[Lingua] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_language_status: List[LangStatus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    learner_language_is_target: Optional[Union[bool, NaString]] = field(
        default=None,
        metadata={
            "name": "learner_language_IsTarget",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_dominant_word_order: List[WordOrderType] = field(
        default_factory=list,
        metadata={
            "name": "learner_language_dominantWordOrder",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    learner_language_group: Optional[LanguageGroup] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_language_is_spoken_home: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "learner_language_isSpokenHome",
            "type": "Element",
            "required": True,
        }
    )
    learner_language_is_spoken_school: List[Union[bool, NaString]] = field(
        default_factory=list,
        metadata={
            "name": "learner_language_isSpokenSchool",
            "type": "Element",
        }
    )
    learner_language_parent_l1: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "learner_language_parentL1",
            "type": "Element",
        }
    )
    exposure: Optional[LanguageExposure] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    proficiency: Optional[LearnerLanguageProficiency] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class TaskBlock:
    """
    :ivar task_id: Unique identifier for the language situation. An
        equivalent field in LC-meta is `situation_id`.
    :ivar task_id_orig: The ID of the task within the source corpus. An
        equivalent field in LC-meta is `situation_id`.
    :ivar task_title: The title of the task. There is no related field
        in LC-meta.
    :ivar task_comparison: Possibility of comparing tasks and time
        points. There is no related field in LC-meta .
    :ivar task_description: Short description of the task. A related
        field in LC-meta is  `task_instructions`.
    :ivar task_description_detailed: Further descriptions with source
        reference. A related field in LC-meta is `task_instructions`.
    :ivar task_duration_minutes: Task duration in minutes.  An
        equivalent field in LC-meta is `task_duration_minutes`.
    :ivar task_instructions: Wording of the task. A related field in LC-
        meta is `task_instructions`.
    :ivar task_is_duration_limited: Was the task timed or not? A related
        field in LC-meta is `task_duration`.
    :ivar task_level_max: CEFR level of the task;  if only approximately
        known, enter the maximum value here. There is no related field
        in LC-meta .
    :ivar task_level_min: CEFR level of the task; if only approximately
        known, enter the minimum value here. There is no related field
        in LC-meta .
    :ivar task_assessed: Was the task part of an exam or any other type
        of language assessment settings (informal or for obtaining a
        certificate)? A related field in LC-meta is `task_assessed`.
    :ivar task_official_language_test: Is the task taken as part of an
        official assignment? A related field in LC-meta is
        `task_assessed`.
    :ivar task_official_language_test_specific: Official language test
        from which the task originates. There is no related field in LC-
        meta .
    :ivar task_options: Were learners able to choose between different
        tasks? There is no related field in LC-meta .
    :ivar task_stimulus_offered: Does the task include material as a
        stimulus for solving the task (e.g. diagram, article, etc.)?
        There is no related field in LC-meta .
    :ivar task_stimulus_type: Categorisation of the stimulus material.
        There is no related field in LC-meta .
    :ivar interaction:
    """
    class Meta:
        name = "Task_Block"

    task_id: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_id_orig: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_title: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_comparison: PossibilitiesForComparisons = field(
        default=PossibilitiesForComparisons.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_description: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_description_detailed: str = field(
        default="notAvailable",
        metadata={
            "name": "task_descriptionDetailed",
            "type": "Element",
            "required": True,
        }
    )
    task_duration_minutes: Union[int, str, NaString] = field(
        default=NaString.NOT_APPLICABLE,
        metadata={
            "name": "task_durationMinutes",
            "type": "Element",
            "required": True,
            "pattern": r"\d{1,3}-\d{1,3}",
        }
    )
    task_instructions: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_is_duration_limited: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "task_isDurationLimited",
            "type": "Element",
            "required": True,
        }
    )
    task_level_max: List[ProficiencyLevel] = field(
        default_factory=list,
        metadata={
            "name": "task_levelMax",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    task_level_min: List[ProficiencyLevel] = field(
        default_factory=list,
        metadata={
            "name": "task_levelMin",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    task_assessed: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_official_language_test: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "task_officialLanguageTest",
            "type": "Element",
            "required": True,
        }
    )
    task_official_language_test_specific: str = field(
        default="notAvailable",
        metadata={
            "name": "task_officialLanguageTestSpecific",
            "type": "Element",
            "required": True,
        }
    )
    task_options: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task_stimulus_offered: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "task_stimulusOffered",
            "type": "Element",
            "required": True,
        }
    )
    task_stimulus_type: List[TaskStimulusType] = field(
        default_factory=list,
        metadata={
            "name": "task_stimulusType",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    interaction: Optional[InteractionBlock] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TextProperties:
    """
    :ivar text_file: Shared ID for files related to the same learner
        production (copies of handwritten texts in pdf, transcriptions,
        sound files, videos, etc.).  An equivalent field in LC-meta is
        `text_file.
    :ivar text_id: Unique identifier for the text. A related field in
        LC-meta is `text_id`.
    :ivar text_id_orig: Unique identifier(s) for the text (original
        version). A related field in LC-meta is `text_id`.
    :ivar text_language: Language. An eqivalent field in LC-meta is
        `text_language`.
    :ivar text_longitudinal_order: Number that reflects a particular
        iteration in case the text was collected as part of a sequence
        of longitudinally collected data. There is no related field in
        LC-meta .
    :ivar text_time_of_creation: Time of creation. An equivalent field
        in LC-meta is `text_time_of_creation`.
    :ivar text_token_count: Number of tokens in the text. An equivalent
        field in LC-meta is `text_token_count`.
    :ivar text_clause_count: Number of sentences. There is no related
        field in LC-meta .
    :ivar text_topic_autom: Automatically assigned topic of the text .
        An equivalent field in LC-meta is `situation_topic_domain`.
    :ivar text_note: Any comments on the text and its origins. An
        equivalent field in LC-meta is `text_note`.
    :ivar learner:
    :ivar proficiency:
    :ivar annotation:
    """
    class Meta:
        name = "Text_Properties"

    text_file: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text_id_orig: Optional[str] = field(
        default=None,
        metadata={
            "name": "text_ID_orig",
            "type": "Element",
            "required": True,
        }
    )
    text_language: Optional[Lingua] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text_longitudinal_order: Optional[Union[int, NaString]] = field(
        default=None,
        metadata={
            "name": "text_longitudinalOrder",
            "type": "Element",
        }
    )
    text_time_of_creation: Union[XmlPeriod, str, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "text_timeOfCreation",
            "type": "Element",
            "required": True,
            "pattern": r"\d{4}-\d{4}",
        }
    )
    text_token_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "text_tokenCount",
            "type": "Element",
            "required": True,
        }
    )
    text_clause_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "text_clauseCount",
            "type": "Element",
            "required": True,
        }
    )
    text_topic_autom: List[TopicType] = field(
        default_factory=list,
        metadata={
            "name": "text_topicAutom",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    text_note: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner: Optional[TextLearner] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    proficiency: Optional[TextProficiency] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    annotation: Optional[TextAnnotation] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Learner:
    """
    :ivar learner_id: Participant ID assigned by the DAKODA project. A
        related field in CMSCL is `learner_id`.
    :ivar learner_id_orig: Participant ID assigned by the source
        project. A related field in CMSCL is `learner_id`.
    :ivar learner_l_count: Number of languages spoken including L1.
        There is no related field in CMSCL .
    :ivar learner_multiple_l1: Does the learner have more than one L1? A
        related field in CMSCL is `learner_L1`.
    :ivar learner_text_count: Number of existing texts from this person.
        There is no related field in CMSCL .
    :ivar learner_note: Any comments regarding this learner/L1 speaker.
        An equivalent field in LC-meta is `learner_note`.
    :ivar sociodemographic:
    :ivar language:
    """
    learner_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner_id_orig: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    learner_l_count: Union[int, float, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "learner_lCount",
            "type": "Element",
            "required": True,
            "min_exclusive": 0,
        }
    )
    learner_multiple_l1: Union[bool, NaString] = field(
        default=NaString.NOT_AVAILABLE,
        metadata={
            "name": "learner_multipleL1",
            "type": "Element",
            "required": True,
        }
    )
    learner_text_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "learner_textCount",
            "type": "Element",
            "required": True,
        }
    )
    learner_note: str = field(
        default="notAvailable",
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sociodemographic: Optional[Sociodemographics] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    language: List[LanguageOfSpeaker] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Document1:
    class Meta:
        name = "Document"

    corpus: Optional[Corpus] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    production_setting: Optional[ProductionSetting] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    task: Optional[TaskBlock] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    learner: Optional[Learner] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    text: Optional[TextProperties] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    target_hypothesis: List[TargetHypothesis] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    annotator: List[Annotator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Document(Document1):
    class Meta:
        name = "document"
