# Sudoku Game

## Purpose
The Sudoku game is a game where there are m x m rows and columns such that each row and column can have numbers from 1 to 9. The main idea of the game is at the beginning the 9x9 grid has random numbers generated to it.
The user then has to figure out whhich numbers to put where until the full grid is completed!


## Note on Python Version

The application has been tested with Python version 3.8. Issues may arise, especially with older Python versions.


## Dokumetation

[vaatimusmaarittely](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/vaatimusmaarittely.md)


[tuntikirjanpito](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/tuntikirjanpito.md)


[Changelogin](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/tammekasra/ot-harjoitustyo2024/blob/main/Dokumentaatio/arkkitehtuuri.md)



## Installation

1. Install dependencies with the following command:

```bash
poetry install
```

2. Perform necessary initialization steps with the command:

```bash
poetry run invoke build
```

3. Start the application with the command:

```bash
poetry run invoke start
```

## Command Line Operations

### Running the Program

You can run the program with the following command:

```bash
poetry run invoke start
```

### Testing

Tests can be run with the command:

```bash
poetry run invoke test
```

### Test Coverage

Generate a test coverage report with the command:

```bash
poetry run invoke coverage-report
```

### Pylint coverage

Generate a test coverage using pylint command:

```bash
poetry run invoke lint
```

