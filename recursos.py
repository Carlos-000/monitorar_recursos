import psutil
import time

def monitorar_recursos(segInterval):
    while True:
        #Obter o uso da CPU
        _cpu =  psutil.cpu_percent(interval=segInterval)

        #Memória RAM
        _ram =  psutil.virtual_memory().percent

        #disco
        _disk = psutil.disk_usage('/').percent

        #temperatura
        _temp = psutil.sensors_temperatures

        #processos
        _process = psutil.process_iter()
        #Saída
        
        print(f'CPU: {_cpu}% | Memória: {_ram}% | Disco: {_disk}%')
        print("...")
        #Espera o intervalo passado no parâmetro da função para atualizar as informações
        time.sleep(segInterval)
if __name__ == "__main__":
    print("Digite a quantidade de tempo em segundos, que os resultados serão atualizados.")
    monitorar_recursos(int(input()))