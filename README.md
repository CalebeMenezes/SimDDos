# DDoS Attack Simulator (Simulador de Ataque DDoS) 

A Python script that simulates a DDoS (Distributed Denial of Service) attack for educational purposes only. The project was developed for professional cybersecurity study to understand how DDoS attacks work, without causing real damage.

Um script em Python que simula um ataque de DDoS (Distributed Denial of Service) apenas para fins educacionais. O projeto foi desenvolvido para estudo profissional de cybersecurity a entender como funcionam os ataques de DDoS, sem causar danos reais.

# Important Notice (Aviso Importante)

This project is designed for __educational purposes only__. It simulates a DDoS attack, but does __not send real packets and does not cause any damage to systems or networks__. Malicious use of cybersecurity tools is illegal and unethical. Please make sure to use this script only in controlled environments and with explicit permission.

Este projeto foi __desenvolvido apenas para fins educacionais__. Ele simula um ataque de DDoS, mas __não envia pacotes reais e não causa danos a sistemas ou redes__. O uso malicioso de ferramentas de cybersecurity é ilegal e antiético. Certifique-se de usar este script apenas em ambientes controlados e com permissão explícita

# Features (Funcionalidades)
  - DDoS Attack Simulation (Simulação de Ataque DDoS):
    - Simulates sending large volumes of TCP or UDP packets. (Simula o envio de pacotes TCP ou UDP em grande volume.)
    - No real packets are sent (simulation mode is on by default). (Nenhum pacote real é enviado (modo de simulação ativado por padrão).)
  - Multithreading:
    - Uses multiple threads to simulate sending packets in parallel. (Usa múltiplas threads para simular o envio de pacotes de forma paralela.)
  - Real-Time Monitoring (Monitoramento em Tempo Real):
    - Displays statistics such as simulated packets per second, elapsed time, and total progress (Exibe estatísticas como pacotes simulados por segundo, tempo decorrido e progresso total)
  - Abuse Protection (Proteção contra Abuso)
    - Limits the maximum number of packets and threads. (Limita o número máximo de pacotes e threads.)
    - Checks if the target IP address is valid and not on a banned network (Verifica se o endereço IP do alvo é válido e não está em uma rede proibida)
   
# how to use (Como Usar)
  - Python 3.x
  - Required libraries:  scapy, argparse, threading, time, ipaddress.

# Usage Example (Exemplo de Uso)
  TPC
  -python ddos_simulator.py 192.16x.x.x 80 -p 1000 -t 10 --protocol tcp

  UDP
  -python ddos_simulator.py 192.16x.x.x 80 -p 1000 -t 10 --protocol udp
