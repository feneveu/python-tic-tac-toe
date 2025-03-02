# python-tic-tac-toe
python-TicTacToe-Ai

Easy - Tic Tac Toe
  The creation of the basic board layout/gameplay was a fairly easy challenge. With the help of a board class to control prints and layouts as
  well as different methods to manipulate the board data, implementing a 2 Player gameplay was intuitive.

Medium/Easy - MinMax algorithm
  To make things a bit more complex, I implemetented an AI, one random and one Impossible to beat - it will always win or tie. To do this, I 
  researched the minmax algorithm. I gained a good sense of the function as explained in the YT video:
  https://www.youtube.com/watch?v=Bk9hlNZc6sE&t=5664s
  from 59:46 to 1:13:00 in the video there is a really good description of how the function is supposed to work

  MinMax Overview:
    There are two functions within MinMax, as per the name, a minimizing function and a maximizing function. 
    The minimizing function works with the AI's 'player' and tries to minimize the win of the other player.
    The maximizing function tries to maximize the the other player - not the AI. 
    
    By having these two functions, they can call each other recursively
    The board is given to the AI and the AI looks at all of the empty squares, from there the AI recursively 
    plays out all of the possibilities for those empty squares. The min and max function go back and forth, 
    playing a maximizing X then a minimizing Y unwil there is an 'end'

    The 'end' is the base case, if the AI wins, it is -1, if the User wins its a 1 and if its a tie, its 0,
    in the minimizing function, the goal is to have the AI win with a win of -1 or 0.

    My code always has the AI as PLayer 2, aka calling the minimizing funciton then the maximizing function
    

I designed the overall layout of my game by hand, then after watching the video merged the minmax functionality into my own developed game.


I enjoyed making this project! It was a good test of my basic skills and I am glad to say I fully understand the recursion based around the 
MinMax function.
