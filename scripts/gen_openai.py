from scripts.get_lang import get_lang

def gen_openai(messages, api_config):
    import openai
    openai.api_base = api_config.get('api_base', 'https://api.openai.com/v1')
    openai.api_key = api_config.get('api_key', '')
    model = api_config.get('model', 'gpt-3.5-turbo')
    if not openai.api_key:
        raise Exception(get_lang('is_required', {'0': 'API Key'}))
    if not messages or len(messages) == 0:
        raise Exception(get_lang('is_required', {'0': 'messages'}))
    completion = openai.ChatCompletion.create(model=model, messages=messages, timeout=60)
    if len(completion.choices) == 0:
        raise Exception(get_lang('no_response_from', {'0': 'OpenAI'}))
    content = completion.choices[0].message.content
    return content
