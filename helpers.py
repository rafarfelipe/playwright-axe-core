
def assert_sem_violacoes_graves(
    resultado: dict,
    severidades: tuple = ('critical', 'serious'),
    ):
    graves = [v for v in resultado['violations'] if v['impact'] in severidades ]
    if not graves:
        return

    detalhes = '\n'.join(''f'\n'
                f'- [{v["impact"]}] {v['id']}: {len(v['nodes'])} elemento(s) afetado(s)' for v in graves)
    assert not graves, f'{len(graves)} violações graves: \n{detalhes}'