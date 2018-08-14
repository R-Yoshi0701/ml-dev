# -*- coding:utf-8 -*-

from polyglot.detect import Detector

t = "Hé ! bonjour, Monsieur du Corbeau.Que vous êtes joli ! Que vous me semblez beau !"
detector = Detector(t)
print(detector)

t = "em nghe nói chuẩn bị có tiệc chia tay"
detector = Detector(t)
print(detector)


t = "今回の地域紹介が逆￥限定ですので、希望女性会員の数により、男性様へのご紹介は人数限定と致しまして、長時間経過してもご返答のない方は自動破棄と判断し他の方に移行させて頂く事も有りますので、予めご了承下さい。"
detector = Detector(t)
print(detector)

t = "??????/????????? ??/????POP?????? ?????????????? ???????????? ????/??????????? ????&quot;??????????&quot;???? ??? http://nathaniel.forum.telrock.net My up to date work: http://ashlee.w.telrock.org"
detector = Detector(t)
print(detector)

t = "Мы развозим питьевую воду как частным так и юридическим лицам. Наша транспортная служба осуществляет доставку питьевой воды на следующий деньосле заказа. »-  http://voda-nn.ru - voda-nn.ru - водовозофф нижний новгород официальный сайт. Срочная доставка в день заказа доступна для владельцев клубных карт. Доставка воды прои сходит во все районы Нижнего Новгорода в верхнюю и нижнюю части города:"
detector = Detector(t)
print(detector)
