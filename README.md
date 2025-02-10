# **Border Crossing**

[Click here to go to the Live Project](https://bordercrossing-840fd789a5e7.herokuapp.com/)

![Cover Art](/assets/images/cover.webp)




## **Table of contents**

- [**Border Crossing**](#border-crossing)
  - [**Table of contents**](#table-of-contents)
  - [**Planning**](#planning)
    - [**Programmer Goals**](#programmer-goals)
    - [**User Stories**](#user-stories)
  - [**Features**](#features)
    - [**Used Technologies**](#used-technologies)
    - [**Design**](#design)
  - [**Testing**](#testing)
    - [**Manual Testing**](#manual-testing)
    - [**Validation and Issues**](#validation-and-issues)
      - [**Phython**](#phython)
    - [**Bugs**](#bugs)
  - [**Deployment**](#deployment)
  - [**Version Control**](#version-control)
  - [**Development Process and Commands**](#development-process-and-commands)
  - [**Clone and Fork the Repository**](#clone-and-fork-the-repository)
    - [**Clone the Repository**](#clone-the-repository)
    - [**Fork the Repository**](#fork-the-repository)
  - [**Future Enhancements**](#future-enhancements)
  - [**Credits**](#credits)
  - [**Finished Product**](#finished-product)

## **Planning**

### **Site Owner Goals**

- As a Programmer, I want to build up my Phython skills
- As a Game Creator, I want to produce a meaningful game that deals with moral choices 

### **User Stories**

- As a player, I want to be morally challenged and make though choices
- As a player, I want to play games that have a lasting impact
- As a player, I want to play as a border guard in passport control 

## **Features**

**Border Crossing** is a small textgame, made in Phython, about moral choices and consequences. 

The player takes the position of a new border guard officer at the border between two -unnamed-, fictitious countries. 

Both countries have a long and bloody history and only recently achieved peace.

Borders are now open, but animosities are still great within both countries, so everything could set off a diplomatic incident. 

The player has to make a decsision on who he lets into the country and who he rejects. 

Sometimes, there are secret outcomes, by asking the right questions. 

#### **Used Technologies**

- **Python:** Python 3.13.1

#### Design

The Design orients itself on old, text-based rpgs. 

The text flows naturally instead of printing out entire blocks and the image greeting the player at start makes full use of the available space.

## Testing

### Manual Testing
- Manual testing was used during the entire development process by me (the Creator) and at least five other persons. 
- "Man-of-street" everybody who came by my flat was asked to play a round 
- A friend programmer helped with identifying bugs
- Testing was done in Chrome and Edge browser

### Validation and Issues

#### Python 3.13.1

#### PEP8 Linter

**PLEASE NOTE** I did not use any autocorrection tools for the PEP8 Format (i.e. autopep8)
This is due to the fact, that the visual presentation is heavily reliant on empty spaces and sometimes empty print commands. 

The visual style might be limited by fully committing to PEP8in autopep.

**Result: Comments below.**

I have drasticlly reduced the number of comments from Phython Linter, but there are still some remaining. 

Biggest issues for Phython Linter are:
- E122 continuation line missing indentation or outdented **PLEASE NOTE** I keep it the way it is due to better readability of the code. This is in the Case Library Section.
- E501 line too long **PLEASE NOTE** This is due to me making comments after a line. I use overhead comments for Headlines in code, but no visible line to the user is effected. 
- W291 trailing whitespace **PLEASE NOTE** I have reduced the number drastiacally, but there are still some left. 

![CI Phython Linter](/assets/images/pythonlinter.webp)

## Bugs

No known defects remaining.

## **Deployment**

Code Institutes Guidlines for deployments are used and recommended:

1. Open the [repository](https://github.com/askavian/border) 
2. Heroku was set up and configured to the standards given by the CI
3. In Heroku python interpreter was included in the settings `heroku/python`
4. In Heroku nodejs was included in the settings `heroku/nodejs`
5. For Browser Vies Configs are configured as follows: Included in _Config Var_ called `PORT`. Set this to `8000` 
5. The github repository is connected to the Heroku deployment. Automatic deployments are activated in settings, but final deployment is manually triggered

The link to my live site is: [Border Crossing](https://bordercrossing-840fd789a5e7.herokuapp.com/)

## Version Control
* [GitHub](https://github.com/) is used for Version Control.
* There is only a single branch **main** used.
* The entire code is stored in run.py

## Development Process and Commands

- Using the template provide by Code Institute as basis [githup template](https://github.com/Code-Institute-Org/python-essentials-template).  
- I used VSCode and via GitPod and tried to maintain **meningfull** and regular commits (i.e. features, bugs fixes, etc...). 
- Sometimes commits where commited as **testing** if the code was too small to count as a regular commit but I needed to test something in Heroku.
- Each Git Commit deployes after a short delay directly als to Heroku.

## Clone and Fork the Repository

You can easily clone or fork the **Border Crossing** repository to make changes or use it as a reference. Follow the steps below based on your operating system:

#### **Fork the Repository**

1. Visit the repository on GitHub: [Border Crossing](https://github.com/askavian/border).  
2. Click the **Fork** button in the top-right corner to create your own copy of the repository under your GitHub account.

#### **Clone the Repository**

The repository has a single branch, with code committed sequentially for clarity. It can be forked or cloned for further development.

## Future Enhancements

To further improve the typing game, I would add the following features:

- **More Content:** Include more Cases (up to 30).
- **Textflow:** Finetune the textflow so it comes more naturally.
- **Difficulty Level:** Finetune time settings and case numbers to enhance LoD.
- **Pictures:** Include more ASCII Art (i.e. Pictures of individuals).
- **Highscore:** Include a Highscore with user names.
- **Music:** Include Background Music for Ambience. 

## Credits

- My friend René (CI alumni) for Phython Degugging. [Rene's Github](https://github.com/renebaumann3000).
- My friend Ivy (fellow stundent from CI) for helping with the idea and talking when needed. [Ivy's Github](https://github.com/Ivrigy).
- Code Institute Students and Alumnis for Phython. 
- bbtong for a great YouTube Tutorial series. I took inspiration for file structure and especially how to handle text output so that is flows naturally and does not print all at once [bbtong's text rpg](https://github.com/bbtong/python-text-rpg/blob/master/exampleTextRPG.py).
- The 40k Name Generator to create completely outlandish names so that the game is completely fictional [Warhammer 40.000 Name Generator](https://www.realmofplastic.com/warhammer-40k-blog/imperial-citizens-40k-character-name-generator).

## Finished Product

Thank you for reading this. I hope you enjoy my work!

Author: [Malte M. Boettcher](https://github.com/askavian/)












