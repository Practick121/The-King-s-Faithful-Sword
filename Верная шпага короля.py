import random as r
mycoins = 15.0
pokyp = 0
shevaledm = True # показывает что пресонаж жив
vs_te_ze_kam = False
sila = r.randrange(14, 23, 2)
lovkost = r.randrange(7, 13)
brk = 0
otvet = '' # ответ пользователся на разные вопросы
moydpr = 0 # мощность удара противника
moydme = 0 # мощность удара меня
yronor = 2
invent = list()
oryg = "шпага"
print("Ваши основные параметры, ловкость и сила, определенны случайно")
print("Ваша текущая ловкость", lovkost)
print("Ваша текущая сила", sila)
print("Вам дается изначально - 15 экю")
print("Если вы хотите узнать текущие параметры, то напишите 1".upper())
print("Игра начинается!")
print()
    
def death():
    print()
    print("Ваши силы кончились, и это означает смерть. Путешествие окончено, придется начать игру сначала.")
    exit()
        
def printPr():
    print()
    print("Ваша текущаяя ловкость", lovkost)
    print("Ваша текущая сила", sila)
    print("На данный момент у вас", mycoins, "экю")
    print("А такеже ваш инвентарь: ", ', '.join(invent))
    
def printparag(text, silaplus=0, ekyplus=0):
    global sila
    global mycoins
    print()
    print(text)
    sila += silaplus
    mycoins += ekyplus

def magaz(pred1, price1, pred2, price2, pred3=0, price3=0, pred4=0, price4=0, pred5=0, price5=0):
    global otvet
    global mycoins
    global pokyp
    def buy(pred, cost):
        global mycoins
        if mycoins >= cost:
            print("Вы приобрели", pred, "за", cost, "экю.")
            mycoins -= cost
            return True
        print("У тебя недостаточно экю")
        return False
    print("1) ", pred1, "- стоит", price1, "экю.")
    print("2) ", pred2, "- стоит", price2, "экю.")
    if pred3:
        print("3) ", pred3, "- стоит", price3, "экю.")
    if pred4:
        print("4) ", pred4, "- стоит", price4, "экю.")
    if pred5:
        print("5) ", pred5, "- стоит", price5, "экю.")
    print("Ваше текущее количество экю -", mycoins)
    otvet = 1
    while otvet != 0:
        otvet = input("Напишите номер товара, который хотите купить, а если ничего не хотите купить, то напишите 0. ")
        while otvet not in {str(int(bool(pred1))), str(int(bool(pred2)) * 2), str(int(bool(pred3)) * 3), str(int(bool(pred2)) * 4), str(int(bool(pred2)) * 5), "0"}:
            otvet = input("Напишите номер товара, который хотите купить, а если ничего не хотите купить, то напишите 0. ")
        if otvet == "1":
            if buy(pred1, price1):
                invent.append(pred1)
                pred1 = 0
                pokyp = True
        elif otvet == "2":
            if buy(pred2, price2):
                invent.append(pred2)
                pred2 = 0
                pokyp = True
        elif otvet == "3":
            if pred3:
               if buy(pred3, price3):
                   invent.append(pred3)
                   pred3 = 0
                   pokyp = True
            else:
                print("Такого предмета нету!")
        elif otvet == "4":
            if pred4:
                if buy(pred4, price4):
                    invent.append(pred4)
                    pred4 = 0
                    pokyp = True
            else:
                print("Такого предмета нету!")
        elif otvet == "5":
            if pred5:
                if buy(pred5, price5):
                    invent.append(pred5)
                    pred5 = 0
                    pokyp = True
            else:
                print("Такого предмета нету!")
        if otvet == "0":
            break
        else:
            if input("Если вы хотите еще что-то купить, то напишите да ").lower() == "да":
                continue
            else:
                otvet = 0
    if pokyp: 
        print("Ваш инвентарь после покупок -: ", ", ".join(invent))

def printpvp(namep, lovkp, silp, lovkstminus=0, pomil=0):
    global pobeda
    global lovkost
    lovkost -= lovkstminus
    def pvp(namep, lovkp, silp):
        global lovkost
        global sila
        print("Атака противника - ")
        print("Мощность удара равна случайное число * 2 + ловкость")
        input("Бросить кубик(нажми ENTER)")
        print()
        brk = r.randrange(1, 7)
        moydpr = brk * 2 + lovkp
        print("Выпало число -", brk, "    Мощность удара противника -", moydpr)
        print("Теперь ваша атака - ")
        input("_Бросить кубик_(Нажми ENTER)")
        print()
        brk = r.randrange(1, 7)
        moydme = brk * 2 + lovkost
        print("Выпало число -", brk, "  Ваша мощность удара  -", moydme)
        if moydme > moydpr:
            if namep == "молодой дворянин" and brk == 3:
                print("Ваш удар заблокировала кольчуга!")
            else:
                silp -= yronor
                print("Вам удалось ранить противника, его сила - ", silp)
        elif moydme == moydpr:
            print("Вы парируете удар противника, схватка продолжается")
        elif moydme < moydpr:
            if "кольчуга" in invent and (moydpr - lovkp) // 2 == 6:
                print("Ваша кольчуга заблокировала удар! Вы не получили урон.")
            else:
                print("Вам нанесли урон")
                sila -= 2
                print("Ваши силы -", sila)
        if sila < 1:
            death()
        while sila > 0 and silp > 0:
            if silp <= pomil and pomil != 0:
                if namep == "шевалье де мишуар":
                    print('''Вы наносите шевалье сильный удар. Пока он приходит в себя, вы должны решить, убивать Шевалье Де Мишуар (290),
сорвав на нем вою злость, или попытаться расспросить его (360). ''')
                    lovkost += lovkstminus
                    return
            input("Нажми ENTER")
            print()
            print()
            print("Следующий раунд")
            brk = r.randrange(1, 7)
            moydpr = brk * 2 + lovkp
            print("Выпало число -", brk, "    Мощность удара противника -", moydpr)
            print()
            brk = r.randrange(1, 7)
            moydme = brk * 2 + lovkost
            print("Выпало число -", brk, "  Ваша мощность удара  -", moydme)
            if moydme > moydpr:
                if namep == "молодой дворянин" and brk == 3:
                    print("Ваш удар заблокировала кольчуга!")
                else:
                    silp -= yronor
                    print("Вам удалось ранить противника, его силы - ", silp)
            elif moydme == moydpr:
                print("Вы парируете удар противника, схватка продолжается")
            elif moydme < moydpr:
                if "кольчуга" in invent and (moydpr - lovkp) // 2 == 6:
                    print("Ваша кольчуга заблокировала удар! Вы не получили урон.")
                else:
                    print("Вам нанесли урон")
                    sila -= 2
                    print("Ваши силы -", sila)
        if sila < 1:
            death()
        elif silp < 1:
            print("Вы убиваете своего противника")
            lovkost += lovkstminus
    print(' ' * 5, namep.upper(), ' ' * 5)
    print("Ловкость", lovkp, " " * 5, "Сила", silp)
    printPr()
    print("Ваше оружие -", oryg, "       Ваш урон -", yronor)
    pvp(namep, lovkp, silp)
def p1():
    global otvet
    print('''Слуга выводит Арбалета из конюшни, и вы легко вскакиваете в седло. Тихий провинциальный Ажен еще спит; стук копыт гулко разносится по мостовым.
У ворот приходится первый раз воспользоваться королевским перстнем: выскочившая из караулки заспанная стража не решается нарушить строгий запрет губернатора:
никого из города не выпускать. Генрих принял необходимые меры предосторожности: теперь вы можете быть уверены, что даже самый ловкий шпион не смог бы выехать
из Ажена раньше вас. Но вот ворота позади. Теперь предстоит решить, по какой дороге направить своего коня: на Вильнев(83) или на Каор(321)?''')
    while otvet != "83" and otvet != "321":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "83":
        p83()
    else:
        print("321()")
        
def p83():
    global otvet
    print()
    print('''Через пару лье справа от дороги попадается небольшой трактир. У коновязи слуга держит лошадь, с которой спрыгивает какой-то гасконец.
Лицо его кажется странно знакомым. Увидев вас, он выходит на дорогу и знаком приглашает вас остановиться.
Задержитесь, чтобы узнать, что ему надо (401), или крикните, что у вас нет времени, и пришпорите коня(535)? ''')
    while otvet != "401" and otvet != "535":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "401":
        p401()
    else:
        p535()
        
def p535():
    global otvet
    global sila
    print()
    print('''Внимательно глядя на дворянина, чтобы он не смог незаметно достать пистолет (кто знает, что отделяет ответственность за порученное дело от мантии преследования),
даете Арбалету шпор. И через несколько минут уже лежите на земле. Тонкая, но прочная веревка, протянутая через дорогу недалеко от трактира сделала свое дело.
Арбалет упал, и вы вместе с ним (хорошо еще, что хоть немного в сторону). Вы теряете 2 СИЛЫ, правый бок болит так, как будто на него наступил слон, а в глазах даже потемнело от боли.
К счастью, вы ничего не сломали и можете подняться на ноги с помощью того самого дворянина. Он говорит, что его зовут шевалье де Мишуар, и он видел вас вчера вечером
за королевским столом. Как же он оказался здесь раньше меня? - думаете вы, но шевалье, как будто прочитав мысли, рассказывает, что он выехал из Ажена еще вчера вечером,
заночевал в этом трактире, и уже был готов тронуться в путь, как вспомнил, что не позавтракал, а , увидев вас, подумал, почему бы это не сделать вдвоем.
Про себя вы длинно и со вкусом проклинаете эту ненавязчивую любезность, которая чуть не стоила вам сломанного ребра, но делать нечего. Прямо сейчас сесть на лошадь вы все равно
не в силах, почему бы и не позавтракать. Де Мишуар помогает отвязать веревку, бормоча тысячи извинений. Что вы сделаете? Спокойно согласитесь позавтракать, понимая,
что автора этого замечательного произведения все равно не наqти (544), решите, что шевалье наверняка что-то знает, и постараетесь выбить из него эти сведения,
благо трактир кажется безлюдным (220), или наоборот, направитесь туда,намереваясь перевернуть все вверх дном, но уж добиться от хозяина, кто и зачем устроил эту ловушку (176)?''')
    sila -= 2
    while otvet != "544" and otvet != "220" and otvet != "176":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "544":
        print("544()")
    elif otvet == "220":
        p220()
    else:
        p176()
        
def p401():
    global vs_te_ze_kam
    global otvet
    print()
    print('''Дворянин говорит,что его зовут шевалье де Мишуар, и он видел вас вчера вечером за королевским столом. Перед закрытием ворот он уехал из города,
переночевал в этом трактире, а сейчас решил уже было продолжать путь, но увидел вас и вспомнил, что не позавтракал. Так почему бы не сделать это вместе? Ему все равно ехать в Бержерак,
и он с удовольствием составит вам компанию. И в самом деле, вы тоже не завтракали. Примете его приглашение (544) или ответите, что у вас нет времени (341)?''')
    while otvet != "544" and otvet != "341":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "544":
        p544()
    else:
        p341()

def p544():
    global otvet
    global sila
    global vs_te_ze_kam
    sila += 2
    print()
    print('''Позавтракать никогда не помешает, и вы с де Мишуаром заходите в трактир. Еда недурна, хозяин приветлив(Вы получаете 2 СИЛЫ), и завтрак омрачает только одно,
казалось бы незначительное происшествие. За едой вы видите, как мимо трактира на полном скаку пролетает какой-то всадник, одетый в темнозеленый камзол
на прекрасном сером в яблоках коне. А вдруг он ищет вас или, наоборот, хочет помешать продолжать путь. Долгие годы религиозных войн, когда смертельным врагом
мог оказаться самый близкий друг, приучили к подозрительности. Теперь в дальнейшем, вы сможете спросить у кого-то про этого всадника. Вам будет предложен соответствующий вариант.
 После завтрака де Мишуар предлагает составить вам компанию до Бержерака. Согласитесь на это (41) или откажетесь, сказав, что вам надо ехать очень-очень быстро(346)  ?''')
    vs_te_ze_kam = True
    while otvet != "41" and otvet != "346":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "41":
        p41()
    else:
        p346() 

def p220():
    global otvet
    global shevaledm 
    print()
    print('''Вы собираетесь быстро выхватить шпагу и пригвоздить де Мишуара к дереву, но сделать это быстро не получается - больной бок сковывает движения.
Шевалье  успевает достать свою шпагу и приготовиться к обороне. Во время боя у вас будет на одну единицу ловкости меньше: недавнее падение дает о себе знать.''')
    printpvp("шевалье де мишуар", 9, 8, 1, 2)
    shevaledm = False
    while otvet != "290" and otvet != "360":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "290":
        p290()
    else:
        p360()
    
def p341():
    global otvet
    global sila
    print()
    print('''Объяснив свой отказ недостатком времени, вы берете сразу с места в карьер и... через несколько минут лежите на земле. Обернувшись на де Мишуара, вы не заметили тонкой,
но прочной веревки, натянутой поперек дороги неподалеку от трактира. Арбалет споткнулся и с трудом удержал равновесие, но вам этого сделать не удалось. Пролетев по воздуху около
полутора метров, вы приземлились на мягкую траву на краю дороги (Вы теряете 2 СИЛЫ). Правый бок болит так, как будто в него забили несколько гвоздей, но, по счастью,
вроде бы ничего не сломано. Подбежав, де Мишуар помогает вам подняться и отвязать проклятую веревку. Сразу сесть на лошадь вы все равно не в силах, поэтому он вновь предлагает
вместе позавтракать. Но вам не дает покоя одна мысль: ведь кому-то! Но кому и зачем? Очевидно, что в ответе на этот вопрос что-то кроется и, возможно, это «что-то» направлено
против вас. Что вы сделаете? Спокойно согласитесь позавтракать, решив, что автора этой «шутки» все равно не найти (544), склонитесь к тому, что шевалье наверняка что-то знает
и постараетесь выбить из него эти сведения, благо до трактира не так уж и близко (220), или, наоборот, предпочтете направиться туда и попробуете любой ценой узнать у хозяина,
кто это сделал (176)? ''')
    sila -= 2
    while otvet != "220" and otvet != "544" and otvet != "176":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "220":
        p220()
    elif otvet == "176":
        p176()
    else:
        p544()

def p176():
    global otvet
    print()
    print('''Засунув за пояс пистолет, вы ковыляете к трактиру, чтобы вытрясти душу из хозяина, но добиться ответа на вопрос, кто подстроил эту ловушку.
Увидев ваше решительное лицо, не предвещающее ничего хорошего, тот снимает со стены мушкет, а двое поваров вооружаются кинжалами. Будете устраивать побоище (490)
или сделаете вид, что ничего не произошло, откажетесь от своей затеи, уберете пистолет и войдете в трактир безоружным (544)?''')
    while otvet != "490" and otvet != "544":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "490":
        p490()
    else:
        p544()

def p490():
    global otvet
    global vs_te_ze_kam
    printparag('''Вы достаете из-за пояса пистолет и направляете его на хозяина трактира. Тот понимает, что с оружием вы умеете обращаться гораздо лучше, чем он, и опускает мушкет.
К тому же тот оказывается незаряженным. Приставив пистолет к его груди, говорите, чтобы он приказал поварам бросить кинжалы. Он повинуется, и те кидают оба кинжала к вашим ногам.
В этот момент на дороге слышится стук копыт, и мимо трактира на полном скаку проезжает какой-то всадник, одетый в темно-зеленый камзол. Серый в яблоках конь под ним,
как это не обидно сознавать, смотрится совсем не хуже Арбалета. А вдруг он послан вашими врагами, чтобы предупредить впереди на дороге людей Лиги? Так или иначе, осторожность
не помешает. Если в будущем захотите кого-нибудь расспросить об этом всаднике, выбирайте дополнительный вариант, который будет предложен снизу.
А пока что трактирщик с полным недоумением отвечает на все вопросы. Какая еще веревка, когда он и так еле-еле успевает обслуживать посетителей? Кажется, он и впрямь не знает,
о чем идет речь. Но вы так его напугали, что завтраком вас кормят бесплатно (Вы получаете 2 СИЛЫ). После завтрака де Мишуар предлагает составить вам компанию до Бержерака.
Согласитесь (41) или откажетесь (346)?''', 2)    
    vs_te_ze_kam = True
    while otvet != "41" and otvet != "346":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "41":
        p41()
    else:
        p346()

def p41():
    global otvet
    printparag('''Вместе вы быстро добираетесь до Вильнева. Хотите заехать на рынок (552) или поторопитесь дальше(363)?''')
    while otvet != "552" and otvet != "363":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "552":
        p552()
    else:
        p363()
        
def p346():
    global otvet
    printparag('''Вы благодарите за предложение, но отвечаете, что, к сожалению, у вас нет времени на неторопливую и приятную беседу в пути: приходится торопиться и скакать,
как можно быстрее. Де Мишуар резонно возражает, что он торопится не меньше нашего. Но в этих краях нередки разбойники, поэтому вдвоем путешествовать гораздо безопасней.
Делать нечего, приходится с ним согласиться — 41 ''')
    input("Нажми ENTER ")
    print()
    p41()

def p552():
    printparag('''Если хотите купить пистолет, то он стоит 4 экю, шпага - 3, пули и порох на 5 выстрелов - тоже 3, кинжал - 2, лошадь 6. Де Мишуар советует купить хороший кинжал и
пистолет - вещи в дороге необходимые. Последуете его совету или нет, делайте необходимые покупки и торопитесь дальше - 363.''')
    magaz("пистолет", 4, "шпага", 3, "пули и порох на пять выстрелов", 3, "кинжал", 2)
    input("Нажми ENTER ")
    print()
    p363()

def p360():
    global otvet
    printparag('''Де Мишуар, обливаясь кровью, в изнеможении прислоняется к дереву. Ваша шпага упирается ему в грудь: его жизнь в ваших руках. «Зачем и кто вас подослал?»
— вот главный вопрос, на который вы хотите получить ответ. Шевалье рассказывает, что ему заплатили 2 экю за то, чтобы он вас задержал во что бы то ни стало, но вот с какой целью,
он не знает. Слова даются ему с огромным трудом, после последнего он испускает дух. Вы лезете ему в карман и забираете пресловутые 2 экю, которые покойнику уже не понадобятся — 440.''')
    input("Нажми ENTER ")
    print()
    p440()

def p290():
    global otvet
    printparag('''Последний мастерский удар, и ваша шпага попадает де Мишуару между ребрами. Быстро обыскав карманы убитого, вы находите 2 экю, которые и можете взять собой, - 440''')
    input("Нажми ENTER ")
    print()
    p440()

def p440():
    global otvet
    global vs_te_ze_kam
    printparag('''В этот момент мимо проносится всадник в зеленом камзоле на сером в яблоках коне. Что-то в нем привлекает ваше внимание и кажется подозрительным.
Если впоследствии захотите при въезде в какой-нибудь город или при встрече с кем-нибудь задать вопрос об этом незнакомце, выберите вариант, дополнительно предложенный снизу.
И если повезет, услышите ответ. А теперь хотите дойти до трактира и позавтракать (531) или же поскорее отправитесь в путь (374)?''')
    vs_te_ze_kam = True
    while otvet != "531" and otvet != "374":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "531":
        p531()
    else:
        p374()

def p531():
    global otvet
    printparag('''Решив, что все равно потеряно много и времени, и сил, решаете вернуться в трактир, чтобы по крайней мере сегодня не думать больше о еде.
За полэкю вам подают прекрасный завтрак (Вы получаете 2 СИЛЫ). Хозяин словоохотлив, все время болтает без умолку, но так и не удается понять,
видел ли он ваш поединок с шевалье де Мишуаром. По крайней мере, вопросов он никаких не задает, все больше сам рассказывает — и то ладно.
Несколько раз стараетесь сосредоточиться и прислушаться к тому, что он говорит, но боль в боку ужасно мешает. Ну, ничего, в следующий раз будете внимательней, и ни Лиге,
ни самому Дьяволу поймать вас на такой простейший трюк с веревкой больше не удастся. Поев, вы отправляетесь в путь, потрепав по холке лошадь де Мишуара, все еще сиротливо
привязанную у крыльца — 374.''', 2, -0.5)
    input("Нажми ENTER ")
    print()
    p374()

def p374():
    global otvet
    printparag('''Вот и Вильнев. Хотите заехать на рынок (645) или поедете дальше (125)?''')
    while otvet != "645" and otvet != "125":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "645":
        p645()
    else:
        p125()

def p645():
    global otvet
    printparag('''Пистолет здесь обойдется вам в 4 экю, шпага - 3, во столько же пули и порох на пять выстрелов, кинжал - в 2. После этого вы едете дальше - 125.''')
    magaz("пистолет", 4, "шпага", 3, "пули и порох на пять выстрелов", 3, "кинжал", 2)
    input("Нажми ENTER ")
    print()
    p125()

def p125():
    global otvet
    printparag('''На одной из улиц вас поджидает не столько странное, сколько неприятное происшествие: где-то наверху открывается окно, и вас окатывает поток грязной воды.
Что это: чья-то оплошность или ловушка? Остановитесь и зайдете в дом, чтобы потребовать извинений (55) или поедете дальше (619) ?''')
    while otvet != "55" and otvet != "619":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "619":
        p619()
    else:
        p55()

def p363():
    global otvet
    printparag('''Когда вы проезжаете по одной из улиц, где-то наверху неожиданно открывается окно, и вас окатывает поток грязной воды. Что это: чья-то оплошность или ловушка?
Хотите остановиться и зайти в этот дом, чтобы потребовать извинений (55), или поедете дальше (568)''')
    while otvet != "55" and otvet != "568":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "55":
        p55()
    else:
        p568()

def p568():
    global otvet
    printparag('''Де Мишуар ужасно удивлен, видя, что вы собираетесь как ни в чем не бывало продолжать путь. "Как! - воскликцает он. Разве можно прощать такое оскорбление?"
Вы ловите в его глазах некий оттенок презрения. Теперь остается только два выхода: дуель с де Мишуаром, который посмел комментировать ваши поступки и давать им оценку (397),
или решить, что шевалье прав и зайти в дом(55).''')
    while otvet != "55" and otvet != "397":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "55":
        p55()
    else:
        p397()   

def p55():
    global otvet
    printparag('''Рывком открыв дверь дома, сталкиваетесь нос к носу с его хозяином. Тот, взревев: «Да как ты, мерзавец, посмел ко мне вломиться», хватается за шпагу.
Дуэль неизбежна.''')
    printpvp("Хозяин дома", 7, 9)
    print("Теперь вы можете либо побыстрее уехать (262), либо все же войти в дом и узнать, кто вылил на вас воду (575)")
    while otvet != "262" and otvet != "575":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
    if otvet == "262":
        p262()
    else:
        p575()

def p397():
    global otvet
    global shevaledm
    printpvp("Шевалье де Мишуар", 9, 8)
    shevaledm = False
    input("Нажми ENTER")
    p65()

def p65():
    global otvet
    global mycoins
    global sila
    printparag('''В карманах убитого находите 2 экю, которые можете взять себе. Кроме того, не выезжая из Вильнёва, вы продаете его лошадь и шпагу еще за 5 экю.
Конечно, некоторым это может показаться предрассудительным, но если рассматривать лошадь как военную добычу… Впрочем, до предрассудков ли, когда сам Король столь беден,
и выделенных им денег ну никак не может хватить на такое длинное и опасное путешествие. За 1 экю можете пообедать в трактире (и восстановить 2 СИЛЫ)
и продолжать путь — до Перигё, где вы наметили заночевать, еще добрых тридцать лье — 619.''', ekyplus=7)
    otvet = input("Вы собираетесь пообедать в трактире или сразу продолжите приключение? да/619")
    while otvet.lower() != "да" and otvet != "619":
        otvet = input("Выберите число или слово из предложенных и напишите его ")
        if otvet == "1":
            printPr()
    if otvet.lower() == "да":
        mycoins -= 1
        sila += 2
        print("Дальше откладывать путешествие незачем, поэтому в путь - 619")
        p619()
    else:
        p619()

def p619():
    global otvet
    global mycoins
    printparag(''' Часам к четырем вечера вы в Бержераке. Небольшой уютный городок ещё не познал всех тягот войны.
Армия Короля Наварры пока что надежно защищает ее. Если вам почему-либо перестала нравиться дорога, которую вы избрали, то можете за 2 экю сесть на небольшое судно,
которое доставит вас к вечеру до причала рядом с Суйаком (72). Добавив еще полтора су, можете доплыть почти до самого Орийака (278).Иначе же поторопитесь,
чтобы до захода солнца добраться до Перигё — 528.''')
    while otvet != "72" and otvet != "278" and otvet != "528":
        otvet = input("(Выберите число из предложенных и напишите его) ")
        if otvet == "1":
            printPr()
        if otvet == "72":
            if mycoins >= 2:
                break
            else:
                print("Недостаточно денег!")
                otvet = 0
        elif otvet == "278":
            if mycoins >= 2.05:
                break
            else:
                print("Недостаточно денег!")
                otvet = 0
    if otvet == "72":
        mycoins -= 2
        print("p72()")
    elif otvet == "278":
        mycoins -= 2.05
        print("p278()")
    else:
        print("p528()")       

def p575():
    global otvet
    printparag('''Быстро взбежав по лестнице на второй этаж, ожидаете увидеть нерадивую служанку, но вместо этого вас встречает пистолетный выстрел.
Едва увернувшись (пуля все же задевает левую руку — вы теряете 2 СИЛЫ), врываетесь в комнату, полную порохового дыма и видите улыбающегося молодого дворянина в легкой кольчуге,
который поджидает вас со шпагой в руках. Так и есть: Лига! Во время боя если за вас на кубике выпадает тройка, то вам не удается благодаря кольчуге ранить противника,
даже если ваша Сила удара и получится выше.''', -2)
    printpvp("молодой дворянин", 8, 8)
    input("Нажми ENTER")
    p296()

def p296():
    global otvet
    printparag('''Теперь кольчуга ваша. Когда во время боя на кубике у вашего противника выпадет 6, она отразит удар. А теперь лучше побыстрее уехать — 262.''')
    invent.append("кольчуга")
    input("Нажми ENTER")
    p262()

def p262():
    if shevaledm:
        p587()
    else:
        p619()

def p587():
    global otvet
    printparag('''Вы оглядываетесь в поисках шевалье де Мишуара, но видите, что он исчез. Значит, подозрения оказались правильными — он был подослан Лигой,
чтобы проследить за тем, чтобы вы исправно попали в ловушку. Теперь его задание выполнено. А вы покидаете Вильнёв и отправляетесь дальше — 619.''')
    input('Нажми ENTER')
    p619()

    
print()
p1()
