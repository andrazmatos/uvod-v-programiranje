import re

with open("2000\\VE_1.html", "r", encoding="UTF-8") as dat:
    vsebina = dat.read()

vzorec = r'<tr><td width="\d+%" align="left"><font  >(?P<stranka>.*?)</font></td><td width="\d+%" align="right" ><font  >(<b>)*(?P<skupaj>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1001>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1002>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1003>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1004>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1005>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1006>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1007>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1008>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1009>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1010>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*(?P<o_1011>\d+(\.\d+)*)<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td></tr>'


'''<tr><td width="\d+%" align="left"><font  >.*?</font></td><td width="\d+%" align="right" ><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td><td width="\d+%" align="right"><font  >(<b>)*\d+(\.\d+)*<br>(<b>)*\d+,\d+&nbsp;%(</b>)*</font></td></tr>'''

filmi = []
for najdba in re.finditer(
    vzorec,
    vsebina,
    flags=re.DOTALL,
):
    filmi.append(
        {
            "stranka": najdba["stranka"],
            "1001": najdba["o_1001"],
            "1002": najdba["o_1002"],
            "1003": najdba["o_1003"],
            "1004": najdba["o_1004"],
            "1005": najdba["o_1005"],
            "1006": najdba["o_1006"],
            "1007": najdba["o_1007"],
            "1008": najdba["o_1008"],
            "1009": najdba["o_1009"],
            "1010": najdba["o_1010"],
            "1011": najdba["o_1011"],
        }
    )

    print(filmi)
