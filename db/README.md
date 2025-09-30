ISTRUZIONI PER USARE CORRETTAMENTE IL MODULO DI CONNESSIONE AL DATABASE.

Creare un file chiamato db_config.yaml nel folder db e strutturarlo come segue.
Il modulo di connessione leggerà da questo yaml le configurazioni per fare
ssh tunneling e per connettersi al database.

I valori presenti nel template sono i default. Se si vogliono mantenere questi valori
si possono anche ignorare le chiavi corrispondenti nel file yaml.

db:
  user: 
  password: 
  schema: #opzionale -> il parametro schema nei metodi fetch e modify ha comunque la precedenza
ssh-tunnel:
  path-pem: 
  admin: 
  url: 
  port: 22
  remote-host: 127.0.0.1
  remote-port: 3306
  local-host: 127.0.0.1
  local-port: 0
