# PyDrone-Controle
# Controle Bluetooth para pyDrone

Sistema de controle de um drone **pyDrone** via Bluetooth Low Energy (BLE) utilizando Python. O programa detecta automaticamente o drone, estabelece conexão e permite o controle em tempo real através do teclado.

## Funcionalidades

* Busca automática pelo dispositivo **pyDrone**
* Conexão Bluetooth Low Energy (BLE)
* Controle de movimento em tempo real
* Controle de altitude
* Decolagem e pouso
* Botão de emergência
* Comunicação utilizando a biblioteca Bleak

---

## Requisitos

### Python

* Python 3.8 ou superior

### Bibliotecas

Instale as dependências com:

```bash
pip install bleak keyboard
```

---

## Como Executar

1. Ligue o drone.
2. Certifique-se de que o Bluetooth do computador está ativado.
3. Execute o programa:

```bash
python controle_drone.py
```

4. O sistema irá:

* Procurar um dispositivo chamado `pyDrone`
* Conectar automaticamente ao drone
* Iniciar o envio dos comandos de controle

---

## Controles do Teclado

| Tecla  | Função                |
| ------ | --------------------- |
| W      | Avançar               |
| S      | Recuar                |
| A      | Mover para a esquerda |
| D      | Mover para a direita  |
| Q      | Girar para a esquerda |
| E      | Girar para a direita  |
| R      | Aumentar altitude     |
| F      | Diminuir altitude     |
| Espaço | Decolar               |
| Enter  | Pousar                |
| X      | Emergência            |

---

## Estrutura do Pacote de Dados

Os comandos enviados ao drone possuem 8 bytes:

| Byte | Descrição     |
| ---- | ------------- |
| 0    | Reservado     |
| 1    | Roll          |
| 2    | Pitch         |
| 3    | Yaw           |
| 4    | Throttle      |
| 5    | Botão/Comando |
| 6    | Reservado     |
| 7    | Reservado     |

### Valores Padrão

```python
roll = 127
pitch = 127
yaw = 127
throttle = 127
button = 0
```

O valor `127` representa a posição neutra dos controles.

---

## Comandos Especiais

### Decolagem

```python
button = 24
```

### Pouso

```python
button = 72
```

### Emergência

```python
button = 136
```

O comando de emergência interrompe imediatamente o funcionamento dos motores.

---

## UUID Utilizada

O programa envia comandos através da característica BLE:

```text
6e400002-b5a3-f393-e0a9-e50e24dcca9e
```

---

## Fluxo de Funcionamento

```text
Início
   ↓
Procurar pyDrone
   ↓
Encontrado?
   ├─ Não → Encerrar
   └─ Sim
         ↓
Conectar via BLE
         ↓
Ler teclado continuamente
         ↓
Montar pacote
         ↓
Enviar comando
         ↓
Aguardar 50 ms
         ↓
Repetir
```

---

## Tecnologias Utilizadas

* Python
* AsyncIO
* Bleak (Bluetooth Low Energy)
* Keyboard

---

## Autor

Projeto desenvolvido para controle remoto do **pyDrone** utilizando comunicação BLE em Python.
