## Teleportación en VirtualBox
Comandos para realizar teleportacion en VBox usando Localhost:

1. **Preparar la máquina de destino (Utarget):**

   ```bash
   VBoxManage modifyvm Utarget --teleporter on --teleporterport 6000
   ``` 
2. **Generar carga en la máquina a teletransportar (Ubu):**

    ```bash
    stress-ng --cpu 4 --cpu-method matrixprod --timeout 300s --metrics-brief
    ``` 
3. **Preparar la máquina a teletransportar (Ubu):**

    ```bash
    VBoxManage controlvm ubu teleport --host localhost --port 6000   
    ``` 
