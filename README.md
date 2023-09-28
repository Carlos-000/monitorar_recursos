# # Monitor de Recursos do Sistema

Este é um simples monitor de recursos do sistema em Python que exibe o uso da CPU, memória RAM e espaço em disco. Ele também oferece funcionalidades como alertas de limite e coleta de histórico de dados.

## Como Usar

1. Clone o repositório:
    ```
    git clone https://github.com/Carlos-000/monitor-recursos-sistema.git
    cd monitor-recursos-sistema
    ```
2. Execute o script Python:
    ```
    python3 monitor_recursos.py
    ```
3. Siga as instruções no console para inserir o intervalo de atualização e os limites de alerta.

## Funcionalidades

1. **Monitoramento de Recursos**:
   - Uso da CPU
   - Uso de Memória RAM
   - Espaço em Disco
   - Número de Processos em Execução
   - Temperatura da CPU (se disponível no sistema)

2. **Alertas de Limite**:
   - É possível definir limites (em percentagem) para o uso da CPU, memória RAM e espaço em disco.
   - Se o uso exceder esses limites, alertas serão exibidos no console.

   Exemplo:
   - Se o limite da CPU for definido como 80%:
     - Se o uso da CPU atingir 85%, um alerta será exibido.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
