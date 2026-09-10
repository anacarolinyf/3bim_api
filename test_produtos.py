from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from main import app, get_db
from models import ProdutoDB, FilmeDB

client = TestClient(app)


def test_listar_produtos_com_mock():
    db_mock = MagicMock()

    db_mock.query.return_value.all.return_value = [
        ProdutoDB(
            id=1,
            nome="Teclado",
            preco=89.90,
            quantidade=15
        )
    ]

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get("/produtos")

    assert resposta.status_code == 200
    assert resposta.json()[0]["nome"] == "Teclado"

    app.dependency_overrides.clear()


def test_criar_produto_com_mock():
    db_mock = MagicMock()

    def simular_refresh(produto):
        produto.id = 1

    db_mock.refresh.side_effect = simular_refresh

    app.dependency_overrides[get_db] = lambda: db_mock

    novo_produto = {
        "nome": "Monitor",
        "preco": 799.90,
        "quantidade": 5
    }

    resposta = client.post("/produtos", json=novo_produto)

    assert resposta.status_code == 201
    assert resposta.json()["nome"] == "Monitor"
    assert resposta.json()["id"] == 1

    db_mock.add.assert_called_once()
    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()


def test_obter_produto_com_mock():
    db_mock = MagicMock()

    produto = ProdutoDB(
        id=1,
        nome="Mouse",
        preco=49.90,
        quantidade=10
    )

    db_mock.query.return_value.filter.return_value.first.return_value = produto

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get("/produtos/1")

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Mouse"
    assert resposta.json()["id"] == 1

    app.dependency_overrides.clear()


def test_remover_produto_com_mock():
    db_mock = MagicMock()

    produto = ProdutoDB(
        id=1,
        nome="Teclado",
        preco=89.90,
        quantidade=15
    )

    db_mock.query.return_value.filter.return_value.first.return_value = produto

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.delete("/produtos/1")

    assert resposta.status_code == 204
    db_mock.delete.assert_called_once_with(produto)
    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()


def test_atualizar_produto_com_mock():
    db_mock = MagicMock()

    produto = ProdutoDB(
        id=1,
        nome="Mouse",
        preco=49.90,
        quantidade=10
    )

    db_mock.query.return_value.filter.return_value.first.return_value = produto

    app.dependency_overrides[get_db] = lambda: db_mock

    dados = {
        "nome": "Mouse Gamer",
        "preco": 99.90,
        "quantidade": 20
    }

    resposta = client.put("/produtos/1", json=dados)

    assert resposta.status_code == 200
    assert resposta.json()["nome"] == "Mouse Gamer"
    assert resposta.json()["preco"] == 99.90
    assert resposta.json()["quantidade"] == 20

    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()



def test_listar_filmes_com_mock():
    db_mock = MagicMock()

    db_mock.query.return_value.all.return_value = [
        FilmeDB(
            id=1,
            titulo="Interestelar",
            diretor="Christopher Nolan",
            genero="Ficção Científica",
            duracao_minutos=169
        )
    ]

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get("/filmes")

    assert resposta.status_code == 200
    assert resposta.json()[0]["titulo"] == "Interestelar"

    app.dependency_overrides.clear()


def test_criar_filme_com_mock():
    db_mock = MagicMock()

    def simular_refresh(filme):
        filme.id = 1

    db_mock.refresh.side_effect = simular_refresh

    app.dependency_overrides[get_db] = lambda: db_mock

    novo_filme = {
        "titulo": "Interestelar",
        "diretor": "Christopher Nolan",
        "genero": "Ficção Científica",
        "duracao_minutos": 169
    }

    resposta = client.post("/filmes", json=novo_filme)

    assert resposta.status_code == 201
    assert resposta.json()["titulo"] == "Interestelar"
    assert resposta.json()["id"] == 1

    db_mock.add.assert_called_once()
    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()


def test_obter_filme_com_mock():
    db_mock = MagicMock()

    filme = FilmeDB(
        id=1,
        titulo="Oppenheimer",
        diretor="Christopher Nolan",
        genero="Drama",
        duracao_minutos=180
    )

    db_mock.query.return_value.filter.return_value.first.return_value = filme

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.get("/filmes/1")

    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Oppenheimer"
    assert resposta.json()["id"] == 1

    app.dependency_overrides.clear()


def test_remover_filme_com_mock():
    db_mock = MagicMock()

    filme = FilmeDB(
        id=1,
        titulo="Oppenheimer",
        diretor="Christopher Nolan",
        genero="Drama",
        duracao_minutos=180
    )

    db_mock.query.return_value.filter.return_value.first.return_value = filme

    app.dependency_overrides[get_db] = lambda: db_mock

    resposta = client.delete("/filmes/1")

    assert resposta.status_code == 204
    db_mock.delete.assert_called_once_with(filme)
    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()


def test_atualizar_filme_com_mock():
    db_mock = MagicMock()

    filme = FilmeDB(
        id=1,
        titulo="Oppenheimer",
        diretor="Christopher Nolan",
        genero="Drama",
        duracao_minutos=180
    )

    db_mock.query.return_value.filter.return_value.first.return_value = filme

    app.dependency_overrides[get_db] = lambda: db_mock

    dados = {
        "titulo": "Oppenheimer Atualizado",
        "diretor": "Christopher Nolan",
        "genero": "Drama",
        "duracao_minutos": 181
    }

    resposta = client.put("/filmes/1", json=dados)

    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Oppenheimer Atualizado"

    db_mock.commit.assert_called_once()

    app.dependency_overrides.clear()