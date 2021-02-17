#execucao_direta 1 python3 {esse-arquivo}
import sys, os
sys.path.append( os.getcwd())
from bibliotecas.python.smq.cliente import SmqCliente
from codigos.web.arquivo.post import envia_novo_arquivo
import tornado.ioloop
import tornado.web
import tornado.platform.asyncio

class MainHandler(tornado.web.RequestHandler):
    smq_client = SmqCliente()

    def post(self):
        retorno = envia_novo_arquivo( self.smq_client,self.request.body)
        self.write(retorno.result())


def make_app():
    return tornado.web.Application([
        (r"/arquivo", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(1200)
    tornado.ioloop.IOLoop.current().start()