from random import randint

def encurta_link(link, cursor, conn):
    cursor.execute(f'insert into links (caminho, nome) values ("{link}", {randint(0, 99999)})')
    conn.commit()
    cursor.execute(f'select nome from links where caminho = "{link}"')
    nome = cursor.fetchone()[0]
    return f'http://localhost:5000/{nome}'

def acessar(conn, cursor, nome):
    cursor.execute(f'select idlinks from links where nome = {nome}')
    idlink = cursor.fetchone()
    if idlink:
        cursor.execute(f'update links set acesso = acesso + 1 where idlinks = {idlink[0]}')
        conn.commit()
    cursor.execute(f'select caminho from links where nome = "{nome}"')
    caminho = cursor.fetchone()
    return caminho

def show_relatorio(cursor):
    cursor.execute(f'select nome, acesso, caminho from links order by acesso desc')
    ordem = cursor.fetchall()
    return ordem
