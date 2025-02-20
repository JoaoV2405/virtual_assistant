# Voice Assistant

## Sobre o Projeto
Este é um assistente de voz simples que responde a comandos de áudio e executa diversas ações, como abrir sites, explorar arquivos e definir lembretes.

## Funcionalidades
- **Abrir sites**: Comandos para abrir YouTube, Gmail e a plataforma DIO.
- **Explorador de Arquivos**: Permite abrir o File Explorer do Windows.
- **Reconhecimento de Voz**: Utiliza `speech_recognition` para entender comandos do usuário.
- **Síntese de Voz**: Usa `gTTS` para converter texto em fala e responder ao usuário.

## Como Funciona
1. O programa escuta comandos de áudio usando o microfone.
2. Converte a fala em texto e analisa os comandos.
3. Executa a ação correspondente com base no comando detectado.
4. Caso o usuário peça para sair, o assistente encerra a execução.

## Como Usar
1. Certifique-se de que os pacotes necessários estão instalados (`speech_recognition`, `gTTS`, `playsound`, etc.).
2. Execute o script Python.
3. Diga um dos comandos, como:
   - "Open YouTube"
   - "Open email"
   - "Open DIO"
   - "Open file explorer"
4. O assistente responderá e executará a ação correspondente.

## Requisitos
- Python 3
- Bibliotecas:
  - `speech_recognition`
  - `gTTS`
  - `playsound`
  - `webbrowser`
  - `os`
  - `time`


