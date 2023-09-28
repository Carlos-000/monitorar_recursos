import psutil
import time


def monitorar_recursos(segInterval, limiteCPU, limiteRAM, limiteDisco):
    while True:
        # Obter o uso da CPU
        _cpu = psutil.cpu_percent(interval=segInterval)

        # Memória RAM
        _ram = psutil.virtual_memory().percent

        # disco
        _disk = psutil.disk_usage('/').percent

        # temperatura
        _temp = psutil.sensors_temperatures

        # processos
        _process = len(psutil.pids())

        # Tenta obter as informações da temperatura da CPU, não vai funcionar em todos os sistemas.
        try:
            _temp = psutil.sensors_temperatures()['coretemp'][0].current
        except Exception as e:
            _temp = "N/A"

        # Saída
        output = f'CPU: {_cpu:.f}% | Memória: {_ram:.f}% | Disco: {_disk:.f}%\n'
        output += f'Processos em execução:{_process}\n'
        output += f'Temperatura da CPU: {_temp} °C'

        # Verificação dos limites
        if _cpu > limiteCPU:
            output += f'\nAlerta: Uso da CPU excedeu {limiteCPU}% ({_cpu:.2f}%)'

        if _disk > limiteRAM:
            output += f'\nAlerta: Uso de memória excedeu {limiteRAM}% ({_ram:.2f}%)'

        if _disk > limiteDisco:
            output += f'\nAlerta: Espaço em disco excedeu {limiteDisco}% ({_disk:.2f}%)'

        print(output)
        # Espera o intervalo passado no parâmetro da função para atualizar as informações
        time.sleep(segInterval)


if __name__ == "__main__":
    # Obter informações do usuário
    intervalo_segundos = float(
        input("Informe o intervalo de atualização em segundos: "))
    limite_cpu = float(
        input("Informe o limite de uso da CPU em percentagem: "))
    limite_memoria = float(
        input("Informe o limite de uso de memória em percentagem: "))
    limite_disco = float(
        input("Informe o limite de uso do disco em percentagem: "))

    # Chamar a função para monitorar recursos com as informações fornecidas pelo usuário
    monitorar_recursos(intervalo_segundos, limite_cpu,limite_memoria, limite_disco)
