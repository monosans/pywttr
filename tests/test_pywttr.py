from __future__ import annotations

from requests import Session

import pywttr


def test_pywttr() -> None:
    wttr = pywttr.Wttr("Paris")
    wttr.en()
    with Session() as session:
        wttr.session = session
        wttr.af()
        wttr.am()
        wttr.ar()
        wttr.be()
        wttr.bn()
        wttr.ca()
        wttr.da()
        wttr.de()
        wttr.el()
        wttr.et()
        wttr.fa()
        wttr.fr()
        wttr.gl()
        wttr.hi()
        wttr.hu()
        wttr.ia()
        wttr.id()
        wttr.it()
        wttr.lt()
        wttr.mg()
        wttr.nb()
        wttr.nl()
        wttr.oc()
        wttr.pl()
        wttr.pt_br()
        wttr.ro()
        wttr.ru()
        wttr.ta()
        wttr.th()
        wttr.tr()
        wttr.uk()
        wttr.vi()
        wttr.zh_cn()
        wttr.zh_tw()
