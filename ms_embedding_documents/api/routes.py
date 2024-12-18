import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import APIRouter, File, UploadFile, Request, HTTPException
from service.index_contents import indexar_arquivos
from service.search_contents import pesquisar_conteudo_indexado
import tempfile
import shutil
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

# Inicializar roteador da API
router = APIRouter()

# Enviar documentos txt ou pdf para serem indexados
@router.post("/embedd_documents")
async def embedd_documents(file: UploadFile = File(...)):
    if file.content_type not in ["text/plain", "application/pdf"]:
        return {"error": "Suporte apenas para arquivos txt e pdf."}

    try:
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, file.filename)
        with open(temp_file_path, "wb") as temp_file:
            content = await file.read()
            temp_file.write(content)
        
        indexar_arquivos(temp_file_path)
    except Exception as e:
        return {"error": f"Erro ao indexar arquivo: {str(e)}"}
    finally:
        shutil.rmtree(temp_dir)
    return {"message": "Arquivo indexado com sucesso."}

# Rota para buscar similaridade entre documentos
@router.post("/search_similarity")
async def search_similarity(text_request: TextRequest):
    try:
        data = text_request.dict() # Recuperando dados do modelo
        text = data['text']
        results = pesquisar_conteudo_indexado(text)
        return results
    except Exception as e:
        return {"error": f"Erro ao pesquisar conteúdo: {str(e)}"}



