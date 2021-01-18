from ting_file_management.file_process import process, remove, file_metadata
from src.deque import Deque


def test_validar_funcao_process_com_sucesso(capsys):
    project = Deque()
    process("statics/arquivo_teste.txt", project)
    out, err = capsys.readouterr()
    assert "'nome_do_arquivo': 'statics/arquivo_teste.txt'" in out
    assert "'qtd_linhas': 3" in out
    assert "'linhas_do_arquivo': ['Acima de tudo,'" in out


def test_validar_funcao_process_ignorando_mesmo_nome(capsys):
    project = Deque()
    process("statics/arquivo_teste.txt", project)
    len(project) == 1


def test_remover_arquivo_com_sucesso(capsys):
    project2 = Deque()
    process("statics/arquivo_teste.txt", project2)
    remove(project2)
    out, err = capsys.readouterr()
    assert "Arquivo statics/arquivo_teste.txt removido com sucesso\n" in out


def test_remover_arquivo_inexistente(capsys):
    project = Deque()
    remove(project)
    out, err = capsys.readouterr()
    assert out == "Não há elementos\n"


def test_validar_funcao_file_metadata_com_sucesso(capsys):
    project = Deque()
    process("statics/novo_paradigma_globalizado-min.txt", project)
    file_metadata(project, 0)
    out, err = capsys.readouterr()
    assert (
        "'nome_do_arquivo': 'statics/novo_paradigma_globalizado-min.txt'"
        in out
    )
    assert "'qtd_linhas': 19" in out
    assert (
        "'linhas_do_arquivo': ['Estratégias em um Novo Paradigma Globalizado'"
        in out
    )


def test_validar_funcao_file_metadata_com_posicao_invalida(capsys):
    project = Deque()
    process("statics/novo_paradigma_globalizado-min.txt", project)
    file_metadata(project, 200)
    out, err = capsys.readouterr()
    assert "Posição inválida" in err
