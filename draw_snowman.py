def draw_snowman(num_of_wrong_guesses):
    if num_of_wrong_guesses == 1:
        print(
        '''
      ________  
     /    o   \ 
     \________/
        '''
        )
    elif num_of_wrong_guesses == 2:
        print(
        '''
       ______ 
      /   o  \ 
      \______/
     /    o   \ 
     \________/
        '''
        )
    elif num_of_wrong_guesses == 3:
        print(
        '''
        ____
       /    \ 
       |    |
       \____/
      /   o  \ 
      \______/
     /    o   \ 
     \________/
        '''
        )
    elif num_of_wrong_guesses == 4:
        print(
        '''
       ______
       |====|
     __ꓕ____ꓕ__
       /    \ 
       |    |
       \____/
      /   o  \ 
      \______/
     /    o   \ 
     \________/
        '''
        )
    elif num_of_wrong_guesses == 5:
        print(
        '''
       ______
       |====|
     __ꓕ____ꓕ__
       /    \ 
       |    |      0
       \____/     /
      /   o  \---/
      \______/
     /    o   \ 
     \________/ 
        '''
        )
    elif num_of_wrong_guesses == 6:
        print(
        '''
       ______
       |====|
     __ꓕ____ꓕ__
       /    \ 
       |    |      0
       \____/     /
  /---/   o  \---/
 /    \______/
0    /    o   \ 
     \________/ 
        '''
        )
    elif num_of_wrong_guesses == 7:
        print(
        '''
       ______
       |====|
     __ꓕ____ꓕ__
       /    \ 
       | O  |      0
       \____/     /
  /---/   o  \---/
 /    \______/
0    /    o   \ 
     \________/ 
        '''
        )
    elif num_of_wrong_guesses == 8:
        print(
        '''
       ______
       |====|
     __ꓕ____ꓕ__
       /    \ 
       | O O|      0
       \____/     /
  /---/   o  \---/
 /    \______/
0    /    o   \ 
     \________/
        '''
        )

