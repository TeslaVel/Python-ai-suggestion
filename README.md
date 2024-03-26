# Python AI Suggestions
Basic context-based interaction analyzer between a client and agent with OpenAI/ChatGPT integration. To returns three suggestions based on the interactions.

## Installation

Install required packages.
```
pip3 install openai pymongo flask constants
```

## To use locally
Rename `constants.py.template` to `constants.py`(Get OpenAI API creds[OpenAI API key](https://platform.openai.com/account/api-keys))

## To use on heroku or others
set the following environment variables

```
APIKEY=your-openai-api-key
MONGO_URL=your-database-url
```

## Request Body - POST

```json
{
  "interactions": [
    "Client: Buenos días, estoy buscando un nuevo televisor. ¿Qué opciones tienen disponibles?",
    "Agent: ¡Buenos días! Tenemos una amplia variedad de televisores para diferentes necesidades y presupuestos. ¿Qué tamaño le interesa? ¿Tiene alguna preferencia en cuanto a características como calidad de imagen, funcionalidades inteligentes o capacidades para juegos?",
  ],
  "client": {
    "name": "Rosh Schneider"
  },
  "agent": {
    "name": "Addam Sandler"
  },
  "products": [
    "TV UUID: 123\nName: StellarVision X1\nBrand: Stellar Electronics\nDescription: The StellarVision X1 is a top-of-the-line 4K Ultra HD TV with HDR support. It features a 65-inch Quantum Dot display, Dolby Vision, and Dolby Atmos audio. Enjoy immersive visuals and crystal-clear sound.\nPrice: $1,499.99\nDiscounted Price: $1,049.99 (30% off).\nBuy: [Link](http://site.com/cart/buy/124)",
    "TV UUID: 67890\nName: LuminaVista S9\nBrand: Lumina Electronics\nDescription: The LuminaVista S9 offers a 55-inch OLED display with 4K resolution. It supports HDR10+ and features a sleek design with ultra-thin bezels. Immerse yourself in lifelike visuals and vibrant colors.\nPrice: $1,899.99\nBuy: [Link](http://site.com/cart/buy/125)",
	]
}
```


## Response Payload

#### Response code 200
```json
{
  "suggestions": [
        "Estoy encantado de confirmar que el TCL 6-Series, con su impresionante calidad de imagen gracias a la tecnología QLED y Mini-LED, es una excelente elección. Aquí tiene el enlace directo para adquirirlo: [Comprar TCL 6-Series](http://site.com/cart/buy/143)",
        "Si en el futuro decide ampliar su experiencia de visualización, el Philips OLED 805 podría ser una magnífica opción secundaria con su tecnología Ambilight única. Aquí está el enlace para más detalles: [Philips OLED 805](http://site.com/cart/buy/144)",
        "Para complementar su nueva TV, ¿ha considerado mejorar su sistema de sonido? Un barra de sonido puede realzar significativamente la calidad del audio para películas y series."
    ]
}
```

#### Response code 500
```json
{
  "error": "En estos momentos no tengo sugerencias, el servicio de IA no está disponible, reintente en un momento"
}
```
