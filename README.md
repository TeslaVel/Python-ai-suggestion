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
    "name": "Morgan Freeman"
  },
  "agent": {
    "name": "John Doe"
  },
  "products": [
    "TV UUID: 12345\nName: StellarVision X1\nBrand: Stellar Electronics\nDescription: The StellarVision X1 is a top-of-the-line 4K Ultra HD TV with HDR support. It features a 65-inch Quantum Dot display, Dolby Vision, and Dolby Atmos audio. Enjoy immersive visuals and crystal-clear sound.\nPrice: $1,499.99\nDiscounted Price: $1,049.99 (30% off).\nBuy: [Link](http://mercately.com/cart/buy/12345)",
    "TV UUID: 67890\nName: LuminaVista S9\nBrand: Lumina Electronics\nDescription: The LuminaVista S9 offers a 55-inch OLED display with 4K resolution. It supports HDR10+ and features a sleek design with ultra-thin bezels. Immerse yourself in lifelike visuals and vibrant colors.\nPrice: $1,899.99\nBuy: [Link](http://mercately.com/cart/buy/67890)",
	]
}
```


## Response Payload

#### Response code 200
```json
{
  "suggestions": [
    "Dado que te interesó el TCL 6-Series por su calidad de imagen y precio, quizás también te gustaría considerar el Hisense U8G. Aunque es un poco más grande, de 65 pulgadas, ofrece una excelente calidad de imagen con Dolby Vision HDR y una frecuencia de actualización de 120Hz para hacer que las películas y series se vean increíblemente fluidas. Además, viene con Android TV para acceder fácilmente a tus aplicaciones de streaming favoritas.",
    "Si estás buscando algo un poco más avanzado y no te importa invertir un poco más, el Philips OLED 805 podría ser una excelente elección. Con su tecnología Ambilight, no solo obtendrás una calidad de imagen excepcional gracias a su pantalla OLED y soporte para Dolby Vision y Atmos, sino que también disfrutarás de una experiencia visual envolvente única que extiende los colores más allá del televisor hacia las paredes circundantes.",
    "Entiendo que las funciones inteligentes no son tu prioridad principal, pero si en algún momento decides explorar otras opciones con características avanzadas, el Sony Bravia A"
  ]
}
```

#### Response code 500
```json
{
  "error": "En estos momentos no tengo sugerencias, el servicio de IA no está disponible, reintente en un momento"
}
```
