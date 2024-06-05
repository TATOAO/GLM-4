# Load model directly
from transformers import AutoModel
model = AutoModel.from_pretrained("THUDM/glm-4-9b-chat", trust_remote_code=True)
