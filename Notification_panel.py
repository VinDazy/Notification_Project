from winotify import Notification,audio
from Quotes import messages
from random import randint
#import time
i=randint(0,len(messages)-1)
quote=messages[i]
emojis=['โฅ','๐','๐','๐','๐งก','โฃ','๐ค','๐','๐','๐','๐','๐','๐งจ','โจ','โจ','๐','๐','๐','๐','๐','๐ผ','๐','๐','๐','๐ซ','๐งฟ','๐','๐' ,'๐ช','๐ฏ','๐ฅ','๐','๐ข','๐ฃ','๐']
j=randint(0,len(emojis)-1)
emoji1=emojis[j]
j=randint(0,len(emojis)-1)
emoji2=emojis[j]


panel=Notification(app_id=f"{emoji1} Daily Affirmations {emoji1}",
                    title=f"                          Hey You {emoji2}",
                    msg=quote,
                    duration="long",
                    icon=r"C:/Users/ebdel/Desktop/Notification_project/stich.jpg"
                    )
panel.set_audio(audio.Mail,loop=False)
if quote=="Don't forget to journal and refect":
    panel.add_actions(label="Let's Reflect ๐", 
                  launch="https://habitica.com")
elif quote=="Time to Grow ! ":
        panel.add_actions(label="Let's Learm Javascript ๐ป โคต โฌ", 
                  launch="https://www.sololearn.com/learning/1024")
        

    





panel.show()