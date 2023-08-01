tempo = float(input("Informe o tempo da viagem: "))  
velocidade = int(input("Informe a velocidade média: "))
distancia = velocidade * tempo 
consumo = distancia / 8
print(f"Serão necessários {consumo:.1f}l de combustível")
