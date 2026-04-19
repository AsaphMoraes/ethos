import sys
import os
import subprocess
import threading
import webview
import warnings

from pathlib import Path

# Suprimir warning do Fontconfig
warnings.filterwarnings('ignore', message='.*fontconfig.*')

class StreamlitWrapper:
    def __init__(self):
        self.process = None
        self.stdout_thread = None
        self.running = False
        self.port = 8501

    def start_streamlit(self):
        """Inicia o Streamlit em subprocesso dentro do webview"""
        try:
            streamlit_cmd = [
                "streamlit",
                "run",
                str(Path(__file__).parent / "app" / "views" / "streamlit_app.py"),
                "--server.port", str(self.port),
                "--server.headless", "true"
            ]
            
            env = os.environ.copy()
            env['PYTHONPATH'] = str(Path(__file__).parent)
            
            self.process = subprocess.Popen(
                streamlit_cmd,
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # Redirecionar stderr para stdout
                text=True,
                bufsize=1
            )
            
            self.running = True
            
            # Iniciar thread para ler output
            self.stdout_thread = threading.Thread(target=self.read_output)
            self.stdout_thread.daemon = True
            self.stdout_thread.start()
            
            print(f"Streamlit iniciado na porta {self.port}")
            
            return True
        except Exception as e:
            print(f"Erro ao iniciar Streamlit: {e}")
            return False

    def read_output(self):
        """Lê e exibe a saída do Streamlit"""
        while self.running:
            if self.process.poll() is not None:
                break
            
            try:
                output = self.process.stdout.readline()
                if output:
                    print(output.strip())
            except Exception as e:
                print(f"Erro ao ler stdout: {e}")
                break

    def stop(self):
        """Para o Streamlit"""
        self.running = False
        
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
                print("Streamlit encerrado")
            except subprocess.TimeoutExpired:
                self.process.kill()
                print("Streamlit forçado a encerrar")
            except Exception as e:
                print(f"Erro ao encerrar Streamlit: {e}")
            finally:
                self.process = None

def main():
    """Função principal para iniciar o webview"""
    streamlit_wrapper = StreamlitWrapper()
    
    print("Inicializando aplicativo Ethos...")
    
    if not streamlit_wrapper.start_streamlit():
        print("Não foi possível iniciar o Streamlit")
        return
    
    print("Aguardando Streamlit inicializar...")
    
    # Aguardar Streamlit inicializar
    import time
    time.sleep(3)
    
    print(f"Webview abrindo em http://localhost:{streamlit_wrapper.port}...")
    
    window = webview.create_window(
        'Ethos Financeiro',
        f'http://localhost:{streamlit_wrapper.port}',
        width=1200,
        height=800
    )
    def on_closing():
        """Callback quando o webview está sendo fechado"""
        print("Encerrando aplicativo...")
        
        streamlit_wrapper.stop()

    window.events.closing += on_closing
    
    try:
        webview.start(gui='qt')
    except Exception as e:
        print(f"Erro ao iniciar webview: {e}")
    finally:
        streamlit_wrapper.stop()

if __name__ == "__main__":
    main()