from scapy.all import *
import argparse
import threading
import time
import ipaddress
from threading import Lock

total_packets_sent = 0
packets_lock = Lock()

MAX_PACKETS = 10000  # Número máximo de pacotes por thread
MAX_THREADS = 50     # Número máximo de threads

def is_valid_target_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private or ip_obj.is_loopback:
            return False
        return True
    except ValueError:
        return False

def send_tcp_packets(target_ip, target_port, num_packets):
    global total_packets_sent
    for _ in range(num_packets):
        # Simula o envio de pacotes (não envia nada)
        with packets_lock:
            total_packets_sent += 1

def send_udp_packets(target_ip, target_port, num_packets):
    global total_packets_sent
    for _ in range(num_packets):
        # Simula o envio de pacotes (não envia nada)
        with packets_lock:
            total_packets_sent += 1

def monitor_progress(total_packets, start_time):
    global total_packets_sent
    while True:
        with packets_lock:
            packets_sent = total_packets_sent
        elapsed_time = time.time() - start_time
        packets_per_second = packets_sent / elapsed_time if elapsed_time > 0 else 0
        progress = (packets_sent / total_packets) * 100

        print(f"Pacotes simulados: {packets_sent}/{total_packets} ({progress:.2f}%) | "
              f"Pacotes/s: {packets_per_second:.2f} | "
              f"Tempo decorrido: {elapsed_time:.2f}s", end="\r")

        if packets_sent >= total_packets:
            break
        time.sleep(1)

def attack(target_ip, target_port, num_packets, num_threads, protocol):
    global total_packets_sent
    total_packets_sent = 0
    start_time = time.time()

    threads = []

    monitor_thread = threading.Thread(target=monitor_progress, args=(num_packets * num_threads, start_time))
    monitor_thread.start()

    for _ in range(num_threads):
        if protocol == "tcp":
            thread = threading.Thread(target=send_tcp_packets, args=(target_ip, target_port, num_packets))
        else:
            thread = threading.Thread(target=send_udp_packets, args=(target_ip, target_port, num_packets))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    monitor_thread.join()

def main():
    parser = argparse.ArgumentParser(description="Simulador de Ataque DDoS (Modo de Simulação)")
    parser.add_argument("target_ip", help="Endereço IP do alvo")
    parser.add_argument("target_port", type=int, help="Porta do alvo")
    parser.add_argument("-p", "--packets", type=int, default=1000, help="Número de pacotes por thread")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Número de threads")
    parser.add_argument("--protocol", choices=["tcp", "udp"], default="tcp", help="Protocolo a ser usado (tcp ou udp)")
    args = parser.parse_args()

    # Verifica os limites
    if args.packets > MAX_PACKETS:
        print(f"Erro: O número máximo de pacotes por thread é {MAX_PACKETS}.")
        return
    if args.threads > MAX_THREADS:
        print(f"Erro: O número máximo de threads é {MAX_THREADS}.")
        return

    # Verifica o endereço IP
    if not is_valid_target_ip(args.target_ip):
        print(f"Erro: O endereço IP {args.target_ip} é inválido ou está em uma rede proibida.")
        return

    print("Modo de simulação ativado. Nenhum pacote será enviado.")
    print(f"Iniciando simulação de ataque DDoS em {args.target_ip}:{args.target_port} usando {args.protocol.upper()}...")
    start_time = time.time()

    attack(args.target_ip, args.target_port, args.packets, args.threads, args.protocol)

    end_time = time.time()
    print(f"\nSimulação concluída em {end_time - start_time:.2f} segundos.")

if __name__ == "__main__":
    main()