# RIT-trading-python

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5412099a50854132801b34e4e65bb327)](https://www.codacy.com/app/samhunsadamant/RIT-trading-python?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SamSamhuns/RIT-trading-python&amp;utm_campaign=Badge_Grade) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Python trading modules for the Rotman Interactive Trader trading software.
<img src='https://raw.githubusercontent.com/SamSamhuns/RIT-trading-python/master/rit_image.PNG'>

## Prerequisites
Recommended Python version 3

The Rotman Interactive Trading Client which can only be operated in a Windows system.

The full documentation for the Rotman Interactive Trader Client REST API can be found here at swaggerhub https://app.swaggerhub.com/apis/306w/rit-client-api/1.0.0. The documentation is also present in a JSON format in the swagger-client-generated folder.


## Installing

### RIT Client Software
The RIT Client for Windows system can be downloaded at http://rit.rotman.utoronto.ca/software.asp.

Instructions for setting up an RIT demonstration client account for the <a href="cases/RIT - Case Brief - LT3 - Dynamic Order Arrival.pdf">Liability Trading 3 case file</a> can be found at RIT's website at http://rit.rotman.utoronto.ca/demo.asp.

Virtual environment packages with `virtualenv` or `anaconda` are recommended for both Windows and Linux/BSD based systems.

### Windows

Download a copy of this github repository at https://github.com/SamSamhuns/RIT-trading-python.
Two options are available after this:

-    <a href='https://www.anaconda.com/download/#macos'>Anaconda </a> is recommended for Windows system.
Open the anaconda prompt and use the following command to install all modules from requirements.txt.
`conda install --yes --file requirements.txt`

-    Install <a href='https://www.python.org/downloads/'>`python`</a> and add it to your `PATH` system variable. Then install the <a  href='https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation'>`pip`</a> package.                The `pip install -r requirements.txt` command now be used in the command prompt.

### Linux/BSD

After cloning the repository, install the required python packages using pip.
```
git clone https://github.com/SamSamhuns/RIT-trading-python
pip install -r requirements.txt
```

## Running the tests

Once python has been added to the `PATH` system variable in Windows, the code for running the scripts on Windows and Linux/BSD based systems are the same.


In the command line:

To run the `main.py` script to get an interactive program to submit or cancel orders.
```
python main.py
```


## Built With

-   [Python 3.6](https://www.python.org/downloads/release/python-360/) - The Programming tool used

## Versioning

Version tracked online with GitHub

## Authors

-   **Samridha Shrestha**

## License

This project is licensed under the Apahce 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
  
-   Rotman School of Manangement, University of Toronto http://www.rotman.utoronto.ca/
-   Rotman Interactive Trader http://rit.rotman.utoronto.ca/
-   Python open source libraries
-   Joel Hasbrouck, NYU Stern Principles of Securities Trading, FINC-UB.0049, Spring 201. http://people.stern.nyu.edu/jhasbrou/

## Contributions  

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/SamSamhuns)

## Disclaimer

All RIT software and external RIT links are provided by the Rotman School of Management and are their exclusive property.
