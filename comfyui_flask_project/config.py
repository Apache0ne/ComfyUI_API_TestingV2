import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    COMFYUI_API_URL = 'http://127.0.0.1:8188/api'
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    @staticmethod
    def load_checkpoint_models():
        models_file = os.path.join(os.path.dirname(__file__), 'CKPmodels.txt')
        models = {'SDXL': [], 'SD': [], 'FLUX': []}
        current_category = None

        if os.path.exists(models_file):
            with open(models_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('[') and line.endswith(']'):
                        current_category = line[1:-1]
                    elif line and current_category:
                        models[current_category].append(line)

        return models

    CHECKPOINT_MODELS = load_checkpoint_models.__func__()