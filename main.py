from fastapi import FastAPI

app = FastAPI(title="Minha primeira API")

@app.get('/')
def principal():
    return {'mensagem1': 'Minha primeira API em FastAPI'}

@app.get('/sobre')
def principal():
    return {'mensagem2': 'Pagina Sobre'}