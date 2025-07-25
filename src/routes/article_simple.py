import json
import re
from flask import Blueprint, request, jsonify
import requests

article_bp = Blueprint('article', __name__)

def validate_api_key(api_key, provider):
    """Valida o formato da chave de API baseado no provedor"""
    patterns = {
        'openai': r'^sk-[a-zA-Z0-9\-_]{20,}$',
        'gemini': r'^AIza[a-zA-Z0-9\-_]{35}$',
        'groq': r'^gsk_[a-zA-Z0-9]{52}$',
        'xai': r'^xai-[a-zA-Z0-9\-_]{20,}$'
    }
    
    pattern = patterns.get(provider)
    if not pattern:
        return False
    
    return bool(re.match(pattern, api_key))

def call_openai_api(api_key, prompt):
    """Chama a API da OpenAI usando requests"""
    try:
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'gpt-4',
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 4000,
            'temperature': 0.7
        }
        
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=60
        )
        
        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}: {response.text}")
        
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Erro OpenAI: {str(e)}")

def call_gemini_api(api_key, prompt):
    """Chama a API do Google Gemini usando requests"""
    try:
        url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}'
        
        data = {
            'contents': [{
                'parts': [{'text': prompt}]
            }],
            'generationConfig': {
                'temperature': 0.7,
                'maxOutputTokens': 4000
            }
        }
        
        response = requests.post(url, json=data, timeout=60)
        
        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}: {response.text}")
        
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        raise Exception(f"Erro Gemini: {str(e)}")

def call_groq_api(api_key, prompt):
    """Chama a API do Groq usando requests"""
    try:
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'llama3-8b-8192',
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 4000,
            'temperature': 0.7
        }
        
        response = requests.post(
            'https://api.groq.com/openai/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=60
        )
        
        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}: {response.text}")
        
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Erro Groq: {str(e)}")

def call_xai_api(api_key, prompt):
    """Chama a API do xAI usando requests"""
    try:
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'grok-beta',
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 4000,
            'temperature': 0.7
        }
        
        response = requests.post(
            'https://api.x.ai/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=60
        )
        
        if response.status_code != 200:
            raise Exception(f"Status {response.status_code}: {response.text}")
        
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        raise Exception(f"Erro xAI: {str(e)}")

def call_ai_api(api_key, provider, prompt):
    """Chama a API de IA apropriada baseada no provedor"""
    if provider == 'openai':
        return call_openai_api(api_key, prompt)
    elif provider == 'gemini':
        return call_gemini_api(api_key, prompt)
    elif provider == 'groq':
        return call_groq_api(api_key, prompt)
    elif provider == 'xai':
        return call_xai_api(api_key, prompt)
    else:
        raise Exception(f"Provedor não suportado: {provider}")

def generate_article_prompt(data):
    """Gera o prompt para criação do artigo"""
    language_map = {
        'pt-br': 'português brasileiro',
        'en': 'inglês',
        'es': 'espanhol',
        'fr': 'francês'
    }
    
    tone_map = {
        'professional': 'profissional e autoritativo',
        'casual': 'casual e conversacional',
        'technical': 'técnico e detalhado',
        'friendly': 'amigável e acessível',
        'formal': 'formal e acadêmico',
        'review': 'estilo review/análise crítica'
    }
    
    language = language_map.get(data['language'], 'português brasileiro')
    tone = tone_map.get(data['tone'], 'profissional')
    
    prompt = f"""
Você é um especialista em criação de conteúdo e SEO. Crie um artigo completo e otimizado sobre o tema "{data['theme']}" para o nicho "{data['niche']}", direcionado ao público-alvo "{data['target_audience']}".

ESPECIFICAÇÕES:
- Idioma: {language}
- Tom: {tone}
- Número de seções H2: {data['h2_sections']}
- Palavras aproximadas: {data['word_count']}
- Incluir subtópicos H3: {'Sim' if data['include_h3'] else 'Não'}

ESTRUTURA OBRIGATÓRIA:
1. Título principal (H1) - atrativo e otimizado para SEO
2. Introdução envolvente (2-3 parágrafos)
3. {data['h2_sections']} seções principais (H2) com conteúdo substancial
{'4. Subtópicos (H3) dentro de cada seção H2' if data['include_h3'] else ''}
5. Conclusão impactante
6. Call-to-action final

DIRETRIZES DE QUALIDADE:
- Use linguagem clara e envolvente
- Inclua informações práticas e acionáveis
- Mantenha foco no público-alvo especificado
- Otimize para SEO naturalmente
- Use formatação HTML adequada (h1, h2, h3, p, ul, li, strong, em)
- Crie conteúdo original e valioso

IMPORTANTE: Retorne APENAS o HTML do artigo, sem explicações adicionais. Use tags HTML apropriadas para formatação.
"""
    
    return prompt

def generate_meta_description_prompt(data, article_content):
    """Gera o prompt para criação da meta descrição"""
    language_map = {
        'pt-br': 'português brasileiro',
        'en': 'inglês',
        'es': 'espanhol',
        'fr': 'francês'
    }
    
    language = language_map.get(data['language'], 'português brasileiro')
    
    prompt = f"""
Com base no artigo fornecido sobre "{data['theme']}" para o nicho "{data['niche']}", crie uma meta descrição otimizada para SEO.

ESPECIFICAÇÕES:
- Idioma: {language}
- Máximo: 155 caracteres
- Deve ser atrativa e incluir palavra-chave principal
- Deve incentivar o clique
- Foque no público-alvo: {data['target_audience']}

ARTIGO DE REFERÊNCIA:
{article_content[:500]}...

IMPORTANTE: Retorne APENAS a meta descrição, sem aspas ou explicações adicionais.
"""
    
    return prompt

def generate_tags_prompt(data, article_content):
    """Gera o prompt para criação das tags SEO"""
    language_map = {
        'pt-br': 'português brasileiro',
        'en': 'inglês',
        'es': 'espanhol',
        'fr': 'francês'
    }
    
    language = language_map.get(data['language'], 'português brasileiro')
    
    prompt = f"""
Com base no artigo sobre "{data['theme']}" para o nicho "{data['niche']}", crie 8-12 tags SEO relevantes.

ESPECIFICAÇÕES:
- Idioma: {language}
- Tags devem ser palavras-chave relevantes
- Misture termos específicos e gerais
- Foque no público-alvo: {data['target_audience']}
- Inclua variações da palavra-chave principal

ARTIGO DE REFERÊNCIA:
{article_content[:500]}...

FORMATO: Retorne as tags separadas por vírgula, sem numeração ou explicações.
Exemplo: marketing digital, e-commerce, vendas online, estratégias digitais
"""
    
    return prompt

def generate_faq_prompt(data, article_content):
    """Gera o prompt para criação do FAQ"""
    language_map = {
        'pt-br': 'português brasileiro',
        'en': 'inglês',
        'es': 'espanhol',
        'fr': 'francês'
    }
    
    language = language_map.get(data['language'], 'português brasileiro')
    
    prompt = f"""
Com base no artigo sobre "{data['theme']}" para o nicho "{data['niche']}", crie 5-7 perguntas frequentes (FAQ) com respostas.

ESPECIFICAÇÕES:
- Idioma: {language}
- Perguntas que o público-alvo "{data['target_audience']}" realmente faria
- Respostas claras e práticas (2-3 frases cada)
- Complementem o conteúdo do artigo

ARTIGO DE REFERÊNCIA:
{article_content[:500]}...

FORMATO JSON:
[
  {
    "question": "Pergunta aqui?",
    "answer": "Resposta clara e prática aqui."
  }
]

IMPORTANTE: Retorne APENAS o JSON válido, sem explicações adicionais.
"""
    
    return prompt

def generate_image_prompts_prompt(data, article_content):
    """Gera o prompt para criação dos prompts de imagem"""
    language_map = {
        'pt-br': 'português brasileiro',
        'en': 'inglês',
        'es': 'espanhol',
        'fr': 'francês'
    }
    
    language = language_map.get(data['language'], 'português brasileiro')
    
    prompt = f"""
Com base no artigo sobre "{data['theme']}" para o nicho "{data['niche']}", crie 4 prompts profissionais para geração de imagens com IA.

ESPECIFICAÇÕES:
- Prompts em inglês (padrão para IAs de imagem)
- Cada prompt deve ser detalhado e específico
- Inclua estilo visual, composição, cores, iluminação
- Adequados para o público-alvo: {data['target_audience']}

TIPOS DE IMAGEM:
1. Imagem principal/hero (destaque do artigo)
2. Imagem conceitual/ilustrativa
3. Imagem de processo/tutorial
4. Imagem de resultado/benefício

ARTIGO DE REFERÊNCIA:
{article_content[:300]}...

FORMATO JSON:
[
  {
    "type": "Hero Image",
    "description": "Descrição da finalidade da imagem",
    "prompt": "Prompt detalhado em inglês para IA de imagem"
  }
]

IMPORTANTE: Retorne APENAS o JSON válido, sem explicações adicionais.
"""
    
    return prompt

@article_bp.route('/generate-article', methods=['POST'])
def generate_article():
    try:
        data = request.get_json()
        
        # Validação dos dados obrigatórios
        required_fields = ['api_key', 'ai_provider', 'theme', 'niche', 'target_audience']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400
        
        # Validação do formato da chave de API
        if not validate_api_key(data['api_key'], data['ai_provider']):
            provider_formats = {
                'openai': 'deve começar com "sk-"',
                'gemini': 'deve começar com "AIza"',
                'groq': 'deve começar com "gsk_"',
                'xai': 'deve começar com "xai-"'
            }
            format_info = provider_formats.get(data['ai_provider'], 'formato inválido')
            return jsonify({'error': f'Formato de chave de API inválido para {data["ai_provider"]} ({format_info})'}), 400
        
        result = {}
        
        # 1. Gerar artigo principal
        article_prompt = generate_article_prompt(data)
        article_content = call_ai_api(data['api_key'], data['ai_provider'], article_prompt)
        result['article'] = article_content
        
        # 2. Gerar meta descrição (se solicitado)
        if data.get('enhanced_meta', False):
            meta_prompt = generate_meta_description_prompt(data, article_content)
            meta_description = call_ai_api(data['api_key'], data['ai_provider'], meta_prompt)
            result['meta_description'] = meta_description.strip()
        
        # 3. Gerar tags SEO (se solicitado)
        if data.get('generate_tags', False):
            tags_prompt = generate_tags_prompt(data, article_content)
            tags_response = call_ai_api(data['api_key'], data['ai_provider'], tags_prompt)
            # Processar tags (remover espaços extras e dividir por vírgula)
            tags = [tag.strip() for tag in tags_response.split(',') if tag.strip()]
            result['tags'] = tags
        
        # 4. Gerar FAQ (se solicitado)
        if data.get('generate_faq', False):
            faq_prompt = generate_faq_prompt(data, article_content)
            faq_response = call_ai_api(data['api_key'], data['ai_provider'], faq_prompt)
            try:
                # Tentar parsear JSON
                faq_data = json.loads(faq_response)
                result['faq'] = faq_data
            except json.JSONDecodeError:
                # Se falhar, criar FAQ básico
                result['faq'] = [
                    {
                        "question": "Como posso aplicar essas informações?",
                        "answer": "Siga as orientações apresentadas no artigo e adapte-as à sua realidade específica."
                    }
                ]
        
        # 5. Gerar prompts de imagem (se solicitado)
        if data.get('generate_images', False):
            images_prompt = generate_image_prompts_prompt(data, article_content)
            images_response = call_ai_api(data['api_key'], data['ai_provider'], images_prompt)
            try:
                # Tentar parsear JSON
                images_data = json.loads(images_response)
                result['images'] = images_data
            except json.JSONDecodeError:
                # Se falhar, criar prompts básicos
                result['images'] = [
                    {
                        "type": "Hero Image",
                        "description": "Imagem principal do artigo",
                        "prompt": f"Professional illustration about {data['theme']}, modern design, clean composition, high quality, detailed"
                    },
                    {
                        "type": "Concept Image",
                        "description": "Imagem conceitual",
                        "prompt": f"Abstract concept visualization of {data['theme']}, minimalist style, professional colors"
                    },
                    {
                        "type": "Process Image",
                        "description": "Imagem de processo",
                        "prompt": f"Step-by-step process illustration for {data['theme']}, infographic style, clear and organized"
                    },
                    {
                        "type": "Result Image",
                        "description": "Imagem de resultado",
                        "prompt": f"Success visualization related to {data['theme']}, positive outcome, professional photography style"
                    }
                ]
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

