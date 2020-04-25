### Dear diary 4/24/2020 
https://github.com/Arnzero/Space-Invaders-Pygame/blob/master/SpaceInvadersLiceCap.gif

I watched the tutorial which was very insightful and it didn't feel that long
even tho it was around 2 hours. Couple of things I focused on were;
spacing enemies, pause feature, ship selection, y and x boundaries
and a CAUTION icon to appear when enemies close to endgoal and high scores.
The spacing seemed impossible at first but I managed to find a way
to make sure they never had 'true' overlap. I wrote something like
create enemy coordinates into the list of enemies while the exact
coordinate does not exist. It helped to reduce overlap but there are 
times where the enemies are still touching but still barely noticeable.

The pause feature was probably the easiest, I had to disable the 
controls and enemies so that the pause feature worked correctly
using the 'p' button on the keyboard. The ship selection wasn't
difficult, it was a bit tedious having to find good flat icons
from the site that the video recommended, the video tutorial had
like 3 website references for icons, music and backgrounds which was
very helpful to add to the toolkit. I made the ship selection
as easy as possible where each ship corresponds to a number
but a more user friendly UI would be to have a cursor
while allowing the player to move left/right and enter
to select but I wanted to leave this rough draft for now.

The high scores part gave me the most trouble from
all of these and in fact, even my rough draft is making
me change my whole approach for storing the rankings in a file.
Originally I had a hash map where the ranking had the values
player name and player score but I realize now that, I would have to
manually add code to find the correct ranking before replacing the ranking
I never got to this part but I know I can do it if I had more time on
hands. I experimented 2 ways to save the player score rankings, once 
with pickle library but that didn't have much documentation and
instead I switched to using regular python functions via code
that I forked from stackoverflow(hurray).

Similar approach for how I would accept the user input,
I tried to use  pygame_textinput but it didn't have much documentation.
So I switched to eztext library and managed to get to display 
the enter initials and I was able to grab the input but
the hashing part it updates the new rankings is still missing.
Displaying all the high scores was some more code from
stackoverflow, since blit can only displaying per line
I had to use pythonic code to display each line with a
fixed amount of spacing between them.

The game is missing replay logic after the game over but
this is as far as I'm going to go for now as I prepare
for the semester's final stretch.

Also, I did mention I was going to go back and fix
my first assignment and email Adam C. since I have
a '0' but I turned it in an hour later forgetting how 
to submit. I'd rather take the grade that I get 
from what I was able to scrap from my newbie days
although I am more confident with POST forms and html
but not so much in markdown.
