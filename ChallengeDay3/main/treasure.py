def adventure():
    print('Welcome to Treasure Island.')
    print('Your mission is to find the treasure. Take your map and start the adventure!')
    print('''
  _____________________________________________________________________
  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
  |___________________________________________________________________|
  ''')
    choice1 = input(
        'When following the map, you need to decide to go left or right. Type Left or Right to continue: ')
    choice1 = choice1.lower()
    choice2 = None
    choice3 = None

    if choice1 == 'right':
        print('''


                                            ,---._
                                          ,~~,-._  `._
                                            v'~   `-.  `.
                                                _,- ~.  \
                                              .'  ,--`.  `\_
                                              V-'~ ,'~~~`-. `-.
                                  ___             /_/~~~) ` `. `._
                          ____,---'   ;            V     `.__ `--, `;
                          `-._    ;  `.                ____)       :
                              `.;  ; .'              ,'        _    |
                                ; |   ;              ,';'~~~`--' `;  :
                              ,': .-'               `,'  __ __   :  |
                              )_  `-, ___     __        (__:__)   ; ;
                          _,---. \___,'` ~`---;  `-.       |||    ;  ;
                      _,-/   :;     !   `     `|    `-.   |~~~~|   ; :
                  _,-' /~   .,'  ;  !!  `..    ``.    `.  :    ;  | :
                ,'  ,-'    .;   `; !!   _,'-' ,--._    ====\__/===: `.
              .'  ,-'   ,--.  ~~`-. !!  ~    ,'    `     `./  \   |  |
            .'  :;   ,'    \        !: .   ;--.__   `;.  |. ~.|   : ;
            .'  ,;    ' ,-'~~`-.     ,!  ;-'     #;   `;. \____/  : `.
          .'  ,;      /__      `-._,'!!( _(0'~~`-'    `;.  `.     ; ;
          .'  ,;    ,'    `---._(0))  !! ~   _,-,        `;  `.   ;  :
          ;  ,;    ,' ;;-.__,-._~~~   !!__,--::::|.      `;:  :   `; )
          ;  :|   ,'  ;/;;; :::;;;;----'|:: |::;\/#.      `;  |    ) ;
          :  |:  ,'  ,' :/  :;; \/))):;;::/  ::' ##:      ;;  ;    ; |
          |  :|  :;  :      `'    \/ \/ `'   `'  ##;      ;  .'  ,'  ;
          :  |;  || .'        ;\.   ____ __,--._ ##;     ;' .'--'   ;
      _,--`. `.  :: `./;   /\/;:;,-'    `-.     `--.__     .'~   ,'~
    /     ;. `; ``. :::;\;.-'~~`./~~\/\ ..    _  :::  --. ' ,-'~
    /    .  `. `; `   ~~~ ;~      ~~~~~~`--.__~~`-. :::   ) ~
  /'    ;`--`. `. `.    :;      `;       ;   `---`._    ,'
  `.  \/      `-.` `_,_ `:,-'-. `.      :_,_    ;   `--'
    `.  `.        ` (___)-: ( ) :--,-'- -(___),'~~~`.
    {_  `.               `.___.' ( ; ;)      :((:)):
      `.  `                       `--'       `.___.'
        `. `.                 ;;:::;
          `-  `.              ;;;. .;
            `-. `.__        \\;;; - ;; //
              `. ` `--..___ \\,--v-, //      Help luquitas !!!
                `--._   ~~~~~`)____(//
                      )    ~~   ~~~~~~;
                      `.    ~~  ------;
                      `.~~_   ______,' f guerreiro
                        `. `.--';: |:
                        ;  `. Cc; Cc
                        `.  ;  __
                          `. `-'  ~\
                          `-.__,--'~

      ''')
        return 'A giant pumpkin killed you. Game Over.'

    elif choice1 == 'left':
        choice2 = input('Swim or Wait? Type Swim or Wait to continue: ')
        choice2 = choice2.lower()
        if choice2 == 'wait':
            print('''
                            ___
                .dSSSS$$pp..
              .dSSSS$$$$$$$$;
            .dSSSS$$$$$$$$$$$
            :SSP^" T$$$$$$$$$$b_
          dSSP     $$$S$$$$$$$b`
          dSS$;_.  .:$$$SS$$$$$$b
        dSS$$$_ ;  __."^TSS$$$$$b
        dSS$$P;"    ""'  :lSS$$$$$b
      :SS$$$ ;          ::SS$$$$$$b_.
      SSS$$$ :  `       ;:SS$$$$$$$bp.
      :SS$$$$b \ -=-  .-" SSS$$$$$$$$$$b
      SSS$$$$$b.`.   /   d$SS$$$$$$$$$$$b
      :SS$$$$$$$; ""T   :$$$SS$$$$$$$$P^^t--'
      SSS$$$S$$$   :   $$$$$SS$$$$$$$   :
      :SS$$$SS$; __;  _$$$$$$SS$$$$$$   :
        SSS$SS l;:  ;  :  $$$$SS$$$$$;   ;
        :SS$SS $;:  ;  :  $$$SS$$$$$$;  /;
        TSSSS :$ \ ;  ;  :$S$$$$$$$$.-"/
          `SP; :;  ;:  ;   T$$$$$$$$;  /;
          : ;  ;  : `.;   /)T$$$$$P .' :
          ; :  :   ;    .'/ :$$$P'.'  .'\
          ;  \    :;   /   /$P^".' .-"   ;
          :       ;:     .'  .-"        / \
            `.____/_'.___:--""\    --' .'   )
          .-"      .'     "-._ "-._   ..--"")\
        :-'      :     "-.   "-._    ---""" /;
        ;    :   :        \      "-._....____;
        :  :   \  :\        `.                 \
        ;  ;    \  \\   \     \                 ;
      :  :      `. \\   \     \                :
      ;  ;       ;"-t\   `.    \               :
      :  :       :    `;         \              ;
      ;  ;       ;     :          \            /
    :  :       /       ;          \-..__    .';
    :  ;      /        :           ;    """T  ;
    : /      /          ; \        :       ;  ;
    ;/      :           :  \        ;      ;  ;
    ;       ;            ;  ;       :      ;  ;
    /       :             :  :        ;     ;  ;
  /        ;             :;          :     ;  ;
  /        :              ::           ;    ;  ;_
  `""--..__;              :_;      __  ;____;.-;';
    ;.__.:                 :..t-""  j"       ;  ;
    :    ;                 ;   ;--"" \ [bug] ;  ;
    ;    :                 ;   :      \      ;  ;
    :     \                ;    ;      ;.    ;  ;
      \     \               ;    :     /  ;   ;  ;
      \     \              ;    :        ;   ;  ;
        \     `-.           ;    ;      .'    ;  ;
        \       \          ;___/      /______;.-'
          \    ---;            /      /
          ;______:         .-'      /
                            '-------'

          ''')
            return 'Waited so long that he died of hunger. Game Over.'
        elif choice2 == 'swim':
            print("""
                                              o
                              .-""|
                              |-""|
                                  |   _,.-+.
                                  .|-""      '.
                                '.'           '.
                                | '.        _.-'|
                                |   +    .-"   J
              _.+        .....'.'|    '.-"      |
        _,.-"   '.   ..'88888888|     |       J''..
      +:"          '.'88888888888;-+.  |    _+.|8888:
      | \         _.-+88888888_."  _.F F +:'   '.8888'....
      L \   _.-""   |8888_.-"  _." J J J  '.    +88888888:
      |  '+"        |_.-"  _.-"    | | |    +    '.888888'._-'.
    .'8L  L         J  _.-"        | | |     '.    '.88_.-"    '.
    :888|  |         J-"            F F F       '.  _.-"          '.
  :88888L  L     _,  L            J J J          '|.               ';
  :888888J  |  +-"  \ L         _.-+.|.+.          F '.          _.-"J
  :8888888|  L L\    \|     _.-"     '   '.       J    '.     .-"    |
  :8888888.L | | \    ',_.-"               '.     |      "..-"      J'.
  :888888: |  L L '.    \    _,.-+.          '.   :+-.     |        F88'.
  :888888:  L | |   \    ;.-"      '.          :-"    ":, J        |88888:
  :888888:  |  L L   +:""            '.    _.-"     .-" | |       J:888888:
  :888888:   L | |   J \               '.-'     _.-'   J J        F :888888:
  :88888:    \ L L   L \             _.-+  _.-'       | |       |   :888888:
  :888888:    \| |   |  '.       _.-"   |-"          J J       J     :888888:
  :888888'.    +'\   J    \  _.-"       F    ,-T"\   | |    .-'      :888888:
    :888888 '.     \   L    +"          J    /  | J  J J  .-'        .'888888:
    :8888888 :     \  |    |           |    F  '.|.-'+|-'         .' 8888888:
      :8888888 :     \ J    |           F   J     '...           .' 888888888:
      :8888888 :     \ L   |          J    |      \88'.''.''''.' 8888888888:
        :8888888 :     \|   |          |  .-'\      \8888888888888888888888:
        :8888888 '.    J   |          F-'  .'\      \8888888888888888888.'
          :88888888 :    L  |         J     : 8\      \8888888888888888.'
          :88888888 :   |  |        .+  ...' 88\      \8888888888.''.'
            :88888888 :  J  |     .-'  .'    8888\      \'.'''.'.'
            :88888888 :  \ |  .-'   .' 888888888.\    _-'
            :888888888 :  \|-'     .' 888888888.' \_-"
              '.88888888'..         : 8888888.'
                :88888888  ''''.''.' 88888888:  hs
                :8888888888888888888888888888:
                :88888888888888888888888888:
                  :888888888888888888888888:
                  ''.8888888888888...'.'''
                      '''''......''
          """)
            print('Congratulations! you arrived at the castle.')
            choice3 = input('Enter the castle? Type Yes or No: ')
            choice3 = choice3.lower()
            if choice3 == 'no':
                print('''

          ('(
            \ \                    " Help !!!   Alligators...."
        d@b | |
        @@@@' |
    ('(  Y@P   `--..
      \ `--'      .' `.
      `---....__/    |
                /   . \                     /^^^^\
              /  .'\  \       /^^\________/0     \
                \  \  \  \     (                    `~+++,,_____,,++~^^^^^^^
    -unknown-    \  \  \__\  ...V^V^V^V^V^V^\...............................
                _`--` `--'     mordida na bunda
                `---'
              ''')
                return 'Game Over.'
            elif choice3 == 'yes':
                print('''
              *******************************************************************************
            |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/
  *******************************************************************************
              ''')

                print('''

                          __,,,__
                  ,-""-,-"       "-,-""-,
                /,-' , .-'-.7.-'-. , '-,\
                \(    /  _     _  \    )/
                  '-,  { (0)   (0) }  ,-'
                  /    >  .---.  <    \
                  |/ .-'   \___/   '-. \|
                  {, /  ,_       _,  \ ,}
                  \ {,    \     /    ,} /
                  ',\.    '---'    ./,'
              _.-""""""-._     _.-""""""-._
            .'            `._.`            '.
          _/_               _                \
        .'`   `\            | |                \
      /        |           | |                 ;
      |        /           |_|                 |
      \  ;'---'    _    ___  _  _  ___         ;
        '. ;       | |  /   \| || ||  _|     _ ;
          `-\      | |_ | | || |/ /|  _|   .' `,
            `\    |___|\___/ \__/ |___|  |     \
              \            _ _           \     |
          jgs  `\         | | |         /`   _/
      ,-""-.    .'`\       | | |       /`-,-'` .-""-,
    /      `\.'    `\     \___/     /`    './`      \
    ;  .--.   \       '\           /'       /   .--.  ;
    | (    \   |,       '\       /'        |   /    ) |
    \ ;    }             ;\   /;         `   {    ; /
      `;\   \         _.-'  \ /  `-._         /   /;`
        \ \__.'   _.-'       Y       `-._    '.__//
        '.___,.-'                       `-.,___.'

              ''')
                return 'You have found the secret treasure of luquinhas adventure bank! Let is see what is inside.'
