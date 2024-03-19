from flask import Flask, request, jsonify
import openai
import os
# from pymongo import MongoClient
import constants

app = Flask(__name__)

NO_SUGGESTION_MSG = 'No tengo una respuesta para usted en este momento, pero voy a averiguarlo y le contacto de nuevo'
OPENAI_API_KEY = constants.APIKEY
# MONGO_URL = os.environ["MONGO_URL"]

# mongo_client = MongoClient(MONGO_URL)
# db = mongo_client["test_ai"]
# collection = db["interaction"]

@app.route('/analyze_chat', methods=['POST'])
def analyze_chat():
  openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

  if request.method == 'POST':
    data = request.json
    interactions = "\n".join(data.get('interactions'))
    products = "\n".join([f"- {product}" for product in data.get('products')])

    prompt = f"""A partir de las siguientes 25 interacciones de un chat de atención al cliente, donde el cliente ha expresado sus preferencias, necesidades y preguntas:
      {interactions}

      Y considerando esta lista de productos y servicios disponibles:

      {products}

      Genera 3 sugerencias de productos o acciones basadas en la conversación.

      Las sugerencias deben ser completamente independientes entre sí no deben estar conectadas entre si, y deben presentarse en un lenguaje natural y conversacional, evitando sonar como si fueran generadas por una IA.

      Las sugerencias no deben quedar incompletas por lo que deben ser maximos de 300 caracteres cada una y deben tener coherencia.

      Si no encuentras una respuesta adecuada basada en la conversación para alguna de las sugerencias, utiliza el siguiente mensaje: "{NO_SUGGESTION_MSG}".

      Debes retornar las sugerencias separadas con un doble barras

      El siguiente es un ejemplo de como debes retornarme las sugerenicas:

      Aqui va la sugerencia 1 || Aqui va la sugerencia 1 || Aqui va la sugerencias 1
    """

    if not interactions:
      return jsonify({"error": "Faltan datos en el request"}), 400

    messages = [
      {
          "role": "system",
          "content": prompt
      }
    ]

    try:
      response = openai_client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=messages,
        temperature=0.7,
        max_tokens=300,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        response_format={"type": "text"}
      )
    except (openai.APIConnectionError) as e:
      print("The server could not be reached")
      print(e.__cause__)  # an underlying Exception, likely raised within httpx.
      return error_response()
    except (openai.RateLimitError) as e:
      print("A 429 status code was received; we should back off a bit.")
      return error_response()
    except (openai.APIStatusError) as e:
      print("Another non-200-range status code was received")
      print(e)
      print(e.response)
      return error_response()

    # Procesar la respuesta para extraer las sugerencias
    content = response.choices[0].message.content.strip()
    suggestions = list(map(str.strip, content.split("||")))

    client = data.get('client')
    agent = data.get('agent')

    # Asegurarse de que el array tenga siempre tres elementos
    while len(suggestions) < 3:
        suggestions.append(NO_SUGGESTION_MSG)

    # Almacenar en la base de datos y enviar respuesta
    # collection.insert_one({
    #     "client": client,
    #     "agent": agent,
    #     "request": data,
    #     "response": suggestions
    # })

    # Enviar las suggestions como respuesta
    return jsonify({"suggestions": suggestions}), 200

def error_response():
  return jsonify({"error": "En estos momentos no tengo sugerencias, el servicio de IA no está disponible, reintente en un momento"}), 500

if __name__ == '__main__':
    app.run(debug=True)