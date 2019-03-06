
# Fake News Detector

## Installation

Install the requierements included in `requirements.txt`:
```
pip install -r requirements.txt
```

## Setting Fakebox Service

In order to Analyze news content and detect Fake News making use of Fakebox, first create an account on [MachineBox](https://machinebox.io/)

1. Make sure you have Docker running with at least 2 CPUs and 4GB RAM
2. Get your `MB_KEY` as an environment variable. 

For help on setting your key, read the [documentation.](https://machinebox.io/docs/setup/box-key).

## Usage

1. Run this code in your terminal to start the box:

```
$MB_KEY=MB_KEY
docker run -p 8080:8080 -e "MB_KEY=$MB_KEY" machinebox/fakebox
```
2. Run `fake.news.detector.py` followed by the url of the news to analyze:
```
python fake.news.detector.py "https://www.sample-url.com"
```

## License
Do What The F*ck You Want To Public License