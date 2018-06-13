string_in = "今日もしないとね"


def mecab_tokenize(str_in):
    import MeCab
    m = MeCab.Tagger("-Ochasen")
    parsed_mecab_str = m.parse(str_in)
    mecab_list = parsed_mecab_str.split('\n')
    mecab_tokens = []
    for mecab_word in mecab_list:
        token = mecab_word.split('\t')[0]
        if len(token) > 0 and token != 'EOS':
            mecab_tokens.append(token)
    return mecab_tokens

print(mecab_tokenize(string_in))