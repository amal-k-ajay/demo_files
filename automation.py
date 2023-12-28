import subprocess

def run_openssl_scripts(script_paths):
    for script_path in script_paths:
        process = subprocess.Popen(f'bash {script_path}', shell=True)
        process.wait()

def run_python_scripts(python_scripts):
    for script_path in python_scripts:
        process = subprocess.Popen(f'python3 {script_path}', shell=True)
        process.wait()

if __name__ == '__main__':
    script_paths = [
        '/home/amal/Desktop/workspace/certs/IDevID_stage_automation/create_ca.sh',
        '/home/amal/Desktop/workspace/certs/IDevID_stage_automation/server.sh',
        '/home/amal/Desktop/workspace/certs/IDevID_stage_automation/create_ca_LDevID.sh',
        '/home/amal/Desktop/workspace/certs/IDevID_stage_automation/client_LDevID.sh',
    ]

    run_openssl_scripts(script_paths)
    python_scripts = ['gen_keystore_file.py', 'gen_truststore_file.py', '/home/amal/Desktop/workspace/connect_first.py']
    run_python_scripts(python_scripts)
