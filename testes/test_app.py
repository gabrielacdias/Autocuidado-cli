import pytest
from src.app import AutocuidadoManager

def test_adicionar_meta_sucesso():
    """Caminho Feliz: Adicionar uma meta válida"""
    manager = AutocuidadoManager()
    sucesso, msg = manager.adicionar_meta("Beber 2L de água")
    assert sucesso is True
    assert len(manager.listar_metas()) == 1

def test_adicionar_meta_vazia():
    """Entrada Inválida: Tente adicionar meta sem nome"""
    manager = AutocuidadoManager()
    sucesso, msg = manager.adicionar_meta("")
    assert sucesso is False
    assert "Erro" in msg

def test_concluir_meta_inexistente():
    """Caso Limite: tentar concluir uma meta que não existe"""
    manager = AutocuidadoManager()
    sucesso, msg = manager.concluir_meta(99)
    assert sucesso is False
    assert "não encontrada" in msg


