from __future__ import annotations

from requests import Session

from pywttr import Wttr


def test_validation() -> None:
    with Session() as session:
        wttr = Wttr("Paris", session=session)
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
