# Sudoku Game

## Purpose
The Sudoku game is a game where there are m x m rows and columns such that each row and column can have numbers from 1 to 9. The main idea of the game is at the beginning the 9x9 grid has random numbers generated to it.
The user then has to figure out whhich numbers to put where until the full grid is completed!




[vaatimusmaarittely](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/vaatimusmaarittely.md)


[tuntikirjanpito](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/tuntikirjanpito.md)


!!! Vieläkin nämä __pycache__ ovat generoitu jos command "poetry run invoke test " vaikka .gitignore sisältää __pycache__ .... olen yrittänyt parantaa tätä mutta jostain syystä see ei toimi, nyt käytän  git clean -fdX saadakesni nämä pois...


[Changelogin](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/changelog.md)

Additional commands that work - 
     poetry run invoke main - käynnistää ohjelmaan
     
     poetry run invoke start - käynnistää invoke start 
     
     poetry run invoke test - suorittaa testit pytestin avulla
     
     poetry run invoke coverage-report - kerää coveragen avulla testikattavuuden ja muodostaa sen perusteella selaimessa avattavan, HTML-muotoisen testikattavuusraportin

     petry run invoke lint - käynnistä testinkattavuuten
