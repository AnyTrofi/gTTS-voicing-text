## Info

API service for voicing text using gTTS

## Tested on versions:

Python - 3.9.13

Flask - 3.0.2

gTTS - 2.5.1

## Launch

```
python3 app.py
```

## Request

POST request
```
/say
```

```
{
    "text": "Hello World!", # STR
    "language": "en",       # STR
    "speed": "True"         # bool - Optional
}
```
