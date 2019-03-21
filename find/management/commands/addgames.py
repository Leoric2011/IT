import django
from django.core.management.base import BaseCommand
from find.models import UserProfile, Discount


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def populate(self):
        game1 = Discount(
            name='Hellblade: Senuas Sacrifice',
            description='Hellblade: Senuas Sacrifice is a dark fantasy action-adventure game developed and published by the British video game development studio Ninja Theory. Self-described as an "independent AAA game", it was created by a team of approximately twenty developers led by writer and director Tameem Antoniades. It was released worldwide for Microsoft Windows and PlayStation 4 in August 2017, with an Xbox One version in April 2018. The game features support for virtual reality, which was added in an update in 2018. A Nintendo Switch version is planned for a Spring 2019 release.',
            image='game_images/default.jpg',
            price='original £24.99,now at £12.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            judgediscount = True,
            url='https://www.youtube.com/embed/HVWigiK4NTs')
        game1.save()

        game2 = Discount(
            name='Red Dead Redemption 2',
            description='Red Dead Redemption 2[a] is a Western action-adventure game developed and published by Rockstar Games. It was released on October 26, 2018, for the PlayStation 4 and Xbox One consoles. The third entry in the Red Dead series, it is a prequel to the 2010 game Red Dead Redemption. Set in 1899 in a fictionalized version of the Western United States, the story centers on outlaw Arthur Morgan, a member of the Van der Linde gang dealing with the decline of the Wild West whilst attempting to survive against government forces, rival gangs, and other enemies. The story also follows fellow gang member John Marston, protagonist from the first Red Dead Redemption.',
            image='game_images/default2.png',
            price='original £59.99,now at £39.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            judgediscount = True,
            url='https://www.youtube.com/embed/yoFvVAMcwOE')

        game2.save()

        game3 = Discount(
            name='Persona 5',
            description='Persona 5[a] is a role-playing video game developed by Atlus. The game is chronologically the sixth installment in the Persona series, which is part of the larger Megami Tensei franchise. It was released for the PlayStation 3 and PlayStation 4 in Japan in September 2016, and worldwide in April 2017, where it was published by Atlus in Japan and North America and by Deep Silver in Europe and Australia. ',
            image='game_images/default3.jpg',
            price='original £49.99,now at £19.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            judgediscount = True,
            url='https://www.youtube.com/embed/9tP4UkC6dB0')

        game3.save()

        game4 = Discount(
            name='Marvels Spider-Man',
            description='Marvels Spider-Man[a] is a 2018 action-adventure game developed by Insomniac Games and published by Sony Interactive Entertainment. Based on the Marvel Comics superhero Spider-Man, it is inspired by the long-running comic book mythology and adaptations in other media. In the games main storyline, the super-human crime lord Mr. Negative orchestrates a plot to seize control of New York Citys criminal underworld. When Mr. Negative threatens to release a deadly virus, Spider-Man must confront him and protect the city while dealing with the personal problems of his civilian persona, Peter Parker.',
            image='game_images/default4.jpg',
            price='£54.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            url='https://www.youtube.com/embed/NG-Mv7cucGo',
            judgediscount = False)
        game4.save()

        game5 = Discount(
            name='God Of War Digital Deluxe Edition',
            description='God of War[a] is an action-adventure video game developed by Santa Monica Studio and published by Sony Interactive Entertainment (SIE). Released on April 20, 2018, for the PlayStation 4 (PS4) console, it is the eighth installment in the God of War series, the eighth chronologically, and the sequel to 2010s God of War III. Unlike previous games, which were loosely based on Greek mythology, this installment is loosely based on Norse mythology, with the majority of it set in ancient Norway in the realm of Midgard. For the first time in the series, there are two main protagonists: Kratos, the former Greek God of War who remains as the only playable character, and his young son Atreus; at times, the player may passively control him. Following the death of Kratos second wife and Atreus mother, they journey to fulfill her promise to spread her ashes at the highest peak of the nine realms. Kratos keeps his troubled past a secret from Atreus, who is unaware of his divine nature. Along their journey, they encounter monsters and gods of the Norse world.',
            image='game_images/default5.png',
            price='£52.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=True,
            url='https://www.youtube.com/embed/x_MtcOznfM4',
            judgediscount =False)

        game5.save()

        game6 = Discount(
            name='Yakuza Zero',
            description='Yakuza 0[b] is an action-adventure video game developed and published by Sega. It is a prequel to the Yakuza series. The game takes place in December 1988 in Kamurocho, a fictionalized recreation of Tokyos Kabukicho, and Sotenbori, a fictionalized recreation of Osakas Dotonbori. It was released for PlayStation 3 and PlayStation 4 in Japan in March 2015,[2][3] and in North America and Europe for PlayStation 4 in January 2017.[4] It was released on Microsoft Windows on August 1, 2018.[5]',
            image='game_images/default6.png',
            price='original £15.99,now at £8.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            judgediscount = True,
            url='https://www.youtube.com/embed/yYpN2LjkUmk')

        game6.save()

        game7 = Discount(
            name='Horizon Zero Dawn Complete Edition',
            description='Horizon Zero Dawn is an action role-playing game developed by Guerrilla Games and published by Sony Interactive Entertainment. It was released for the PlayStation 4 in early 2017. The plot follows Aloy, a hunter in a world overrun by machines, who sets out to uncover her past. The player uses ranged weapons, a spear and stealth to combat mechanised creatures and loot their remains. A skill tree provides the player with new abilities and bonuses. The player can explore the open world to discover side quests.',
            image='game_images/default7.png',
            price='£44.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            url='https://www.youtube.com/embed/HrxIRk3q-ck',
            judgediscount=False)
        game7.save()

        game8 = Discount(
            name='Nioh',
            description='Nioh (Japanese: 仁王 Hepburn: Niō, "benevolent king") is an action role-playing video game developed by Team Ninja for the PlayStation 4 and Microsoft Windows. It was first released worldwide in February 2017, and was published by Sony Interactive Entertainment for the PS4 internationally, and Koei Tecmo for the PS4 in Japan and Windows internationally. Gameplay revolves around navigating levels and defeating monsters that have infested an area. Nioh takes place in the early 1600s during a fictionalized version of the Sengoku period, when Japan was in the midst of civil war prior to the ascension of the Tokugawa shogunate. An Anglo-Irish sailor named William, in pursuit of an enemy, arrives in Japan and is enlisted by Hattori Hanzo, servant to Tokugawa Ieyasu, in defeating yōkai that are flourishing in the chaos of war.',
            image='game_images/default8.png',
            price='original £34.99,now at £12.99',
            reviews=0,
            rating=0,
            numberratings=0,
            avgrating=0,
            popularity=0,
            broken=False,
            judgediscount = True,
            url='https://www.youtube.com/embed/qZg6kMZbAzU')
        game8.save()

    def handle(self, *args, **options):
        self.populate()