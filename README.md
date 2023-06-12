# Get Weather Data by City Name

## Requirements
- Python 3.11

## Installation
- Clone the repository
```bash
    git clone https://github.com/rohit1kumar/verloop-assignment.git
```

- Install the requirements
```bash
    pip install -r requirements.txt
```

## Usage
- Export the API KEY
```bash
    export APIKEY=your_api_key
```

- Run the script
```bash
    python run.py
```

- Make a `POST` request
```bash
    curl --location 'http://127.0.0.1:5000/getCurrentWeather' \
    --header 'Content-Type: application/json' \
    --data '{
        "output_format":"xml",
        "city":"mumbai"
    }'
```

- Response
```bash
    <root>
        <Weather>34.0C</Weather>
        <Latitude>18.98</Latitude>
        <Longitude>72.83</Longitude>
        <City>Mumbai India</City>
    </root>
```
