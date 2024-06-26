### Spotify API and UI test with the help of PyQualityServices based on Python

### `a.moinur@a1qa.com`

### Spotify UI and REST API Test
This project is a client for interacting with the Spotify API and UI.

## Setup
### Prerequisites
- **Python 3.x**
- **pip (Python package installer)**
- **Spotify Developer Account (to get your `CLIENT_ID` and `CLIENT_SECRET`)**
### Installation
1) **Clone the repository**

2) **Create virtual env:** `env/scripts/activate`

3) **Install the required packages:** `pip install -r requirements.txt`

4) Create a `.env` file in the root directory of the project and add your Spotify API credentials: The .env file should look like this:

**CLIENT_ID =** "your `CLIENT ID`"

**CLIENT_SECRET =** "your `CLIENT SECRET`"

### Running Test in parallel with allure report generation
**1. To run the test in parallel:** `pytest framework/tests/ -k "xdist_group and (UI or API)" -n 0`

**2. Command for report generation:** `python -m pytest framework/tests/ --alluredir allure-results`

**3. Generate report :** `allure serve allure-results`
