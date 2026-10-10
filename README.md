# Trump Tweet Trading Bot
Automated trading bot that leverages financial sentiment analysis from Trump's tweets to execute trades on publicly traded companies

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-0.1.0-blue.svg)](https://github.com/AvicenaIG/trump-tweet-trading-bot)
[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Contributing](#contributing)
7. [License](#license)

## Features
### 1. **Streaming Trump's Tweets**
 Stream Trump's tweets in real-time using the Twitter Streaming API and filter out non-relevant tweets.

### 2. **Sentiment Analysis**
 Utilize the Cloud Natural Language API to analyze the sentiment of Trump's tweets and assign a sentiment score to each relevant company mentioned.

### 3. **Company Identification**
 Use the Wikidata Query Service to identify the ticker symbol and other information for each company mentioned in Trump's tweets.

### 4. **Trade Execution**
 Execute trades on the relevant stocks using the TradeKing API based on the expected market reaction.

### 5. **Tweet Summary**
 Tweet out a summary of the analysis and trades executed in real-time using the Twitter API.

## Installation
```bash
git clone https://github.com/AvicenaIG/trump-tweet-trading-bot.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start
```python
from main import Monitor

monitor = Monitor()
monitor.start()
```

## Usage
### Example 1: Trading based on Trump's tweet about Apple
Trump tweets "I love Apple's new iPhone, it's amazing!" and the bot identifies Apple as a relevant company with a sentiment score of 1. The bot executes a buy order on Apple's stock.

### Example 2: Trading based on Trump's tweet about Tesla
Trump tweets "Tesla is a disaster, a total failure" and the bot identifies Tesla as a relevant company with a sentiment score of -1. The bot executes a sell short order on Tesla's stock.

## Configuration
| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `TWITTER_API_KEY` | string |  | Twitter API key |
| `TWITTER_API_SECRET` | string |  | Twitter API secret |
| `TRADING_API_KEY` | string |  | TradeKing API key |
| `TRADING_API_SECRET` | string |  | TradeKing API secret |

## Contributing
Contributions are welcome! Please submit a pull request with your changes and a brief description of what you've added or fixed.

## License
MIT License

Copyright (c) 2026 Trump Tweet Trading Bot contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.