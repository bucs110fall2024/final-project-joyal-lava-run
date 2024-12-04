
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Joyal Paul

*** 

## Project Description

There is a player that starts off at the bottom of a volcano. The objective is to get to the top and escape the volcano before the magma rises and kills the player. 
There are obstacles on each level of the volcano, like monsters, falling or cracking steps, and dripping lava that hurts and slows down the player. 
Some of the steps can drop you to lower levels and some can kill you due to fall damage. The player must escape in limited time and make a final jump to the helicopter to be rescued. 
If the player doesn't make it up in time, the player loses. I might add levels with faster times and more obstacles to let the player pick a difficulty level. 

***    

## GUI Design

### Initial Design

![initial gui](gui-1.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. Rising lava
3. Moving / falling objects
4. Screen shaking when taking damage
5. Game over screen

### Classes

- Controller - 
- Player - creates a player object thats able to move around, jump, and block
- Enemies - creates an enemy or multiple enemy objects that are able to move back and forth, face the player, and shoot bullets
- Goku -
- Shoot - 
- Helicopter - 
- Lava - 
- Platforms - 
- Collision_plat -  
- Winner - 
- GameOver -


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears                 |
|  2                   | Press A or D         |If A, player goes left, if D, plyaer goes right      |
|  3                   | Run Counter Program  |GUI window appears with count = 0  |
|  4                   | click count button   | display changes to count = 1      |
|  5                   | Run Counter Program  |GUI window appears with count = 0  |

Test Case 1: Movement
 - Test Description: Verifies that player movement works when going left and right.
 - Test Steps:
    1. Start Game
    2. Press "A" key.
    3. Verify that player goes left.
    4. Press "D" key.
    5. Verify that player goes right. 
 - Expected Outcome: Player moves left and right if arrow keys "A" and "D" are pressed respectively.  

Test Case 2: Player hits Lava
 - Test Description: Verifies that player hits lava and dies. 
 - Test Steps:
    1. Start Game
    2. Avoid objects and fall towards lava.
    3. Player and lava hits.
    4. Verify that the player dies.
 - Expected Outcome: Player hits lava and disappears from screen, indicating death. Game over screen is shown. 

Test Case 3: Player and Platform collisions
 - Test Description: Verifies that player is able to stand and move on top of the platform.
 - Test Steps:
    1. Start Game
    2. Wait till player lands on the top of the platform, indicated by the line above it.
    3. Verify that the player stops falling down. 
    4. Press "A" or "D".
    5. Verify the player goes left or right. 
 - Expected Outcome: Player doesnt' fall and is able to move around. 

Test Case 4: Player and border collisions
 - Test Description: Verifies that player hits borders and dies. 
 - Test Steps:
    1. Start Game
    2. Hold "W" and "A" until player hits left border.
    3. Verify player hits left border. 
    4. Verify player dies.  
 - Expected Outcome: Player goes left, hits border, and dies. Game over screen is shown. 

Test Case 5: Game over Condition
 - Test Description: Verifies that game over screen is shown when player dies without reaching helicopter. 
 - Test Steps:
    1. Start Game
    2. Hold "W" and "A" until player hits left border.
    3. Verify player hits left border. 
    4. Verify player dies.
    5. Verify game over screen shows up.  
 - Expected Outcome: Game over screen is shown after player's death. 


