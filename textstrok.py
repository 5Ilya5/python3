from collections import Counter
import re

txt = ''' Легенда гласит, что в 1641 году нидерландский капитан Филипп Ван дер Деккен (или по некоторым версиям Ван Страатен) возвращался из Ост-Индии и вёз на борту молодую пару. 
Капитану приглянулась девушка; он убил её суженого, а ей сделал предложение стать его женой, но девушка выбросилась за борт.
При попытке обогнуть мыс Доброй Надежды корабль попал в сильный шторм. 
Среди суеверных матросов началось недовольство, и штурман предложил переждать непогоду в какой-нибудь бухте. 
Но капитан застрелил его и нескольких недовольных, а затем поклялся, что никто из команды не сойдёт на берег до тех пор, пока они не обогнут мыс,— даже если на это уйдёт вечность. 
Голос с неба сказал: «Да будет так!». Этим Ван дер Деккен, слывший страшным сквернословом и богохульником, навлёк на свой корабль проклятие. 
Теперь он, бессмертный, неуязвимый, но неспособный сойти на берег, обречён бороздить волны мирового океана до второго пришествия. 
Хотя, по некоторым версиям, у него есть шанс обрести покой: раз в десять лет Ван дер Деккен может вернуться на землю и попытаться найти ту, что добровольно согласится стать его женой.
 По другой версии, есть некое магическое слово, которое может снять проклятие и упокоить «Летучего голландца» и его экипаж.'''

cnt = Counter (x for x in re.findall(r'[А-я\']{2,}', txt))
print(cnt.most_common(10))

#Пометка! Если текст на латинице, то параметр [А-я\'] нужно поменять тоже на латинский: [A-z\']#