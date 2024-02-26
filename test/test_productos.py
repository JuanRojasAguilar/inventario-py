import sys
import pytest

sys.path.append("..")
from modules import productos as p


seed = {
    "productos":{
        "001": {
            "codigo": "001",
            "nombre": "cepillo",
            "stock": {
                "stockMin": 4,
                "stockActual": 7,
                "stockMax": 10
                },
            "estado": "DISPONIBLE",
            "proveedor": "pepito"
        }
    }
}

@pytest.fixture
def mock_input(monkeypatch, text_input):
    def mock_func(_):
        return text_input
    monkeypatch.setattr('builtins.input', mock_func)

@pytest.mark.parametrize("text_input,expected", [("001", f"ID: {seed['productos']['001']['codigo']}")], ids=["capfd"])
def test_Search_Producto(mock_input,monkeypatch, text_input, expected, capfd):
    p.searchProduct(seed)
    out, err = capfd.readouterr()
    assert out.strip() == expected

