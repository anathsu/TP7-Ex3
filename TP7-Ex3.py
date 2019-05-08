from psutil import net_connections
import socket, json

def obtem_nome_familia(familia):
      if familia == socket.AF_INET:
          return("IPv4")
      elif familia == socket.AF_INET6:
          return("IPv6")
      elif familia == socket.AF_UNIX:
          return("Unix")
      else:
          return("-")

def infonet_pid():
    informacao = []
    for process in net_connections(kind='inet'):
        informacao.append("PID: " + str(process[6]))
        informacao.append("Tipo de Endereco: " + str(obtem_nome_familia(process[1])))
        informacao.append("IP Local: " + str(process[3][0]))
        informacao.append("Porta: " + str(process[3][1]))
        arquivo_json = json.dumps(informacao)
    return arquivo_json
    
print(infonet_pid())

with open("informacoes_rede.json", "w") as fp:
    json.dump(infonet_pid() , fp)