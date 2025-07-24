# 🤖 Gerador de Artigos IA - Versão Melhorada

Um aplicativo web completo para geração de artigos otimizados para SEO usando múltiplos provedores de IA.

## ✨ Funcionalidades

### 🔧 Configuração Flexível
- **Múltiplos Provedores de IA**: OpenAI (GPT-4), Google Gemini, Groq (Llama), xAI (Grok)
- **Validação Inteligente**: Validação automática do formato das chaves de API
- **Configuração Personalizada**: Tom de voz, idioma, número de seções, palavras desejadas

### 📝 Geração de Conteúdo
- **Artigos Completos**: Estrutura otimizada com H1, H2, H3 e formatação HTML
- **Meta Descrição Aprimorada**: Otimizada para SEO (máximo 155 caracteres)
- **Tags SEO**: 8-12 tags relevantes para melhor indexação
- **FAQ Inteligente**: 5-7 perguntas e respostas relacionadas ao tema
- **Prompts de Imagem**: 4 prompts profissionais para geradores de IA (DALL-E, Midjourney, etc.)

### 💾 Recursos de Exportação
- **Copiar Artigo**: Copia o texto limpo para a área de transferência
- **Download HTML**: Baixa o artigo formatado em HTML
- **Download TXT**: Baixa o artigo em texto simples
- **Copiar Prompts**: Copia prompts de imagem individualmente

### 🎨 Interface Moderna
- **Design Responsivo**: Funciona perfeitamente em desktop e mobile
- **Feedback Visual**: Indicadores de loading e confirmações de ação
- **Validação em Tempo Real**: Verificação instantânea de chaves de API
- **Mensagens de Erro Claras**: Orientações específicas para cada problema

## 🚀 Como Usar

### 1. Configuração da API
1. Escolha seu provedor de IA preferido
2. Insira sua chave de API no formato correto:
   - **OpenAI**: `sk-...`
   - **Gemini**: `AIza...`
   - **Groq**: `gsk_...`
   - **xAI**: `xai-...`

### 2. Configuração do Artigo
1. **Tema Principal**: O assunto principal do seu artigo
2. **Nicho**: A área específica de atuação
3. **Público-Alvo**: Para quem o artigo é direcionado
4. **Tom de Voz**: Escolha entre profissional, casual, técnico, amigável, formal ou review
5. **Configurações Avançadas**: Número de seções, palavras desejadas, idioma

### 3. Funcionalidades Extras
Marque as opções desejadas:
- ✅ **Gerar FAQ**: Perguntas e respostas relevantes
- ✅ **Gerar Tags SEO**: Tags otimizadas para busca
- ✅ **Gerar Prompts de Imagem**: Para uso em IAs de imagem
- ✅ **Meta Descrição Aprimorada**: Otimizada para SEO

### 4. Geração e Exportação
1. Clique em "🚀 Gerar Artigo Completo"
2. Aguarde o processamento (pode levar alguns minutos)
3. Use os botões de exportação para salvar seu conteúdo

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.11+
- Chave de API de pelo menos um provedor de IA

### Instalação
```bash
# Clone ou baixe o projeto
cd gerador-artigos-ia

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
python src/main.py
```

### Acesso
Abra seu navegador e acesse: `http://localhost:5000`

## 📋 Dependências

- **Flask**: Framework web
- **OpenAI**: Integração com GPT-4
- **Google Generative AI**: Integração com Gemini
- **Groq**: Integração com Llama
- **Requests**: Para chamadas HTTP (xAI)

## 🔒 Segurança

- As chaves de API são validadas antes do uso
- Não há armazenamento permanente de chaves
- Comunicação segura com todos os provedores
- Validação de entrada para prevenir ataques

## 🎯 Casos de Uso

### Para Profissionais de Marketing
- Criação rápida de conteúdo otimizado
- Geração de múltiplos artigos com diferentes tons
- Prompts prontos para criação de imagens

### Para Blogueiros e Criadores
- Estrutura profissional para artigos
- FAQ automático para engajamento
- Tags SEO para melhor alcance

### Para Agências
- Produção em escala de conteúdo
- Múltiplos provedores para redundância
- Exportação em diferentes formatos

## 🔧 Personalização

O aplicativo permite personalização completa:
- **Idiomas**: Português, Inglês, Espanhol, Francês
- **Tons**: 6 opções diferentes incluindo review/análise
- **Estrutura**: 3-10 seções H2 configuráveis
- **Tamanho**: 500-5000 palavras

## 📞 Suporte

Para dúvidas sobre:
- **OpenAI**: [platform.openai.com](https://platform.openai.com/account/api-keys)
- **Gemini**: [aistudio.google.com](https://aistudio.google.com/app/apikey)
- **Groq**: [console.groq.com](https://console.groq.com/keys)
- **xAI**: [console.x.ai](https://console.x.ai/)

## 🎉 Versão Atual

**v2.0** - Versão Melhorada
- ✅ Múltiplos provedores de IA
- ✅ Validação robusta de chaves
- ✅ FAQ automático
- ✅ Tags SEO inteligentes
- ✅ Prompts de imagem profissionais
- ✅ Interface responsiva
- ✅ Exportação múltipla

---

**Desenvolvido com ❤️ para criadores de conteúdo**

