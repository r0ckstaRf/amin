import os
import random
from os import system
import urllib
import json
from json import dumps, load
import argparse
from urllib.request import urlopen
import amino
import time
from gtts import gTTS
import requests
from uuid import uuid4
client = amino.Client()
print("\t\033[1;32m Моречка  \033[1;36m камунити бот \n\n")
email = "hellocrite4@gmail.com"
password = "24112006"

client.login(email=email, password=password)

cid = "165541630"
cidy = 165541630

adm = ["http://aminoapps.com/p/1wl9ab0"]
self = client.socket


def generate_transaction_id(self):
    return str(uuid4())


transaction = generate_transaction_id(self)

admx = ["http://aminoapps.com/p/1wl9ab0"]

client.join_community(cid)
for i in admx:
    try:
        w = client.get_from_code(i).objectId
        adm.append(w)
    except:
        print("Invalid link")
subclient = amino.SubClient(comId=cid, profile=client.profile)
msg = """Follow GC rules
1.БЕЗ СПАМААА
2.уважайте лидеров(асобенно пери лох абъелся блох уххмахазхаа)
3.Нот токсик битчес
4.будьте вежливы и устройте резню хухзапзпхпзах"""
print("Bot joined community")
subclient = amino.SubClient(comId=cid, profile=client.profile)
print("Joining All chatrooms")
subclient = amino.SubClient(comId=cid, profile=client.profile)
chts = subclient.get_public_chat_threads(type="recommended", start=0, size=25).chatId
for chats in chts:
    try:
        subclient.join_chat(chatId=chats)
    except Exception:
        pass
print("Joined all chatrooms")
print("Alexa 1.0 Ready")
l = []
lis = ["Это точно",
       "Это решительно так",
       "Без сомнения",
       "Да, безусловно",
       "Вы можете положиться на него",
       "Насколько я понимаю, да",
       "Наверняка",
       "Прогноз хороший",
       "Да",
       "Знаки указывают на да",
       "Напишите ещё раз я тупая",
       "Спросите позже я дцп",
       "Лучше не говорить тебе сейчас",
       "Не могу сейчас предсказать",
       "Сконцентрируйся и спроси еще раз",
       "Не рассчитывай на это",
       "Мой ответ нет",
       "Мои источники говорят нет",
       "Прогноз не очень хороший",
       "Очень сомнительно", "Да", "Нет", "наверное", "100%", "Не уверен"]


@client.event("on_group_member_join")
def on_group_member_join(data):
    if data.comId == cidy:
        try:
            x = data.message.author.icon
            response = requests.get(f"{x}")
            file = open("sample.png", "wb")
            file.write(response.content)
            file.close()
            img = open("sample.png", "rb")
            subclient.send_message(chatId=data.message.chatId, message=f"""
[C]━━━━━━━━━━━━━━━
[c]приветики пистолетики <${data.message.author.nickname}$>
[C]━━━━━━━━━━━━━━━
{msg}
[C]━━━━━━━━━━━━━━━""", embedId=data.message.author.userId, embedTitle=data.message.author.nickname,
                                   embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}", embedImage=img,
                                   mentionUserIds=[data.message.author.userId])
            print(f"\nwelcomed {data.message.author.nickname} to gc ")
        except Exception as e:
            print(e)


@client.event("on_group_member_leave")
def on_group_member_leave(data):
    if data.comId == cidy:
        try:
            subclient.send_message(chatId=data.message.chatId, message="""[c]какой-то додик ушёл""")
            print(f"Someone left the gc")
        except Exception as e:
            print(e)


@client.event("on_text_message")
def on_text_message(data):
    if data.comId == cidy:
        ex = data.message.content
        cd = ex.split(' ')
        x = cd[0]
        c = cd[1:]
        adx = []
        for w in cd:
            adx.append(w)
        print(adx)
        if ex:
            for i in adx:
                if len(i) <= 50:
                    if i[:23] == "http://aminoapps.com/p/" or i[:23] == "http://aminoapps.com/c/":
                        fok = client.get_from_code(i)
                        cidx = fok.path[1:fok.path.index("/")]
                        if cidx != cid:
                            try:
                                subclient.delete_message(chatId=data.message.chatId, messageId=data.message.messageId,
                                                         asStaff=True)
                                s = subclient.get_chat_thread(data.message.chatId).title
                                subclient.start_chat(userId=adm,
                                                     message=f"ndc://x{cid}/user/profile/{data.message.author.userId} was advertisng in {s}")

                                subclient.send_message(chatId=data.message.chatId,
                                                       message=f"<${data.message.author.nickname} don't advertise here")
                                print("spotted advertiser")
                            except Exception as e:
                                print(e)
            if x.lower() == "/info" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="[ci]Я крч ботяра тупая сделано фишлёй")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/global":
                try:
                    for i in c:
                        mention = subclient.get_message_info(chatId=data.message.chatId,
                                                             messageId=data.message.messageId).mentionUserIds
                        for user in mention:
                            h = subclient.get_user_info(userId=str(user)).nickname
                            AID = client.get_user_info(userId=str(user)).aminoId
                            d = client.get_from_code(i).objectId
                            subclient.send_message(chatId=data.message.chatId,
                                                   message="https://aminoapps.com/u/" + str(AID),
                                                   embedTitle="Global Id", embedContent=f"{h}")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/clear":
                if x.lower() not in l:
                    try:
                        for i in c:
                            d = int(i)
                            a = subclient.get_chat_messages(chatId=data.message.chatId, size=d)
                            for i in a.messageId:
                                subclient.delete_message(chatId=data.message.chatId, messageId=i, asStaff=True,
                                                         reason="clear")
                            subclient.send_message(chatId=data.message.chatId, message=f"очищено {d} сообщений")
                    except:
                        subclient.send_message(chatId=data.message.chatId,
                                               message="[ci]дайте ботяре лидерку или куратора чтобы эта функция заработала ну екалемане")
                else:
                    subclient.send_message(chatId=data.message.chatId, message="Clear заблокирована ботяры")
            if x.lower() == "/llock" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message=f"заблокированные комманды {l}")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/lock":
                if data.message.author.userId in adm:
                    try:
                        for i in c:
                            l.append(i)
                            subclient.send_message(chatId=data.message.chatId,
                                                   message=f"заблокирована {i} комманда, ботяры не могут её использывать упзхапзапхлщах")
                            print(l)
                            print(f"Info requested by {data.message.author.nickname}")
                    except Exception as e:
                        print(e)
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message="Ты не имеешь право использывать эту команду батиха")
                    except Exception as e:
                        print(e)
            if x.lower() == "/unlock":
                if data.message.author.userId in adm:
                    try:
                        for i in c:
                            l.remove(i)
                            subclient.send_message(chatId=data.message.chatId, message=f"разблокирована {i} команда")
                            print(l)
                            print(f"Info requested by {data.message.author.nickname}")
                    except Exception as e:
                        print(e)
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message="Ты не имеешь право использывать эту команду батиха")
                    except Exception as e:
                        print(e)
            if x.lower() == "/say":
                if x.lower() not in l:
                    if c == []:
                        try:
                            subclient.send_message(chatId=data.message.chatId,
                                                   message=f"{data.message.author.nickname}, Я пока что немая стала, если ты не напишешь что-нибудь после команды")
                        except:
                            pass
                    else:
                        try:
                            t = ''
                            lx = 'en'
                            for i in c:
                                t = t + i
                            out = gTTS(text=t, lang=lx, tld='co.in', slow=False)
                            out.save("soundfx.mp3")
                            with open("soundfx.mp3", "rb") as f:
                                subclient.send_message(chatId=data.message.chatId, file=f, fileType="audio")
                            f.close()
                            print(f"Info requested by {data.message.author.nickname}")
                        except Exception as e:
                            print(e)
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId, message="say command is locked")
                    except:
                        pass
            if x.lower() == "/join":
                if c == []:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message=f"{data.message.author.nickname}, вставь ссылку дурачье")
                    except:
                        pass
                else:
                    try:
                        for i in c:
                            try:
                                d = client.get_from_code(i).objectId
                                subclient.join_chat(chatId=d)
                                subclient.send_message(chatId=data.message.chatId,
                                                       message="я присоединилась к гей пати !!")
                            except Exception as e:
                                print(e)
                        print(f"Info requested by {data.message.author.nickname}")
                    except Exception as e:
                        print(e)
            if x.lower() == "/vc" and c == []:
                try:
                    subclient.invite_to_vc(userId=data.message.author.userId, chatId=data.message.chatId)
                    print(f"Invited {data.message.author.nickname} to vc")
                except Exception as e:
                    print(e)
                    subclient.send_message(chatId=data.message.chatId,
                                           message=f"[ic]я не могу тебя пригласить у меня спид, <$@{data.message.author.nickname}$>")
            if x.lower() == "/inviteall" and c == []:
                if x.lower() not in l:
                    try:
                        h = subclient.get_all_users(start=0, size=1000).profile.userId
                        m = len(h)
                        for u in h:
                            try:
                                subclient.invite_to_chat(userId=u, chatId=data.message.chatId)
                            except Exception as e:
                                print(e)
                                pass
                        subclient.send_message(chatId=data.message.chatId, message=f"[ic]пригласила {m} бомжар в гч")
                        print(f"invited {data.message.author.nickname} to vc")
                    except Exception as e:
                        print(e)
                        subclient.send_message(chatId=data.message.chatId,
                                               message=f"[ic]я не могу тебя пригласить у меня спид, <$@{data.message.author.nickname}$>")
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId, message="Inviteall заблокана батихи")
                    except:
                        pass
            if x.lower() == "/pm" and c == []:
                if x.lower() not in l:
                    try:
                        subclient.start_chat(userId=data.message.author.userId, message="чо хотел пидор!")
                        subclient.send_message(chatId=data.message.chatId,
                                               message=f"я тебе скинула ножки в дисике <${data.message.author.nickname}$> !!",
                                               mentionUserIds=[data.message.author.userId])
                        print(f"invite {data.message.author.nickname} to pm")
                    except Exception as e:
                        print(e)
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message=f"Pm команда заблокана батиха <${data.message.author.nickname}$> !!",
                                               mentionUserIds=[data.message.author.userId])
                    except:
                        pass
            if x.lower() == "/startvc" and c == []:
                if x.lower() not in l:
                    try:
                        subclient.send_message(chatId=data.message.chatId, message="через 5 сек я начну громко пукать")
                        time.sleep(5)
                        client.start_vc(comId=cid, chatId=data.message.chatId, joinType=1)
                        # subclient.send_message(chatId=data.message.chatId,message=f"Vc started")
                        print(f"VC started")
                    except Exception as e:
                        print(e)
                        try:
                            subclient.send_message(chatId=data.message.chatId,
                                                   message=f"[ic]я не могу тебя пригласить у меня спид, <${data.message.author.nickname}$>",
                                                   mentionUserIds=[data.message.author.userId])
                        except:
                            pass
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message=f"Start команда заблокана <${data.message.author.nickname}$> !!",
                                               mentionUserIds=[data.message.author.userId])
                    except:
                        pass
            if x.lower() == "/endlive" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="а я помру щас через 5 сек")
                    time.sleep(5)
                    client.end_vc(comId=cid, chatId=data.message.chatId, joinType=2)
                except Exception as e:
                    print(e)
                    subclient.send_message(chatId=data.message.chatId,
                                           message=f"[ic]я не могу тебя пригласить у меня спид, <${data.message.author.nickname}$>",
                                           mentionUserIds=[data.message.author.userId])
            if x.lower() == "/onlinemem" and c == []:
                if x.lower() not in l:
                    try:
                        o = ""
                        q = subclient.get_online_users(start=0, size=1000)
                        for uid in q.profile.nickname:
                            o = o + uid + "\n"
                        subclient.send_message(chatId=data.message.chatId, message=f"""[c]смотрят на тебя около
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
[c]{o}
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
                        print("done")
                    except Exception as e:
                        print(e)
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId, message="Members Заблокана")
                    except:
                        pass

            if x.lower() == "/goodmorning" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId,
                                           message=f"[cb]доброе утро чувырла <${data.message.author.nickname}$> !!",
                                           mentionUserIds=[data.message.author.userId])
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/follow" and c == []:
                try:
                    subclient.follow(userId=data.message.author.userId)
                    subclient.send_message(chatId=data.message.chatId,
                                           message=f"[c]я подписалась, теперь ты мой раб уащзвпапзщхвпщз <${data.message.author.nickname}$> ",
                                           mentionUserIds=[data.message.author.userId])
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/goodevening" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId,
                                           message=f"[cb] добрый вечер <${data.message.author.nickname}$> !!",
                                           mentionUserIds=[data.message.author.userId])
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/love":
                try:
                    for i in c:
                        msg = i + " null null "
                        msg = msg.split(" ")
                        msg[2] = msg[1]
                        msg[1] = msg[0]
                        subclient.send_message(chatId=data.message.chatId, message=f"""[c]-----------------
[c]Match ❤️  {random.randint(0, 100)}%
[c]---------------""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/dance" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="""
(_＼ヽ
　 ＼＼ .Λ＿Λ.
　　 ＼(　ˇωˇ)　
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|   я тут пукнула
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ ) 　 Lﾉ
(_／""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/help" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="""[c]команды
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
/peri (трахайте пери ему понравиться)
/join                       /global
/say                        /pm
/goodmorning      /unlock
/startvc                 /dance
/goodnight            /leader
/playlist                 /inviteall
/llock                       /clear
/play                       /goodnight
/endlive                  /meme
/mori                  /info
/chocolate             /nickname
/profilepic              /dance
/joke                       /8ball
/follow                    /coin
/onlinemem           /lock
/love                        /gf

[ci]
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/coin":
                try:
                    for i in c:
                        d = int(i)
                        print(transaction)
                        subclient.send_coins(coins=d, chatId=data.message.chatId, transactionId=transaction)
                        subclient.send_message(chatId=data.message.chatId, message=f"прислала {d} манет хозяину а вы батихпалпавовлдроврваршпарв аоплквп")
                except Exception as e:
                    print(e)
            if x.lower() == "/goodnight" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId,
                                           message=f"[cb]тебе завтра в садик <${data.message.author.nickname}$> !!",
                                           mentionUserIds=[data.message.author.userId])
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/music" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId,
                                           message="""[ci]Вечеринка всю ночь ... Вечеринка всю ночь .""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/nickname":
                try:
                    t = ''
                    for i in c:
                        t = t + i
                        subclient.edit_profile(nickname=t)
                        subclient.send_message(chatId=data.message.chatId, message=f"ты чо изменил ник на {i}")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/profilepic" and c == []:
                try:
                    info = subclient.get_message_info(chatId=data.message.chatId, messageId=data.message.messageId)
                    reply_message = info.json['extensions']
                    if reply_message:
                        image = info.json['extensions']['replyMessage']['mediaValue']
                        filename = image.split("/")[-1]
                        filetype = image.split(".")[-1]
                        urllib.request.urlretrieve(image, filename)
                        with open(filename, 'rb') as fp:
                            for i in range(1, 8):
                                try:
                                    subclient.edit_profile(icon=fp)
                                except Exception as e:
                                    subclient.send_message(data.message.chatId, message="аватарка изменена",
                                                           replyTo=data.message.messageId)
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/playlist" and c == []:
                try:
                    files = os.listdir("music")
                    o = ""
                    for f in files:
                        o = o + f + "\n"
                    subclient.send_message(chatId=data.message.chatId, message=f"""
[c]музыка с рекламай
[c]𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁
{o}
𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁𐄙𐄁""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/gf" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="""[bi]ты одинок (づ｡◕‿‿◕｡)づ
[i] ну ты и лох конечно""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/joke" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId,
                                           message="""[i]нашли как-то 4 негра золотую лампу....""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/8ball":
                try:
                    subclient.send_message(chatId=data.message.chatId, message=str(random.choice(lis)),
                                           replyTo=data.message.messageId)
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/play":
                if subclient.get_chat_thread(data.message.chatId).title != None:
                    mx = random.choice(os.listdir("music"))
                    if x.lower() not in l:
                        sounds = f"music/{mx}"
                        with open(sounds, "rb") as f:
                            try:
                                subclient.send_message(chatId=data.message.chatId, file=f, fileType="audio")
                                print(f"Info requested by {data.message.author.nickname}")
                            except Exception as e:
                                print(e)
                    else:
                        try:
                            subclient.send_message(chatId=data.message.chatId, message="заблокана команда")
                        except:
                            pass
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message="только в личке, напиши /pm чтобы я тебе скинула чулочки из ашана")
                    except:
                        pass
            if x.lower() == "/meme":
                if subclient.get_chat_thread(data.message.chatId).title != None:
                    hx = random.choice(os.listdir("memes"))
                    if x.lower() not in l:
                        sounds = f"memes/{hx}"
                        with open(sounds, "rb") as f:
                            try:
                                subclient.send_message(chatId=data.message.chatId, file=f, fileType="image")
                                print(f"Info requested by {data.message.author.nickname}")
                            except Exception as e:
                                print(e)
                    else:
                        try:
                            subclient.send_message(chatId=data.message.chatId, message=" заблокана")
                        except:
                            pass
                else:
                    try:
                        subclient.send_message(chatId=data.message.chatId,
                                               message="только в личке, напиши /pm чтобы я тебе скинула чулочки из ашана")
                    except:
                        pass
            if x.lower() == "/leader" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="себя чекни")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/mori" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="Вы оттарабанили фишлю. вот так ему и надо а то как обычно хуи пинает")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/peri" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId,message="Вы потрахали пери. ДАЙТЕ ЕМУ БОЛЬШИЕ ЧЛЕНЫ")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/aboutme" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="""ты батиха ухаазпазщпвхплвщп""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)
            if x.lower() == "/chocolate" and c == []:
                try:
                    subclient.send_message(chatId=data.message.chatId, message="""
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ шоколадку негров(hot bebra)
╚╩╩╩╝""")
                    print(f"Info requested by {data.message.author.nickname}")
                except Exception as e:
                    print(e)


def socketRoot():
    j = 0
    while True:
        if j >= 300:
            print("Updating socket.......")
            client.close()
            client.start()
            print("Socket updated")
            j = 0
        j = j + 1
        time.sleep(1)


socketRoot()
