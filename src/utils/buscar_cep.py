import requests

def buscar_cep(cep):
    try:
        url_brasilapi = f"https://brasilapi.com.br/api/cep/v1/{cep}"
        response = requests.get(url_brasilapi)
    
        if response.ok:
            return {"success": True, "status": response.status_code, "data": response.json()}
        
        if 400 <= response.status_code < 500:
            return {
                "success": False,
                "status": response.status_code,
                "data": [],
                "message": f"Não encontramos nenhuma correspondencia com CEP informado: {response.json()['message']}"}
        
        if 500 <= response.status_code < 600:
            url_viacep = f"https://viacep.com.br/ws/{cep}/json/"
            try:
                response = requests.get(url_viacep)

                if 'erro' in response.json():
                    raise
                
                return {"success": True, "status": response.status_code, "data": response.json()}
                   
            except:
                return {"success": False,
                        "status": 404,
                        "data": [],
                        "message": f"Nenhum serviço externo encontrou o CEP informado"}
            
    except Exception as err:
        return {"success": False,
                "status": 500,
                "data": [],
                "message": f"Erro no servidor: {err}"}